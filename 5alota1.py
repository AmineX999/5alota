import heapq
import random

values = [707, 684, 722, 586, 699, 703, 620, 821, 834, 843, 859, 588, 717, 819, 815, 817, 581, 834, 711, 874, 820, 842, 638, 890, 693, 823, 860, 635, 393, 805, 799, 865, 852, 910, 362, 707, 608, 925, 918, 829, 784, 832, 914, 900, 833, 815, 731, 952, 857, 706, 400, 927, 867, 897, 925, 920, 785, 726, 736, 1010, 972, 570, 893, 695, 547, 1018, 952, 929, 583, 853, 707, 701, 821, 879, 912, 978, 1025, 880, 891, 793, 931, 969, 714, 1004, 993, 1041, 593, 815, 938, 1062, 895, 920, 772, 1062, 717, 955, 994, 558, 659, 909, 1060, 649, 780, 920, 943, 793, 999, 544, 675, 789, 1061, 767, 954, 932, 1088, 857, 1093, 921, 601, 964, 755, 739, 1104, 754, 555, 768, 1051, 990, 684, 523, 1063, 816, 797, 777, 1076, 534, 796, 722, 704, 1090, 978, 957, 841, 1037, 994, 708, 924, 692, 622, 843, 1089, 954, 735, 753, 1076, 925, 907, 923, 719, 984, 932, 801, 828, 1018, 907, 1085, 1128, 1151, 886, 673, 919, 826, 939, 761, 1111, 819, 563, 805, 1013, 835, 1193, 975, 706, 786, 642, 1199, 757, 837, 711, 992, 824, 1067, 691, 937, 1142, 1212, 780, 813, 447, 967, 1051, 1028, 773, 703, 919, 598, 587, 1177, 695, 724, 641, 838, 1324, 965, 796, 746, 1205, 755, 700, 646, 1086, 527, 345, 888, 961, 694, 963, 884, 1200, 410, 835, 1002, 643, 856, 390, 916, 789, 869, 907, 619, 916, 860, 645, 577, 878, 834, 946, 1016, 789, 959, 829, 549, 708, 757, 389, 837, 805, 719, 930, 938, 822, 562, 655, 632, 885, 601, 774, 507, 926, 746, 836, 841, 723, 845, 828, 820, 945, 867, 643, 797, 715, 927, 828, 470, 699, 623, 1048, 580, 671, 712, 963, 855, 695, 596, 625, 643, 819, 821, 473, 770, 447, 687, 775, 834, 912, 399, 450, 703, 1124, 616, 661, 477, 683, 942, 747, 359, 942, 750, 989, 525, 582, 596, 718, 926, 495, 929, 941, 722, 810, 775, 735, 516, 516, 981, 826, 671, 503, 516, 656, 798, 710, 837, 647, 399, 880, 612, 894, 927, 617, 769, 835, 611, 505, 927, 776, 798, 588, 687, 368, 668, 836, 473, 505, 531, 452, 573, 402, 522, 681, 571, 538, 727, 664, 701, 661, 821, 882, 681, 434, 899, 620, 251, 752, 711, 830, 554, 678, 1067, 830, 718, 598, 519, 615, 726, 597, 572, 521, 494, 904, 555, 735, 701, 818, 753, 755, 769, 684, 427, 494, 714, 553, 656, 741, 619, 781, 666, 547, 776, 625, 415, 612, 610, 718, 466, 638, 336, 703, 623, 513, 725, 508, 876, 580, 681, 647, 653, 483, 869, 708, 805, 432, 655, 431, 577, 805, 667, 451, 691, 492, 455, 573, 370, 510, 645, 581, 715, 700, 330, 346, 467, 491, 470, 795, 641, 795, 732, 184, 611, 427, 683, 580, 552, 706, 417, 392, 522, 715, 478, 705, 580, 388, 379, 278, 388, 496, 866, 641, 516, 778, 508, 705, 475, 543, 466, 608, 548, 222, 605, 691, 393]
items_requirements = [
[88, 520, 258, 337, 301, 654, 252, 220, 118, 210, 637, 97, 349, 202, 508, 438, 36, 147, 41, 635, 265, 36, 485, 325, 149, 967, 817, 188, 106, 192, 139, 37, 579, 248, 78, 897, 695, 362, 209, 518, 864, 52, 67, 629, 81, 464, 2, 368, 133, 414, 145, 1, 201, 948, 344, 254, 179, 379, 71, 722, 243, 164, 345, 344, 700, 908, 981, 640, 24, 777, 46, 335, 280, 763, 599, 591, 457, 559, 653, 375, 184, 182, 71, 162, 85, 913, 3, 412, 683, 911, 456, 470, 381, 927, 243, 100, 119, 593, 795, 447, 373, 221, 32, 527, 694, 534, 699, 701, 880, 338, 372, 319, 194, 809, 527, 819, 481, 567, 25, 502, 276, 62, 782, 751, 697, 603, 496, 694, 39, 554, 86, 853, 618, 434, 853, 282, 471, 165, 552, 277, 617, 918, 890, 811, 217, 288, 459, 362, 18, 442, 787, 126, 704, 831, 607, 553, 364, 685, 662, 171, 469, 189, 546, 904, 154, 860, 887, 325, 551, 101, 930, 269, 570, 764, 160, 917, 633, 364, 653, 793, 225, 841, 377, 909, 776, 704, 6, 173, 791, 368, 718, 606, 447, 28, 613, 464, 993, 605, 389, 890, 852, 883, 96, 531, 171, 90, 299, 935, 7, 10, 323, 835, 934, 625, 49, 678, 360, 881, 554, 598, 827, 552, 96, 307, 537, 253, 421, 278, 448, 142, 969, 515, 279, 771, 24, 931, 758, 598, 998, 397, 262, 469, 542, 461, 810, 887, 258, 184, 618, 10, 545, 426, 104, 197, 486, 906, 645, 440, 761, 961, 636, 113, 959, 824, 998, 64, 493, 114, 605, 144, 542, 612, 389, 569, 691, 956, 793, 328, 573, 511, 901, 174, 301, 530, 20, 581, 900, 220, 259, 375, 604, 767, 479, 527, 260, 723, 903, 605, 170, 335, 541, 622, 631, 892, 543, 351, 287, 42, 765, 363, 990, 332, 195, 840, 118, 118, 672, 580, 905, 605, 503, 352, 665, 485, 373, 427, 948, 119, 227, 917, 927, 393, 653, 855, 653, 21, 568, 656, 192, 624, 967, 811, 589, 478, 741, 466, 971, 543, 897, 568, 189, 417, 784, 714, 861, 292, 469, 300, 777, 497, 350, 183, 322, 618, 353, 185, 51, 688, 779, 197, 431, 22, 598, 748, 943, 470, 969, 667, 517, 561, 329, 214, 44, 835, 426, 721, 476, 762, 1000, 16, 854, 267, 960, 821, 886, 922, 669, 637, 819, 426, 205, 828, 991, 791, 859, 514, 880, 351, 595, 680, 602, 725, 768, 356, 533, 854, 439, 864, 297, 788, 144, 878, 576, 371, 153, 112, 371, 582, 199, 754, 406, 511, 781, 34, 812, 786, 39, 648, 334, 676, 373, 404, 164, 894, 262, 583, 141, 830, 491, 86, 182, 495, 120, 212, 474, 820, 898, 230, 366, 503, 42, 436, 945, 579, 373, 707, 37, 153, 907, 999, 304, 546, 909, 101, 848, 139, 369, 419, 667, 393, 284, 120, 266, 765, 743, 981, 173, 724, 937, 734, 87, 135, 309, 394, 814, 704, 98, 148, 693, 650] ,
[169, 232, 220, 348, 400, 48, 501, 876, 983, 652, 686, 71, 172, 42, 55, 157, 418, 549, 649, 303, 122, 656, 81, 45, 834, 543, 90, 117, 67, 836, 163, 442, 16, 415, 205, 321, 126, 454, 289, 206, 714, 638, 664, 567, 541, 245, 600, 567, 713, 713, 429, 368, 540, 739, 633, 381, 639, 519, 132, 397, 946, 32, 355, 38, 78, 131, 406, 245, 153, 250, 461, 352, 690, 308, 507, 259, 55, 333, 48, 263, 335, 717, 396, 871, 812, 792, 272, 558, 209, 573, 976, 158, 415, 889, 610, 698, 610, 496, 260, 612, 585, 37, 725, 662, 416, 490, 241, 233, 63, 359, 765, 459, 917, 820, 670, 35, 492, 499, 68, 841, 993, 922, 191, 87, 296, 453, 830, 402, 163, 155, 552, 381, 194, 188, 488, 41, 522, 286, 238, 856, 385, 49, 867, 653, 953, 589, 655, 423, 303, 955, 912, 584, 839, 276, 217, 210, 751, 140, 19, 835, 346, 674, 185, 162, 959, 867, 213, 605, 412, 831, 8, 343, 188, 234, 888, 53, 31, 346, 575, 459, 663, 850, 723, 207, 105, 839, 456, 973, 652, 867, 973, 860, 409, 771, 591, 969, 302, 188, 45, 834, 432, 18, 771, 333, 927, 91, 676, 822, 439, 277, 588, 458, 876, 863, 786, 519, 914, 70, 438, 366, 996, 461, 211, 711, 16, 876, 975, 576, 562, 56, 604, 995, 105, 591, 385, 471, 740, 752, 547, 39, 538, 764, 411, 405, 458, 299, 720, 726, 850, 968, 245, 730, 599, 427, 45, 980, 441, 522, 868, 702, 193, 216, 100, 114, 396, 179, 896, 114, 333, 279, 759, 531, 588, 802, 584, 320, 713, 735, 308, 887, 364, 382, 371, 222, 492, 158, 837, 17, 477, 645, 859, 723, 511, 154, 118, 304, 767, 837, 601, 432, 94, 302, 712, 216, 595, 178, 356, 830, 774, 211, 294, 200, 477, 931, 993, 46, 869, 156, 380, 146, 160, 345, 232, 393, 565, 888, 385, 849, 746, 751, 384, 253, 107, 569, 533, 612, 227, 970, 516, 444, 359, 563, 756, 448, 244, 280, 932, 872, 499, 498, 935, 214, 97, 303, 92, 676, 820, 783, 258, 315, 972, 446, 192, 333, 97, 398, 294, 37, 822, 523, 527, 967, 307, 487, 495, 547, 115, 898, 498, 848, 655, 26, 981, 374, 935, 401, 301, 896, 666, 614, 52, 659, 98, 594, 987, 614, 305, 369, 608, 596, 767, 735, 993, 373, 354, 753, 356, 76, 493, 983, 84, 591, 888, 583, 757, 52, 951, 300, 535, 28, 647, 863, 121, 474, 555, 427, 875, 265, 468, 861, 258, 598, 370, 892, 444, 649, 373, 851, 606, 885, 168, 673, 864, 220, 858, 665, 39, 894, 215, 286, 729, 260, 940, 683, 709, 876, 830, 191, 367, 124, 788, 67, 661, 864, 749, 909, 84, 807, 330, 202, 796, 180, 856, 597, 223, 915, 996, 245, 947, 763, 606, 733, 369, 195, 894, 825, 935, 173, 801, 404, 902, 636, 413, 728, 841, 332, 276, 656, 836, 99] ,
[296, 227, 335, 54, 45, 69, 216, 9, 579, 210, 164, 499, 24, 958, 611, 303, 420, 695, 276, 108, 978, 53, 260, 571, 81, 330, 101, 277, 104, 491, 778, 450, 688, 120, 99, 67, 273, 50, 771, 227, 94, 82, 96, 114, 416, 202, 143, 211, 995, 91, 198, 645, 276, 314, 511, 485, 11, 391, 297, 587, 543, 736, 627, 456, 112, 781, 119, 255, 622, 583, 456, 247, 74, 386, 675, 355, 918, 395, 7, 620, 964, 440, 116, 183, 9, 53, 700, 374, 870, 107, 462, 628, 845, 635, 856, 617, 931, 12, 99, 755, 526, 635, 690, 281, 131, 705, 753, 250, 28, 505, 595, 174, 983, 185, 728, 564, 779, 495, 676, 278, 103, 606, 713, 90, 129, 138, 598, 477, 94, 451, 997, 23, 338, 575, 424, 796, 167, 167, 753, 347, 967, 18, 50, 243, 672, 51, 142, 615, 744, 331, 496, 759, 274, 69, 964, 204, 681, 803, 113, 997, 389, 565, 663, 66, 642, 669, 765, 700, 391, 210, 997, 183, 489, 444, 963, 85, 603, 766, 382, 563, 945, 328, 282, 427, 99, 999, 949, 135, 110, 647, 402, 403, 427, 504, 462, 703, 596, 839, 463, 510, 36, 978, 332, 46, 105, 488, 260, 958, 758, 304, 190, 498, 431, 124, 516, 406, 879, 426, 138, 214, 816, 19, 240, 403, 649, 175, 743, 882, 938, 202, 892, 577, 233, 685, 91, 747, 60, 82, 550, 910, 897, 913, 181, 163, 948, 480, 618, 978, 507, 996, 540, 232, 74, 953, 437, 370, 284, 561, 123, 916, 321, 541, 136, 770, 444, 310, 212, 392, 528, 909, 302, 712, 14, 370, 994, 693, 278, 793, 833, 144, 566, 931, 433, 280, 145, 558, 368, 294, 520, 940, 219, 14, 350, 295, 888, 867, 271, 565, 120, 858, 406, 261, 915, 493, 912, 27, 225, 58, 944, 579, 625, 551, 916, 539, 735, 286, 947, 802, 895, 271, 99, 874, 67, 613, 124, 767, 759, 392, 490, 19, 343, 256, 855, 453, 320, 887, 528, 153, 492, 753, 452, 133, 143, 169, 760, 83, 492, 493, 360, 738, 821, 557, 111, 839, 608, 818, 119, 841, 227, 947, 538, 505, 588, 682, 555, 762, 381, 422, 246, 909, 36, 420, 78, 647, 297, 654, 895, 105, 268, 895, 774, 270, 494, 997, 518, 486, 228, 976, 582, 625, 19, 195, 1, 586, 59, 239, 577, 502, 510, 379, 781, 558, 873, 960, 937, 746, 302, 17, 580, 845, 647, 411, 743, 897, 546, 593, 85, 867, 265, 228, 305, 7, 599, 941, 549, 376, 711, 505, 893, 689, 767, 830, 453, 368, 593, 730, 543, 611, 755, 638, 172, 567, 22, 594, 961, 266, 872, 53, 366, 551, 315, 27, 426, 561, 716, 486, 638, 372, 369, 619, 287, 449, 874, 102, 834, 550, 411, 553, 150, 796, 978, 206, 493, 657, 447, 933, 995, 160, 266, 989, 82, 459, 82, 334, 534, 802, 247, 462, 180, 606, 850, 423, 754, 408, 723, 531, 38, 618, 654, 94] ,
[234, 59, 506, 46, 361, 231, 158, 567, 11, 326, 123, 193, 749, 343, 440, 552, 178, 217, 93, 234, 455, 513, 218, 916, 81, 9, 264, 879, 287, 147, 238, 780, 516, 681, 54, 20, 151, 921, 286, 89, 50, 389, 874, 496, 453, 209, 493, 880, 247, 312, 85, 817, 776, 222, 607, 331, 834, 384, 620, 496, 458, 112, 785, 146, 273, 292, 286, 766, 65, 466, 505, 480, 454, 111, 319, 990, 410, 575, 636, 393, 404, 937, 386, 913, 759, 873, 500, 315, 349, 979, 256, 355, 205, 22, 187, 181, 392, 274, 492, 277, 945, 348, 175, 197, 734, 281, 598, 146, 636, 228, 299, 754, 194, 106, 971, 402, 694, 74, 166, 920, 638, 400, 661, 797, 392, 32, 919, 363, 935, 301, 480, 995, 355, 570, 760, 193, 833, 611, 89, 794, 228, 774, 143, 565, 870, 361, 990, 250, 696, 331, 472, 747, 100, 650, 914, 956, 715, 196, 746, 532, 741, 4, 720, 920, 576, 666, 918, 752, 513, 140, 202, 728, 834, 370, 379, 487, 185, 336, 475, 426, 937, 240, 403, 462, 413, 501, 69, 904, 188, 263, 311, 966, 722, 760, 920, 808, 195, 57, 355, 193, 987, 723, 346, 716, 968, 343, 164, 95, 426, 907, 747, 240, 922, 412, 432, 161, 882, 139, 462, 240, 447, 119, 56, 988, 994, 558, 672, 876, 897, 89, 127, 708, 903, 334, 332, 481, 566, 695, 184, 391, 891, 169, 414, 518, 94, 820, 552, 395, 64, 671, 673, 72, 700, 679, 165, 416, 653, 450, 492, 485, 633, 587, 50, 258, 355, 679, 578, 423, 927, 614, 546, 862, 658, 984, 322, 564, 599, 745, 24, 571, 579, 955, 728, 50, 763, 79, 940, 838, 603, 480, 654, 540, 665, 799, 10, 283, 210, 77, 432, 496, 37, 721, 454, 986, 318, 632, 342, 811, 873, 423, 287, 506, 806, 432, 413, 398, 504, 900, 765, 638, 795, 250, 786, 880, 84, 823, 949, 976, 643, 775, 395, 66, 179, 994, 607, 504, 167, 100, 695, 800, 742, 943, 13, 350, 974, 471, 579, 795, 547, 601, 514, 453, 233, 1000, 838, 693, 113, 105, 65, 66, 393, 153, 808, 288, 294, 93, 820, 679, 255, 290, 412, 938, 917, 312, 762, 561, 533, 332, 280, 819, 90, 35, 472, 132, 977, 54, 966, 998, 98, 811, 939, 127, 809, 388, 360, 493, 106, 470, 793, 479, 385, 67, 394, 841, 415, 601, 869, 343, 372, 302, 224, 191, 340, 215, 909, 685, 113, 392, 795, 550, 818, 458, 947, 134, 666, 9, 138, 838, 359, 768, 274, 972, 706, 951, 312, 82, 805, 841, 470, 854, 864, 800, 648, 363, 724, 530, 307, 774, 916, 913, 938, 156, 329, 878, 517, 911, 675, 264, 479, 190, 441, 459, 381, 714, 974, 443, 247, 486, 488, 863, 502, 975, 116, 217, 303, 472, 120, 719, 956, 576, 234, 328, 23, 208, 171, 803, 868, 703, 940, 694, 814, 295, 912, 557, 410, 903, 355, 700, 631, 772] ,
[361, 175, 30, 311, 213, 379, 93, 3, 20, 339, 191, 374, 217, 200, 127, 329, 231, 244, 525, 675, 33, 650, 408, 184, 454, 53, 725, 17, 351, 209, 552, 316, 205, 677, 416, 374, 199, 411, 639, 942, 153, 829, 487, 349, 504, 833, 530, 281, 2, 192, 124, 459, 355, 2, 205, 838, 309, 156, 736, 354, 274, 401, 164, 793, 236, 492, 651, 482, 638, 125, 358, 397, 627, 709, 265, 342, 832, 437, 984, 424, 555, 270, 909, 514, 950, 115, 98, 506, 385, 256, 238, 846, 219, 368, 23, 964, 616, 123, 127, 360, 437, 514, 497, 838, 597, 153, 438, 157, 244, 736, 883, 407, 344, 656, 112, 551, 580, 917, 734, 150, 98, 79, 745, 394, 46, 933, 113, 850, 700, 18, 895, 65, 760, 443, 540, 210, 278, 831, 377, 838, 598, 980, 460, 703, 144, 746, 412, 343, 31, 371, 476, 539, 206, 352, 413, 755, 116, 853, 548, 325, 766, 899, 297, 913, 312, 102, 508, 994, 733, 699, 569, 913, 691, 435, 899, 884, 216, 578, 928, 246, 800, 677, 342, 366, 545, 578, 808, 349, 413, 865, 102, 415, 100, 792, 895, 753, 296, 798, 117, 538, 917, 554, 831, 544, 668, 838, 420, 840, 527, 756, 148, 582, 967, 987, 710, 573, 741, 850, 606, 611, 330, 510, 485, 400, 844, 335, 239, 189, 958, 811, 60, 390, 526, 347, 412, 293, 398, 655, 625, 252, 357, 450, 527, 310, 516, 200, 899, 991, 505, 453, 677, 317, 815, 198, 131, 57, 602, 375, 803, 11, 920, 396, 922, 126, 742, 765, 397, 649, 700, 547, 648, 115, 787, 127, 209, 247, 826, 348, 450, 601, 28, 722, 997, 526, 974, 761, 558, 626, 450, 13, 986, 911, 401, 290, 890, 57, 713, 788, 340, 593, 504, 526, 34, 369, 865, 227, 387, 756, 637, 618, 167, 120, 55, 636, 422, 442, 401, 266, 624, 238, 548, 336, 849, 988, 654, 475, 401, 313, 866, 384, 657, 932, 113, 759, 945, 461, 373, 37, 541, 344, 119, 671, 912, 46, 574, 1000, 392, 790, 26, 500, 697, 669, 688, 660, 546, 560, 720, 592, 77, 726, 950, 527, 29, 120, 440, 773, 6, 205, 548, 304, 692, 492, 695, 549, 94, 988, 958, 682, 148, 423, 607, 450, 991, 488, 449, 545, 737, 630, 975, 807, 539, 845, 614, 542, 119, 49, 463, 33, 964, 390, 870, 683, 106, 132, 564, 587, 443, 1000, 32, 193, 770, 850, 393, 567, 577, 649, 745, 889, 794, 192, 723, 433, 868, 113, 872, 552, 994, 548, 336, 123, 534, 952, 255, 771, 706, 647, 382, 908, 980, 532, 348, 477, 226, 506, 809, 963, 675, 576, 240, 225, 437, 751, 517, 619, 247, 185, 173, 463, 17, 721, 710, 766, 828, 733, 787, 814, 85, 885, 148, 391, 181, 725, 996, 421, 55, 48, 958, 756, 557, 71, 667, 190, 603, 373, 57, 780, 892, 448, 936, 49, 802, 840, 287, 214, 223, 259, 341, 898, 638, 352] ,
]
capacities = [61202, 61807, 58959, 62375, 62163]

