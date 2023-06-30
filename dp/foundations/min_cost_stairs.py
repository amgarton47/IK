def min_cost_climbing_stairs(cost):
    if len(cost) == 2:
        return min(cost)

    table = [0 for _ in range(len(cost))]

    table[0] = cost[0]
    table[1] = cost[1]

    for i in range(1, len(cost)):
        table[i] = cost[i] + min(table[i - 1], table[i - 2])

    return min(table[-2], table[-1])


input = [1, 1, 2]
# input = [3, 4]

# input = [
#     700,
#     983,
#     364,
#     791,
#     108,
#     462,
#     744,
#     1,
#     477,
#     670,
#     602,
#     147,
#     995,
#     173,
#     970,
#     171,
#     810,
#     174,
#     803,
#     755,
#     22,
#     754,
#     525,
#     137,
#     403,
#     325,
#     270,
#     402,
#     623,
#     331,
#     371,
#     689,
#     680,
#     978,
#     852,
#     810,
#     403,
#     622,
#     54,
#     239,
#     146,
#     491,
#     478,
#     318,
#     319,
#     597,
#     228,
#     847,
#     111,
#     429,
#     810,
#     57,
#     25,
#     690,
#     840,
#     4,
#     138,
#     513,
#     601,
#     144,
#     935,
#     477,
#     91,
#     440,
#     866,
#     829,
#     393,
#     222,
#     395,
#     212,
#     407,
#     275,
#     381,
#     443,
#     669,
#     842,
#     42,
#     632,
#     945,
#     218,
#     687,
#     926,
#     936,
#     440,
#     603,
#     925,
#     685,
#     189,
#     128,
#     616,
#     232,
#     222,
#     40,
#     315,
#     621,
#     444,
#     532,
#     778,
#     449,
#     14,
#     466,
#     467,
#     578,
#     672,
#     635,
#     705,
#     225,
#     790,
#     971,
#     729,
#     252,
#     620,
#     665,
#     107,
#     153,
#     878,
#     538,
#     982,
#     573,
#     154,
#     645,
#     136,
#     192,
#     62,
#     844,
#     550,
#     90,
#     895,
#     824,
#     477,
#     248,
#     229,
#     686,
#     820,
#     865,
#     262,
#     50,
#     479,
#     466,
#     334,
#     105,
#     810,
#     253,
#     391,
#     140,
#     656,
#     682,
#     999,
#     220,
#     396,
#     73,
#     506,
#     208,
#     354,
#     702,
#     140,
#     968,
#     343,
#     936,
#     981,
#     710,
#     67,
#     335,
#     626,
#     661,
#     96,
#     616,
#     754,
#     471,
#     222,
#     656,
#     276,
#     510,
#     217,
#     29,
#     969,
#     563,
#     595,
#     922,
#     115,
#     276,
#     677,
#     874,
#     412,
#     239,
#     819,
#     654,
#     131,
#     733,
#     627,
#     893,
#     482,
#     57,
#     346,
#     870,
#     769,
#     294,
#     150,
#     812,
#     227,
#     950,
#     434,
#     437,
#     884,
#     565,
#     335,
#     175,
#     171,
#     47,
#     671,
#     147,
#     303,
#     286,
#     427,
#     329,
#     177,
#     331,
#     430,
#     667,
#     830,
#     841,
#     270,
#     185,
#     326,
#     875,
#     875,
#     486,
#     389,
#     214,
#     453,
#     777,
#     28,
#     609,
#     880,
#     592,
#     439,
#     83,
#     984,
#     505,
#     922,
#     974,
#     339,
#     389,
#     953,
#     692,
#     414,
#     993,
#     351,
#     407,
#     316,
#     606,
#     700,
#     342,
#     415,
#     337,
#     480,
#     975,
#     941,
#     370,
#     71,
#     662,
#     699,
#     442,
#     933,
#     881,
#     811,
#     708,
#     914,
#     705,
#     305,
#     588,
#     193,
#     227,
#     558,
#     431,
#     769,
#     316,
#     941,
#     845,
#     252,
#     795,
#     930,
#     373,
#     612,
#     166,
#     570,
#     771,
#     518,
#     911,
#     557,
#     450,
#     704,
#     866,
#     484,
#     361,
#     575,
#     492,
#     536,
#     132,
#     722,
#     526,
#     656,
#     963,
#     306,
#     924,
#     668,
#     796,
#     290,
#     499,
#     526,
#     156,
#     640,
#     206,
#     988,
#     713,
#     453,
#     959,
#     687,
#     205,
#     896,
#     469,
#     788,
#     16,
#     349,
#     854,
#     584,
#     580,
#     190,
#     140,
#     631,
#     892,
#     282,
#     357,
#     927,
#     883,
#     751,
#     720,
#     191,
#     404,
#     876,
#     857,
#     14,
#     600,
#     837,
#     207,
#     821,
#     399,
#     817,
#     569,
#     411,
#     824,
#     743,
#     161,
#     662,
#     614,
#     324,
#     528,
#     363,
#     733,
#     748,
#     320,
#     153,
#     503,
#     639,
#     290,
#     25,
#     907,
#     518,
#     525,
#     693,
#     891,
#     367,
#     140,
#     976,
#     137,
#     140,
#     147,
#     866,
#     129,
#     733,
#     264,
#     137,
#     415,
#     400,
#     118,
#     893,
#     711,
#     833,
#     708,
#     451,
#     913,
#     257,
#     654,
#     425,
#     686,
#     964,
#     854,
#     815,
#     682,
#     154,
#     978,
#     923,
#     831,
#     953,
#     539,
#     746,
#     78,
#     361,
#     417,
#     824,
#     338,
#     103,
#     780,
#     257,
#     86,
#     285,
#     776,
#     788,
#     527,
#     324,
#     180,
#     731,
#     7,
#     107,
#     228,
#     383,
#     199,
#     545,
#     463,
#     188,
#     263,
#     171,
#     796,
#     279,
#     316,
#     102,
#     31,
#     420,
#     288,
#     457,
#     304,
#     608,
#     464,
#     106,
#     947,
#     409,
#     879,
#     968,
#     570,
#     535,
#     932,
#     925,
#     951,
#     975,
#     741,
#     880,
#     468,
#     216,
#     959,
#     168,
#     624,
#     729,
#     20,
#     815,
#     986,
#     302,
#     35,
#     624,
#     167,
#     553,
#     742,
#     292,
#     687,
#     126,
#     606,
#     543,
#     207,
#     685,
#     101,
#     226,
#     548,
#     880,
#     734,
#     313,
#     125,
#     434,
#     639,
#     784,
#     241,
#     198,
#     549,
#     660,
#     745,
#     731,
#     897,
#     583,
#     408,
#     189,
#     37,
#     187,
#     884,
#     564,
#     428,
#     425,
#     449,
#     275,
#     262,
#     203,
#     188,
#     493,
#     310,
#     977,
#     195,
#     521,
#     995,
#     376,
#     824,
#     424,
#     718,
#     421,
#     592,
#     463,
#     950,
#     889,
#     22,
#     975,
#     270,
#     654,
#     553,
#     782,
#     798,
#     495,
#     628,
#     499,
#     112,
#     758,
#     280,
#     997,
#     776,
#     343,
#     105,
#     657,
#     754,
#     19,
#     59,
#     702,
#     75,
#     214,
#     586,
#     25,
#     192,
#     746,
#     348,
#     675,
#     836,
#     158,
#     182,
#     44,
#     791,
#     916,
#     396,
#     241,
#     48,
#     217,
#     133,
#     164,
#     283,
#     901,
#     44,
#     466,
#     8,
#     366,
#     438,
#     592,
#     789,
#     257,
#     912,
#     121,
#     643,
#     197,
#     620,
#     737,
#     691,
#     213,
#     751,
#     688,
#     647,
#     231,
#     479,
#     878,
#     601,
#     508,
#     122,
#     652,
#     791,
#     984,
#     316,
#     390,
#     89,
#     84,
#     144,
#     623,
#     442,
#     445,
#     857,
#     779,
#     130,
#     436,
#     448,
#     564,
#     348,
#     149,
#     60,
#     34,
#     757,
#     291,
#     653,
#     245,
#     111,
#     468,
#     86,
#     866,
#     651,
#     906,
#     380,
#     105,
#     463,
#     769,
#     600,
#     284,
#     831,
#     943,
#     787,
#     648,
#     244,
#     322,
#     634,
#     929,
#     98,
#     337,
#     194,
#     555,
#     48,
#     741,
#     820,
#     158,
#     553,
#     193,
#     258,
#     80,
#     903,
#     976,
#     311,
#     316,
#     846,
#     596,
#     918,
#     568,
#     5,
#     697,
#     179,
#     622,
#     682,
#     304,
#     962,
#     890,
#     705,
#     24,
#     694,
#     615,
#     486,
#     928,
#     786,
#     9,
#     12,
#     336,
#     649,
#     95,
#     315,
#     539,
#     430,
#     740,
#     730,
#     631,
#     60,
#     854,
#     62,
#     673,
#     479,
#     693,
#     982,
#     609,
#     581,
#     934,
#     99,
#     328,
#     808,
#     929,
#     480,
#     119,
#     109,
#     155,
#     880,
#     394,
#     158,
#     876,
#     636,
#     493,
#     961,
#     915,
#     703,
#     885,
#     10,
#     372,
#     218,
#     876,
#     366,
#     298,
#     143,
#     485,
#     364,
#     690,
#     978,
#     312,
#     442,
#     305,
#     480,
#     800,
#     737,
#     149,
#     829,
#     555,
#     102,
#     357,
#     893,
#     667,
#     900,
#     555,
#     499,
#     21,
#     412,
#     378,
#     294,
#     486,
#     766,
#     374,
#     561,
#     331,
#     522,
#     200,
#     777,
#     390,
#     79,
#     815,
#     326,
#     121,
#     348,
#     116,
#     846,
#     139,
#     822,
#     784,
#     672,
#     455,
#     712,
#     649,
#     364,
#     475,
#     44,
#     922,
#     366,
#     145,
#     333,
#     812,
#     936,
#     64,
#     417,
#     644,
#     432,
#     670,
#     149,
#     625,
#     390,
#     846,
#     462,
#     668,
#     935,
#     713,
#     237,
#     264,
#     194,
#     871,
#     425,
#     783,
#     96,
#     42,
#     734,
#     456,
#     794,
#     856,
#     729,
#     297,
#     800,
#     264,
#     620,
#     774,
#     505,
#     13,
#     614,
#     483,
#     904,
#     2,
#     155,
#     25,
#     369,
#     258,
#     354,
#     990,
#     948,
#     437,
#     398,
#     757,
#     621,
#     535,
#     386,
#     710,
#     190,
#     841,
#     952,
#     964,
#     764,
#     907,
#     791,
#     738,
#     218,
#     66,
#     832,
#     153,
#     730,
#     57,
#     324,
#     930,
#     685,
#     440,
#     584,
#     299,
#     971,
#     745,
#     237,
#     96,
#     933,
#     331,
#     126,
#     157,
#     925,
#     257,
#     797,
#     17,
#     212,
#     389,
#     605,
#     238,
#     171,
#     738,
#     493,
#     305,
#     640,
#     44,
#     839,
#     17,
#     861,
#     499,
#     212,
#     749,
#     401,
#     524,
#     526,
#     252,
#     212,
#     74,
#     34,
#     136,
#     36,
#     6,
#     188,
#     281,
#     947,
#     984,
#     764,
#     133,
#     750,
#     169,
#     277,
#     541,
#     516,
#     879,
#     610,
#     176,
#     203,
#     301,
#     536,
#     820,
#     207,
#     711,
#     185,
#     284,
#     373,
#     168,
#     37,
#     472,
#     165,
#     470,
#     459,
#     109,
#     723,
#     324,
#     485,
#     785,
#     123,
#     505,
#     780,
#     704,
#     706,
#     751,
#     559,
#     430,
#     558,
#     144,
#     810,
#     748,
#     234,
#     968,
#     4,
#     848,
#     212,
#     412,
#     695,
#     660,
#     763,
#     22,
#     485,
#     32,
#     165,
#     34,
#     394,
#     757,
#     824,
#     648,
#     846,
#     917,
#     67,
#     639,
#     974,
#     655,
#     329,
#     777,
#     284,
#     4,
#     901,
#     643,
#     854,
#     255,
#     989,
#     203,
#     348,
#     549,
#     657,
#     650,
#     372,
#     700,
#     980,
#     97,
#     934,
#     586,
#     422,
#     929,
#     445,
#     122,
#     309,
#     240,
#     888,
#     178,
#     251,
#     39,
#     253,
#     959,
#     387,
#     323,
#     336,
#     194,
#     325,
#     233,
#     78,
#     81,
#     280,
#     333,
#     522,
#     216,
#     744,
#     91,
# ]

out = min_cost_climbing_stairs(input)
print(out)
