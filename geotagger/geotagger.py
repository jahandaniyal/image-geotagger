import pyexiv2
from .utils import Rational


def to_deg(value, loc):
    if value < 0:
        loc_value = loc[0]
    elif value > 0:
        loc_value = loc[1]
    else:
        loc_value = ""
    abs_value = abs(value)
    deg = int(abs_value)
    t1 = (abs_value - deg) * 60
    min = int(t1)
    sec = round((t1 - min) * 60, 5)
    return (deg, min, sec, loc_value)


def set_gps_metadata(img_file, lat, lng):
    """Adds GPS information as EXIF metadata

    Keyword arguments:
    file_name -- image file
    lat -- latitude (as float)
    lng -- longitude (as float)

    """
    try:
        image = pyexiv2.Image(img_file)
    except:
        raise FileNotFoundError

    lat_deg = to_deg(lat, ["S", "N"])
    lng_deg = to_deg(lng, ["W", "E"])

    # convert decimal coordinates into degrees, munutes and seconds
    exiv_lat = (str(Rational(lat_deg[0] * 60 + lat_deg[1], 60)), str(Rational(lat_deg[2] * 100, 6000)),
                str(Rational(0, 1)))
    exiv_lng = (str(Rational(lng_deg[0] * 60 + lng_deg[1], 60)), str(Rational(lng_deg[2] * 100, 6000)),
                str(Rational(0, 1)))

    exif_dict = {}

    exif_dict["Exif.GPSInfo.GPSLatitude"] = " ".join(exiv_lat)
    exif_dict["Exif.GPSInfo.GPSLatitudeRef"] = lat_deg[3]
    exif_dict["Exif.GPSInfo.GPSLongitude"] = " ".join(exiv_lng)
    exif_dict["Exif.GPSInfo.GPSLongitudeRef"] = lng_deg[3]
    exif_dict["Exif.Image.GPSTag"] = 654
    exif_dict["Exif.GPSInfo.GPSMapDatum"] = "WGS-84"
    exif_dict["Exif.GPSInfo.GPSVersionID"] = '2 0 0 0'

    image.modify_exif(exif_dict)
    print(image.read_exif())


def read_exif_data(img_file):
    image = pyexiv2.Image(img_file)
    return image.read_exif()


if __name__=="__main__":
    set_gps_metadata('samples/img.jpg', 52.497008189053105, 13.223473351164454)