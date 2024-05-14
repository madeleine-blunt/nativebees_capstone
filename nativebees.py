## Import Python Libraries

import pandas as pd
import numpy as np
import streamlit as st

### Park Dictionary
park_dict = {
    'Acadia National Park' : 'ACAD',
    'Arches National Park' : 'ARCH', 
    'Badlands National Park' : 'BADL',
    'Big Bend National Park' : 'BIBE',
    'Biscayne National Park' : 'BISC', 
    'Black Canyon of the Gunnison National Park' : 'BLCA', 
    'Bryce Canyon National Park' : 'BRCA',
    'Canyonlands National Park' : 'CANY', 
    'Capitol Reef National Park' : 'CARE', 
    'Carlsbad Caverns National Park' : 'CAVE',
    'Channel Islands National Park' : 'CHIS', 
    'Congaree National Park' : 'CONG', 
    'Crater Lake National Park' : 'CRLA', 
    'Cuyahoga Valley National Park' : 'CUVA',
    'Death Valley National Park' : 'DEVA', 
    'Denali National Park' : 'DENA', 
    'Dry Tortugas National Park' : 'DRTO', 
    'Everglades National Park' : 'EVER',
    'Gates of the Arctic National Park' : 'GAAR', 
    'Gateway Arch National Park' : 'JEFF', 
    'Glacier Bay National Park' : 'GLBA', 
    'Glacier National Park' : 'GLAC',
    'Grand Canyon National Park' : 'GRCA', 
    'Grand Teton National Park' : 'GRTE', 
    'Great Basin National Park' : 'GRBA', 
    'Great Sand Dunes National Park' : 'GRSA',
    'Great Smoky Mountains National Park' : 'GRSM', 
    'Guadalupe Mountains National Park' : 'GUMO', 
    'Haleakalā National Park' : 'HALE',
    'Hawaii Volcanoes National Park' : 'HAVO', 
    'Hot Springs National Park' : 'HOSP', 
    'Indiana Dunes National Park' : 'INDU', 
    'Isle Royale National Park' : 'ISRO',
    'Joshua Tree National Park' : 'JOTR', 
    'Katmai National Park' : 'KATM', 
    'Kenai Fjords National Park' : 'KEFJ', 
    'Kings Canyon National Park' : 'KICA',
    'Kobuk Valley National Park' : 'KOVA', 
    'Lake Clark National Park': 'LACL', 
    'Lassen Volcanic National Park' : 'LAVO', 
    'Mammoth Cave National Park': 'MACA',
    'Mesa Verde National Park':'MEVE', 
    'Mount Rainier National Park':'MORA', 
    'National Park of American Samoa':'NPSA', 
    'New River Gorge National Park and Preserve':'NERI',
    'North Cascades National Park':'NOCA', 
    'Olympic National Park':'OLYM',
    'Petrified Forest National Park':'PEFO',
    'Pinnacles National Park':'PINN',
    'Redwood National Park':'REDW',
    'Rocky Mountain National Park':'ROMO', 
    'Saguaro National Park':'SAGU', 
    'Sequoia National Park':'SEQU', 
    'Sequoia and Kings Canyon National Park': 'SEKI',
    'Shenandoah National Park': 'SHEN',
    'Theodore Roosevelt National Park':'THRO',
    'Virgin Islands National Park': 'VIIS',
    'Voyageurs National Park':'VOYA', 
    'White Sands National Park':'WHSA', 
    'Wind Cave National Park':'WICA', 
    'Wrangell-St. Elias National Park':'WRST',
    'Yellowstone National Park':'YELL', 
    'Yosemite National Park':'YOSE',
    'Zion National Park':'ZION'
}

parks = ['ACAD', 'ARCH', 'BADL', 'BIBE', 'BISC', 'BLCA', 'BRCA', 'CANY', 'CARE', 'CAVE', 'CHIS', 'CONG', 'CRLA', 'CUVA', 'DEVA', 'DENA',
'DRTO', 'EVER', 'GAAR', 'JEFF', 'GLBA', 'GLAC', 'GRCA', 'GRTE', 'GRBA', 'GRSA', 'GRSM', 'GUMO', 'HALE', 'HAVO', 'HOSP', 'INDU',
'ISRO', 'JOTR', 'KATM', 'KEFJ', 'KICA', 'KOVA', 'LACL', 'LAVO', 'MACA', 'MEVE', 'MORA', 'NPSA', 'NERI', 'NOCA', 'OLYM', 'PEFO',
'PINN', 'REDW', 'ROMO', 'SAGU', 'SEQU', 'SEKI', 'SHEN', 'THRO', 'VIIS', 'VOYA', 'WHSA', 'WICA', 'WRST', 'YELL', 'YOSE', 'ZION']

