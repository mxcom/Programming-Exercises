from typing import List, Dict, Any, Optional
from enum import Enum
from datetime import datetime


class Ies:
    pass

    def __init__(self, ) -> None:
        pass


class AggregatedOrigin:
    origin: str
    percent: int

    def __init__(self, origin: str, percent: int) -> None:
        self.origin = origin
        self.percent = percent


class OriginsOfIngredients:
    aggregated_origins: List[AggregatedOrigin]
    epi_score: int
    epi_value: int
    origins_from_origins_field: List[str]
    transportation_scores: Dict[str, int]
    transportation_values: Dict[str, int]
    values: Dict[str, int]

    def __init__(self, aggregated_origins: List[AggregatedOrigin], epi_score: int, epi_value: int, origins_from_origins_field: List[str], transportation_scores: Dict[str, int], transportation_values: Dict[str, int], values: Dict[str, int]) -> None:
        self.aggregated_origins = aggregated_origins
        self.epi_score = epi_score
        self.epi_value = epi_value
        self.origins_from_origins_field = origins_from_origins_field
        self.transportation_scores = transportation_scores
        self.transportation_values = transportation_values
        self.values = values


class PackagingPackaging:
    ecoscore_material_score: int
    ecoscore_shape_ratio: int
    material: str
    shape: str

    def __init__(self, ecoscore_material_score: int, ecoscore_shape_ratio: int, material: str, shape: str) -> None:
        self.ecoscore_material_score = ecoscore_material_score
        self.ecoscore_shape_ratio = ecoscore_shape_ratio
        self.material = material
        self.shape = shape


class AdjustmentsPackaging:
    non_recyclable_and_non_biodegradable_materials: int
    packagings: List[PackagingPackaging]
    score: int
    value: int
    warning: str

    def __init__(self, non_recyclable_and_non_biodegradable_materials: int, packagings: List[PackagingPackaging], score: int, value: int, warning: str) -> None:
        self.non_recyclable_and_non_biodegradable_materials = non_recyclable_and_non_biodegradable_materials
        self.packagings = packagings
        self.score = score
        self.value = value
        self.warning = warning


class ProductionSystem:
    labels: List[Any]
    value: int
    warning: str

    def __init__(self, labels: List[Any], value: int, warning: str) -> None:
        self.labels = labels
        self.value = value
        self.warning = warning


class Adjustments:
    origins_of_ingredients: OriginsOfIngredients
    packaging: AdjustmentsPackaging
    production_system: ProductionSystem
    threatened_species: Ies

    def __init__(self, origins_of_ingredients: OriginsOfIngredients, packaging: AdjustmentsPackaging, production_system: ProductionSystem, threatened_species: Ies) -> None:
        self.origins_of_ingredients = origins_of_ingredients
        self.packaging = packaging
        self.production_system = production_system
        self.threatened_species = threatened_species


class Agribalyse:
    warning: str

    def __init__(self, warning: str) -> None:
        self.warning = warning


class Missing:
    agb_category: int
    labels: int
    packagings: int

    def __init__(self, agb_category: int, labels: int, packagings: int) -> None:
        self.agb_category = agb_category
        self.labels = labels
        self.packagings = packagings


class EcoscoreData:
    adjustments: Adjustments
    agribalyse: Agribalyse
    missing: Missing
    missing_agribalyse_match_warning: int
    status: str

    def __init__(self, adjustments: Adjustments, agribalyse: Agribalyse, missing: Missing, missing_agribalyse_match_warning: int, status: str) -> None:
        self.adjustments = adjustments
        self.agribalyse = agribalyse
        self.missing = missing
        self.missing_agribalyse_match_warning = missing_agribalyse_match_warning
        self.status = status


class The100:
    h: int
    w: int

    def __init__(self, h: int, w: int) -> None:
        self.h = h
        self.w = w


class Sizes:
    the_100: The100
    the_400: The100
    full: The100
    the_200: Optional[The100]

    def __init__(self, the_100: The100, the_400: The100, full: The100, the_200: Optional[The100]) -> None:
        self.the_100 = the_100
        self.the_400 = the_400
        self.full = full
        self.the_200 = the_200


class FrontEnClass:
    geometry: str
    imgid: int
    normalize: Optional[str]
    rev: int
    sizes: Sizes
    white_magic: None

    def __init__(self, geometry: str, imgid: int, normalize: Optional[str], rev: int, sizes: Sizes, white_magic: None) -> None:
        self.geometry = geometry
        self.imgid = imgid
        self.normalize = normalize
        self.rev = rev
        self.sizes = sizes
        self.white_magic = white_magic


class The1:
    sizes: Sizes
    uploaded_t: int
    uploader: str

    def __init__(self, sizes: Sizes, uploaded_t: int, uploader: str) -> None:
        self.sizes = sizes
        self.uploaded_t = uploaded_t
        self.uploader = uploader


class Images:
    the_1: The1
    the_2: The1
    the_3: The1
    the_4: The1
    the_5: The1
    front: FrontEnClass
    front_en: FrontEnClass
    ingredients: FrontEnClass
    ingredients_en: FrontEnClass
    nutrition: FrontEnClass
    nutrition_en: FrontEnClass

    def __init__(self, the_1: The1, the_2: The1, the_3: The1, the_4: The1, the_5: The1, front: FrontEnClass, front_en: FrontEnClass, ingredients: FrontEnClass, ingredients_en: FrontEnClass, nutrition: FrontEnClass, nutrition_en: FrontEnClass) -> None:
        self.the_1 = the_1
        self.the_2 = the_2
        self.the_3 = the_3
        self.the_4 = the_4
        self.the_5 = the_5
        self.front = front
        self.front_en = front_en
        self.ingredients = ingredients
        self.ingredients_en = ingredients_en
        self.nutrition = nutrition
        self.nutrition_en = nutrition_en


class HasSubIngredients(Enum):
    YES = "yes"


