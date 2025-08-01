import re
import sys

shuffle = (
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59,),
    (0, 30, 1, 31, 2, 32, 3, 33, 4, 34, 5, 35, 6, 36, 7, 37, 8, 38, 9, 39, 10, 40, 11, 41, 12, 42, 13, 43, 14, 44, 15, 45, 16, 46, 17, 47, 18, 48, 19, 49, 20, 50, 21, 51, 22, 52, 23, 53, 24, 54, 25, 55, 26, 56, 27, 57, 28, 58, 29, 59,),
    (0, 20, 40, 1, 21, 41, 2, 22, 42, 3, 23, 43, 4, 24, 44, 5, 25, 45, 6, 26, 46, 7, 27, 47, 8, 28, 48, 9, 29, 49, 10, 30, 50, 11, 31, 51, 12, 32, 52, 13, 33, 53, 14, 34, 54, 15, 35, 55, 16, 36, 56, 17, 37, 57, 18, 38, 58, 19, 39, 59,),
    (0, 12, 24, 36, 48, 1, 13, 25, 37, 49, 2, 14, 26, 38, 50, 3, 15, 27, 39, 51, 4, 16, 28, 40, 52, 5, 17, 29, 41, 53, 6, 18, 30, 42, 54, 7, 19, 31, 43, 55, 8, 20, 32, 44, 56, 9, 21, 33, 45, 57, 10, 22, 34, 46, 58, 11, 23, 35, 47, 59,),
    (0, 9, 18, 27, 36, 44, 52, 1, 10, 19, 28, 37, 45, 53, 2, 11, 20, 29, 38, 46, 54, 3, 12, 21, 30, 39, 47, 55, 4, 13, 22, 31, 40, 48, 56, 5, 14, 23, 32, 41, 49, 57, 6, 15, 24, 33, 42, 50, 58, 7, 16, 25, 34, 43, 51, 59, 8, 17, 26, 35,),
    (0, 7, 14, 21, 28, 35, 42, 48, 54, 1, 8, 15, 22, 29, 36, 43, 49, 55, 2, 9, 16, 23, 30, 37, 44, 50, 56, 3, 10, 17, 24, 31, 38, 45, 51, 57, 4, 11, 18, 25, 32, 39, 46, 52, 58, 5, 12, 19, 26, 33, 40, 47, 53, 59, 6, 13, 20, 27, 34, 41,),
    (0, 6, 12, 18, 24, 30, 35, 40, 45, 50, 55, 1, 7, 13, 19, 25, 31, 36, 41, 46, 51, 56, 2, 8, 14, 20, 26, 32, 37, 42, 47, 52, 57, 3, 9, 15, 21, 27, 33, 38, 43, 48, 53, 58, 4, 10, 16, 22, 28, 34, 39, 44, 49, 54, 59, 5, 11, 17, 23, 29,),
    (0, 5, 10, 15, 20, 25, 30, 35, 40, 44, 48, 52, 56, 1, 6, 11, 16, 21, 26, 31, 36, 41, 45, 49, 53, 57, 2, 7, 12, 17, 22, 27, 32, 37, 42, 46, 50, 54, 58, 3, 8, 13, 18, 23, 28, 33, 38, 43, 47, 51, 55, 59, 4, 9, 14, 19, 24, 29, 34, 39,),
    (0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 39, 42, 45, 48, 51, 54, 57, 1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 40, 43, 46, 49, 52, 55, 58, 2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 41, 44, 47, 50, 53, 56, 59, 3, 7, 11, 15, 19, 23, 27, 31, 35,),
    (0, 4, 8, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 1, 5, 9, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49, 52, 55, 58, 2, 6, 10, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44, 47, 50, 53, 56, 59, 3, 7, 11,),
    (0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 59, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57,),
    (0, 3, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 1, 4, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 2, 5,),
    (0, 3, 6, 9, 12, 15, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 1, 4, 7, 10, 13, 16, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 2, 5, 8, 11, 14, 17,),
    (0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 44, 46, 48, 50, 52, 54, 56, 58, 1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 45, 47, 49, 51, 53, 55, 57, 59, 2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41,),
    (0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41,),
    (0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45,),
)

negate = (
    "878F0B496878F0B0",
    "9607CF2B59607CF0",
    "A59E03CD2A59E030",
    "B416C7AF1B416C70",
    "C3AD1A41EC3AD1B0",
    "D225DE23DD225DF0",
    "E1BC12C5AE1BC130",
    "F034D6A79F034D70",
    "F0B496878F0B4970",
    "E13C52E5BE13C530",
    "A59E03CD2A59E030",
    "B416C7AF1B416C70",
    "C32D5A61FC32D5B0",
    "D2A59E03CD2A59F0",
    "878F0B496878F0B0",
    "9607CF2B59607CF0",
)


