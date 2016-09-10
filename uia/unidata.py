studies = {
     'BACFIL1':     {'courses': ['FIL100-1', 'FIL103-1', 'FIL104-1'],
                     'title': 'Anvendt filosofi - Bachelor 1. år'},
     'BACFIL2':     {'courses': ['FIL200-1', 'EX-102-1', 'EX-100-1'],
                     'title': 'Anvendt filosofi - Bachelor 2. år'},
     'BACBLU1':     {'courses': ['NHB100-1', 'BUL100-1'],
                     'title': 'Barnehagelærerutdanning - Bachelor 1.år'},
     'BACBLU2':     {'courses': ['STM100-1', 'KKK100-1'],
                     'title': 'Barnehagelærerutdanning - Bachelor 2.år'},
     'BACBLU-G1':   {'courses': ['NHB100-G', 'BUL100-G'],
                     'title': 'Barnehagelærerutdanning (Grimstad) - Bachelor 1.år'},
     'BACBLU-G2':   {'courses': ['STM100-G', 'KKK100-G'],
                     'title': 'Barnehagelærerutdanning (Grimstad) - Bachelor 2.år'},
     'BACBIOING1':  {'courses': ['KJ-111-1', 'BIO-111-1', 'ML-112-1'],
                     'title': 'Bioingeniørfag - Bachelor 1. år'},
     'BACBIOING2':  {'courses': ['SV-125-1', 'ML-306-1', 'ML-208-1'],
                     'title': 'Bioingeniørfag - Bachelor 2. år'},
     'BACBIOING3':  {'courses': ['ML-302-1', 'ML-313-1', 'ML-310-1'],
                     'title': 'Bioingeniørfag - Bachelor 3. år'},
     'BACBIO1':     {'courses': ['BIO111-1', 'BIO104-1', 'BIO112-1'],
                     'title': 'Biologi - Bachelor 1. år'},
     'BACBIO2':     {'courses': ['KJ-111-1', 'BIO206-1', 'ML-208-1'],
                     'title': 'Biologi - Bachelor 2. år'},
     'BACBIO3':     {'courses': ['BIO204-1', 'MA-168-1', 'BIO207-1'],
                     'title': 'Biologi - Bachelor 3. år'},
     'MASTBYGG':    {'courses': ['BYG404-G', 'BYG504-G', 'BYG405-G', 'IND422-G'],
                     'title': 'Bygg - Master 1. år'},
     'V-REKTUTD':   {'courses': ['ORG964-1'],
                     'title': 'Den nasjonale rektorutdanningen - 1. semester'},
     'DRAMA60':     {'courses': ['DR-126-1', 'DR-127-1'],
                     'title': 'Drama - Årsstudium'},
     'V-ENGELSK1':  {'courses': ['EN-912-1', 'EN-911-1'],
                     'title': 'Engelsk 1 (1.-7. trinn). Videreutdanning for lærere'},
     'V-ENGELSK2':  {'courses': ['EN-910-1', 'EN-909-1'],
                     'title': 'Engelsk 2 (5.-10. trinn). Videreutdanning for lærere'},
     'MASTENG':     {'courses': ['EN-410-1', 'EN-411-1', 'EN-419-1', 'EN-437-1'],
                     'title': 'Engelsk - Master 1. år'},
     'BACENG09':    {'courses': ['EN-103-1', 'EN-122-1', 'EN-147-1'],
                     'title': 'Engelsk - Bachelor 1. år'},
     'BACIT1':      {'courses': ['IS-100-1', 'IS-104-1', 'IS-109-1', 'IS-111-1'],
                     'title': 'IT og informasjonssystemer - Bachelor 1. år'},
     'BACIT2':      {'courses': ['IS-200-1', 'IS-201-1', 'IS-202-1'],
                     'title': 'IT og informasjonssystemer - Bachelor 2. år'}}

s = sorted(studies, key=lambda x: studies[x]['title'])