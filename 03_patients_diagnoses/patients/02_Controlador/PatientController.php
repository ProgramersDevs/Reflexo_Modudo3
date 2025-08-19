<?php

namespace App\Http\Controllers\Api;

use App\Http\Controllers\Controller;
use App\Http\Requests\Patient\SearchPatientsRequest;
use App\Http\Requests\Patient\StorePatientRequest;
use App\Http\Requests\Patient\UpdatePatientRequest;
use App\Models\Patient;
use App\Services\Patient\PatientService;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;
use App\Http\Resources\Patient\PatientResource;
use App\Http\Resources\Patient\PatientCollection;

class PatientController extends Controller
{
    public function __construct(private PatientService $patientService) {
        $this->patientService = $patientService;

        $this->middleware('can:patients.store')->only('store');
        $this->middleware('can:patients.update')->only('update');
        $this->middleware('can:patients.destroy')->only('destroy');
        $this->middleware('can:patients.index')->only('index');
        $this->middleware('can:patients.show')->only('show');

        $this->middleware('can:patients.search')->only('searchPatients');
        $this->middleware('can:patients.appointments_by_patient')->only('getAppointmentsByPatient');
    }

    public function index(Request $request): PatientCollection 
    {
        $patients = $this->patientService->getPaginated($request);
        return new PatientCollection($patients);
    }

    public function searchPatients(SearchPatientsRequest $request): PatientCollection
    {
        $patients = $this->patientService->searchPatients($request->validated());
        return new PatientCollection($patients);
    }

    public function getAppointmentsByPatient(Patient $patient): JsonResponse
    {
        return $this->patientService->getAppointmentsByPatient($patient);
    }

    public function show(Patient $patient): JsonResponse
    {
        return response()->json(new PatientResource($patient));
    }

    public function store(StorePatientRequest $request): JsonResponse
    {
        return $this->patientService->storeOrRestore($request->validated());
    }

    public function update(UpdatePatientRequest $request, Patient $patient): JsonResponse
    {
        return $this->patientService->update($patient, $request->validated());
    }

    public function destroy(Patient $patient): JsonResponse
    {
        return $this->patientService->destroy($patient);
    }
}