def unobfuscate(row):
    if len(row) != 16:
        raise Exception("Bad row length")

    index     = int(row[-1], 16)
    row_value = row.translate(row.maketrans("76543210EFABCD98", "0123456789ABCDEF"))

    bytes1 = bytes.fromhex(row_value)
    bytes2 = bytes.fromhex(negate[index])

    xor_bytes = bytes([b1 ^ b2 for b1, b2 in zip(bytes1, bytes2)])
    xor_hex   = xor_bytes.hex()
    xor_bin   = format(int(xor_hex, 16), "064b")

    encoded_data = ""

    for x in range(60):
        encoded_data += xor_bin[shuffle[index][x]]
    return encoded_data


def decode_data(encoded_data):
    raw               = encoded_data
    offset            = 0
    end_of_data       = 0
    payload_type      = ""
    payload_type_size = 5

    while not end_of_data:
        payload_type = raw[offset: offset + payload_type_size]
        offset      += payload_type_size

        if not payload_type:
            end_of_data = 1

        if payload_type == "00000":
            payload_00000_size = 4

            payload_data = raw[offset: offset + payload_00000_size]
            offset      += payload_00000_size

            if payload_data == "0000":
                end_of_data = 1
                print("00000/EndOfData")
            elif payload_data == "0001":
                print("00000/StartOfData", end=" ")
            else:
                print(f"Don't recognize type {payload_type} data: {payload_data}", end=" ")

        elif payload_type == "00001":
            payload_00001_size = 12

            payload_data = raw[offset: offset + payload_00001_size]
            offset      += payload_00001_size

            print(f"00001/ID: {int(payload_data, 2)}", end=" ")

        elif payload_type == "00010":
            payload_00010_size = 12

            payload_data = raw[offset: offset + payload_00010_size]
            offset      += payload_00010_size

            print(f"00010/TrickStick: {int(payload_data, 2)}", end=" ")

        elif payload_type == "00011":
            payload_00011_size = 12

            payload_data = raw[offset: offset + payload_00011_size]
            offset      += payload_00011_size

            day     = int(payload_data[0:5], 2)
            month   = int(payload_data[5:9], 2)
            unknown = int(payload_data[9:12], 2)

            print(f"00011/StartDate: {month}/{day}", end=" ")

        elif payload_type == "00100":
            payload_00100_size = 12

            payload_data = raw[offset: offset + payload_00100_size]
            offset      += payload_00100_size

            day     = int(payload_data[0:5], 2)
            month   = int(payload_data[5:9], 2)
            unknown = int(payload_data[9:12], 2)

            print(f"00100/EndDate: {month}/{day}", end=" ")

        elif payload_type == "00111":
            name         = ""
            payload_data = ""

            shift = 1

            letter        = raw[offset: offset + 5]
            offset       += 5
            payload_data += letter

            while letter != "00000":
                if letter == "00001":
                    name += " "
                    shift = 1
                else:
                    name += chr(int(letter, 2) - 1 + (64 if shift else 96))
                    shift = 0

                letter        = raw[offset: offset + 5]
                offset       += 5
                payload_data += letter

                if not letter:
                    letter = "00000"

            print(f"00111/Name: {name}", end=" ")

        elif payload_type == "01000":
            payload_01000_size = 30

            payload_data = raw[offset: offset + payload_01000_size]
            offset      += payload_01000_size

            print(f"01000/Gamertag: {payload_data}", end=" ")

        elif payload_type == "01001":
            payload_01001_size = 2

            payload_data = raw[offset: offset + payload_01001_size]
            offset      += payload_01001_size

            print(f"01001/Wildcard: {int(payload_data, 2)}", end=" ")

        elif payload_type == "01010":
            payload_01010_size = 4

            payload_data = raw[offset: offset + payload_01010_size]
            offset      += payload_01010_size

            print(f"01010/Variant: {int(payload_data, 2)}", end=" ")

        elif payload_type == "01011":
            payload_01011_size = 3

            payload_data = raw[offset: offset + payload_01011_size]
            offset      += payload_01011_size

            print(f"01011/Size: {payload_data}", end=" ")

        elif payload_type == "10000":
            payload_10000_size = 16

            payload_data = raw[offset: offset + payload_10000_size]
            offset      += payload_10000_size

            print(f"10000/Sparse: {payload_data}", end=" ")

        elif payload_type == "10001":
            payload_10001_size = 4

            payload_data = raw[offset: offset + payload_10001_size]
            offset      += payload_10001_size

            print(f"10001/Timewarp: {payload_data}", end=" ")

        elif payload_type == "10010":
            payload_10010_size = 3

            payload_data = raw[offset: offset + payload_10010_size]
            offset      += payload_10010_size

            print(f"10010/Weather: {payload_data}", end=" ")

        elif payload_type == "10011":
            payload_10011_size = 8

            payload_data = raw[offset: offset + payload_10011_size]
            offset      += payload_10011_size

            print(f"10011/Duration: {payload_data}", end=" ")

        elif payload_type == "10100":
            payload_10100_size = 12

            payload_data = raw[offset: offset + payload_10100_size]
            offset      += payload_10100_size

            print(f"10100/ID: {int(payload_data, 2)}", end=" ")

        elif payload_type == "10110":
            payload_10110_size = 5

            payload_data = raw[offset: offset + payload_10110_size]
            offset      += payload_10110_size

            print(f"10110/Reuse: {payload_data}", end=" ")

        elif payload_type == "11000":
            payload_11000_size = 10

            payload_data = raw[offset: offset + payload_11000_size]
            offset      += payload_11000_size

            value     = int(payload_data[0:7], 2)
            magnitude = int(payload_data[7:10], 2)

            cost = value * (10 ** magnitude)

            print(f"11000/UseCost: {cost}", end=" ")

        elif payload_type == "11010":
            payload_11001_size = 4

            payload_data = raw[offset: offset + payload_11001_size]
            offset      += payload_11001_size

            print(f"11010/?: {payload_data}", end=" ")

        elif payload_type == "11101":
            color_count = raw[offset: offset + 4]
            offset     += 4

            items = ""

            item_length  = 8
            color_length = 4

            color_names = (
                "Default",
                "Red",
                "Orange",
                "Yellow",
                "Brown",
                "Pink",
                "Purple",
                "Green",
                "Light Green",
                "Blue",
                "Cyan",
                "Violet",
                "Black",
                "White",
                "14",
                "15",
            )

            color_count = int(color_count, 2)

            for i in range(color_count):
                item    = raw[offset: offset + item_length]
                offset += item_length

                item_color = raw[offset: offset + color_length]
                offset    += color_length

                item_color = int(item_color, 2)

                if len(color_names) > item_color:
                    item_color = color_names[item_color]

                items += f"{item_color} {lookup_accessory(int(item, 2))}{(', ' if (i + 1 != color_count) else '')}"

            count   = raw[offset: offset + 4]
            offset += 4

            count = int(count, 2)

            if color_count:
                items += (', ' if count else '')

            for i in range(count):
                item    = raw[offset: offset + item_length]
                offset += item_length

                items += f"{lookup_accessory(int(item, 2))}{(', ' if (i + 1 != count) else '')}"

            total_count = color_count + count

            print(f"11101/Accessory: {total_count} item{('s ' if (total_count > 1) else ' ')}{items}", end=" ")

        else:
            print(f"Don't recognize this payload type: {payload_type}")
            end_of_data = 1


