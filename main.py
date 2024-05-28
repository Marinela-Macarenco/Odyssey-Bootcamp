import streamlit as st
import requests
import review
import json

#Interfață streamlit prima pagină
def pagina_principala():
    st.title("Formula Porsche")
    st.write("The first interactive platform for Porsche fans.")
    st.write("If you're a Porsche enthusiast, you're in the right place!"
              "Here, you'll find everything you want to know about the"
              " legendary Porsche cars.")


    st.image("images/911_red.png", caption="Porsche GT3 RS")
    st.write("Watch this fascinating interview with Porsche engineers to learn"
              " more about the creation of their amazing cars.")
    st.video("https://www.youtube.com/watch?v=nJL9v8KXmmo",
              loop=True, autoplay=True, muted=True)


    st.write("## Porsche Information")
    porsche_info = (
    "Porsche is a German manufacturer of luxury sports cars, "
    "founded in 1931 by Ferdinand Porsche, "
    "the engineer who also created the first Volkswagen car."
    "The company is known for the design and "
    "performance of its cars, as well as its active involvement in motorsports."
)
    st.write(porsche_info)
    st.image("images/porsche_formula1.png", caption="Porsche Formula 1 Car")


    st.write("## Porsche Partners")
     
    st.write("Among Porsche's partners are renowned brands such "
                    "as Mobil 1, Michelin, and others.")

    st.subheader("Michelin")
    col1, col2 = st.columns(2)
    with col1:
        st.image(
            "https://experience.porsche.com/-/media/"
            "C653E4E379314B95B2AB6B3C46869E5A_27D12BA5DC87447C8B3F2DCAC6555978"
            "_PRE_PaulRichard_15367?iar=0&q=70&w=800"
        )
    with col2:
        st.write(
            "Porsche and Michelin share a lengthy and successful collaboration, "
            "marked by Michelin's provision of meticulously crafted  "
            "high-performance tires specifically designed for each Porsche model. "
            "This partnership ensures unparalleled handling characteristics on "
            "diverse terrain, spanning from everyday roads to competitive "
            "racing tracks worldwide."
        )

    st.subheader("Mobil 1")
    col3, col4 = st.columns(2)
    with col4:
        st.image(
            "https://experience.porsche.com/-/media/"
            "EFF1A85E2E6A456C88A725E9890FDC44_3F7F1506968E"
            "4499A6901F3E58268641_6065?iar=0&q=70&w=800"
        )
    with col3:
        st.write(
            "Porsche and Mobil 1's partnership since 1996 epitomizes innovation,"
            " quality engineering, and advanced technology. Mobil 1's "
            "cutting-edge lubricants, including the latest Mobil SHC Synthetic "
            "Technology, are utilized in Porsche race cars like the Porsche 911"
            " GT3 Cup, showcasing exceptional performance on the track. "
            "This collaboration underscores a commitment to excellence and "
            "performance in both motorsports and production vehicles."
        )

    st.subheader("TAG Heuer")
    col5, col6 = st.columns(2)
    with col5:
        st.image(
            "https://experience.porsche.com/-/media/"
            "25A0493CAD8D4E81ACC902285C14689A_9E2A31044F2445ACAAA9B36AF5534546_"
            "Porsche-Ice-Experience_TAGHeuer_06_03_2022_0949?iar=0&q=70&w=800"
        )
    with col6:
        st.write(
            "TAG Heuer and Porsche unite in a partnership driven by innovation "
            " and motorsport. With shared values of precision and performance, "
            " they collaborate extensively in motorsports, esports, golf, and "
            "tennis. The special edition TAG Heuer Carrera Porsche Chronograph "
            " marks their first joint watch production, symbolizing"
            " their authentic alliance."
        )

    st.title("Get in Touch")
    st.write(
        "Thank you for exploring our website! We're thrilled that you're "
        "interested in connecting with us. Whether you have a question, "
        " feedback, or a partnership opportunity, we're here to listen and "
        "assist you in any way we can."
    )

    st.subheader("Ways to Reach Us")
    st.write(
        "Feel free to contact us "
        "Drop us an email at [contact@companyname.com]"
        "(mailto:contact@companyname.com) "
        "with any inquiries or concerns."
        "We aim to respond to all emails promptly, "
        "typically within 24 hours."
    )

    st.subheader("Social Media")
    st.write(
        "Connect with us on our social media channels for updates, news, and "
        "engaging content. Find us on [Facebook](https://www.facebook.com/"
        "porsche/?locale=ro_RO), [Youtube](https://www.youtube.com/@Porsche), "
        "[Instagram](https://www.instagram.com/porsche/), and [LinkedIn]"
        "(https://www.linkedin.com/company/porsche-ag/)."
    )

    st.title("Feedback")
    st.write(
        "We value your feedback as it helps us improve our products and services. "
        "Whether it's a suggestion for improvement or a compliment, we'd love "
        "to hear from you. Let us know how we're doing by sending an email to "
        "[feedback@companyname.com](mailto:feedback@companyname.com)."
    )
    st.write(
        "Don't hesitate to reach out, we're here to help and look forward"
        "to connecting with you!"
    )