bee_family = ['Melittidae', 'Apidae', 'Megachilidae', 'Andrenidae',
                         'Halictidae', 'Stenotritidae','Colletidae']

Flowers = pd.read_pickle("flowers.pkl")
flower_family = Flowers['Family'].values.tolist()
flower_family = [x.rstrip() for x in flower_family]

NPS_Species = pd.read_pickle("Park Pickles/NPS_Species.pkl")
NPS_bees = pd.read_pickle("Bee Pickles/NPS_bees.pkl")
Native_bees = NPS_bees.loc[NPS_bees['Nativeness'] == "Native"]

NPS_flowers = pd.read_pickle("Flower Pickles/NPS_flowers.pkl") 
Native_flowers = NPS_flowers.loc[NPS_flowers['Nativeness'] == "Native"]


states = set(NPS_Species['State'])



## Streamlight Inputs
st.title("National Park Native Bees and Flowers")

tab1, tab2 = st.tabs(["Bees :bee:", "Flowers :blossom:"])

with tab1:

   geog = st.radio('Data Level', ["National", "State Level", "Park Level"])

   if geog == 'Park Level' :
      select_np = st.selectbox('Pick National Park',['Acadia National Park','Arches National Park', 'Badlands National Park','Big Bend National Park',
                           'Biscayne National Park', 'Black Canyon of the Gunnison National Park', 'Bryce Canyon National Park',
                           'Canyonlands National Park', 'Capitol Reef National Park', 'Carlsbad Caverns National Park',
                           'Channel Islands National Park', 'Congaree National Park', 'Crater Lake National Park', 'Cuyahoga Valley National Park',
                           'Death Valley National Park', 'Denali National Park', 'Dry Tortugas National Park', 'Everglades National Park',
                           'Gates of the Arctic National Park', 'Gateway Arch National Park', 'Glacier Bay National Park', 'Glacier National Park',
                           'Grand Canyon National Park', 'Grand Teton National Park', 'Great Basin National Park', 'Great Sand Dunes National Park',
                           'Great Smoky Mountains National Park', 'Guadalupe Mountains National Park', 'Haleakalā National Park',
                           'Hawaii Volcanoes National Park', 'Hot Springs National Park', 'Indiana Dunes National Park', 'Isle Royale National Park',
                           'Joshua Tree National Park', 'Katmai National Park', 'Kenai Fjords National Park', 'Kings Canyon National Park',
                           'Kobuk Valley National Park', 'Lake Clark National Park', 'Lassen Volcanic National Park', 'Mammoth Cave National Park',
                           'Mesa Verde National Park', 'Mount Rainier National Park', 'National Park of American Samoa', 'New River Gorge National Park and Preserve',
                           'North Cascades National Park', 'Olympic National Park','Petrified Forest National Park','Pinnacles National Park','Redwood National Park',
                           'Rocky Mountain National Park', 'Saguaro National Park', 'Sequoia National Park', 'Shenandoah National Park','Theodore Roosevelt National Park',
                           'Virgin Islands National Park', 'Voyageurs National Park', 'White Sands National Park', 'Wind Cave National Park', 'Wrangell-St. Elias National Park',
                           'Yellowstone National Park', 'Yosemite National Park','Zion National Park'])
      ### Selected National Park
      Park_bees = NPS_bees.loc[NPS_bees['Park Code'] == park_dict[select_np]]
   
      if len(Park_bees) == 0:
         st.info('The species list for this National Park does not have bee data, report your bee sightings at the link below')
         st.link_button('NPS Species List Contribution', 'https://irma.nps.gov/NPSpecies/Suggest')
      else :
         st.header(select_np)
         col1, col2= st.columns(2)
         with col1:

            species_linelist = Park_bees.drop(['Park Code', 'Category', 'Order', 'Family', 'Taxon Code', 'Occurrence', 'Nativeness', 'Abundance', 'State'], axis=1)
            species_linelist.set_index("Scientific Name", inplace=True)
            species_linelist.fillna("-")
            species_count = len(species_linelist)

            st.header("All Bee Species")
            st.metric("(#) of Bee Species", species_count)

            ## (PARK) Number of Bees per Family
            park_bee_family = Park_bees['Family'].value_counts().rename_axis('Family').reset_index(name='counts')

            bee_unique = park_bee_family['Family'].values.tolist()

            temp_bee = []
            for element in bee_family:
               if element not in bee_unique:
                  temp_bee.append(element)

            zeros_list = [0] * len(temp_bee)

            dict = {'Family': temp_bee, 'counts': zeros_list} 
               
            temp_df = pd.DataFrame(dict)

            park_bee_family = pd.concat([park_bee_family,temp_df]).reset_index(drop=True)

            st.divider()
            st.subheader("Number of Bees per Taxon Family")
            st.dataframe(park_bee_family)

            st.divider()
            st.subheader("Line Listing of Bee Species")
            st.dataframe(species_linelist)
            
         with col2:

            native_bees = Park_bees.loc[Park_bees['Nativeness'] == "Native"]
            native_linelist = native_bees.drop(['Park Code', 'Category', 'Order', 'Family', 'Taxon Code', 'Occurrence', 'Nativeness', 'Abundance', 'State'], axis=1)
            native_linelist.set_index("Scientific Name", inplace=True)
            native_linelist.fillna("-")
            native_count = len(native_linelist)
         
            st.header("Native Bee Species")
            st.metric("(#) of Native Bee Species", native_count)
           
            ## (PARK) Number of Native Bees per Family
            park_native_bee_family = native_bees['Family'].value_counts().rename_axis('Family').reset_index(name='counts')

            bee_unique = park_native_bee_family['Family'].values.tolist()

            temp_bee = []
            for element in bee_family:
               if element not in bee_unique:
                  temp_bee.append(element)

            zeros_list = [0] * len(temp_bee)

            dict = {'Family': temp_bee, 'counts': zeros_list} 
               
            temp_df = pd.DataFrame(dict)

            park_native_bee_family = pd.concat([park_native_bee_family,temp_df]).reset_index(drop=True)
            
            st.divider()
            st.subheader("Number of Native Bees per Taxon Family")
            st.dataframe(park_native_bee_family)

            st.divider()
            st.subheader("Line Listing of Native Bee Species")
            st.dataframe(native_linelist)

   elif geog == 'State Level' :
      select_state = st.selectbox('Pick State', states)

      ### Selected State
      State_bees = NPS_bees.loc[NPS_bees['State'] == select_state] 

      if len(State_bees) == 0:
         st.info('The species lists for National Parks in this state do not have bee data, report your bee sightings at the link below')
         st.link_button('NPS Species List Contribution', 'https://irma.nps.gov/NPSpecies/Suggest')
      else :
         st.header(select_state)
         col1, col2= st.columns(2)
         with col1:

            state_species_linelist = State_bees.drop(['Park Code', 'Category', 'Order', 'Family', 'Taxon Code', 'Occurrence', 'Nativeness', 'Abundance', 'State'], axis=1)
            state_species_linelist.set_index("Scientific Name", inplace=True)
            state_species_linelist.fillna("-")
            state_species_count = len(state_species_linelist)

            st.header("All Bee Species")
            st.metric("(#) of Bee Species", state_species_count)

            ## (STATE) Number of Bees per Family
            state_bee_family = State_bees['Family'].value_counts().rename_axis('Family').reset_index(name='counts')

            bee_unique = state_bee_family['Family'].values.tolist()

            temp_bee = []
            for element in bee_family:
               if element not in bee_unique:
                  temp_bee.append(element)

            zeros_list = [0] * len(temp_bee)

            dict = {'Family': temp_bee, 'counts': zeros_list} 
               
            temp_df = pd.DataFrame(dict)

            state_bee_family = pd.concat([state_bee_family,temp_df]).reset_index(drop=True)

            st.divider()
            st.subheader("Number of Bees per Taxon Family")
            st.dataframe(state_bee_family)

            st.divider()
            st.subheader("Line Listing of Bee Species")
            st.dataframe(state_species_linelist)
            
         with col2:

            state_native_bees = State_bees.loc[State_bees['Nativeness'] == "Native"]
            state_native_linelist = state_native_bees.drop(['Park Code', 'Category', 'Order', 'Family', 'Taxon Code', 'Occurrence', 'Nativeness', 'Abundance', 'State'], axis=1)
            state_native_linelist.set_index("Scientific Name", inplace=True)
            state_native_linelist.fillna("-")
            state_native_count = len(state_native_linelist)

            st.header("Native Bee Species")
            st.metric("(#) of Native Bee Species", state_native_count)

            ## (STATE) Number of Native Bees per Family
            state_native_bee_family = state_native_bees['Family'].value_counts().rename_axis('Family').reset_index(name='counts')

            bee_unique = state_native_bee_family['Family'].values.tolist()

            temp_bee = []
            for element in bee_family:
               if element not in bee_unique:
                  temp_bee.append(element)

            zeros_list = [0] * len(temp_bee)

            dict = {'Family': temp_bee, 'counts': zeros_list} 
               
            temp_df = pd.DataFrame(dict)

            state_native_bee_family = pd.concat([state_native_bee_family,temp_df]).reset_index(drop=True)

            st.divider()
            st.subheader("Number of Native Bees per Taxon Family")
            st.dataframe(state_native_bee_family)

            st.divider()
            st.subheader("Line Listing of Native Bee Species")
            st.dataframe(state_native_linelist)

   else : 
      st.header('National Level Bee Data')

      on_park = st.toggle('Show Aggregate Level Park Data :bee:')

      if on_park:
         with st.container():
            col1, col2= st.columns(2)
            with col1:

               ## (National) Number of Bee Families by Park
               nation_park_bee = pd.DataFrame(bee_family)
               nation_park_bee.columns = ["Family"]
               nation_park_bee.set_index("Family", inplace=True)
               for i in parks:
                  temp_bee = NPS_bees.loc[NPS_bees['Park Code'] == i]
                  temp_bee_family = pd.DataFrame(temp_bee['Family'].value_counts().rename_axis('Family').reset_index(name='counts'))
                  nation_park_bee = pd.concat([nation_park_bee,temp_bee_family.set_index('Family')], axis=1).fillna(0)

               nation_park_bee.columns = parks

               st.subheader("Number of Bees per Taxon Family by Park")
               st.dataframe(nation_park_bee)

               ## (National) Number of Native Bee Families by Park
               nation_park_native_bee = pd.DataFrame(bee_family)
               nation_park_native_bee.columns = ["Family"]
               nation_park_native_bee.set_index("Family", inplace=True)
               for i in parks:
                  temp_bee = Native_bees.loc[Native_bees['Park Code'] == i]
                  temp_bee_family = pd.DataFrame(temp_bee['Family'].value_counts().rename_axis('Family').reset_index(name='counts'))
                  nation_park_native_bee = pd.concat([nation_park_native_bee,temp_bee_family.set_index('Family')], axis=1).fillna(0)

               nation_park_native_bee.columns = parks

               st.divider()
               st.subheader("Number of Native Bees per Taxon Family by Park")
               st.dataframe(nation_park_native_bee)

            with col2:

               nation_park_bee['Max'] = nation_park_bee.idxmax(axis=1)
               nation_park_bee_diverse = nation_park_bee[['Max']]

               st.subheader("Where Should I Go to See the Most Species of Bees?")
               st.dataframe(nation_park_bee_diverse)

               nation_park_native_bee['Max'] = nation_park_native_bee.idxmax(axis=1)
               nation_park_native_bee_diverse =nation_park_native_bee[['Max']]

               st.divider()
               st.subheader("Where Should I Go to See the Most Species of Native Bees?")
               st.dataframe(nation_park_native_bee_diverse)

      st.divider()

      on_state = st.toggle('Show Aggregate Level State Data :bee:')

      if on_state:
         with st.container():
            col1, col2= st.columns(2)
            with col1:
               
               ## (National) Number of Bee Families by State
               nation_state_bee = pd.DataFrame(bee_family)
               nation_state_bee.columns = ["Family"]
               nation_state_bee.set_index("Family", inplace=True)
               for i in states:
                  temp_bee = NPS_bees.loc[NPS_bees['State'] == i]
                  temp_bee_family = pd.DataFrame(temp_bee['Family'].value_counts().rename_axis('Family').reset_index(name='counts'))
                  nation_state_bee = pd.concat([nation_state_bee,temp_bee_family.set_index('Family')], axis=1).fillna(0)

               nation_state_bee.columns = states

               st.subheader("Number of Bees per Taxon Family by State")
               st.dataframe(nation_state_bee)

               ## (National) Number of Native Bee Families by State
               nation_state_native_bee = pd.DataFrame(bee_family)
               nation_state_native_bee.columns = ["Family"]
               nation_state_native_bee.set_index("Family", inplace=True)
               for i in states:
                  temp_bee = Native_bees.loc[Native_bees['State'] == i]
                  temp_bee_family = pd.DataFrame(temp_bee['Family'].value_counts().rename_axis('Family').reset_index(name='counts'))
                  nation_state_native_bee = pd.concat([nation_state_native_bee,temp_bee_family.set_index('Family')], axis=1).fillna(0)

               nation_state_native_bee.columns = states

               st.divider()
               st.subheader("Number of Native Bees per Taxon Family by State")
               st.dataframe(nation_state_native_bee)

            with col2:

               nation_state_bee['Max'] = nation_state_bee.idxmax(axis=1)
               nation_state_bee_diverse = nation_state_bee[['Max']]

               st.subheader("Where Should I Go to See the Most Species of Bees?")
               st.dataframe(nation_state_bee_diverse)

               nation_state_native_bee['Max'] = nation_state_native_bee.idxmax(axis=1)
               nation_state_native_bee_diverse = nation_state_native_bee[['Max']]

               st.divider()
               st.subheader("Where Should I Go to See the Most Species of Native Bees?")
               st.dataframe(nation_state_native_bee_diverse)

      st.divider()

      col1, col2= st.columns(2)
      
      with col1:

         ### Number of Bees per Species
         nation_bee = NPS_bees['Scientific Name'].value_counts().rename_axis('Scientific Name').reset_index(name='counts')
         nation_bee.set_index("Scientific Name", inplace=True)
         nation_bee_count = len(NPS_bees)

         st.header("All Bee Species")
         st.metric("(#) of Bee Species", nation_bee_count)

         ## (National) Number of Bees per Family
         nation_bee_family = NPS_bees['Family'].value_counts().rename_axis('Family').reset_index(name='counts')

         bee_unique = nation_bee_family['Family'].values.tolist()

         temp_bee = []
         for element in bee_family:
            if element not in bee_unique:
               temp_bee.append(element)

         zeros_list = [0] * len(temp_bee)

         dict = {'Family': temp_bee, 'counts': zeros_list} 
            
         temp_df = pd.DataFrame(dict)

         nation_bee_family = pd.concat([nation_bee_family,temp_df]).reset_index(drop=True)

         st.divider()
         st.subheader("Number of Bees per Taxon Family")
         st.dataframe(nation_bee_family)
         
      with col2:

         ### Number of Native Bees per Species
         nation_native_bee = Native_bees['Scientific Name'].value_counts().rename_axis('Scientific Name').reset_index(name='counts')
         nation_native_bee.set_index("Scientific Name", inplace=True)
         nation_native_count = len(Native_bees)

         st.header("Native Bee Species")
         st.metric("(#) of Native Bee Species", nation_native_count)

         ## (National) Number of Native Bees per Family
         nation_native_bee_family = Native_bees['Family'].value_counts().rename_axis('Family').reset_index(name='counts')

         bee_unique = nation_native_bee_family['Family'].values.tolist()

         temp_bee = []
         for element in bee_family:
            if element not in bee_unique:
               temp_bee.append(element)

         zeros_list = [0] * len(temp_bee)

         dict = {'Family': temp_bee, 'counts': zeros_list} 
            
         temp_df = pd.DataFrame(dict)

         nation_native_bee_family = pd.concat([nation_native_bee_family,temp_df]).reset_index(drop=True)

         st.divider()
         st.subheader("Number of Native Bees per Taxon Family")
         st.dataframe(nation_native_bee_family)


