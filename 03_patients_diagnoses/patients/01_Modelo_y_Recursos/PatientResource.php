<?php

namespace App\Http\Resources\Patient;

use Illuminate\Http\Request;
use Illuminate\Http\Resources\Json\JsonResource;

class PatientResource extends JsonResource
{
    /**
     * Transform the resource into an array.
     *
     * @return array<string, mixed>
     */
    public function toArray($request)
    {
        return [
            'id' => $this->id,
            'document_number' => $this->document_number,
            'full_name' => "{$this->paternal_lastname} {$this->maternal_lastname} {$this->name}",
            'name' => $this->name,
            'paternal_lastname' => $this->paternal_lastname,
            'maternal_lastname' => $this->maternal_lastname,
            'birth_date' => $this->birth_date,
            'sex' => $this->sex,
            'primary_phone' => $this->primary_phone,
            'secondary_phone' => $this->secondary_phone,
            'email' => $this->email,
            'ocupation' => $this->ocupation,
            'health_condition' => $this->health_condition,
            'address' => $this->address,
            'region' => $this->region?->id,
            'province' => $this->province?->id,
            'district' => $this->district?->id,
            'country' => $this->country?->id,
            'document_type' => $this->documentType?->id,
            'created_at' => $this->created_at,
            'updated_at' => $this->updated_at,
        ];
    }
}