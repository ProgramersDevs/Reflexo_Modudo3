<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;
use Illuminate\Database\Eloquent\Relations\HasMany;
use Illuminate\Database\Eloquent\Relations\HasOne;
use Illuminate\Database\Eloquent\SoftDeletes;

class Patient extends Model
{
    /** @use HasFactory<\Database\Factories\PatientFactory> */
    use HasFactory,SoftDeletes;

    /**
     * The attributes that are mass assignable.
     *
     * @var list<string>
     */
    protected $fillable = [
        'document_number',
        'paternal_lastname',
        'maternal_lastname',
        'name',
        'personal_reference',
        'birth_date',
        'sex',
        'primary_phone',
        'secondary_phone',
        'email',
        'ocupation',
        'health_condition',
        'address',
        'region_id',
        'province_id',
        'district_id',
        'document_type_id',
        'country_id'
    ];

    public function region(): BelongsTo
    {
        return $this->belongsTo(Region::class);
    }

    public function district(): BelongsTo
    {
        return $this->belongsTo(District::class);
    }

    public function province(): BelongsTo
    {
        return $this->belongsTo(Province::class);
    }

    public function country():BelongsTo
    {
        return $this->belongsTo(Country::class);
    }

    public function documentType(): BelongsTo
    {
        return $this->belongsTo(DocumentType::class);
    }

    public function history():HasOne
    {
        return $this->hasOne(History::class);
    }

    public function appointments(): HasMany
    {
        return $this->hasMany(Appointment::class);
    }

}
