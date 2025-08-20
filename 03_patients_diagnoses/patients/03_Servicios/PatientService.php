<?php

namespace App\Services\Patient;

use App\Models\Patient;
use Illuminate\Database\Eloquent\Builder;
use Illuminate\Http\Request;
use Illuminate\Http\JsonResponse;
class PatientService
{
    /**
     * Retorna todos los pacientes (sin paginar).
     *
     * @return \Illuminate\Database\Eloquent\Collection|static[]
     */
    public function getAll()
    {
        return Patient::all();
    }

    /**
     * Obtiene una lista paginada de pacientes.
     *
     * @param Request $request
     * @return \Illuminate\Contracts\Pagination\LengthAwarePaginator
     */
    public function getPaginated(Request $request)
    {
        $perPage = $request->query('per_page', 20);
        return Patient::orderBy('created_at', 'desc')
            ->paginate($perPage)
            ->appends(['per_page' => $perPage]);
    }

    /**
     * Busca pacientes según término con paginación.
     *
     * @param array $request
     * @return \Illuminate\Contracts\Pagination\LengthAwarePaginator
     */
    public function searchPatients(array $request)
    {
        $perPage = $request['per_page'] ?? 30;
        $searchTerm = $request['search'] ?? '';

          $query = Patient::query()->orderBy('created_at', 'desc'); // Orden por defecto

        if (!empty($searchTerm)) {
            $query->where(function ($query) use ($searchTerm) {
                $this->searchByTerm($query, $searchTerm);
            });
        }

        return $query->paginate($perPage)->appends([
            'per_page' => $perPage,
            'search' => $searchTerm,
        ]);
    }

    public function getAppointmentsByPatient(Patient $patient): JsonResponse
    {
        return response()->json($patient->appointments()->with('therapist','paymentType')->get());
    }

    /**
     * Crea o restaura paciente.
     *
     * @param array $data
     * @return \Illuminate\Http\JsonResponse
     */
    public function storeOrRestore(array $data)
    {
        try {
            $patient = Patient::withTrashed()->firstOrNew([
                'name' => $data['name'],
                'paternal_lastname' => $data['paternal_lastname'],
                'maternal_lastname' => $data['maternal_lastname'],
            ]);

            if ($patient->exists) {
                if ($patient->trashed()) {
                    $patient->restore();
                    return response()->json([
                        'message' => 'El paciente fue restaurado',
                        'data' => $patient->fresh(),
                    ], 200);
                }
                return response()->json(['message' => 'El paciente ya existe'], 409);
            }

            $patient->fill($data)->save();
            $patient->history()->create();

            return response()->json($patient, 201);
        } catch (\Exception $e) {
            return response()->json([
                'message' => 'Error al procesar la solicitud',
                'error' => $e->getMessage(),
            ], 500);
        }
    }

    /**
     * Actualiza paciente con datos modificados.
     *
     * @param Patient $patient
     * @param array $data
     * @return \Illuminate\Http\JsonResponse
     */
    public function update(Patient $patient, array $data)
    {
        $filteredData = array_filter(
            $data,
            fn($key, $value) => (string) $patient->$key !== (string) $value,
            ARRAY_FILTER_USE_BOTH
        );

        if (!empty($filteredData)) {
            $patient->update($filteredData);
        }

        return response()->json($patient);
    }

    /**
     * Eliminación suave de paciente.
     *
     * @param Patient $patient
     * @return \Illuminate\Http\JsonResponse
     */
    public function destroy(Patient $patient)
    {
        $patient->delete();
        return response()->json(['message' => 'Paciente eliminado correctamente'], 200);
    }

    /**
     * Búsqueda avanzada por término en varios campos.
     *
     * @param Builder $query
     * @param string $searchTerm
     * @return Builder
     */
    private function searchByTerm(Builder $query, string $searchTerm): Builder
    {
        return $query->where(function ($q) use ($searchTerm) {
            $q->where('document_number', '=', $searchTerm)
                ->orWhere('document_number', 'LIKE', "{$searchTerm}%")
                ->orWhere('name', 'LIKE', "{$searchTerm}%")
                ->orWhere('name', 'LIKE', "% {$searchTerm}%")
                ->orWhere('paternal_lastname', 'LIKE', "{$searchTerm}%")
                ->orWhere('paternal_lastname', 'LIKE', "% {$searchTerm}%")
                ->orWhere('maternal_lastname', 'LIKE', "{$searchTerm}%")
                ->orWhere('maternal_lastname', 'LIKE', "% {$searchTerm}%")
                ->orWhereRaw("CONCAT(paternal_lastname, ' ', name) LIKE ?", ["{$searchTerm}%"])
                ->orWhereRaw("CONCAT(paternal_lastname, ' ', maternal_lastname, ' ', name) LIKE ?", ["{$searchTerm}%"])
                ->orWhereRaw("CONCAT(name, ' ', paternal_lastname, ' ', maternal_lastname) LIKE ?", ["{$searchTerm}%"])
                ->orWhereRaw("CONCAT(COALESCE(paternal_lastname, ''), ' ', COALESCE(SUBSTRING_INDEX(name, ' ', 1), ''), ' ', COALESCE(SUBSTRING_INDEX(name, ' ', -1), '')) LIKE ?", ["{$searchTerm}%"])
                ->orWhereRaw("CONCAT(COALESCE(maternal_lastname, ''), ' ', COALESCE(SUBSTRING_INDEX(name, ' ', 1), ''), ' ', COALESCE(SUBSTRING_INDEX(name, ' ', -1), '')) LIKE ?", ["{$searchTerm}%"])
                ->orWhereRaw("CONCAT(COALESCE(SUBSTRING_INDEX(name, ' ', 1), ''), ' ', COALESCE(paternal_lastname, ''), ' ', COALESCE(maternal_lastname, '')) LIKE ?", ["{$searchTerm}%"])
                ->orWhereRaw("CONCAT(COALESCE(SUBSTRING_INDEX(name, ' ', -1), ''), ' ', COALESCE(paternal_lastname, ''), ' ', COALESCE(maternal_lastname, '')) LIKE ?", ["{$searchTerm}%"]);
        });
    }
}