class Ingredient:
    has_sub_ingredients: Optional[HasSubIngredients]
    id: str
    percent_estimate: float
    percent_max: float
    percent_min: float
    rank: Optional[int]
    text: str
    vegan: Optional[HasSubIngredients]
    vegetarian: Optional[HasSubIngredients]
    processing: Optional[str]

    def __init__(self, has_sub_ingredients: Optional[HasSubIngredients], id: str, percent_estimate: float, percent_max: float, percent_min: float, rank: Optional[int], text: str, vegan: Optional[HasSubIngredients], vegetarian: Optional[HasSubIngredients], processing: Optional[str]) -> None:
        self.has_sub_ingredients = has_sub_ingredients
        self.id = id
        self.percent_estimate = percent_estimate
        self.percent_max = percent_max
        self.percent_min = percent_min
        self.rank = rank
        self.text = text
        self.vegan = vegan
        self.vegetarian = vegetarian
        self.processing = processing


class IngredientsAnalysis:
    en_palm_oil_content_unknown: List[str]
    en_vegan_status_unknown: List[str]
    en_vegetarian_status_unknown: List[str]

    def __init__(self, en_palm_oil_content_unknown: List[str], en_vegan_status_unknown: List[str], en_vegetarian_status_unknown: List[str]) -> None:
        self.en_palm_oil_content_unknown = en_palm_oil_content_unknown
        self.en_vegan_status_unknown = en_vegan_status_unknown
        self.en_vegetarian_status_unknown = en_vegetarian_status_unknown


class Languages:
    en_english: int

    def __init__(self, en_english: int) -> None:
        self.en_english = en_english


class LanguagesCodes:
    en: int

    def __init__(self, en: int) -> None:
        self.en = en


class NutrientLevels:
    fat: str
    salt: str
    saturated_fat: str
    sugars: str

    def __init__(self, fat: str, salt: str, saturated_fat: str, sugars: str) -> None:
        self.fat = fat
        self.salt = salt
        self.saturated_fat = saturated_fat
        self.sugars = sugars


class Nutriments:
    calcium: float
    calcium_100_g: float
    calcium_serving: float
    calcium_unit: str
    calcium_value: int
    carbohydrates: float
    carbohydrates_100_g: float
    carbohydrates_serving: int
    carbohydrates_unit: str
    carbohydrates_value: float
    cholesterol: int
    cholesterol_100_g: int
    cholesterol_serving: int
    cholesterol_unit: str
    cholesterol_value: int
    energy: int
    energy_kcal: int
    energy_kcal_100_g: int
    energy_kcal_serving: int
    energy_kcal_unit: str
    energy_kcal_value: int
    energy_100_g: int
    energy_serving: int
    energy_unit: str
    energy_value: int
    fat: float
    fat_100_g: float
    fat_serving: int
    fat_unit: str
    fat_value: float
    fiber: float
    fiber_100_g: float
    fiber_serving: float
    fiber_unit: str
    fiber_value: float
    fruits_vegetables_nuts_estimate_from_ingredients_100_g: int
    fruits_vegetables_nuts_estimate_from_ingredients_serving: int
    iron: float
    iron_100_g: float
    iron_serving: float
    iron_unit: str
    iron_value: float
    nova_group: int
    nova_group_100_g: int
    nova_group_serving: int
    nutrition_score_fr: int
    nutrition_score_fr_100_g: int
    proteins: float
    proteins_100_g: float
    proteins_serving: int
    proteins_unit: str
    proteins_value: float
    salt: float
    salt_100_g: float
    salt_serving: float
    salt_unit: str
    salt_value: int
    saturated_fat: float
    saturated_fat_100_g: float
    saturated_fat_serving: float
    saturated_fat_unit: str
    saturated_fat_value: float
    sodium: float
    sodium_100_g: float
    sodium_serving: float
    sodium_unit: str
    sodium_value: int
    sugars: float
    sugars_100_g: float
    sugars_serving: int
    sugars_unit: str
    sugars_value: float
    trans_fat: int
    trans_fat_100_g: int
    trans_fat_serving: int
    trans_fat_unit: str
    trans_fat_value: int
    vitamin_a: float
    vitamin_a_100_g: float
    vitamin_a_serving: float
    vitamin_a_unit: str
    vitamin_a_value: int
    vitamin_c: int
    vitamin_c_100_g: int
    vitamin_c_serving: int
    vitamin_c_unit: str
    vitamin_c_value: int

    def __init__(self, calcium: float, calcium_100_g: float, calcium_serving: float, calcium_unit: str, calcium_value: int, carbohydrates: float, carbohydrates_100_g: float, carbohydrates_serving: int, carbohydrates_unit: str, carbohydrates_value: float, cholesterol: int, cholesterol_100_g: int, cholesterol_serving: int, cholesterol_unit: str, cholesterol_value: int, energy: int, energy_kcal: int, energy_kcal_100_g: int, energy_kcal_serving: int, energy_kcal_unit: str, energy_kcal_value: int, energy_100_g: int, energy_serving: int, energy_unit: str, energy_value: int, fat: float, fat_100_g: float, fat_serving: int, fat_unit: str, fat_value: float, fiber: float, fiber_100_g: float, fiber_serving: float, fiber_unit: str, fiber_value: float, fruits_vegetables_nuts_estimate_from_ingredients_100_g: int, fruits_vegetables_nuts_estimate_from_ingredients_serving: int, iron: float, iron_100_g: float, iron_serving: float, iron_unit: str, iron_value: float, nova_group: int, nova_group_100_g: int, nova_group_serving: int, nutrition_score_fr: int, nutrition_score_fr_100_g: int, proteins: float, proteins_100_g: float, proteins_serving: int, proteins_unit: str, proteins_value: float, salt: float, salt_100_g: float, salt_serving: float, salt_unit: str, salt_value: int, saturated_fat: float, saturated_fat_100_g: float, saturated_fat_serving: float, saturated_fat_unit: str, saturated_fat_value: float, sodium: float, sodium_100_g: float, sodium_serving: float, sodium_unit: str, sodium_value: int, sugars: float, sugars_100_g: float, sugars_serving: int, sugars_unit: str, sugars_value: float, trans_fat: int, trans_fat_100_g: int, trans_fat_serving: int, trans_fat_unit: str, trans_fat_value: int, vitamin_a: float, vitamin_a_100_g: float, vitamin_a_serving: float, vitamin_a_unit: str, vitamin_a_value: int, vitamin_c: int, vitamin_c_100_g: int, vitamin_c_serving: int, vitamin_c_unit: str, vitamin_c_value: int) -> None:
        self.calcium = calcium
        self.calcium_100_g = calcium_100_g
        self.calcium_serving = calcium_serving
        self.calcium_unit = calcium_unit
        self.calcium_value = calcium_value
        self.carbohydrates = carbohydrates
        self.carbohydrates_100_g = carbohydrates_100_g
        self.carbohydrates_serving = carbohydrates_serving
        self.carbohydrates_unit = carbohydrates_unit
        self.carbohydrates_value = carbohydrates_value
        self.cholesterol = cholesterol
        self.cholesterol_100_g = cholesterol_100_g
        self.cholesterol_serving = cholesterol_serving
        self.cholesterol_unit = cholesterol_unit
        self.cholesterol_value = cholesterol_value
        self.energy = energy
        self.energy_kcal = energy_kcal
        self.energy_kcal_100_g = energy_kcal_100_g
        self.energy_kcal_serving = energy_kcal_serving
        self.energy_kcal_unit = energy_kcal_unit
        self.energy_kcal_value = energy_kcal_value
        self.energy_100_g = energy_100_g
        self.energy_serving = energy_serving
        self.energy_unit = energy_unit
        self.energy_value = energy_value
        self.fat = fat
        self.fat_100_g = fat_100_g
        self.fat_serving = fat_serving
        self.fat_unit = fat_unit
        self.fat_value = fat_value
        self.fiber = fiber
        self.fiber_100_g = fiber_100_g
        self.fiber_serving = fiber_serving
        self.fiber_unit = fiber_unit
        self.fiber_value = fiber_value
        self.fruits_vegetables_nuts_estimate_from_ingredients_100_g = fruits_vegetables_nuts_estimate_from_ingredients_100_g
        self.fruits_vegetables_nuts_estimate_from_ingredients_serving = fruits_vegetables_nuts_estimate_from_ingredients_serving
        self.iron = iron
        self.iron_100_g = iron_100_g
        self.iron_serving = iron_serving
        self.iron_unit = iron_unit
        self.iron_value = iron_value
        self.nova_group = nova_group
        self.nova_group_100_g = nova_group_100_g
        self.nova_group_serving = nova_group_serving
        self.nutrition_score_fr = nutrition_score_fr
        self.nutrition_score_fr_100_g = nutrition_score_fr_100_g
        self.proteins = proteins
        self.proteins_100_g = proteins_100_g
        self.proteins_serving = proteins_serving
        self.proteins_unit = proteins_unit
        self.proteins_value = proteins_value
        self.salt = salt
        self.salt_100_g = salt_100_g
        self.salt_serving = salt_serving
        self.salt_unit = salt_unit
        self.salt_value = salt_value
        self.saturated_fat = saturated_fat
        self.saturated_fat_100_g = saturated_fat_100_g
        self.saturated_fat_serving = saturated_fat_serving
        self.saturated_fat_unit = saturated_fat_unit
        self.saturated_fat_value = saturated_fat_value
        self.sodium = sodium
        self.sodium_100_g = sodium_100_g
        self.sodium_serving = sodium_serving
        self.sodium_unit = sodium_unit
        self.sodium_value = sodium_value
        self.sugars = sugars
        self.sugars_100_g = sugars_100_g
        self.sugars_serving = sugars_serving
        self.sugars_unit = sugars_unit
        self.sugars_value = sugars_value
        self.trans_fat = trans_fat
        self.trans_fat_100_g = trans_fat_100_g
        self.trans_fat_serving = trans_fat_serving
        self.trans_fat_unit = trans_fat_unit
        self.trans_fat_value = trans_fat_value
        self.vitamin_a = vitamin_a
        self.vitamin_a_100_g = vitamin_a_100_g
        self.vitamin_a_serving = vitamin_a_serving
        self.vitamin_a_unit = vitamin_a_unit
        self.vitamin_a_value = vitamin_a_value
        self.vitamin_c = vitamin_c
        self.vitamin_c_100_g = vitamin_c_100_g
        self.vitamin_c_serving = vitamin_c_serving
        self.vitamin_c_unit = vitamin_c_unit
        self.vitamin_c_value = vitamin_c_value


