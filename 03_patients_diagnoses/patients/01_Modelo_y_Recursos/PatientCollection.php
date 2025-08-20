<?php
namespace App\Http\Resources\Patient;
use Illuminate\Http\Resources\Json\ResourceCollection;
use App\Http\Resources\Patient\PatientResource;
class PatientCollection extends ResourceCollection
{
    public function withResponse($request, $response)
    {
        // Esto evita que Laravel añada `meta` y `links` por defecto
        $response->setData((object) $this->toArray($request));
    }
    public function toArray($request)
    {
        return [
            'current_page' => $this->currentPage(),
            'data' => PatientResource::collection($this->collection),
            'first_page_url' => $this->url(1),
            'from' => $this->firstItem(),
            'last_page' => $this->lastPage(),
            'last_page_url' => $this->url($this->lastPage()),
            'links' => $this->buildLinksArray(),
            'next_page_url' => $this->nextPageUrl(),
            'path' => $this->path(),
            'per_page' => $this->perPage(),
            'prev_page_url' => $this->previousPageUrl(),
            'to' => $this->lastItem(),
            'total' => $this->total(),
        ];
    }

    protected function buildLinksArray()
    {
        $window = 3; // número de enlaces visibles antes y después del actual
        $lastPage = $this->lastPage();
        $currentPage = $this->currentPage();

        $links = [];

        // Enlace a "Previous"
        $links[] = [
            'url' => $this->previousPageUrl(),
            'label' => '&laquo; Previous',
            'active' => false,
        ];

        // Páginas visibles
        for ($i = 1; $i <= min($lastPage, 10); $i++) {
            $links[] = [
                'url' => $this->url($i),
                'label' => (string) $i,
                'active' => $i === $currentPage,
            ];
        }

        // Puntos suspensivos
        if ($lastPage > 10) {
            $links[] = [
                'url' => null,
                'label' => '...',
                'active' => false,
            ];
            $links[] = [
                'url' => $this->url($lastPage - 1),
                'label' => (string) ($lastPage - 1),
                'active' => false,
            ];
            $links[] = [
                'url' => $this->url($lastPage),
                'label' => (string) $lastPage,
                'active' => false,
            ];
        }

        // Enlace a "Next"
        $links[] = [
            'url' => $this->nextPageUrl(),
            'label' => 'Next &raquo;',
            'active' => false,
        ];

        return $links;
    }
}