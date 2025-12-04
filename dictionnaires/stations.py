from collections import namedtuple

FILENAME = 'meteo-france-stations.csv'

def build_stations_dict(csvfile):
    """
    retourne un dictionnaire des stations météo du fichier passé en argument

    Args:
        csvfile: un fichier au format csv contenant une liste de stations météo

    Returns:
        dictionnaire de namedtuple des informations relatives aux stations météo
        
    >>> d = build_stations_dict(FILENAME)
    >>> print(d['NICE'])
    Station(ID='07690', Latitude=43.648833, Longitude=7.209, Altitude=2)
    >>> print(d['BELLE ILE-LE TALUT'])
    Station(ID='07207', Latitude=47.294333, Longitude=-3.218333, Altitude=34)
    >>> print(d['CAYENNE-MATOURY'])
    Station(ID='81405', Latitude=4.822333, Longitude=-52.365333, Altitude=4)
    >>> print(d['NICE'].Latitude)
    43.648833
    """
    result = {}
    with open(csvfile) as file:
        keys = file.readline().strip().split(";")
        nameIndex = keys.index("Nom")
        del keys[nameIndex]
        Data = namedtuple("Station", keys)

        for line in file.readlines():
            splitLine = line.strip().split(";")
            name = splitLine[nameIndex]
            del splitLine[nameIndex]
            result[name] = Data(
                splitLine[0],
                float(splitLine[1]),
                float(splitLine[2]),
                int(splitLine[3])
            )

    return result

def main():
    d = build_stations_dict(FILENAME)
    print(d['NICE'])

if __name__ == '__main__':
    main()