# Core Concept Guide
# For this example, let's assume that the Core set contains the first two items from the sorted list
# of items based on their efficiency scores (X1: items with the highest efficiency, Core: items with medium efficiency)

# Calculate lengths for each category
total_length = len(values)
x1_length = int(total_length * 0.1)  # 10% of the total length
core_length = int(total_length * 0.8)  # 80% of the total length
x0_length = total_length - x1_length - core_length  # Remaining length

# Separate data into categories
X1_values = values[:x1_length]
X1_items_requirements = [item[:x1_length] for item in items_requirements]

Core_values = values[x1_length:x1_length + core_length]
Core_items_requirements = [item[x1_length:x1_length + core_length] for item in items_requirements]

X0_values = values[x1_length + core_length:]
X0_items_requirements = [item[x1_length + core_length:] for item in items_requirements]

# Display the separated data
print("X1 Data:")
print("Values:", X1_values)
print("Items Requirements:", X1_items_requirements)

print("\nCore Data:")
print("Values:", Core_values)
print("Items Requirements:", Core_items_requirements)

print("\nX0 Data:")
print("Values:", X0_values)
print("Items Requirements:", X0_items_requirements)

# Calculate fitness for X1 items
X1_Gaines = sum(X1_values)
print("\nX1 Total Values:", X1_Gaines)
# Calculate remaining capacities after selecting items from Core
remaining_capacities_X1 = [capacity - sum(constraint[i] for i, is_picked in enumerate([True] * len(X1_values)) if is_picked) for capacity, constraint in zip(capacities, X1_items_requirements)]
print("Remaining Capacities after putting X1 items:", remaining_capacities_X1)