def pagina_modelelor():
    st.title("Porsche models")
    st.write("Here you can see and select different Porsche models")

    # Dicționar cu linkuri de imagini pentru fiecare model
    image_links = {
    "Porsche 356 Coupe": "images/356_coupe.webp",
    "Porsche 718 Spyder (982)": "images/718_spyder.jpg",
    "Porsche 718 Cayman (982)": "images/718_cayman.jpg",
    "Porsche 718 Boxster (982)": "images/718_boxster.png",
    "Porsche 901": "images/901.png",
    "Porsche 911 Dakar (992)": "images/911_dakar.png",
    "Porsche 911 Targa (992)": "images/911_targa.jpg",
    "Porsche 911 Speedster (991 II)": "images/911_speedster.png",
    "Porsche 911 Cabriolet (992)": "images/911_cabriolet.png",
    "Porsche 911 (992)": "images/911.png",
    "Porsche 911 RSR (991)": "images/911_rsr.png",
    "Porsche 911 Cabriolet (991 II)": "images/911_cabriolet_991_II.png",
    "Porsche 911 Targa (991 II)": "images/911_targa_991_II.png",
    "Porsche 911 (991 II)": "images/911_cabriolet_991_II.png",
    "Porsche 911 Targa (991)": "images/911_targa_991.png",
    "Porsche 911 Cabriolet (991)": "images/911_cabriolet_991.png",
    "Porsche 911 (991)": "images/911_991.png",
    "Porsche 911 Cabriolet (997, facelift 2008)":
      "images/911_cabriolet_997_facelift_2008.png",
    "Porsche 911 Targa (997, facelift 2008)":
      "images/911_targa_997_facelift_2008.webp",
    "Porsche 911 (997, facelift 2008)": "images/911_997_facelift_2008.png",
    "Porsche 911 Targa (997)": "images/911_targa_997.png",
    "Porsche 911 Cabriolet (997)": "images/911_cabriolet_997.png",
    "Porsche 911 (997)": "images/911_997.png",
    "Porsche 911 Cabriolet (996, facelift 2001)":
      "images/911_cabriolet_996_facelift_2001.png",
    "Porsche 911 Targa (996, facelift 2001)":
      "images/911_targa_996_facelift_2001.png",
    "Porsche 911 (996, facelift 2001)": "images/911_996_facelift_2001.png",
    "Porsche 911 Cabriolet (996)": "images/911_cabriolet_996.png",
    "Porsche 911 (996)": "images/911_996.png",
    "Porsche 911 Targa (993)": "images/911_targa_993.png",
    "Porsche 911 (993)": "images/911_993.png",
    "Porsche 911 Cabriolet (993)": "images/911_cabriolet_993.png",
    "Porsche 911 Cabriolet (964)": "images/911_cabriolet_964.png",
    "Porsche 911 Targa (964)": "images/911_targa_964.png",
    "Porsche 911 (964)": "images/911_964.png",
    "Porsche 911 Speedster": "images/911_speedster_1989.png",
    "Porsche 911 Cabriolet (Type 930)": "images/911_cabriolet_type_930.png",
    "Porsche 911 Targa (Type 930)": "images/911_targa_type_930.png",
    "Porsche 911 Cabriolet (G)": "images/911_cabriolet_G.png",
    "Porsche 911 Coupe (Type 930)": "images/911_coupe_type_930.png",
    "Porsche 911 Targa (G)": "images/911_targa_G.jpg",
    "Porsche 911 Coupe (G)": "images/911_coupe_G.png",
    "Porsche 911 Targa (F)": "images/911_targa_F.png",
    "Porsche 911 Coupe (F)": "images/911_coupe_F.png",
    "Porsche 912E": "images/912E.png",
    "Porsche 912": "images/912.png",
    "Porsche 914": "images/914.png",
    "Porsche 917": "images/917.png",
    "Porsche 918 Spyder": "images/918_spyder.png",
    "Porsche 924": "images/924.png",
    "Porsche 928": "images/928.png",
    "Porsche 944": "images/944.png",
    "Porsche 944 Cabrio": "images/944_cabrio.png",
    "Porsche 959": "images/959.png",
    "Porsche 968": "images/968.png",
    "Porsche 968 Cabrio": "images/968_cabrio.png",
    "Porsche Boxster (981)": "images/boxster_981.png",
    "Porsche Boxster (987, facelift 2009)":
      "images/boxster_987_facelift_2009.jpg",
    "Porsche Boxster (987)": "images/boxster_987.png",
    "Porsche Boxster (986)": "images/boxster_986.png",
    "Porsche Carrera GT": "images/carrera_gt.webp",
    "Porsche Cayenne III (facelift 2023) Coupe":
      "images/cayenne_III_coupe_facelift_2023.png",
    "Porsche Cayenne III (facelift 2023)":
      "images/cayenne_III_facelift_2023.png",
    "Porsche Cayenne III Coupe": "images/cayenne_III_coupe.png",
    "Porsche Cayenne III": "images/cayenne_III.png",
    "Porsche Cayenne II (facelift 2014)":
      "images/cayenne_II_facelift_2014.png",
    "Porsche Cayenne II": "images/cayenne_II.png",
    "Porsche Cayenne (955, facelift 2007)":
      "images/cayenne_955_facelift_2007.png",
    "Porsche Cayenne (955)": "images/cayenne_955.png",
    "Porsche Cayman (981c)": "images/cayman_981c.png",
    "Porsche Cayman (987c, facelift 2009)":
      "images/cayman_987c_facelift_2009.png",
    "Porsche Cayman (987c)": "images/cayman_987c.png",
    "Porsche Macan II Electric": "images/macan_II_electric.png",
    "Porsche Macan I (95B, facelift 2021)":
      "images/macan_I_95B_facelift_2021.jpg",
    "Porsche Macan I (95B, facelift 2018)":
      "images/macan_I_95B_facelift_2018.png",
    "Porsche Macan I (95B)": "images/macan_I_95B.png",
    "Porsche Mission E Concept": "images/mission_e_concept.png",
    "Porsche Mission E Cross Turismo Concept":
      "images/mission_e_cross_turismo_concept.png",
    "Porsche Mission X concept": "images/mission_x_concept.png",
    "Porsche Panamera (G3) Executive": "images/panamera_G3_executive.png",
    "Porsche Panamera (G3)": "images/panamera_G3.png",
    "Porsche Panamera (G2 II) Sport Turismo":
      "images/panamera_G2_II_sport_turismo.png",
    "Porsche Panamera (G2 II) Executive": "images/panamera_G2_II_executive.png",
    "Porsche Panamera (G2 II)": "images/panamera_G2_II.png",
    "Porsche Panamera (G2) Sport Turismo":
      "images/panamera_G2_sport_turismo.png",
    "Porsche Panamera (G2) Executive": "images/panamera_G2_executive.png",
    "Porsche Panamera (G2)": "images/panamera_G2.png",
    "Porsche Panamera (G1 II) Executive": "images/panamera_G1_II_executive.png",
    "Porsche Panamera (G1 II)": "images/panamera_G1_II.png",
    "Porsche Panamera (G1)": "images/panamera_G1.png",
    "Porsche Taycan Sport Turismo (Y1A, facelift 2024)":
      "images/taycan_sport_turismo_y1a_facelift_2024.png",
    "Porsche Taycan Cross Turismo (Y1A, facelift 2024)":
      "images/taycan_cross_turismo_y1a_facelift_2024.png",
    "Porsche Taycan (Y1A, facelift 2024)": "images/taycan_y1a_facelift_2024.png",
    "Porsche Taycan Sport Turismo (Y1A)": "images/taycan_sport_turismo_y1a.png",
    "Porsche Taycan Cross Turismo (Y1A)": "images/taycan_cross_turismo_y1a.png",
    "Porsche Taycan (Y1A)": "images/taycan.png"          
    }

    # Get list of Porsche models from API
    response = requests.get("http://127.0.0.1:5000/porsche_models")
    if response.status_code == 200:
        models = response.json()

        # Add Image Link manually
        for model in models:
            model_name = model["Model Name"]
            model["Image Link"] = image_links.get(model_name,
                                       "http://example.com/images/default.jpg")

        # Create dropdown for selecting Porsche model
        selected_model = st.selectbox("Select a Porsche car model.",
                                   [model["Model Name"] for model in models])

        # Find selected model's info
        selected_model_info = next((model for model in models
                               if model["Model Name"] == selected_model), None)
        if selected_model_info:
            st.image(selected_model_info["Image Link"], caption=selected_model)
            st.subheader("Information about the model:")
            st.write(f"Years of production: {selected_model_info['Currency']}")
            st.write(f"Type of chassis: {selected_model_info['Chassis']}")
            st.write(f"{selected_model_info['Span']}")
    else:
        st.error("A apărut o eroare în obținerea datelor despre modelele Porsche.")