class NutriscoreData:
    energy: int
    energy_points: int
    energy_value: int
    fiber: float
    fiber_points: int
    fiber_value: float
    fruits_vegetables_nuts_colza_walnut_olive_oils: int
    fruits_vegetables_nuts_colza_walnut_olive_oils_points: int
    fruits_vegetables_nuts_colza_walnut_olive_oils_value: int
    grade: str
    is_beverage: int
    is_cheese: int
    is_fat: int
    is_water: int
    negative_points: int
    positive_points: int
    proteins: float
    proteins_points: int
    proteins_value: float
    saturated_fat: float
    saturated_fat_points: int
    saturated_fat_ratio: float
    saturated_fat_ratio_points: int
    saturated_fat_ratio_value: int
    saturated_fat_value: float
    score: int
    sodium: int
    sodium_points: int
    sodium_value: int
    sugars: float
    sugars_points: int
    sugars_value: float

    def __init__(self, energy: int, energy_points: int, energy_value: int, fiber: float, fiber_points: int, fiber_value: float, fruits_vegetables_nuts_colza_walnut_olive_oils: int, fruits_vegetables_nuts_colza_walnut_olive_oils_points: int, fruits_vegetables_nuts_colza_walnut_olive_oils_value: int, grade: str, is_beverage: int, is_cheese: int, is_fat: int, is_water: int, negative_points: int, positive_points: int, proteins: float, proteins_points: int, proteins_value: float, saturated_fat: float, saturated_fat_points: int, saturated_fat_ratio: float, saturated_fat_ratio_points: int, saturated_fat_ratio_value: int, saturated_fat_value: float, score: int, sodium: int, sodium_points: int, sodium_value: int, sugars: float, sugars_points: int, sugars_value: float) -> None:
        self.energy = energy
        self.energy_points = energy_points
        self.energy_value = energy_value
        self.fiber = fiber
        self.fiber_points = fiber_points
        self.fiber_value = fiber_value
        self.fruits_vegetables_nuts_colza_walnut_olive_oils = fruits_vegetables_nuts_colza_walnut_olive_oils
        self.fruits_vegetables_nuts_colza_walnut_olive_oils_points = fruits_vegetables_nuts_colza_walnut_olive_oils_points
        self.fruits_vegetables_nuts_colza_walnut_olive_oils_value = fruits_vegetables_nuts_colza_walnut_olive_oils_value
        self.grade = grade
        self.is_beverage = is_beverage
        self.is_cheese = is_cheese
        self.is_fat = is_fat
        self.is_water = is_water
        self.negative_points = negative_points
        self.positive_points = positive_points
        self.proteins = proteins
        self.proteins_points = proteins_points
        self.proteins_value = proteins_value
        self.saturated_fat = saturated_fat
        self.saturated_fat_points = saturated_fat_points
        self.saturated_fat_ratio = saturated_fat_ratio
        self.saturated_fat_ratio_points = saturated_fat_ratio_points
        self.saturated_fat_ratio_value = saturated_fat_ratio_value
        self.saturated_fat_value = saturated_fat_value
        self.score = score
        self.sodium = sodium
        self.sodium_points = sodium_points
        self.sodium_value = sodium_value
        self.sugars = sugars
        self.sugars_points = sugars_points
        self.sugars_value = sugars_value