import heapq

# Generate a random boolean vector that we consider it as an individual from the population that the Genetic Algorithm has generated
#individual = [random.choice([True, False]) for _ in range(len(Core_values))]
individual = [True, True, True, True, False, False, False, False, False, True, False, True, True, False, True, False, True, False, False, True, True, False, False, True, False, False, False, False, True, True, False, True, False, False, False, False, False, False, False, True, False, False, True, False, True, False, False, False, True, False, False, True, False, False, True, False, False, False, False, False, False, False, False, True, True, True, False, True, True, False, True, False, False, False, True, True, True, False, False, True, True, False, False, False, False, True, True, False, False, False, False, True, True, True, True, False, False, False, True, False, True, False, True, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, True, False, True, False, True, False, False, False, False, True, False, True, True, False, False, False, False, True, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, True, False, True, True, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, True, True, True, False, False, False, False, False, True, False, True, False, True, False, False, False, True, True, False, False, False, False, False, True, True, False, False, False, False, True, False, False, False, False, False, False, False, False, True, False, False, False, True, False, True, False, False, True, False, True, False, False, True, False, False, True, True, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, True, True, True, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, True, False, False, False, False, True, False, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True]
print(individual)

class Node:
    def __init__(self):
        self.ub = 0  # Upper bound
        self.lb = 0  # Lower bound
        self.level = 0  # Level in the decision tree
        self.flag = False  # Flag to indicate if the item is selected or not
        self.tv = 0  # Total value of selected items
        self.tw = []  # Total weight of selected items for each dimension