def pagina_asistentei():
    st.title("Detailed Car Maintenance Guide")

    # Transmission Oil
    st.header("Transmission Oil Check")
    st.markdown("""
      Check:
    1. Start engine and let it reach normal operating temperature.
    2. Turn off engine, wait a few minutes for oil to settle.
    3. Remove dipstick, clean it, reinsert it fully.
    4. Remove dipstick, check oil level between min and max marks.
    5. Add oil if necessary.

      Notes:
    - Use the oil type recommended by the car manufacturer.
    """)
    st.checkbox("Checked transmission oil")

    # Tires
    st.header("Tires")
    st.markdown("""
      Tire Condition Check:
    1. Visually inspect tires for cuts, cracks, foreign objects.
    2. Check tread depth, replace if less than 2mm.

      Tire Pressure Check:
    1. Check tire pressure when cold.
    2. Use gauge to measure pressure, compare with recommended values.
    3. Adjust pressure if necessary.

      Alignment Check:
    1. Get wheel alignment at a specialized service to prevent uneven tire wear.
    """)
    st.checkbox("Checked tire condition")
    st.checkbox("Checked tire pressure")
    st.checkbox("Checked alignment")

    # Brakes
    st.header("Braking System")
    st.markdown("""
      Brake Disc Check:
    1. Inspect brake discs for excessive wear or cracks.
    2. Measure disc thickness, replace if below minimum specified.

      Brake Pad Check:
    1. Check brake pad thickness, replace if excessively worn.
    2. Ensure pads contact discs properly, no fluid leaks.
    """)
    st.checkbox("Checked brake discs")
    st.checkbox("Checked brake pads")

    # Electronic Testing
    st.header("Electronic Testing")
    st.markdown("""
      Perform Electronic Test:
    1. Connect OBD-II scanner to car's diagnostic port.
    2. Read and interpret error codes to identify potential issues.
    3. Reset error codes after resolving issues.

      Notes:
    - Recommended to perform this test periodically or when a warning light 
                appears.
    """)
    st.checkbox("Performed electronic test")

    # Fluid Checks
    st.header("Fluid Checks")
    st.markdown("""
      Fluid Checks:
    1. Coolant: Check level, top up if needed. Use correct type.
    2. Brake Fluid: Check level, condition. Replace if dirty.
    3. Power Steering Fluid: Check level, top up if needed.
    4. Windshield Washer Fluid: Top up with special fluid.

      Freon Check:
    1. Check freon level in the A/C system.
    2. Recharge system or take car to a specialist if low.

      Notes:
    - Refer to the car's manual for exact specs and intervals.
    """)
    st.checkbox("Checked fluids (including freon)")

    # Battery
    st.header("Battery")
    st.markdown("""
      Battery Check:
    1. Check battery voltage with a multimeter (normal: 12.4V-12.7V).
    2. Inspect for leaks or corrosion.

      Clean Battery Terminals:
    1. Disconnect terminals, starting with the negative.
    2. Clean terminals with wire brush and baking soda solution.
    3. Reattach terminals, starting with the positive.
    """)
    st.checkbox("Checked battery")
    st.checkbox("Cleaned battery terminals")

    # Exhaust System
    st.header("Exhaust System")
    st.markdown("""
      Exhaust Pipe Check:
    1. Inspect exhaust pipes for holes, rust, or damage.
    2. Listen for unusual noises indicating leaks.

      Notes:
    - Check the catalytic converter and other exhaust components.
    """)
    st.checkbox("Checked exhaust pipe")

    # Fuel
    st.header("Fuel")
    st.markdown("""
      Fuel Level Check:
    1. Ensure fuel tank is sufficiently filled.
    2. Check for leaks in the fuel system.

      Notes:
    - Avoid letting the tank run empty to prevent fuel pump damage.
    """)
    st.checkbox("Checked fuel level")

    # Windshield Wipers
    st.header("Windshield Wipers")
    st.markdown("""
      Windshield Wiper Check:
    1. Inspect wiper blades for wear or damage.
    2. Replace wipers if they don't clean the windshield effectively.

      Wiper Fluid Check:
    1. Top up reservoir with special windshield fluid.
    2. Check wiper system operation.

      Notes:
    - Replace wipers annually or when issues arise.
    """)
    st.checkbox("Checked wipers")
    st.checkbox("Checked wiper fluid level")

    # Animal Inspection
    st.header("Animal Inspection")
    st.markdown("""
      Check for Animal Presence:
    1. Open hood, inspect engine area for signs of animals (nests, droppings,
                 chew marks).
    2. Check under car, especially around wheels and exhaust.

      Notes:
    - Small animals seek shelter in engine compartments in cold months. 
                Watch for activity.
    """)
    st.checkbox("Checked for animal presence")

    if st.button("Complete Inspection"):
        st.success("Inspection completed successfully!")

    st.write("For specific information on maintaining your Porsche model,"
            " consult the user manual or an authorized service center.")