class ProductPackaging:
    shape: str

    def __init__(self, shape: str) -> None:
        self.shape = shape


class Display:
    en: str

    def __init__(self, en: str) -> None:
        self.en = en


class SelectedImagesFront:
    display: Display
    small: Display
    thumb: Display

    def __init__(self, display: Display, small: Display, thumb: Display) -> None:
        self.display = display
        self.small = small
        self.thumb = thumb


class SelectedImages:
    front: SelectedImagesFront
    ingredients: SelectedImagesFront
    nutrition: SelectedImagesFront

    def __init__(self, front: SelectedImagesFront, ingredients: SelectedImagesFront, nutrition: SelectedImagesFront) -> None:
        self.front = front
        self.ingredients = ingredients
        self.nutrition = nutrition


class Source:
    fields: List[str]
    id: str
    images: List[Any]
    import_t: int
    url: Optional[str]
    manufacturer: None
    name: Optional[str]

    def __init__(self, fields: List[str], id: str, images: List[Any], import_t: int, url: Optional[str], manufacturer: None, name: Optional[str]) -> None:
        self.fields = fields
        self.id = id
        self.images = images
        self.import_t = import_t
        self.url = url
        self.manufacturer = manufacturer
        self.name = name


class OrgDatabaseUsda:
    available_date: datetime
    fdc_category: str
    fdc_data_source: str
    fdc_id: int
    modified_date: datetime
    publication_date: datetime

    def __init__(self, available_date: datetime, fdc_category: str, fdc_data_source: str, fdc_id: int, modified_date: datetime, publication_date: datetime) -> None:
        self.available_date = available_date
        self.fdc_category = fdc_category
        self.fdc_data_source = fdc_data_source
        self.fdc_id = fdc_id
        self.modified_date = modified_date
        self.publication_date = publication_date


class SourcesFields:
    org_database_usda: OrgDatabaseUsda

    def __init__(self, org_database_usda: OrgDatabaseUsda) -> None:
        self.org_database_usda = org_database_usda


