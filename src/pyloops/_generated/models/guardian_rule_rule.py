from enum import StrEnum


class GuardianRuleRule(StrEnum):
    BAREARRAYNODES = "bareArrayNodes"
    EMAILWITHOUTMAILTOBUTTONHREFS = "emailWithoutMailtoButtonHrefs"
    EMAILWITHOUTMAILTOIMAGEHREFS = "emailWithoutMailtoImageHrefs"
    EMAILWITHOUTMAILTOLINKHREFS = "emailWithoutMailtoLinkHrefs"
    INVALIDBUTTONHREFS = "invalidButtonHrefs"
    INVALIDCUSTOMDATAVARIABLES = "invalidCustomDataVariables"
    INVALIDLINKHREFS = "invalidLinkHrefs"
    MISSINGBUTTONHREFS = "missingButtonHrefs"
    MISSINGFALLBACKCONTACTPROPERTIES = "missingFallbackContactProperties"
    MISSINGFALLBACKEVENTPROPERTIES = "missingFallbackEventProperties"
    MISSINGLINKHREFS = "missingLinkHrefs"
    MISSINGREQUIREDDATAVARIABLES = "missingRequiredDataVariables"
    MISSINGSOCIALICONHREFS = "missingSocialIconHrefs"
    SHORTENEDYOUTUBEBUTTONHREFS = "shortenedYouTubeButtonHrefs"
    SHORTENEDYOUTUBEIMAGEHREFS = "shortenedYouTubeImageHrefs"
    SHORTENEDYOUTUBELINKHREFS = "shortenedYouTubeLinkHrefs"
    UNSUPPORTEDCONTACTPROPERTIES = "unsupportedContactProperties"
    UNSUPPORTEDDATAVARIABLES = "unsupportedDataVariables"
    UNSUPPORTEDEVENTPROPERTIES = "unsupportedEventProperties"

    def __str__(self) -> str:
        return str(self.value)
