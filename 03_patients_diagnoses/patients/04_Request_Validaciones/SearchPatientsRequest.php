<?php

namespace App\Http\Requests\Patient;

use Illuminate\Contracts\Validation\Validator;
use Illuminate\Foundation\Http\FormRequest;
use Illuminate\Http\Exceptions\HttpResponseException;

class SearchPatientsRequest extends FormRequest
{
    public function authorize(): bool
    {
        return true;
    }

    public function rules(): array
    {
        return [
            'search' => [
                'present',
                'required',
                'regex:/^[\pL\s0-9\'\(\)]+$/u'
            ],
            'per_page' => 'required|integer|min:1|max:100'
        ];
    }

    public function messages(): array
    {
        return [
            'search.present' => 'Debe incluirse el campo de búsqueda en la solicitud.',
            'search.required' => 'No se especificó ningún término de búsqueda.',
            'search.regex' => 'El término debe incluir letras, números u otros caracteres válidos.',
            'per_page.integer' => 'El número de elementos por página debe ser un número entero.',
            'per_page.required' => 'Es necesario especificar el número de elementos por página',
            'per_page.min' => 'El número mínimo por página es 1.',
            'per_page.max' => 'El número máximo por página es 100.',
        ];
    }

    protected function failedValidation(Validator $validator)
    {
        throw new HttpResponseException(
            response()->json([
                'message' => 'Errores de validación',
                'errors' => $validator->errors()
            ],422)    
        );
        
    }
}
