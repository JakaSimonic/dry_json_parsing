from dataclasses import dataclass, field
from typing import Optional

from dataclasses_json import dataclass_json, config


def single(**kwargs):
    def _deserialize(value):
        if not value:
            raise ValueError("single deserializer does not support None type.")
        return value.get("value", None)
    
    return field(default=None,
            metadata=config(
                decoder=_deserialize,
            ),
            **kwargs
        )

def collection(field_name, **kwargs):
    def _deserialize(datagroup):
        if not datagroup:
            raise ValueError("collection deserializer does not support None type.")
        collection_items = []
        for _, value in datagroup.get("collections", {}).items():
            item = value.get("properties", {}).get(field_name)
            if item:
                collection_items.append(item)
        return collection_items
    
    return field(default=None,
            metadata=config(
                decoder=_deserialize,
            ),
            **kwargs
        )
    

@dataclass_json
@dataclass
class Properties:
    eburyEntity: Optional[str] = single()
    bearerSharesIssuer: Optional[str] = single()
    clientAge: Optional[str] = single()
    companyType: Optional[str] = single()
    complexLegalStructure: Optional[str] = single()
    country: Optional[str] = single()
    eburyCountry: Optional[str] = single()
    countryOfDomicile: Optional[str] = single()
    countryOfIncorporation: Optional[str] = single()
    deliveryChannel: Optional[str] = single()
    destinationOfFundsdatagroup: Optional[list[str]] = collection(
        field_name="destinationOfFunds",
    )
    doesTheClientDeclareRegularIncome: Optional[str] = single()
    industry: Optional[str] = single()
    internalListsOutcome: Optional[str] = single()
    isANonProfitOrganisationCharity: Optional[str] = single()
    isASpv: Optional[str] = single()
    naics: Optional[list[str]] = single()
    nationality: Optional[str] = single()
    negativeMediaOutcome: Optional[str] = single()
    otherMatchesOutcome: Optional[str] = single()
    originOfFundsdatagroup: Optional[list[str]] = collection(field_name="originOfFunds")
    pepOutcome: Optional[str] = single()
    product: Optional[list[str]] = collection(field_name="productJourney")
    recentlyIncorporated: Optional[str] = single()
    sanctionsOutcome: Optional[str] = single()
    specialComplianceFramework: Optional[str] = single()
    totalFxFlowPAGbp: Optional[str] = single()
    uboLocations: Optional[list[str]] = single()
    countryOfResidence: Optional[str] = single()
    role: Optional[str] = single()
    riskRating: Optional[str] = single()
    accountNumber: Optional[str] = single()
    clientStatus: Optional[str] = single()
    legalEntityName: Optional[str] = single()
    complianceRiskOverride: Optional[str] = single()
    nextReviewDate: Optional[str] = single()

    def __post_init__(self):
        self.naics = self.naics.split("|")
        self.uboLocations = self.uboLocations.split("|")

@dataclass_json
@dataclass
class Payload:
    id: Optional[str] = None
    type: Optional[str] = None
    properties: Optional[Properties] = None
    status: Optional[int] = None
    userId: Optional[str] = None
    created: Optional[str] = None
    alternateId: Optional[str] = None
    version: Optional[int] = None


@dataclass_json
@dataclass
class FenexPayload:
    payload: Optional[Payload] = None


with open("fenx-payload.json") as f:
    payload = FenexPayload.from_json(f.read())
    print(payload)