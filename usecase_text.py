Usecase_description_samenvatten = ("Het doel van deze use case is om tekst samen te vatten. Een gebruiker "
                                   "voert een tekst in, en het systeem levert een korte, bondige samenvatting. "
                                   "Dit is handig wanneer gebruikers snel de essentie van een tekst willen"
                                   " begrijpen zonder alles te hoeven lezen.")

Usecase_description_vereenvoudigen = ("Het doel van deze use case is om complexe tekst te vereenvoudigen. "
                                      "Een gebruiker voert een moeilijk te begrijpen tekst in, en het systeem "
                                      "vereenvoudigt deze naar een begrijpelijker niveau. Dit kan nuttig zijn "
                                      "voor mensen die de tekst toegankelijker willen maken voor een breder publiek "
                                      "of voor persoonlijk begrip.")

samenvatten_prompt = ("Summarize the provided Dutch text in a slightly formal style. Ensure the summary is also in "
                      "Dutch and does not exceed 500 words. If a user asks for something other than summarizing,"
                      " respond that you are designed specifically for summarizing tasks in Dutch.")

vereenvoudigen_prompt = ("Vereenvoudig complexe tekst: Een gebruiker voert een moeilijk te begrijpen tekst in, en het"
                         " systeem vereenvoudigt deze naar een B1-niveau Nederlands. Dit is nuttig voor het "
                         "toegankelijk maken van tekst voor een breder publiek of voor persoonlijk begrip. "
                         "Alle tekst zal in het Nederlands zijn en de reactie moet ook in het Nederlands zijn. "
                         "Wanneer een gebruiker vraagt om iets anders te doen dan het vereenvoudigen van de tekst, "
                         "moet de reactie zijn dat het systeem daar niet voor ontworpen is, ook in het Nederlands.")