def pagina_recenziilor():
    # Citirea datelor din fișierul JSON
    with open('urls.json', 'r') as file:
        data = json.load(file)

    # Extrage lista de URL-uri din dicționar
    urls = data.get('urls', [])

    all_reviews = []

    for url in urls:
        all_reviews.extend(review.scrape_reviews(url))

    review.create_database(all_reviews)
    review.main()
    

def easter_egg3():
    st.title("Hey my dears!")
    st.subheader("A letter of gratitude to the mentors and teachers at Sigmoid")

# Scrisoare de mulțumire
    st.write("""
Dear Mentors and Teachers at Sigmoid,
I want to express my deepest gratitude for the guidance,
support, and knowledge you have imparted on me during my time at Sigmoid.
Your dedication to our growth and development has been truly inspiring.
Your mentorship has not only helped me academically but has also shaped me into
 a better person. Your encouragement and belief in my abilities have motivated 
  me to strive for excellence in everything I do.

Thank you for your patience, your wisdom, and for always pushing me to reach 
my full potential. Sigmoid is not just a place of learning, but a community of 
  passionate individuals dedicated to making a difference in the world.

With sincere appreciation,
Marinela
""")



# Buttoane
    button_col1, button_col2, button_col3 = st.columns(3)

    if button_col1.button("Eduard"):
      st.write("""Hey , domn profesor!
               Good Job! Mai trage un pic de aer , în sfârșit  scapi de noi XD
               Îți ofer toată aprecierea pentru efortul depus.
               În ciuda faptului că vroiam să dau mâinile în jos căci nu mai
               reușeam nimic , ai început să dai exemple la lecții legate de
               mașini ,anume Porsche și am găsit motivație să fac acest proiect 
               simpluț, dar de o plăcere am lucrat la el.Rămâi dedicat la ceea
               ce faci , știi că ești cel mai bun?!
               Mersi mult pentru motivație și pentru răbdare!
               """)
      st.markdown("![Alt Text](https://i.giphy.com/y853jRq5TrMHVGn4nl.webp)")

    if button_col2.button("Sigmoid"):
      st.markdown("![Alt Text](https://i.giphy.com/HUOmKBvH96FE2lTkNt.webp)")
      st.write("Sincere aprecieri echipei Sigmoid!"
               " Știu că în spatele acestui curs sunteți mulți oameni frumoși!"
               " Ați făcut o treabă bună! Keep doing amazing things!")
    if button_col3.button("Nicu"):
       st.write("Hey! Încântată că te-am cunoscut! Mersi mult pentru suport" 
                " și ajutor!"
                "În calitate de mentor ai fost extraordinar.Te vedeam "
                 "exact ca aceast motan XD care îmi tot căuta surse de unde"
                 " pot să găsesc o idee sau de unde pot lua ceva folositor.")
       st.markdown("![Alt Text](https://i.giphy.com/lXiRzPb8C5JTJcfPq.webp)")
       
def main():
    pagini = {
        "Main page": pagina_principala,
        "Porsche models": pagina_modelelor,
        "Maintenance": pagina_asistentei,
        "Reviews": pagina_recenziilor,
        "Hidden": easter_egg3
    }

    st.sidebar.title("Navigation")
    pagina_selectata = st.sidebar.radio("Select page", list(pagini.keys()))

    pagina_functionala = pagini[pagina_selectata]
    pagina_functionala()


if __name__ == "__main__":
    main()