with tab2:

   geog_flower = st.radio('Data Level :blossom:', ["National", "State Level", "Park Level"])

   if geog_flower == 'Park Level' :
      select_np = st.selectbox('Pick a National Park',['Acadia National Park','Arches National Park', 'Badlands National Park','Big Bend National Park',
                           'Biscayne National Park', 'Black Canyon of the Gunnison National Park', 'Bryce Canyon National Park',
                           'Canyonlands National Park', 'Capitol Reef National Park', 'Carlsbad Caverns National Park',
                           'Channel Islands National Park', 'Congaree National Park', 'Crater Lake National Park', 'Cuyahoga Valley National Park',
                           'Death Valley National Park', 'Denali National Park', 'Dry Tortugas National Park', 'Everglades National Park',
                           'Gates of the Arctic National Park', 'Gateway Arch National Park', 'Glacier Bay National Park', 'Glacier National Park',
                           'Grand Canyon National Park', 'Grand Teton National Park', 'Great Basin National Park', 'Great Sand Dunes National Park',
                           'Great Smoky Mountains National Park', 'Guadalupe Mountains National Park', 'Haleakalā National Park',
                           'Hawaii Volcanoes National Park', 'Hot Springs National Park', 'Indiana Dunes National Park', 'Isle Royale National Park',
                           'Joshua Tree National Park', 'Katmai National Park', 'Kenai Fjords National Park', 'Kings Canyon National Park',
                           'Kobuk Valley National Park', 'Lake Clark National Park', 'Lassen Volcanic National Park', 'Mammoth Cave National Park',
                           'Mesa Verde National Park', 'Mount Rainier National Park', 'National Park of American Samoa', 'New River Gorge National Park and Preserve',
                           'North Cascades National Park', 'Olympic National Park','Petrified Forest National Park','Pinnacles National Park','Redwood National Park',
                           'Rocky Mountain National Park', 'Saguaro National Park', 'Sequoia National Park', 'Shenandoah National Park','Theodore Roosevelt National Park',
                           'Virgin Islands National Park', 'Voyageurs National Park', 'White Sands National Park', 'Wind Cave National Park', 'Wrangell-St. Elias National Park',
                           'Yellowstone National Park', 'Yosemite National Park','Zion National Park'])
      
      ### Selected National Park
      Park_flowers = NPS_flowers.loc[NPS_flowers['Park Code'] == park_dict[select_np]]
   
      if len(Park_flowers) == 0:
         st.info('The species list for this National Park does not have flower data, report your flower sightings at the link below')
         st.link_button('NPS Species List Contribution', 'https://irma.nps.gov/NPSpecies/Suggest')
      else :
         st.header(select_np)
         col1, col2= st.columns(2)
         with col1:

            flower_species_linelist = Park_flowers.drop(['Park Code', 'Category', 'Order', 'Family', 'Taxon Code', 'Occurrence', 'Nativeness', 'Abundance', 'State'], axis=1)
            flower_species_linelist.set_index("Scientific Name", inplace=True)
            flower_species_linelist.fillna("-")
            flower_species_count = len(flower_species_linelist)
         
            st.header("All Flower Species")
            st.metric("(#) of Flower Species", flower_species_count)

            ## (PARK) Number of Flowers per Family
            park_flower_family = Park_flowers['Family'].value_counts().rename_axis('Family').reset_index(name='counts')

            flower_unique = park_flower_family['Family'].values.tolist()

            temp_flower = []
            for element in flower_family:
               if element not in flower_unique:
                  temp_flower.append(element)

            zeros_list = [0] * len(temp_flower)

            dict = {'Family': temp_flower, 'counts': zeros_list} 
               
            temp_df = pd.DataFrame(dict)

            park_flower_family = pd.concat([park_flower_family,temp_df]).reset_index(drop=True)

            st.divider()
            st.subheader("Number of Flowers per Taxon Family")
            st.dataframe(park_flower_family)

            st.divider()
            st.subheader("Line Listing of Flower Species")
            st.dataframe(flower_species_linelist)
            
         with col2:

            native_flowers = Park_flowers.loc[Park_flowers['Nativeness'] == "Native"]
            flower_native_linelist = native_flowers.drop(['Park Code', 'Category', 'Order', 'Family', 'Taxon Code', 'Occurrence', 'Nativeness', 'Abundance', 'State'], axis=1)
            flower_native_linelist.set_index("Scientific Name", inplace=True)
            flower_native_linelist.fillna("-")
            flower_native_count = len(flower_native_linelist)

            st.header("Native Flower Species")
            st.metric("(#) of Native Flower Species", flower_native_count)

            ## (PARK) Number of Native Flowers per Family
            park_native_flower_family = native_flowers['Family'].value_counts().rename_axis('Family').reset_index(name='counts')

            flower_unique = park_native_flower_family['Family'].values.tolist()

            temp_flower = []
            for element in flower_family:
               if element not in flower_unique:
                  temp_flower.append(element)

            zeros_list = [0] * len(temp_flower)

            dict = {'Family': temp_flower, 'counts': zeros_list} 
               
            temp_df = pd.DataFrame(dict)

            park_native_flower_family = pd.concat([park_native_flower_family,temp_df]).reset_index(drop=True)

            st.divider()
            st.subheader("Number of Native Flowers per Taxon Family")
            st.dataframe(park_native_flower_family)

            st.divider()
            st.subheader("Line Listing of Native Flower Species")
            st.dataframe(flower_native_linelist)

   elif geog_flower == 'State Level' :
      select_state = st.selectbox('Pick State', states)

      ### Selected State
      State_flowers = NPS_flowers.loc[NPS_flowers['State'] == select_state] 

      if len(State_flowers) == 0:
         st.info('The species lists for National Parks in this state do not have flower data, report your flower sightings at the link below')
         st.link_button('NPS Species List Contribution', 'https://irma.nps.gov/NPSpecies/Suggest')
      else :
         st.header(select_state)
         col1, col2= st.columns(2)
         with col1:

            flower_state_species_linelist = State_flowers.drop(['Park Code', 'Category', 'Order', 'Family', 'Taxon Code', 'Occurrence', 'Nativeness', 'Abundance', 'State'], axis=1)
            flower_state_species_linelist.set_index("Scientific Name", inplace=True)
            flower_state_species_linelist.fillna("-")
            flower_state_species_count = len(flower_state_species_linelist)

            st.header("All Flower Species")
            st.metric("(#) of Flower Species", flower_state_species_count)

            ## (STATE) Number of Bees per Family
            state_flower_family = State_flowers['Family'].value_counts().rename_axis('Family').reset_index(name='counts')

            flower_unique = state_flower_family['Family'].values.tolist()

            temp_flower = []
            for element in flower_family:
               if element not in flower_unique:
                  temp_flower.append(element)

            zeros_list = [0] * len(temp_flower)

            dict = {'Family': temp_flower, 'counts': zeros_list} 
               
            temp_df = pd.DataFrame(dict)

            state_flower_family = pd.concat([state_flower_family,temp_df]).reset_index(drop=True)

            st.divider()
            st.subheader("Number of Flowers per Taxon Family")
            st.dataframe(state_flower_family)

            st.divider()
            st.subheader("Line Listing of Flower Species")
            st.dataframe(flower_state_species_linelist)
            
         with col2:

            state_native_flowers = State_flowers.loc[State_flowers['Nativeness'] == "Native"]
            flower_state_native_linelist = state_native_flowers.drop(['Park Code', 'Category', 'Order', 'Family', 'Taxon Code', 'Occurrence', 'Nativeness', 'Abundance', 'State'], axis=1)
            flower_state_native_linelist.set_index("Scientific Name", inplace=True)
            flower_state_native_linelist.fillna("-")
            flower_state_native_count = len(flower_state_native_linelist)

            st.header("Native Flower Species")
            st.metric("(#) of Native Flower Species", flower_state_native_count)

            ## (STATE) Number of Native Bees per Family
            state_native_flower_family = state_native_flowers['Family'].value_counts().rename_axis('Family').reset_index(name='counts')

            flower_unique = state_native_flower_family['Family'].values.tolist()

            temp_flower = []
            for element in flower_family:
               if element not in flower_unique:
                  temp_flower.append(element)

            zeros_list = [0] * len(temp_flower)

            dict = {'Family': temp_flower, 'counts': zeros_list} 
               
            temp_df = pd.DataFrame(dict)

            state_native_flower_family = pd.concat([state_native_flower_family,temp_df]).reset_index(drop=True)

            st.divider()
            st.subheader("Number of Native Flowers per Taxon Family")
            st.dataframe(state_native_flower_family)

            st.divider()
            st.subheader("Line Listing of Native Flower Species")
            st.dataframe(flower_state_native_linelist)

   else : 
      st.header('National Level Flower Data')

      on_park_flower = st.toggle('Show Aggregate Level Park Data :blossom:')

      if on_park_flower:
         with st.container():
            col1, col2= st.columns(2)
            with col1:
               ## (National) Number of Flower Families by Park
               nation_park_flower = pd.DataFrame(flower_family)
               nation_park_flower.columns = ["Family"]
               nation_park_flower.set_index("Family", inplace=True)
               
               for i in parks:
                    temp_flower = NPS_flowers.loc[NPS_flowers['Park Code'] == i]
                    temp_flower_family = pd.DataFrame(temp_flower['Family'].value_counts().rename_axis('Family').reset_index(name='counts'))
                    nation_park_flower = pd.concat([nation_park_flower,temp_flower_family.set_index('Family')], axis=1).fillna(0)

               nation_park_flower.columns = parks
               
               st.subheader("Number of Flower per Taxon Family by Park")
               st.dataframe(nation_park_flower)

               ## (National) Number of Native Flower Families by Park
               nation_park_native_flower = pd.DataFrame(flower_family)
               nation_park_native_flower.columns = ["Family"]
               nation_park_native_flower.set_index("Family", inplace=True)
               
               for i in parks:
                  temp_flower = Native_flowers.loc[Native_flowers['Park Code'] == i]
                  temp_flower_family = pd.DataFrame(temp_flower['Family'].value_counts().rename_axis('Family').reset_index(name='counts'))
                  nation_park_native_flower = pd.concat([nation_park_native_flower,temp_flower_family.set_index('Family')], axis=1).fillna(0)

               nation_park_native_flower.columns = parks

               st.divider()
               st.subheader("Number of Native Flowers per Taxon Family by Park")
               st.dataframe(nation_park_native_flower)

            with col2:

               nation_park_flower['Max'] = nation_park_flower.idxmax(axis=1)
               nation_park_flower_diverse = nation_park_flower[['Max']]

               st.subheader("Where Should I Go to See the Most Species of Flowers?")
               st.dataframe(nation_park_flower_diverse)

               nation_park_native_flower['Max'] = nation_park_native_flower.idxmax(axis=1)
               nation_park_native_flower_diverse =nation_park_native_flower[['Max']]

               st.divider()
               st.subheader("Where Should I Go to See the Most Species of Native Flowers?")
               st.dataframe(nation_park_native_flower_diverse)

      st.divider()

      on_state_flower = st.toggle('Show Aggregate Level State Data :blossom:')

      if on_state_flower:
         with st.container():
            col1, col2= st.columns(2)
            with col1:

               ## (National) Number of Flower Families by State
               nation_state_flower = pd.DataFrame(flower_family)
               nation_state_flower.columns = ["Family"]
               nation_state_flower.set_index("Family", inplace=True)
               for i in states:
                  temp_flower = NPS_flowers.loc[NPS_flowers['State'] == i]
                  temp_flower_family = pd.DataFrame(temp_flower['Family'].value_counts().rename_axis('Family').reset_index(name='counts'))
                  nation_state_flower = pd.concat([nation_state_flower,temp_flower_family.set_index('Family')], axis=1).fillna(0)

               nation_state_flower.columns = states

               st.subheader("Number of Flowers per Taxon Family by State")
               st.dataframe(nation_state_flower)

               ## (National) Number of Native Flower Families by State
               nation_state_native_flower = pd.DataFrame(flower_family)
               nation_state_native_flower.columns = ["Family"]
               nation_state_native_flower.set_index("Family", inplace=True)
               for i in states:
                  temp_flower = Native_flowers.loc[Native_flowers['State'] == i]
                  temp_flower_family = pd.DataFrame(temp_flower['Family'].value_counts().rename_axis('Family').reset_index(name='counts'))
                  nation_state_native_flower = pd.concat([nation_state_native_flower,temp_flower_family.set_index('Family')], axis=1).fillna(0)

               nation_state_native_flower.columns = states

               st.divider()
               st.subheader("Number of Native Flowers per Taxon Family by State")
               st.dataframe(nation_state_native_flower)

            with col2:
               
               nation_state_flower['Max'] = nation_state_flower.idxmax(axis=1)
               nation_state_flower_diverse = nation_state_flower[['Max']]
            
               st.subheader("Where Should I Go to See the Most Species of Flowers?")
               st.dataframe(nation_state_flower_diverse)

               nation_state_native_flower['Max'] = nation_state_native_flower.idxmax(axis=1)
               nation_state_native_flower_diverse = nation_state_native_flower[['Max']]

               st.divider()
               st.subheader("Where Should I Go to See the Most Species of Native Flowers?")
               st.dataframe(nation_state_native_flower_diverse)

      st.divider()

      col1, col2= st.columns(2)
      
      with col1:

         ### Number of Bees per Species
         nation_flower = NPS_flowers['Scientific Name'].value_counts().rename_axis('Scientific Name').reset_index(name='counts')
         nation_flower.set_index("Scientific Name", inplace=True)
         nation_flower_count = len(NPS_flowers)

         st.header("All Flower Species")
         st.metric("(#) of Flower Species", nation_flower_count)

         ## (National) Number of Bees per Family
         nation_flower_family = NPS_flowers['Family'].value_counts().rename_axis('Family').reset_index(name='counts')

         flower_unique = nation_flower_family['Family'].values.tolist()

         temp_flower = []
         for element in flower_family:
            if element not in flower_unique:
               temp_flower.append(element)

         zeros_list = [0] * len(temp_flower)

         dict = {'Family': temp_flower, 'counts': zeros_list} 
            
         temp_df = pd.DataFrame(dict)

         nation_flower_family = pd.concat([nation_flower_family,temp_df]).reset_index(drop=True)

         st.divider()
         st.subheader("Number of Flowers per Taxon Family")
         st.dataframe(nation_flower_family)

         
      with col2:

         ### Number of Native Bees per Species
         nation_native_flower = Native_flowers['Scientific Name'].value_counts().rename_axis('Scientific Name').reset_index(name='counts')
         nation_native_flower.set_index("Scientific Name", inplace=True)
         nation_native_flower_count = len(Native_flowers)

         st.header("Native Flower Species")
         st.metric("(#) of Native Flower Species", nation_native_flower_count)

         ## (National) Number of Native Bees per Family
         nation_native_flower_family = Native_flowers['Family'].value_counts().rename_axis('Family').reset_index(name='counts')

         flower_unique = nation_native_flower_family['Family'].values.tolist()

         temp_flower = []
         for element in flower_family:
            if element not in flower_unique:
               temp_flower.append(element)

         zeros_list = [0] * len(temp_flower)

         dict = {'Family': temp_flower, 'counts': zeros_list} 
            
         temp_df = pd.DataFrame(dict)

         nation_native_flower_family = pd.concat([nation_native_flower_family,temp_df]).reset_index(drop=True)

         st.divider()
         st.subheader("Number of Native Flowers per Taxon Family")
         st.dataframe(nation_native_flower_family)