def assign(a, ub, lb, level, flag, tv, tw):
    # Helper function to assign values to a Node object
    a.ub = ub
    a.lb = lb
    a.level = level
    a.flag = flag
    a.tv = tv
    a.tw = tw


# Core_values Core_items_requirements remaining_capacities_X1
def upper_bound(tv, tw, idx, Core_values, Core_items_requirements, remaining_capacities_X1):
    # Calculate the upper bound of the current node
    value, requirement = tv, tw[:]
    for i in range(idx, len(Core_values)):
        feasible = True
        for j in range(len(remaining_capacities_X1)):
            if requirement[j] + Core_items_requirements[j][i] > remaining_capacities_X1[j]:
                feasible = False
                break
            requirement[j] += Core_items_requirements[j][i]
        if feasible:
            value -= Core_values[i]
        else:
            value -= sum((remaining_capacities_X1[k] - requirement[k]) / Core_items_requirements[k][i] * Core_values[i]
                         for k in range(j + 1))
            break
    return value


# Core_values Core_items_requirements remaining_capacities_X1
def lower_bound(tv, tw, idx, Core_values, Core_items_requirements, remaining_capacities_X1):
    # Calculate the lower bound of the current node
    value, requirement = tv, tw[:]
    for i in range(idx, len(Core_values)):
        feasible = True
        for j in range(len(remaining_capacities_X1)):
            if requirement[j] + Core_items_requirements[j][i] > remaining_capacities_X1[j]:
                feasible = False
                break
            requirement[j] += Core_items_requirements[j][i]
        if feasible:
            value -= Core_values[i]
            for j in range(len(remaining_capacities_X1)):
                requirement[j] += Core_items_requirements[j][i]
        else:
            break
    return value