def lookup_accessory(item):
    names = (
        "",
        "Retro Disco Wig",
        "Breegull Carrier",
        "Shark Tooth Necklace",
        "Cool Shades",
        "Howdy Pardner Hat",
        "Doenut Stalker",
        "Inca Bracelet",
        "Fur Boots",
        "Fair Dinkum Hat",
        "King Tut's Hat",
        "Yokel Teeth",
        "Jurassic Hair",
        "Yee-Haw Hat",
        "Señor Sombrero",
        "Pillager's Helmet",
        "Thunder Cut",
        "Beanie Cap",
        "Weather-Girl Wig",
        "Diggerling Helmet Mk1",
        "Gas Mask",
        "Party Horns",
        "Kazooie Talons",
        "Caterpillars",
        "Yee-Haw Spurs",
        "Super Hero Mask",
        "School Cap",
        "Baseball Cap",
        "Yee-Haw Saddle",
        "Tiara of Tranquility",
        "Slim Tache",
        "Spiked Collar",
        "Geek Glasses",
        "Reporter's Camera",
        "Bling Teeth",
        "Bow",
        "Fez",
        "Fake Winner's Rosette",
        "Diamond Choker",
        "Blackeye Patch",
        "Tap Shoes",
        "Ballet Shoes",
        "Crown",
        "Handlebar Mustache",
        "Football Helmet",
        "Sweaty Wrist Band",
        "Bling Bangle",
        "Beaded Wig",
        "Rashberry Badge",
        "Secret Agent Bowtie",
        "Bling Bracelet",
        "Crystal Broach",
        "Bunnycomb Ears",
        "Bushy Mustache",
        "Soupswill Cook Hat",
        "The Von Ghoul",
        "Yee-Haw Boots",
        "Butcha's",
        "Diamond Necklace",
        "Combat Boots",
        "Pegasus Wings",
        "Romance Earrings",
        "Mermaid Earrings",
        "Big Bling Earrings",
        "Silver Medal",
        "Big Jolly Lips",
        "Comedian's Nose",
        "Buck Teeth",
        "Gold Medal",
        "Soccer Boots",
        "Squazzil Hat",
        "DanceGlow",
        "Pendant Necklace",
        "Halo of Hardness",
        "Safety Helmet",
        "Sweaty Head Band",
        "Breegull Waders",
        "Bronze Medal",
        "Leafos Medallion",
        "Baby's Bib",
        "Toff Monocle",
        "Astro-Walkers",
        "Halloween Bolts",
        "Bling Nose-Ring",
        "Dellmonty",
        "Traditional Watch",
        "Mermaid Necklace",
        "Eighties Watch",
        "Tussle Tricorn",
        "Rashberry Hat",
        "Rashberry Helmet",
        "Reading Glasses",
        "Red Nose",
        "Robber's Mask",
        "Extreme Sports Goggles",
        "Santa Hat",
        "Non-Resident Scarf",
        "Sea-Shell Collar",
        "Bunnycomb Slippers",
        "Snow Shoes",
        "Belly-Splash Specials",
        "Granny's Tache",
        "Funky Tie",
        "Conga's Top Hat",
        "Breegull Turbo Trainers",
        "Ga-Ga Necklace",
        "Dastardos Scarf",
        "Bell",
        "Bonnet",
        "Buzzlegum Keeper Hat",
        "Buttercup Hair Flower",
        "Daisy Hair Flower",
        "Bling Earrings",
        "Not-so-Bling Earrings",
        "Pendant Earrings",
        "Pearly Bracelet",
        "Poppy Hair Flower",
        "Barkbark Tags",
        "Sunflower Hair Flower",
        "Student's Hat",
        "Comedian's Choice",
        "Strong 'n' Macho",
        "Cook Hat",
        "Tail Bow",
        "Super Hero Belt",
        "Fruity Hat",
        "Mr. Pants Hat",
        "Sailor Hat",
        "Conkerific Helmet",
        "Vela Wig",
        "Juno Helmet",
        "Grunty Hat",
        "Jam-Jars Hat",
        "Binner's Hat",
        "Princess Hat",
        "Von Ghoul Helmet",
        "Saberman Helmet",
        "Ortho's Spare Hat",
        "Knight Helmet",
        "Headphones",
        "Jiggy Earrings",
        "Lupus Ears",
        "Disco Shades",
        "Flying Goggles",
        "Bottles' Glasses",
        "Romantic Flower",
        "Battletoad Bracelets",
        "Prisoner Bracelet",
        "Sheriff's Badge",
        "Clockwork Key",
        "Kameo Wings",
        "Fake Fin",
        "Flamenco Shoes",
        "Ash Slippers",
        "Cleopatra's Necklace",
        "Stethoscope",
        "Star Earrings",
        "Furry Earmuffs",
        "Lucky Earrings",
        "Harlequin Mask",
        "Ponocky Club Hat",
        "Camo Cap",
        "Apples and Pears Hat",
        "Chewnicorn Horn",
        "Firefighter's Hat",
        "Nurse's Hat",
        "Golden Necklace",
        "Edo Wig",
        "Pointed Hat",
        "Comrade's Hat",
        "Dentures Of The Night",
        "Turkish Slippers",
        "Bullfighter's Hat",
        "Caesar's Hat",
        "Clogs",
        "Homburg",
        "Safari Hat",
        "La Parisienne",
        "Yeoman's Helm",
        "Hula Necklace",
        "Mountie Hat",
        "Tribal Mask",
        "Liberty Crown",
        "Jokduri",
    )

    if len(names) > item:
        return names[item]
    else:
        return "Unknown"


if len(sys.argv) < 2:
    print("Usage: python pv_decoder.py <input_file> [-debug]\n")
    sys.exit(2)

input_file = sys.argv[1]
debug_mode = "-debug" in sys.argv

try:
    with open(input_file, "r") as file:
        for line in file:
            pinata_card = re.split("\t", line.strip())
            barcode     = pinata_card[0]
            filename    = pinata_card[1]

            encoded_data = ""

            for row in re.split(r"\s", barcode):
                encoded_data += unobfuscate(row) + " "

            if debug_mode:
                print(f"{filename} ->", end=" ")
                decode_data(encoded_data.replace(" ", ""))
            else:
                print(f"{encoded_data[0:-1]}\t{filename}")
except FileNotFoundError:
    print("Error: \033[91m" + input_file + " not found\033[0m\n")
    sys.exit(1)
except Exception as e:
    print("Error: \033[91m" + str(e) + "\033[0m\n")
    sys.exit(1)
