from PIL import Image, ImageFont, ImageDraw


def circle(draws, center, radius, fill):
    draws.ellipse((center[0] - radius + 1, center[1] - radius + 1,
                   center[0] + radius - 1, center[1] + radius - 1), fill=fill, outline=None)


def human_format(num):
    num = float('{:.3g}'.format(num))
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    return '{}{}'.format('{:f}'.format(num).rstrip('0').rstrip('.'), ['', 'K', 'M', 'B', 'T'][magnitude])


Background = Image.open("Images/Xp_Background_With_Boarder.png")
pfp = Image.open("Images/Discord.png")  # Image use is 200,200px
mask_im = Image.open("Images/mask_circle.jpg")
draw = ImageDraw.Draw(Background)

rank_level = ImageFont.truetype('Files/Helios Regular.ttf', 53)
font1 = ImageFont.truetype('Files/Helios Regular.ttf', 30)

name = "Example#1234"
xp = 250
next_xp = 500
full = 880
level = 5
rank = 3
W = 44  # Width of line on progress bar
COLOR = "#007FFF"
percentage = xp / next_xp * 100

#  Avoids line going off the bar
if percentage < 6:
    percentage = 6

coords = ((percentage / 100) * full, 230, 55, 230)
text_size = draw.textsize(name, font=font1)

#  Adds line with circle at ends for cleaner look
draw.line(coords, width=W, fill=COLOR)
circle(draw, (coords[0], coords[1]), W / 2, COLOR)
circle(draw, (coords[2], coords[3]), W / 2, COLOR)

score = F"{human_format(xp)}/{human_format(next_xp)}"
rank_num = F'#{human_format(rank)}'
level = human_format(level)

text_w, text_h = draw.textsize(score, font=font1)
draw.text((880 - text_w, 240 - text_h), score, (0, 0, 0), font=font1)

rank_num_size = draw.textsize(rank_num, font=rank_level)
level_size = draw.textsize(level, font=rank_level)
background_size = Background.size
pfp_size = pfp.size

draw.text((110 - (rank_num_size[0] / 2), 105 - (rank_num_size[1] / 2)), rank_num, (255, 255, 255), font=rank_level)
draw.text((810 - (level_size[0] / 2), 105 - (level_size[1] / 2)), level, (255, 255, 255), font=rank_level)
draw.text((round(background_size[0] / 2 - text_size[0] / 2), round(background_size[1] / 2 - text_size[1] / 2 + 50)),
          name, (255, 255, 255), font=font1)

pfp = pfp.resize((140, 140))
Background.paste(pfp, (round(background_size[0] / 2 - pfp_size[0] / 2 + 20),
                       round(background_size[1] / 2 - pfp_size[0] / 2 - 10)), mask_im)

Background.save("Rank.png", quality=100)