# Main function to solve the Multidimensional Knapsack problem using Branch and Bound
# Core_values Core_items_requirements remaining_capacities_X1
def knapsack_solver(Core_values, Core_items_requirements, remaining_capacities_X1, start_index, end_index):

    # Initialize the root node
    current = Node()
    current.tv = current.ub = current.lb = 0
    current.level = 0
    current.flag = False
    current.tw = [0] * len(remaining_capacities_X1)

    # Initialize variables to track the best solution
    min_lb = 0
    final_lb = float('inf')

    # Lists to track the current and final selected items
    curr_path = [False] * len(Core_values)
    final_path = [False] * len(Core_values)

    # Priority queue for node exploration
    pq = []
    heapq.heappush(pq, (current.lb, id(current), current))

    while pq:
        _, _, current = heapq.heappop(pq)

        # Prune the node if its upper bound is greater than the current minimum lower bound
        if current.ub > min_lb or current.ub >= final_lb:
            continue

        if current.level != 0:
            curr_path[current.level - 1] = current.flag

        # Check if the current node is a leaf node
        if current.level == len(Core_values):
            # Update the final solution if the current lower bound is better
            if current.lb < final_lb:
                final_path = curr_path[:]
                final_lb = current.lb
            continue

        level = current.level

        # Explore right child (item is not included in the knapsack)
        right = Node()
        right.ub = upper_bound(current.tv, current.tw, level + 1, Core_values, Core_items_requirements,
                                remaining_capacities_X1)
        right.lb = lower_bound(current.tv, current.tw, level + 1, Core_values, Core_items_requirements,
                                remaining_capacities_X1)
        assign(right, right.ub, right.lb, level + 1, False, current.tv, current.tw)

        # Explore left child (item is included in the knapsack)
        left = Node()
        feasible = True
        for j in range(len(remaining_capacities_X1)):
            if current.tw[j] + Core_items_requirements[j][level] > remaining_capacities_X1[j]:
                feasible = False
                break
        if feasible:
            left.ub = upper_bound(
                current.tv - Core_values[level],
                [current.tw[k] + Core_items_requirements[k][level] for k in range(len(remaining_capacities_X1))],
                level + 1,
                Core_values,
                Core_items_requirements,
                remaining_capacities_X1
            )
            left.lb = lower_bound(
                current.tv - Core_values[level],
                [current.tw[k] + Core_items_requirements[k][level] for k in range(len(remaining_capacities_X1))],
                level + 1,
                Core_values,
                Core_items_requirements,
                remaining_capacities_X1
            )
            assign(
                left,
                left.ub,
                left.lb,
                level + 1,
                True,
                current.tv - Core_values[level],
                [current.tw[k] + Core_items_requirements[k][level] for k in range(len(remaining_capacities_X1))]
            )
        else:
            # If adding the current item exceeds the capacity, set bounds to 1
            left.ub = 1
            left.lb = 1

        min_lb = min(min_lb, left.lb, right.lb)

        # Add valid children to the priority queue for further exploration
        if min_lb >= left.ub:
            heapq.heappush(pq, (left.lb, id(left), left))
        if min_lb >= right.ub:
            heapq.heappush(pq, (right.lb, id(right), right))

    # Return the selected items and maximum profit
    selected_items = []
    for i in range(len(Core_values)):
        if final_path[i]:
            selected_items.append(1)
        else:
            selected_items.append(0)
    max_profit = -final_lb
    selected_items_boolean = [bool(x) for x in selected_items]

    print("Updated Selected Part:", selected_items_boolean)

    updated_individual = individual
    individual[start_index:end_index] = selected_items_boolean

    return updated_individual, max_profit


