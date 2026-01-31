import svgwrite
import streamlit.components.v1 as components

def draw_city(plan):
    width, height = 720, 460
    dwg = svgwrite.Drawing(size=(width, height))

    # Background
    dwg.add(dwg.rect(
        insert=(0, 0),
        size=(width, height),
        fill="#f3f3f3"
    ))

    # Roads
    road_w = 26 if plan["road_density"] == "high" else 14

    for x in range(120, width, 200):
        dwg.add(dwg.rect(
            insert=(x, 0),
            size=(road_w, height),
            fill="#9e9e9e"
        ))

    for y in range(90, height, 150):
        dwg.add(dwg.rect(
            insert=(0, y),
            size=(width, road_w),
            fill="#9e9e9e"
        ))

    # Residential blocks
    dwg.add(dwg.rect((40, 40), (120, 80), fill="#cfe2f3"))
    dwg.add(dwg.rect((260, 40), (120, 80), fill="#cfe2f3"))

    # Green spaces
    if plan["green_level"] == "high":
        dwg.add(dwg.rect((460, 60), (180, 100), fill="green", rx=25))
        dwg.add(dwg.rect((90, 260), (200, 120), fill="green", rx=25))

    # Render SVG in Streamlit
    components.html(dwg.tostring(), height=500)
