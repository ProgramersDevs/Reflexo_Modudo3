# Serializers package

# Importar todos los serializers
from .country_serializer import (
    CountrySerializer,
    CountryListSerializer,
    CountryCreateSerializer,
    CountryUpdateSerializer
)

from .region_serializer import (
    RegionSerializer,
    RegionListSerializer,
    RegionCreateSerializer,
    RegionUpdateSerializer,
    RegionDetailSerializer
)

from .province_serializer import (
    ProvinceSerializer,
    ProvinceListSerializer,
    ProvinceCreateSerializer,
    ProvinceUpdateSerializer,
    ProvinceDetailSerializer,
    ProvinceWithRegionSerializer
)

from .district_serializer import (
    DistrictSerializer,
    DistrictListSerializer,
    DistrictCreateSerializer,
    DistrictUpdateSerializer,
    DistrictDetailSerializer,
    DistrictWithProvinceSerializer,
    DistrictWithRegionSerializer
)



__all__ = [
    # Country serializers
    'CountrySerializer',
    'CountryListSerializer',
    'CountryCreateSerializer',
    'CountryUpdateSerializer',
    
    # Region serializers
    'RegionSerializer',
    'RegionListSerializer',
    'RegionCreateSerializer',
    'RegionUpdateSerializer',
    'RegionDetailSerializer',
    
    # Province serializers
    'ProvinceSerializer',
    'ProvinceListSerializer',
    'ProvinceCreateSerializer',
    'ProvinceUpdateSerializer',
    'ProvinceDetailSerializer',
    'ProvinceWithRegionSerializer',
    
    # District serializers
    'DistrictSerializer',
    'DistrictListSerializer',
    'DistrictCreateSerializer',
    'DistrictUpdateSerializer',
    'DistrictDetailSerializer',
    'DistrictWithProvinceSerializer',
    'DistrictWithRegionSerializer',
    

]
