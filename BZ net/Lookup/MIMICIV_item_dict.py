chart_item_dict = {
'AF0': 224690,
'AF1': 220210,
'BE_arteriell': 224828,
'Compliance': 229661,
'DAP': 220051,
'FiO2': 223835,
'GOT': 220587,
'GPT': 220644,
'HF': 220045,
'Expiratory Ratio': 226871,
'Inspiratory Ratio': 226873,
'Koerperkerntemperatur F': 223761,
'Koerperkerntemperatur C': 223762,
'MAP': 220052,
'PEEP': 220339,
'SAP': 220050,
'SaO2': 220227,
'SpO2': 220277,
'SzvO2': 223772,
'ZVD': 220074,
'pH_arteriell': 223830,
'paCO2_(ohne_Temp-Korrektur)': 220235,
'paO2_(ohne_Temp-Korrektur)': 220224,
'EVLWI': 228179,
'CK-MB_MIMIC': 227445,
'PCWP': 223771,
'MPAP': 220061,
'SV_kontinuierlich0': 227547,
'SV_kontinuierlich1': 228374,
'HZV_(kontinuierlich)': 224842,
'BNP_MIMIC': 227446,
'Inhalatives_NO': 224749,
'DPAP': 220060,
'SVRI': 228185,
'GEDVI': 228180,
'P_EI': 224696,
'SPAP': 220059,
'etCO2': 228640,
'Tidalvolumen': 224685,
'Tidalvolumen_spont0': 224686,
'Tidalvolumen_spont1': 224421,
'SVI_(kontinuierlich)': 228182,
'AF_spontan0': 224689,
'AF_spontan1': 224422,
'LDH_MIMIC': 220632,
'Lymphozyten_absolut': 229358,
'HI_(kontinuierlich)': 228368,
'Lagerungstherapie': 224093,
'ECMO': 229267,
'Extrakorporaler_Gasfluss_(O2)': 229278,
'Gaszusammensetzung_(%O2)': 229280,
'Extrakorporaler_Blutfluss': 229270,
'D-Dimere': 225636
}
lab_item_dict = {
'Amylase': 50867,
'Bilirubin_ges.': 50885,
'CK': 50910,
'Harnstoff': 51006,
'Haematokrit': 51221,
'Haemoglobin0': 51222,
'Haemoglobin1': 50811,
'INR': 51237,
'Kreatinin': 50912,
'Leukozyten': 51301,
'Lipase_MIMIC': 50956,
'pTT': 51275,
'Troponin': 51003,
'Thrombozyten': 51265,
'Albumin': 50862,
'CRP': 50889,
'NT-pro_BNP': 50963
}
input_item_dict = {
'Furosemid_intravenoes_kontinuierlich': 221794,
'Norepinephrin_intravenoes_kontinuierlich': 221906,
'Propofol_intravenoes_kontinuierlich': 222168,
'Vasopressin_intravenoes_kontinuierlich': 222315,
'Rocuronium_intravenoes_bolusweise': 229233,
'Midazolam_intravenoes_kontinuierlich': 221668,
'Morphin_intravenoes_kontinuierlich': 225154,
'Milrinon_intravenoes_kontinuierlich': 221986,
'Fentanyl_intravenoes_kontinuierlich': 221744,
'Dobutamin_intravenoes_kontinuierlich': 221653,
'Ketanest_intravenoes_kontinuierlich': 221712,
'Epinephrin_intravenoes_kontinuierlich': 221289,
'Dexmedetomidin_intravenoes_kontinuierlich': 229420
}
procedure_item_dict = {
'Sevofluran_inhalativ': 229984,
'Isofluran_inhalativ': 229983
}
lab_item_dict_rev = {
50867 : 'Amylase',
50885 : 'Bilirubin_ges.',
50910 : 'CK',
51006 : 'Harnstoff',
51221 : 'Haematokrit',
51222 : 'Haemoglobin0',
50811 : 'Haemoglobin1',
51237 : 'INR',
50912 : 'Kreatinin',
51301 : 'Leukozyten',
50956 : 'Lipase_MIMIC',
51275 : 'pTT',
51003 : 'Troponin',
51265 : 'Thrombozyten',
50862 : 'Albumin',
50889 : 'CRP',
50963 : 'NT-pro_BNP'
}
lab_index_dict = {
50867 : 0,
50885 : 1,
50910 : 2,
51006 : 3,
51221 : 4,
51222 : 5,
50811 : 6,
51237 : 7,
50912 : 8,
51301 : 9,
50956 : 10,
51275 : 11,
51003 : 12,
51265 : 13,
50862 : 14,
50889 : 15,
50963 : 16
}
lab_index_dict_rev = {
0 : 50867,
1 : 50885,
2 : 50910,
3 : 51006,
4 : 51221,
5 : 51222,
6 : 50811,
7 : 51237,
8 : 50912,
9 : 51301,
10 : 50956,
11 : 51275,
12 : 51003,
13 : 51265,
14 : 50862,
15 : 50889,
16 : 50963
}
chart_item_dict_rev = {
224690 : 'AF0',
220210 : 'AF1',
224828 : 'BE_arteriell',
229661 : 'Compliance',
220051 : 'DAP',
223835 : 'FiO2',
220587 : 'GOT',
220644 : 'GPT',
220045 : 'HF',
226871 : 'Expiratory Ratio',
226873 : 'Inspiratory Ratio',
223761 : 'Koerperkerntemperatur F',
223762 : 'Koerperkerntemperatur C',
220052 : 'MAP',
220339 : 'PEEP',
220050 : 'SAP',
220227 : 'SaO2',
220277 : 'SpO2',
223772 : 'SzvO2',
220074 : 'ZVD',
223830 : 'pH_arteriell',
220235 : 'paCO2_(ohne_Temp-Korrektur)',
220224 : 'paO2_(ohne_Temp-Korrektur)',
228179 : 'EVLWI',
227445 : 'CK-MB_MIMIC',
223771 : 'PCWP',
220061 : 'MPAP',
227547 : 'SV_kontinuierlich0',
228374 : 'SV_kontinuierlich1',
224842 : 'HZV_(kontinuierlich)',
227446 : 'BNP_MIMIC',
224749 : 'Inhalatives_NO',
220060 : 'DPAP',
228185 : 'SVRI',
228180 : 'GEDVI',
224696 : 'P_EI',
220059 : 'SPAP',
228640 : 'etCO2',
224685 : 'Tidalvolumen',
224686 : 'Tidalvolumen_spont0',
224421 : 'Tidalvolumen_spont1',
228182 : 'SVI_(kontinuierlich)',
224689 : 'AF_spontan0',
224422 : 'AF_spontan1',
220632 : 'LDH_MIMIC',
229358 : 'Lymphozyten_absolut',
228368 : 'HI_(kontinuierlich)',
224093 : 'Lagerungstherapie',
229267 : 'ECMO',
229278 : 'Extrakorporaler_Gasfluss_(O2)',
229280 : 'Gaszusammensetzung_(%O2)',
229270 : 'Extrakorporaler_Blutfluss',
225636 : 'D-Dimere'
}
chart_index_dict = {
224690 : 0,
220210 : 1,
224828 : 2,
229661 : 3,
220051 : 4,
223835 : 5,
220587 : 6,
220644 : 7,
220045 : 8,
226871 : 9,
226873 : 10,
223761 : 11,
223762 : 12,
220052 : 13,
220339 : 14,
220050 : 15,
220227 : 16,
220277 : 17,
223772 : 18,
220074 : 19,
223830 : 20,
220235 : 21,
220224 : 22,
228179 : 23,
227445 : 24,
223771 : 25,
220061 : 26,
227547 : 27,
228374 : 28,
224842 : 29,
227446 : 30,
224749 : 31,
220060 : 32,
228185 : 33,
228180 : 34,
224696 : 35,
220059 : 36,
228640 : 37,
224685 : 38,
224686 : 39,
224421 : 40,
228182 : 41,
224689 : 42,
224422 : 43,
220632 : 44,
229358 : 45,
228368 : 46,
224093 : 47,
229267 : 48,
229278 : 49,
229280 : 50,
229270 : 51,
225636 : 52
}
chart_index_dict_rev = {
0 : 224690,
1 : 220210,
2 : 224828,
3 : 229661,
4 : 220051,
5 : 223835,
6 : 220587,
7 : 220644,
8 : 220045,
9 : 226871,
10 : 226873,
11 : 223761,
12 : 223762,
13 : 220052,
14 : 220339,
15 : 220050,
16 : 220227,
17 : 220277,
18 : 223772,
19 : 220074,
20 : 223830,
21 : 220235,
22 : 220224,
23 : 228179,
24 : 227445,
25 : 223771,
26 : 220061,
27 : 227547,
28 : 228374,
29 : 224842,
30 : 227446,
31 : 224749,
32 : 220060,
33 : 228185,
34 : 228180,
35 : 224696,
36 : 220059,
37 : 228640,
38 : 224685,
39 : 224686,
40 : 224421,
41 : 228182,
42 : 224689,
43 : 224422,
44 : 220632,
45 : 229358,
46 : 228368,
47 : 224093,
48 : 229267,
49 : 229278,
50 : 229280,
51 : 229270,
52 : 225636
}
input_item_dict_rev = {
221794 : 'Furosemid_intravenoes_kontinuierlich',
221906 : 'Norepinephrin_intravenoes_kontinuierlich',
222168 : 'Propofol_intravenoes_kontinuierlich',
222315 : 'Vasopressin_intravenoes_kontinuierlich',
229233 : 'Rocuronium_intravenoes_bolusweise',
221668 : 'Midazolam_intravenoes_kontinuierlich',
225154 : 'Morphin_intravenoes_kontinuierlich',
221986 : 'Milrinon_intravenoes_kontinuierlich',
221744 : 'Fentanyl_intravenoes_kontinuierlich',
221653 : 'Dobutamin_intravenoes_kontinuierlich',
221712 : 'Ketanest_intravenoes_kontinuierlich',
221289 : 'Epinephrin_intravenoes_kontinuierlich',
229420 : 'Dexmedetomidin_intravenoes_kontinuierlich'
}
input_index_dict = {
221794 : 0,
221906 : 1,
222168 : 2,
222315 : 3,
229233 : 4,
221668 : 5,
225154 : 6,
221986 : 7,
221744 : 8,
221653 : 9,
221712 : 10,
221289 : 11,
229420 : 12
}
input_index_dict_rev = {
0 : 221794,
1 : 221906,
2 : 222168,
3 : 222315,
4 : 229233,
5 : 221668,
6 : 225154,
7 : 221986,
8 : 221744,
9 : 221653,
10 : 221712,
11 : 221289,
12 : 229420
}
procedure_item_dict_rev = {
229984 : 'Sevofluran_inhalativ',
229983 : 'Isofluran_inhalativ'
}
procedure_index_dict = {
229984 : 0,
229983 : 1
}
procedure_index_dict_rev = {
0 : 229984,
1 : 229983
}
# FIXME adjust AF, Temperatur, Tidalvolumen_spont, AF_spont SV_(kontinuierlich), Haemoglobin
mimiciv_mapping = {
224690 : 'AF',
220210 : 'AF',
224828 : 'BE_arteriell',
229661 : 'Compliance',
220051 : 'DAP',
223835 : 'FiO2',
220587 : 'GOT',
220644 : 'GPT',
220045 : 'HF',
226871 : 'Expiratory Ratio',
226873 : 'Inspiratory Ratio',
223761 : 'Koerperkerntemperatur',
223762 : 'Koerperkerntemperatur',
220052 : 'MAP',
220339 : 'PEEP',
220050 : 'SAP',
220227 : 'SaO2',
220277 : 'SpO2',
223772 : 'SzvO2',
220074 : 'ZVD',
223830 : 'pH_arteriell',
220235 : 'paCO2_(ohne_Temp-Korrektur)',
220224 : 'paO2_(ohne_Temp-Korrektur)',
228179 : 'EVLWI',
227445 : 'CK-MB_MIMIC',
223771 : 'PCWP',
220061 : 'MPAP',
227547 : 'SV_(kontinuierlich)',
228374 : 'SV_(kontinuierlich)',
224842 : 'HZV_(kontinuierlich)',
227446 : 'BNP_MIMIC',
224749 : 'Inhalatives_NO',
220060 : 'DPAP',
228185 : 'SVRI',
228180 : 'GEDVI',
224696 : 'P_EI',
220059 : 'SPAP',
228640 : 'etCO2',
224685 : 'Tidalvolumen',
224686 : 'Tidalvolumen_spont',
224421 : 'Tidalvolumen_spont',
228182 : 'SVI_(kontinuierlich)',
224689 : 'AF_spontan',
224422 : 'AF_spontan',
220632 : 'LDH_MIMIC',
229358 : 'Lymphozyten_absolut',
228368 : 'HI_(kontinuierlich)',
224093 : 'Lagerungstherapie',
229267 : 'ECMO',
229278 : 'Extrakorporaler_Gasfluss_(O2)',
229280 : 'Gaszusammensetzung_(%O2)',
229270 : 'Extrakorporaler_Blutfluss',
225636 : 'D-Dimere',
50867 : 'Amylase',
50885 : 'Bilirubin_ges.',
50910 : 'CK',
51006 : 'Harnstoff',
51221 : 'Haematokrit',
51222 : 'Haemoglobin',
50811 : 'Haemoglobin',
51237 : 'INR',
50912 : 'Kreatinin',
51301 : 'Leukozyten',
50956 : 'Lipase_MIMIC',
51275 : 'pTT',
51003 : 'Troponin',
51265 : 'Thrombozyten',
50862 : 'Albumin',
50889 : 'CRP',
50963 : 'NT-pro_BNP',
221794 : 'Furosemid_intravenoes_kontinuierlich',
221906 : 'Norepinephrin_intravenoes_kontinuierlich',
222168 : 'Propofol_intravenoes_kontinuierlich',
222315 : 'Vasopressin_intravenoes_kontinuierlich',
229233 : 'Rocuronium_intravenoes_bolusweise',
221668 : 'Midazolam_intravenoes_kontinuierlich',
225154 : 'Morphin_intravenoes_kontinuierlich',
221986 : 'Milrinon_intravenoes_kontinuierlich',
221744 : 'Fentanyl_intravenoes_kontinuierlich',
221653 : 'Dobutamin_intravenoes_kontinuierlich',
221712 : 'Ketanest_intravenoes_kontinuierlich',
221289 : 'Epinephrin_intravenoes_kontinuierlich',
229420 : 'Dexmedetomidin_intravenoes_kontinuierlich',
229984 : 'Sevofluran_inhalativ',
229983 : 'Isofluran_inhalativ'
}

dict_multiple = {
    223761: 0,
    223762: 0,
    227547: 1,
    224689: 1,
    51222: 2, 
    50811: 2,
    224690 : 3,
    220210 : 3,
    224689 : 4,
    224422 : 4,
    224686 : 5,
    224421 : 5
}

dict_multiple_rev = {
    
    0: [223761,223762],
    1: [227547, 228374],
    2: [51222, 50811],
    3: [224690, 220210],
    4: [224689, 224422],
    5: [224686, 224421]
}