class Product:
    id: str
    keywords: List[str]
    added_countries_tags: List[Any]
    additives_debug_tags: List[Any]
    additives_n: int
    additives_old_n: int
    additives_old_tags: List[str]
    additives_original_tags: List[str]
    additives_prev_original_tags: List[str]
    additives_tags: List[str]
    additives_tags_n: None
    allergens: str
    allergens_from_ingredients: str
    allergens_from_user: str
    allergens_hierarchy: List[str]
    allergens_tags: List[str]
    amino_acids_prev_tags: List[Any]
    amino_acids_tags: List[Any]
    brand_owner: str
    brand_owner_imported: str
    brands: str
    brands_debug_tags: List[Any]
    brands_tags: List[str]
    categories: str
    categories_hierarchy: List[str]
    categories_imported: str
    categories_lc: str
    categories_old: str
    categories_properties: Ies
    categories_properties_tags: List[str]
    categories_tags: List[str]
    category_properties: Ies
    checkers: List[Any]
    checkers_tags: List[Any]
    ciqual_food_name_tags: List[str]
    cities_tags: List[Any]
    code: str
    codes_tags: List[str]
    compared_to_category: str
    complete: int
    completeness: float
    correctors: List[str]
    correctors_tags: List[str]
    countries: str
    countries_debug_tags: List[Any]
    countries_hierarchy: List[str]
    countries_imported: str
    countries_lc: str
    countries_tags: List[str]
    created_t: int
    creator: str
    data_quality_bugs_tags: List[Any]
    data_quality_errors_tags: List[Any]
    data_quality_info_tags: List[str]
    data_quality_tags: List[str]
    data_quality_warnings_tags: List[str]
    data_sources: str
    data_sources_imported: str
    data_sources_tags: List[str]
    debug_param_sorted_langs: List[str]
    ecoscore_data: EcoscoreData
    ecoscore_grade: str
    ecoscore_tags: List[str]
    editors: List[str]
    editors_tags: List[str]
    emb_codes: str
    emb_codes_20141016: str
    emb_codes_debug_tags: List[Any]
    emb_codes_orig: str
    emb_codes_tags: List[Any]
    entry_dates_tags: List[str]
    expiration_date: str
    expiration_date_debug_tags: List[Any]
    food_groups: str
    food_groups_tags: List[str]
    fruits_vegetables_nuts_100_g_estimate: int
    generic_name: str
    generic_name_en: str
    generic_name_en_debug_tags: List[Any]
    product_id: str
    image_front_small_url: str
    image_front_thumb_url: str
    image_front_url: str
    image_ingredients_small_url: str
    image_ingredients_thumb_url: str
    image_ingredients_url: str
    image_nutrition_small_url: str
    image_nutrition_thumb_url: str
    image_nutrition_url: str
    image_small_url: str
    image_thumb_url: str
    image_url: str
    images: Images
    informers: List[str]
    informers_tags: List[str]
    ingredients: List[Ingredient]
    ingredients_analysis: IngredientsAnalysis
    ingredients_analysis_tags: List[str]
    ingredients_debug: List[Optional[str]]
    ingredients_from_or_that_may_be_from_palm_oil_n: int
    ingredients_from_palm_oil_n: int
    ingredients_from_palm_oil_tags: List[Any]
    ingredients_hierarchy: List[str]
    ingredients_ids_debug: List[str]
    ingredients_n: int
    ingredients_n_tags: List[str]
    ingredients_original_tags: List[str]
    ingredients_percent_analysis: int
    ingredients_tags: List[str]
    ingredients_text: str
    ingredients_text_debug: str
    ingredients_text_en: str
    ingredients_text_en_debug_tags: List[Any]
    ingredients_text_en_imported: str
    ingredients_text_with_allergens: str
    ingredients_text_with_allergens_en: str
    ingredients_that_may_be_from_palm_oil_n: int
    ingredients_that_may_be_from_palm_oil_tags: List[Any]
    ingredients_with_specified_percent_n: int
    ingredients_with_specified_percent_sum: int
    ingredients_with_unspecified_percent_n: int
    ingredients_with_unspecified_percent_sum: int
    interface_version_created: int
    interface_version_modified: int
    known_ingredients_n: int
    labels: str
    labels_hierarchy: List[str]
    labels_lc: str
    labels_old: str
    labels_tags: List[str]
    lang: str
    lang_debug_tags: List[Any]
    languages: Languages
    languages_codes: LanguagesCodes
    languages_hierarchy: List[str]
    languages_tags: List[str]
    last_edit_dates_tags: List[str]
    last_editor: str
    last_image_dates_tags: List[str]
    last_image_t: int
    last_modified_by: str
    last_modified_t: int
    lc: str
    lc_imported: str
    link: str
    link_debug_tags: List[Any]
    main_countries_tags: List[Any]
    manufacturing_places: str
    manufacturing_places_debug_tags: List[Any]
    manufacturing_places_tags: List[Any]
    max_imgid: int
    minerals_prev_tags: List[Any]
    minerals_tags: List[Any]
    misc_tags: List[str]
    new_additives_n: int
    no_nutrition_data: str
    nova_group: int
    nova_group_debug: str
    nova_groups: int
    nova_groups_tags: List[str]
    nucleotides_prev_tags: List[Any]
    nucleotides_tags: List[Any]
    nutrient_levels: NutrientLevels
    nutrient_levels_tags: List[str]
    nutriments: Nutriments
    nutriscore_data: NutriscoreData
    nutriscore_grade: str
    nutriscore_score: int
    nutriscore_score_opposite: int
    nutrition_data: str
    nutrition_data_per: str
    nutrition_data_per_debug_tags: List[Any]
    nutrition_data_per_imported: str
    nutrition_data_prepared: str
    nutrition_data_prepared_per: str
    nutrition_data_prepared_per_debug_tags: List[Any]
    nutrition_data_prepared_per_imported: str
    nutrition_grade_fr: str
    nutrition_grades: str
    nutrition_grades_tags: List[str]
    nutrition_score_beverage: int
    nutrition_score_warning_fruits_vegetables_nuts_estimate_from_ingredients: int
    nutrition_score_warning_fruits_vegetables_nuts_estimate_from_ingredients_value: int
    origins: str
    origins_hierarchy: List[str]
    origins_lc: str
    origins_old: str
    origins_tags: List[str]
    other_nutritional_substances_tags: List[Any]
    packaging: str
    packaging_hierarchy: List[str]
    packaging_lc: str
    packaging_old: str
    packaging_old_before_taxonomization: str
    packaging_tags: List[str]
    packagings: List[ProductPackaging]
    photographers: List[str]
    photographers_tags: List[str]
    pnns_groups_1: str
    pnns_groups_1__tags: List[str]
    pnns_groups_2: str
    pnns_groups_2__tags: List[str]
    popularity_key: int
    popularity_tags: List[str]
    product_name: str
    product_name_en: str
    product_name_en_debug_tags: List[Any]
    product_name_en_imported: str
    product_quantity: int
    purchase_places: str
    purchase_places_debug_tags: List[Any]
    purchase_places_tags: List[Any]
    quantity: str
    quantity_debug_tags: List[Any]
    removed_countries_tags: List[Any]
    rev: int
    scans_n: int
    selected_images: SelectedImages
    serving_quantity: int
    serving_size: str
    serving_size_debug_tags: List[Any]
    serving_size_imported: str
    sortkey: int
    sources: List[Source]
    sources_fields: SourcesFields
    states: str
    states_hierarchy: List[str]
    states_tags: List[str]
    stores: str
    stores_debug_tags: List[Any]
    stores_tags: List[Any]
    traces: str
    traces_debug_tags: List[Any]
    traces_from_ingredients: str
    traces_from_user: str
    traces_hierarchy: List[str]
    traces_tags: List[str]
    unique_scans_n: int
    unknown_ingredients_n: int
    unknown_nutrients_tags: List[Any]
    update_key: str
    vitamins_prev_tags: List[Any]
    vitamins_tags: List[Any]

    def __init__(self, id: str, keywords: List[str], added_countries_tags: List[Any], additives_debug_tags: List[Any], additives_n: int, additives_old_n: int, additives_old_tags: List[str], additives_original_tags: List[str], additives_prev_original_tags: List[str], additives_tags: List[str], additives_tags_n: None, allergens: str, allergens_from_ingredients: str, allergens_from_user: str, allergens_hierarchy: List[str], allergens_tags: List[str], amino_acids_prev_tags: List[Any], amino_acids_tags: List[Any], brand_owner: str, brand_owner_imported: str, brands: str, brands_debug_tags: List[Any], brands_tags: List[str], categories: str, categories_hierarchy: List[str], categories_imported: str, categories_lc: str, categories_old: str, categories_properties: Ies, categories_properties_tags: List[str], categories_tags: List[str], category_properties: Ies, checkers: List[Any], checkers_tags: List[Any], ciqual_food_name_tags: List[str], cities_tags: List[Any], code: str, codes_tags: List[str], compared_to_category: str, complete: int, completeness: float, correctors: List[str], correctors_tags: List[str], countries: str, countries_debug_tags: List[Any], countries_hierarchy: List[str], countries_imported: str, countries_lc: str, countries_tags: List[str], created_t: int, creator: str, data_quality_bugs_tags: List[Any], data_quality_errors_tags: List[Any], data_quality_info_tags: List[str], data_quality_tags: List[str], data_quality_warnings_tags: List[str], data_sources: str, data_sources_imported: str, data_sources_tags: List[str], debug_param_sorted_langs: List[str], ecoscore_data: EcoscoreData, ecoscore_grade: str, ecoscore_tags: List[str], editors: List[str], editors_tags: List[str], emb_codes: str, emb_codes_20141016: str, emb_codes_debug_tags: List[Any], emb_codes_orig: str, emb_codes_tags: List[Any], entry_dates_tags: List[str], expiration_date: str, expiration_date_debug_tags: List[Any], food_groups: str, food_groups_tags: List[str], fruits_vegetables_nuts_100_g_estimate: int, generic_name: str, generic_name_en: str, generic_name_en_debug_tags: List[Any], product_id: str, image_front_small_url: str, image_front_thumb_url: str, image_front_url: str, image_ingredients_small_url: str, image_ingredients_thumb_url: str, image_ingredients_url: str, image_nutrition_small_url: str, image_nutrition_thumb_url: str, image_nutrition_url: str, image_small_url: str, image_thumb_url: str, image_url: str, images: Images, informers: List[str], informers_tags: List[str], ingredients: List[Ingredient], ingredients_analysis: IngredientsAnalysis, ingredients_analysis_tags: List[str], ingredients_debug: List[Optional[str]], ingredients_from_or_that_may_be_from_palm_oil_n: int, ingredients_from_palm_oil_n: int, ingredients_from_palm_oil_tags: List[Any], ingredients_hierarchy: List[str], ingredients_ids_debug: List[str], ingredients_n: int, ingredients_n_tags: List[str], ingredients_original_tags: List[str], ingredients_percent_analysis: int, ingredients_tags: List[str], ingredients_text: str, ingredients_text_debug: str, ingredients_text_en: str, ingredients_text_en_debug_tags: List[Any], ingredients_text_en_imported: str, ingredients_text_with_allergens: str, ingredients_text_with_allergens_en: str, ingredients_that_may_be_from_palm_oil_n: int, ingredients_that_may_be_from_palm_oil_tags: List[Any], ingredients_with_specified_percent_n: int, ingredients_with_specified_percent_sum: int, ingredients_with_unspecified_percent_n: int, ingredients_with_unspecified_percent_sum: int, interface_version_created: int, interface_version_modified: int, known_ingredients_n: int, labels: str, labels_hierarchy: List[str], labels_lc: str, labels_old: str, labels_tags: List[str], lang: str, lang_debug_tags: List[Any], languages: Languages, languages_codes: LanguagesCodes, languages_hierarchy: List[str], languages_tags: List[str], last_edit_dates_tags: List[str], last_editor: str, last_image_dates_tags: List[str], last_image_t: int, last_modified_by: str, last_modified_t: int, lc: str, lc_imported: str, link: str, link_debug_tags: List[Any], main_countries_tags: List[Any], manufacturing_places: str, manufacturing_places_debug_tags: List[Any], manufacturing_places_tags: List[Any], max_imgid: int, minerals_prev_tags: List[Any], minerals_tags: List[Any], misc_tags: List[str], new_additives_n: int, no_nutrition_data: str, nova_group: int, nova_group_debug: str, nova_groups: int, nova_groups_tags: List[str], nucleotides_prev_tags: List[Any], nucleotides_tags: List[Any], nutrient_levels: NutrientLevels, nutrient_levels_tags: List[str], nutriments: Nutriments, nutriscore_data: NutriscoreData, nutriscore_grade: str, nutriscore_score: int, nutriscore_score_opposite: int, nutrition_data: str, nutrition_data_per: str, nutrition_data_per_debug_tags: List[Any], nutrition_data_per_imported: str, nutrition_data_prepared: str, nutrition_data_prepared_per: str, nutrition_data_prepared_per_debug_tags: List[Any], nutrition_data_prepared_per_imported: str, nutrition_grade_fr: str, nutrition_grades: str, nutrition_grades_tags: List[str], nutrition_score_beverage: int, nutrition_score_warning_fruits_vegetables_nuts_estimate_from_ingredients: int, nutrition_score_warning_fruits_vegetables_nuts_estimate_from_ingredients_value: int, origins: str, origins_hierarchy: List[str], origins_lc: str, origins_old: str, origins_tags: List[str], other_nutritional_substances_tags: List[Any], packaging: str, packaging_hierarchy: List[str], packaging_lc: str, packaging_old: str, packaging_old_before_taxonomization: str, packaging_tags: List[str], packagings: List[ProductPackaging], photographers: List[str], photographers_tags: List[str], pnns_groups_1: str, pnns_groups_1__tags: List[str], pnns_groups_2: str, pnns_groups_2__tags: List[str], popularity_key: int, popularity_tags: List[str], product_name: str, product_name_en: str, product_name_en_debug_tags: List[Any], product_name_en_imported: str, product_quantity: int, purchase_places: str, purchase_places_debug_tags: List[Any], purchase_places_tags: List[Any], quantity: str, quantity_debug_tags: List[Any], removed_countries_tags: List[Any], rev: int, scans_n: int, selected_images: SelectedImages, serving_quantity: int, serving_size: str, serving_size_debug_tags: List[Any], serving_size_imported: str, sortkey: int, sources: List[Source], sources_fields: SourcesFields, states: str, states_hierarchy: List[str], states_tags: List[str], stores: str, stores_debug_tags: List[Any], stores_tags: List[Any], traces: str, traces_debug_tags: List[Any], traces_from_ingredients: str, traces_from_user: str, traces_hierarchy: List[str], traces_tags: List[str], unique_scans_n: int, unknown_ingredients_n: int, unknown_nutrients_tags: List[Any], update_key: str, vitamins_prev_tags: List[Any], vitamins_tags: List[Any]) -> None:
        self.id = id
        self.keywords = keywords
        self.added_countries_tags = added_countries_tags
        self.additives_debug_tags = additives_debug_tags
        self.additives_n = additives_n
        self.additives_old_n = additives_old_n
        self.additives_old_tags = additives_old_tags
        self.additives_original_tags = additives_original_tags
        self.additives_prev_original_tags = additives_prev_original_tags
        self.additives_tags = additives_tags
        self.additives_tags_n = additives_tags_n
        self.allergens = allergens
        self.allergens_from_ingredients = allergens_from_ingredients
        self.allergens_from_user = allergens_from_user
        self.allergens_hierarchy = allergens_hierarchy
        self.allergens_tags = allergens_tags
        self.amino_acids_prev_tags = amino_acids_prev_tags
        self.amino_acids_tags = amino_acids_tags
        self.brand_owner = brand_owner
        self.brand_owner_imported = brand_owner_imported
        self.brands = brands
        self.brands_debug_tags = brands_debug_tags
        self.brands_tags = brands_tags
        self.categories = categories
        self.categories_hierarchy = categories_hierarchy
        self.categories_imported = categories_imported
        self.categories_lc = categories_lc
        self.categories_old = categories_old
        self.categories_properties = categories_properties
        self.categories_properties_tags = categories_properties_tags
        self.categories_tags = categories_tags
        self.category_properties = category_properties
        self.checkers = checkers
        self.checkers_tags = checkers_tags
        self.ciqual_food_name_tags = ciqual_food_name_tags
        self.cities_tags = cities_tags
        self.code = code
        self.codes_tags = codes_tags
        self.compared_to_category = compared_to_category
        self.complete = complete
        self.completeness = completeness
        self.correctors = correctors
        self.correctors_tags = correctors_tags
        self.countries = countries
        self.countries_debug_tags = countries_debug_tags
        self.countries_hierarchy = countries_hierarchy
        self.countries_imported = countries_imported
        self.countries_lc = countries_lc
        self.countries_tags = countries_tags
        self.created_t = created_t
        self.creator = creator
        self.data_quality_bugs_tags = data_quality_bugs_tags
        self.data_quality_errors_tags = data_quality_errors_tags
        self.data_quality_info_tags = data_quality_info_tags
        self.data_quality_tags = data_quality_tags
        self.data_quality_warnings_tags = data_quality_warnings_tags
        self.data_sources = data_sources
        self.data_sources_imported = data_sources_imported
        self.data_sources_tags = data_sources_tags
        self.debug_param_sorted_langs = debug_param_sorted_langs
        self.ecoscore_data = ecoscore_data
        self.ecoscore_grade = ecoscore_grade
        self.ecoscore_tags = ecoscore_tags
        self.editors = editors
        self.editors_tags = editors_tags
        self.emb_codes = emb_codes
        self.emb_codes_20141016 = emb_codes_20141016
        self.emb_codes_debug_tags = emb_codes_debug_tags
        self.emb_codes_orig = emb_codes_orig
        self.emb_codes_tags = emb_codes_tags
        self.entry_dates_tags = entry_dates_tags
        self.expiration_date = expiration_date
        self.expiration_date_debug_tags = expiration_date_debug_tags
        self.food_groups = food_groups
        self.food_groups_tags = food_groups_tags
        self.fruits_vegetables_nuts_100_g_estimate = fruits_vegetables_nuts_100_g_estimate
        self.generic_name = generic_name
        self.generic_name_en = generic_name_en
        self.generic_name_en_debug_tags = generic_name_en_debug_tags
        self.product_id = product_id
        self.image_front_small_url = image_front_small_url
        self.image_front_thumb_url = image_front_thumb_url
        self.image_front_url = image_front_url
        self.image_ingredients_small_url = image_ingredients_small_url
        self.image_ingredients_thumb_url = image_ingredients_thumb_url
        self.image_ingredients_url = image_ingredients_url
        self.image_nutrition_small_url = image_nutrition_small_url
        self.image_nutrition_thumb_url = image_nutrition_thumb_url
        self.image_nutrition_url = image_nutrition_url
        self.image_small_url = image_small_url
        self.image_thumb_url = image_thumb_url
        self.image_url = image_url
        self.images = images
        self.informers = informers
        self.informers_tags = informers_tags
        self.ingredients = ingredients
        self.ingredients_analysis = ingredients_analysis
        self.ingredients_analysis_tags = ingredients_analysis_tags
        self.ingredients_debug = ingredients_debug
        self.ingredients_from_or_that_may_be_from_palm_oil_n = ingredients_from_or_that_may_be_from_palm_oil_n
        self.ingredients_from_palm_oil_n = ingredients_from_palm_oil_n
        self.ingredients_from_palm_oil_tags = ingredients_from_palm_oil_tags
        self.ingredients_hierarchy = ingredients_hierarchy
        self.ingredients_ids_debug = ingredients_ids_debug
        self.ingredients_n = ingredients_n
        self.ingredients_n_tags = ingredients_n_tags
        self.ingredients_original_tags = ingredients_original_tags
        self.ingredients_percent_analysis = ingredients_percent_analysis
        self.ingredients_tags = ingredients_tags
        self.ingredients_text = ingredients_text
        self.ingredients_text_debug = ingredients_text_debug
        self.ingredients_text_en = ingredients_text_en
        self.ingredients_text_en_debug_tags = ingredients_text_en_debug_tags
        self.ingredients_text_en_imported = ingredients_text_en_imported
        self.ingredients_text_with_allergens = ingredients_text_with_allergens
        self.ingredients_text_with_allergens_en = ingredients_text_with_allergens_en
        self.ingredients_that_may_be_from_palm_oil_n = ingredients_that_may_be_from_palm_oil_n
        self.ingredients_that_may_be_from_palm_oil_tags = ingredients_that_may_be_from_palm_oil_tags
        self.ingredients_with_specified_percent_n = ingredients_with_specified_percent_n
        self.ingredients_with_specified_percent_sum = ingredients_with_specified_percent_sum
        self.ingredients_with_unspecified_percent_n = ingredients_with_unspecified_percent_n
        self.ingredients_with_unspecified_percent_sum = ingredients_with_unspecified_percent_sum
        self.interface_version_created = interface_version_created
        self.interface_version_modified = interface_version_modified
        self.known_ingredients_n = known_ingredients_n
        self.labels = labels
        self.labels_hierarchy = labels_hierarchy
        self.labels_lc = labels_lc
        self.labels_old = labels_old
        self.labels_tags = labels_tags
        self.lang = lang
        self.lang_debug_tags = lang_debug_tags
        self.languages = languages
        self.languages_codes = languages_codes
        self.languages_hierarchy = languages_hierarchy
        self.languages_tags = languages_tags
        self.last_edit_dates_tags = last_edit_dates_tags
        self.last_editor = last_editor
        self.last_image_dates_tags = last_image_dates_tags
        self.last_image_t = last_image_t
        self.last_modified_by = last_modified_by
        self.last_modified_t = last_modified_t
        self.lc = lc
        self.lc_imported = lc_imported
        self.link = link
        self.link_debug_tags = link_debug_tags
        self.main_countries_tags = main_countries_tags
        self.manufacturing_places = manufacturing_places
        self.manufacturing_places_debug_tags = manufacturing_places_debug_tags
        self.manufacturing_places_tags = manufacturing_places_tags
        self.max_imgid = max_imgid
        self.minerals_prev_tags = minerals_prev_tags
        self.minerals_tags = minerals_tags
        self.misc_tags = misc_tags
        self.new_additives_n = new_additives_n
        self.no_nutrition_data = no_nutrition_data
        self.nova_group = nova_group
        self.nova_group_debug = nova_group_debug
        self.nova_groups = nova_groups
        self.nova_groups_tags = nova_groups_tags
        self.nucleotides_prev_tags = nucleotides_prev_tags
        self.nucleotides_tags = nucleotides_tags
        self.nutrient_levels = nutrient_levels
        self.nutrient_levels_tags = nutrient_levels_tags
        self.nutriments = nutriments
        self.nutriscore_data = nutriscore_data
        self.nutriscore_grade = nutriscore_grade
        self.nutriscore_score = nutriscore_score
        self.nutriscore_score_opposite = nutriscore_score_opposite
        self.nutrition_data = nutrition_data
        self.nutrition_data_per = nutrition_data_per
        self.nutrition_data_per_debug_tags = nutrition_data_per_debug_tags
        self.nutrition_data_per_imported = nutrition_data_per_imported
        self.nutrition_data_prepared = nutrition_data_prepared
        self.nutrition_data_prepared_per = nutrition_data_prepared_per
        self.nutrition_data_prepared_per_debug_tags = nutrition_data_prepared_per_debug_tags
        self.nutrition_data_prepared_per_imported = nutrition_data_prepared_per_imported
        self.nutrition_grade_fr = nutrition_grade_fr
        self.nutrition_grades = nutrition_grades
        self.nutrition_grades_tags = nutrition_grades_tags
        self.nutrition_score_beverage = nutrition_score_beverage
        self.nutrition_score_warning_fruits_vegetables_nuts_estimate_from_ingredients = nutrition_score_warning_fruits_vegetables_nuts_estimate_from_ingredients
        self.nutrition_score_warning_fruits_vegetables_nuts_estimate_from_ingredients_value = nutrition_score_warning_fruits_vegetables_nuts_estimate_from_ingredients_value
        self.origins = origins
        self.origins_hierarchy = origins_hierarchy
        self.origins_lc = origins_lc
        self.origins_old = origins_old
        self.origins_tags = origins_tags
        self.other_nutritional_substances_tags = other_nutritional_substances_tags
        self.packaging = packaging
        self.packaging_hierarchy = packaging_hierarchy
        self.packaging_lc = packaging_lc
        self.packaging_old = packaging_old
        self.packaging_old_before_taxonomization = packaging_old_before_taxonomization
        self.packaging_tags = packaging_tags
        self.packagings = packagings
        self.photographers = photographers
        self.photographers_tags = photographers_tags
        self.pnns_groups_1 = pnns_groups_1
        self.pnns_groups_1__tags = pnns_groups_1__tags
        self.pnns_groups_2 = pnns_groups_2
        self.pnns_groups_2__tags = pnns_groups_2__tags
        self.popularity_key = popularity_key
        self.popularity_tags = popularity_tags
        self.product_name = product_name
        self.product_name_en = product_name_en
        self.product_name_en_debug_tags = product_name_en_debug_tags
        self.product_name_en_imported = product_name_en_imported
        self.product_quantity = product_quantity
        self.purchase_places = purchase_places
        self.purchase_places_debug_tags = purchase_places_debug_tags
        self.purchase_places_tags = purchase_places_tags
        self.quantity = quantity
        self.quantity_debug_tags = quantity_debug_tags
        self.removed_countries_tags = removed_countries_tags
        self.rev = rev
        self.scans_n = scans_n
        self.selected_images = selected_images
        self.serving_quantity = serving_quantity
        self.serving_size = serving_size
        self.serving_size_debug_tags = serving_size_debug_tags
        self.serving_size_imported = serving_size_imported
        self.sortkey = sortkey
        self.sources = sources
        self.sources_fields = sources_fields
        self.states = states
        self.states_hierarchy = states_hierarchy
        self.states_tags = states_tags
        self.stores = stores
        self.stores_debug_tags = stores_debug_tags
        self.stores_tags = stores_tags
        self.traces = traces
        self.traces_debug_tags = traces_debug_tags
        self.traces_from_ingredients = traces_from_ingredients
        self.traces_from_user = traces_from_user
        self.traces_hierarchy = traces_hierarchy
        self.traces_tags = traces_tags
        self.unique_scans_n = unique_scans_n
        self.unknown_ingredients_n = unknown_ingredients_n
        self.unknown_nutrients_tags = unknown_nutrients_tags
        self.update_key = update_key
        self.vitamins_prev_tags = vitamins_prev_tags
        self.vitamins_tags = vitamins_tags


class Welcome10:
    code: str
    product: Product
    status: int
    status_verbose: str

    def __init__(self, code: str, product: Product, status: int, status_verbose: str) -> None:
        self.code = code
        self.product = product
        self.status = status
        self.status_verbose = status_verbose
