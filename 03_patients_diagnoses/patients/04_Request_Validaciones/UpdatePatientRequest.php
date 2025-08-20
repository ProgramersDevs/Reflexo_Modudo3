<?php

namespace App\Http\Requests\Patient;

use Illuminate\Foundation\Http\FormRequest;
use Illuminate\Validation\Rule;

class UpdatePatientRequest extends FormRequest
{
    /**
     * Determine if the user is authorized to make this request.
     */
    public function authorize(): bool
    {
        return true;
    }

    /**
     * Get the validation rules that apply to the request.
     *
     * @return array<string, \Illuminate\Contracts\Validation\ValidationRule|array<mixed>|string>
     */
    public function rules(): array
    {
        $patientId = $this->route('patient')->id ?? null;

        return [
            'document_number' => [
                'sometimes',
                'string',
                'max:20',
                Rule::unique('patients', 'document_number')->ignore($patientId),
            ],
            'paternal_lastname' => 'required|string|max:255',
            'maternal_lastname' => 'nullable|string|max:255',
            'name' => 'required|string|max:255',
            'personal_reference' => 'nullable|string|max:255',
            'birth_date' => 'nullable|string|max:255',
            'sex' => 'required|string|max:255',
            'primary_phone' => 'nullable|string|max:255',
            'secondary_phone' => 'nullable|string|max:255',
            'email' => [
                'nullable',
                'string',
                'max:255',
                Rule::unique('patients', 'email')->ignore($patientId),
            ],
            'ocupation' => 'nullable|string|max:255',
            'health_condition' => 'nullable|string|max:255',
            'address' => 'nullable|string|max:255',
            'region_id' => 'nullable|exists:regions,id',
            'province_id' => 'nullable|exists:provinces,id',
            'district_id' => 'nullable|exists:districts,id',
            'document_type_id' => 'required|exists:document_types,id',
            'country_id' => 'nullable|exists:countries,id',
        ];
    }

    public function messages()
    {
        return [
            'document_number.unique' => 'El número de documento ya está registrado.',
            'email.unique' => 'El correo electrónico ya está registrado.',
        ];
    }
}