def calculate_remaining_capacities(individual, Core_items_requirements, remaining_capacities_X1):
    remaining_capacities = [remaining_capacities_X1[i] for i in range(len(remaining_capacities_X1))]
    total_capacities = [0] * len(remaining_capacities_X1)
    start_index = 80
    end_index = 102
    for i, item_selected in enumerate(individual):
        if i < start_index or i >= end_index:
            for j in range(len(remaining_capacities_X1)):
                total_capacities[j] += Core_items_requirements[j][i] * item_selected * int(individual[i])

    for j in range(len(remaining_capacities_X1)):
        remaining_capacities[j] -= total_capacities[j]

    print("Remaining capacities:", remaining_capacities)
    print("Start Index:", start_index, "/ End Index:", end_index)
    print("Selected Part:", individual[start_index:end_index])

    Selected_Part_binary = [int(x) for x in individual[start_index:end_index]]
    print("Selected Part Binary:", Selected_Part_binary)
    Selected_Part_value = 0

    # Use the length of Selected_Part_binary for the loop, which matches the length of Core_values[start_index:end_index]
    for i in range(len(Selected_Part_binary)):
        Selected_Part_value += Selected_Part_binary[i] * Core_values[i + start_index]

    print("The value of the selected part:", Selected_Part_value)

    print("Capacities occupied by items outside the selected part", total_capacities)
    print("Remaining capacities out of selected part:", remaining_capacities)

    # Separate data into categories
    Selected_Part_values = Core_values[start_index:end_index]
    Selected_Part_requirements = [item[start_index:end_index] for item in Core_items_requirements]

    return remaining_capacities, Selected_Part_values, Selected_Part_requirements, start_index, end_index


# Main function
def main():

    remaining_capacities, Selected_Part_Values, Selected_Part_requirements, start_index, end_index = calculate_remaining_capacities(individual, Core_items_requirements, remaining_capacities_X1)
    selected_items, max_profit = knapsack_solver(Selected_Part_Values, Selected_Part_requirements, remaining_capacities, start_index, end_index)
    print("Selected items:", selected_items)
    print("Maximum profit is:", max_profit)
    # Calculate remaining capacity for each dimension
    print("Remaining capacity for each dimension:", remaining_capacities)


if __name__ == "__main__":
    main()
