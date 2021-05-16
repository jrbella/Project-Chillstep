# imports
import matplotlib.pyplot as plt

# Types of rehabilitation
raw_data = ["back", "back", "hand", "neck", "knee", "knee",
            "wrist", "back", "groin", "shoulder", "shoulder",
            "back", "elbow", "back", "back", "back", "back", "back",
            "back", "shoulder", "shoulder", "knee", "knee", "back",
            "hip", "knee", "hip", "hand", "back", "wrist"]


back = raw_data.count("back")
elbow = raw_data.count("elbow")
hand = raw_data.count("hand")
neck = raw_data.count("neck")
knee = raw_data.count("knee")
hip = raw_data.count("hip")
wrist = raw_data.count("wrist")
groin = raw_data.count("groin")
shoulder = raw_data.count("shoulder")

frequency_of_data = [back, elbow, hand, neck, knee, hip, wrist, groin, shoulder]

print(str(frequency_of_data))

sum_of_frequency = sum(frequency_of_data)

print("The sum of the data is : " + str(sum_of_frequency))

def relative_frequency(sum_frequency, sample):
    result = sample/sum_frequency
    print("The relative freq is : " + str(result))
    return result

back_relative_frequency = relative_frequency(sum_of_frequency, back)
elbow_relative_frequency = relative_frequency(sum_of_frequency, elbow)
hand_relative_frequency = relative_frequency(sum_of_frequency, hand)
neck_relative_frequency = relative_frequency(sum_of_frequency, neck)
knee_relative_frequency = relative_frequency(sum_of_frequency, knee)
hip_relative_frequency = relative_frequency(sum_of_frequency, hip)
wrist_relative_frequency = relative_frequency(sum_of_frequency, wrist)
groin_relative_frequency = relative_frequency(sum_of_frequency, groin)
shoulder_relative_frequency = relative_frequency(sum_of_frequency, shoulder)



data_sample = {}


def construct_type_data(type_of_rehab, frequency, relative_frequency, dict_to_add):
    #construct the strings for the dictionary 
    freq_construct = type_of_rehab + "_frequency"
    rel_freq_constrcut = type_of_rehab + "_relative_frequency"

    temp_dict = {
        freq_construct : frequency, 
        rel_freq_constrcut : relative_frequency        
    }

    # append to target dictionary
    print("Adding " + type_of_rehab + " to dictionary")
    dict_to_add[type_of_rehab] = temp_dict


# Building the dictionary
construct_type_data("back", back, back_relative_frequency, data_sample)
construct_type_data("elbow", elbow, elbow_relative_frequency, data_sample)
construct_type_data("hand", hand, hand_relative_frequency, data_sample)
construct_type_data("neck", neck, neck_relative_frequency, data_sample)
construct_type_data("knee", knee, knee_relative_frequency, data_sample)
construct_type_data("hip", hip, hip_relative_frequency, data_sample)
construct_type_data("wrist", wrist, wrist_relative_frequency, data_sample)
construct_type_data("groin", groin, groin_relative_frequency, data_sample)
construct_type_data("shoulder", shoulder, shoulder_relative_frequency, data_sample)


print(data_sample)

# Creating the bar graphs

therapy_types = ['back', "elbow", "hand", "neck", "knee", "hip", "wrist", "groin", "shoulder"]
frequency_of_types = [back, elbow, hand, neck, knee, hip, wrist, groin, shoulder]
relative_frequency_of_types = [
    back_relative_frequency,
    elbow_relative_frequency,
    hand_relative_frequency,
    neck_relative_frequency,
    knee_relative_frequency,
    hip_relative_frequency,
    wrist_relative_frequency,
    groin_relative_frequency,
    shoulder_relative_frequency
]


# quick bar graph function

def show_bar_graph(x_plot, y_plot):
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    ax.bar(x_plot, y_plot)
    plt.show()

# create bar graph for relative frequency
show_bar_graph(therapy_types, relative_frequency_of_types)
show_bar_graph(therapy_types, frequency_of_types)