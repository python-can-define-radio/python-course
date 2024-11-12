#!/bin/bash

set -e

echo "- Setting screen blank timeout, lock timeout, bash terminal timeout, bash prompt, and nautilus executable"
gsettings set org.gnome.desktop.session idle-delay 900
gsettings set org.gnome.desktop.screensaver lock-delay 1800
gsettings set org.gnome.nautilus.preferences executable-text-activation 'ask'
echo "

## Make TMOUT variable arbitrarily large to avoid terminal auto-closing
export TMOUT=30000" >> ~/.bashrc

# echo "## Modify prompt to put $ on the next line " >> ~/.bashrc
# echo PS1=\'\${debian_chroot:+(\$debian_chroot)}\\\[\\033\[01\;32m\\\]\\u@\\h\\\[\\033\[00m\\\]:\\\[\\033\[01\;34m\\\]\\w\\\[\\033\[00m\\\]\\n\\\$ \' >> ~/.bashrc

echo "- Disabling middle click to avoid accidental pasting"
# this works for a single session only (non-persistent).
xmodmap -e "pointer = 1 25 3 4 5 6 7 8 9 10"

# the next part will disable middle-click on login (persistently).
## create a script that runs the command that we saw above
scriptFile=Desktop/disable_middle_click.sh
echo 'xmodmap -e "pointer = 1 25 3 4 5 6 7 8 9 10"' > ~/$scriptFile
## Mark the script as executable
chmod 770 ~/$scriptFile
## Make autostart directory
mkdir -p ~/.config/autostart
## Create a .desktop file which Ubuntu/GNOME auto-loads on login
echo "[Desktop Entry]
Type=Application
Name=run_disable_middle_click_script
X-GNOME-Autostart-enabled=true
Exec=$HOME/$scriptFile
" > ~/.config/autostart/disable_middle_click.desktop


if ! [ -d ~/.config/Code/User ]; then
    echo "ERROR: You need to launch VS Code before running this script."
    exit
fi

echo "- Customizing VS Code default setttings"
echo "{
    \"window.zoomLevel\": 1,
    \"editor.tokenColorCustomizations\":
      {  \"[*]\": 
          {\"textMateRules\":
            [   {   \"name\": \"Docstrings\",
                    \"scope\": \"string.quoted.docstring\",
                    \"settings\":
                    {    \"foreground\": \"#CE9178\"
                    }
                }
            ]
          }
      },
}" > ~/.config/Code/User/settings.json

echo "- Running command to install commonly used packages: pip3 install thonny rich guizero pyautogui asciimatics prompt_toolkit termcolor"
pip3 install thonny rich guizero pyautogui asciimatics prompt_toolkit termcolor

echo "- Creating example content in ~/Desktop/term_example_files"

cd ~/Desktop

echo "Feel free to take notes in this file if you'd like." > mod_f_notes.txt

mkdir -p term_example_files
cd term_example_files

echo "A kangaroo is an animal that can jump." > kangaroo.txt

echo "Facts about the Ford Mustang include:
The Mustang was Ford’s first model to be designed with ‘floating bumpers’.
The Ford Mustang quickly became available to buy with an automatic three speed gearbox, or with two manual options of either three or five speed gearboxes.
The Ford Mustang weighs 1109 kg or 2445 lbs. on average.
The Ford Mustang is a series of American automobiles manufactured by Ford.
The Mustang is currently the longest-produced Ford car nameplate.
Currently in its sixth generation, it is the fifth-best selling Ford car nameplate..
(Source: Bing search)" > Mustang.txt

echo "Facts and information about Mustang horses include:
Mustangs are small, swift, surefooted, and hardy.
They range from an average size of 14″2 – 15″2 hands and 1,000 lbs or more in weight.
They come in a variety of colors ranging from reddish-brown, bay, sorrel, brown or black in color.
Mustangs have a life span of about 25 – 30 years.
Mustangs average about 56 inches at the shoulder and weigh between 700 and 900 pounds.
There are approximately 50,000 wild mustangs.
There is a controversy over whether they are feral or truly wild.
Mustangs can run up to 35 miles an hour.
(Source: Bing search)" > mustang.txt

mkdir -p animals
cd animals

echo "Pets (dogs, cats, ferrets, hamsters, etc.)
Livestock (cattle, sheep, pigs, goats, etc.)
Beasts of burden (horses, camels, donkeys, etc.)
(Source: Bing search)" > domestic_animals.txt

echo "A monkey is a primate with a tail." > monkey.txt
echo "A dog is one of the most common domestic animals in the world." > dog.txt
echo "A cactus is a plant that grows in the desert." > cactus.txt

cd ..
mkdir -p plants
cd plants

echo "Plants are a major food group for most living organisms.
Facts about  food plants include:
There are about 380,000 known species of plants, of which the majority, some 260,000, produce seeds.
Green plants provide a substantial proportion of the world's molecular oxygen and are the basis of most of Earth's ecosystems.
Grain, fruit, and vegetables are basic human foods and have been domesticated for millennia.
Oats and soy are some of the most popular ingredients used in plant-based products.
US retail sales of plant-based foods grew by 6.2% in 2021.
Plant-based milk is the most developed of all alt protein categories.
The global plant-based foods industry could make up to 7.7% of the global protein market by 2030.
Plants make their own food by the process of photosynthesis.
A lot of plant species are used for medicinal purposes.
(Source: Bing search)" > general_info_plants.txt

mkdir -p trees
mkdir -p food_plants
mkdir -p weeds
cd trees

echo "There are many different types of trees.
Oak trees: large, deciduous trees with lobed leaves and acorns
Birch trees: hardwood, deciduous trees with white or gray bark and catkins
Ash trees: deciduous trees with dense, rounded crowns and winged seeds
Sycamore trees: deciduous trees with mottled bark and maple-like leaves
Maple trees: deciduous trees with opposite, lobed leaves and winged fruits
Cedar trees: evergreen, coniferous trees with scaly leaves and woody cones
Juniper trees: evergreen, coniferous trees with needle-like leaves and berry-like cones
Willow trees: deciduous trees with long, slender leaves and catkins
(Source: Bing search)" > tree_types.txt

echo "Some facts about trees are:
Trees are the largest plants in existence and reproduce by seeds.
Trees are the longest living species on earth, with some trees over 5000 years old.
Trees help improve water quality, reduce noise, air and water pollution, and provide oxygen.
Dead wood is valuable for a forest, creating nitrogen and microhabitats for wildlife.
A large oak tree can drop 10,000 acorns in one year.
(Source: Bing search)" > general_info_trees.txt

cd ..
cd food_plants

echo "Plants for food are plants that can be eaten by humans or animals.
Some examples of plants for food are:
Roots, such as radish, turnip, carrot, and beetroot
Stems, such as potato and ginger
Leaves, such as spinach, cabbage, and lettuce
Flowers, such as broccoli and cauliflower
Cattails, which are edible and useful in many ways
Yarrow, which is a medicinal herb
Mullein, which is a plant with soft leaves and yellow flowers
Rose hips, which are the fruits of roses and rich in vitamin C
(Source: Bing search)" > common_plants_used_as_food.txt

echo "There are more than 50,000 edible plants in the world, 
but just 15 of them provide 90 percent of the world’s food energy intake. 
Rice, corn (maize), and wheat make up two-thirds of this. 
Other food staples include millet and sorghum; tubers such as potatoes, cassava, yams, and taro;
and animal products such as meat, fish, and dairy.

Plants are a source of a wide variety of nutrients required to keep the human body in perfect working condition. 
Humans consume everything from fruits, flowers, even the stem of some plants, leaves and stem-like lettuce, celery, 
roots of some plants like carrots, beetroot, and seeds like wheat, rice.
(Source: Bing search)" > general_info_food_plants.txt

cd ..
cd weeds

echo "Weeds are plants that are considered undesirable in a particular situation.
They are opportunistic and aggressive, and genetically designed to germinate, grow, and propagate faster than most desirable plants.
Weeds spread easily and their seeds are specially adapted to spread.
Some general facts and statistics about weeds include:
There are three main types of weeds: sedges, grass weeds, and broadleaf weeds.
Weeds have three life cycles: annual, biennial, and perennial.
Invasive weeds in the US are largely non-native plants introduced from Asia and Europe.
Over 90% of the 350 million acres of federal public land in the West still hasn’t been infected by exotic weeds.
(Source: Bing search)" > general_info_weeds.txt

echo "Weeds generally fall into three categories—annual weeds, perennials, and biennial weed plants.
Annual weeds that spread by seed can grow every year in new places. 
Perennial weeds produce long taproots and can be challenging to remove.
Biennial weeds produce flowers in the first year and seeds in their second.

There are many types of weeds that fall into these categories. 
Some common types of weeds include Asiatic Bittersweet, Bindweed, Dandelions, Giant Ragweed, Hedge Bindweed, Ground Ivy, Purslane, Stinging Nettle and many more.
(Source: Bing search)" > types_of_weeds.txt

cd ..
cd ..

mkdir -p vehicles
cd vehicles
mkdir -p engines
mkdir -p manufacturers
cd engines

echo "A combustion engine is a heat engine that converts the heat released from burning a fuel to mechanical energy.
The fuel is usually mixed with air and ignited in a combustion chamber that is part of the fluid flow circuit.
The combustion causes the gases to expand and push pistons, crankshafts, flywheels, or turbines that produce mechanical energy.
Internal combustion engines are the most common type of combustion engines and are used in various vehicles and machines.
(Source: Bing search)" > combustion_engines.txt

echo "There are different ways to categorize engines, but some common categories include:
Internal combustion engines
Hybrid engines (Internal combustion engine + electric engine)
Electric engines
Petrol engines
Diesel engines
Gas engines
Otto cycle engines
Diesel cycle engines
Dual combustion cycle engines
(Source: Bing search)" > types_of_engines.txt

echo "Common engine sizes for cars include:
1.2-liter engines for smaller three-cylinder setups.
2.0-liter, 2.4-liter, or 2.5L engines for four-cylinder configurations.
Engines of 1.0-litre or less usually feature three or four cylinders, with many using turbochargers for an extra boost.
Other engine sizes include 262-400, 396-454, LS1/LS6, 221-351W, 351C, 429-460, 352-427FE, and 4.6L SOHC.
(Source: Bing search)" > engine_sizes.txt

cd ..
cd manufacturers

echo "General Motors:-----Buick, Cadillac, Chevrolet, GMC

Buick: Founded in 1899 as 'Buick Auto-Vim and Power Company'.
Formed General Motors in 1908.

Cadillac: Founded as Henry Ford Company in 1901.
Renamed to Cadillac in 1902.
Acquired by General Motors in 1909.

Chevrolet: Founded in 1911.
Acquired by General Motors in 1918.

GMC: Formed as General Motors Truck Company (GMTC) in 1912 after merging Rapid Motor Vehicle co. and Reliance Motor Truck co.

Stellantis:-----Chrysler, Dodge, Jeep, RAM

Chrysler: Formed in 1925 as the founding brand of Chrysler Corporation (the predecessor to Fiat Chrysler Automobiles).
Became a part of Stellantis in 2021.

Dodge: Formed in 1914.
Acquired by Chrysler in 1928.

Jeep: Formed by Willys-Overland in 1941.
Merged with Kaiser Motors in 1953.
Acquired by AMC in 1970.
Acquired by Chrysler in 1987.

RAM: Formed in 2010 during a restructure of Chrysler's truck brands.

Ford Motor Company:-----Ford, Lincoln

Ford: Founded in 1903 as Ford.

Lincoln: Founded in 1917.
Acquired by Ford Motor Company in 1922.
(Source: Wikipedia (https://en.wikipedia.org/wiki/List_of_automobile_manufacturers_of_the_United_States))" > vehicle_manufacturers.txt

cd ~/Desktop
repo_url="https://raw.githubusercontent.com/python-can-define-radio/python-course/main/resources/rich_presentations/rich_presentations.zip"
download_dir="richzip"
mkdir -p "$download_dir"
curl -L -o "$download_dir/rich_presentations.zip" "$repo_url"

if [ $? -eq 0 ]; then
    echo -e "\e[32m- Download successful.\e[35m"
else
    echo "Download failed. Please check the URL and try again."
fi

# cleanup from possible previous run
rm -rf $download_dir/rich_presentations

unzip -q "$download_dir/rich_presentations.zip" -d "$download_dir"
    
    # Check if unzip was successful
    if [ $? -eq 0 ]; then
        echo -e "\e[32m- Unzip successful.\e[35m"
    else
        echo "Unzip failed."
    fi
  
username=$(whoami)   
source_file="/home/$username/Desktop/richzip/rich_presentation_launcher.desktop"
destination_dir="/home/$username/.local/share/applications/"
mv "$source_file" "$destination_dir"

if [ $? -eq 0 ]; then
    echo -e "\e[32m- Successfully moved rich_presentation_launcher.desktop.\e[35m"
else
    echo "Move failed."
fi   

source_file_launcher="/home/$username/Desktop/richzip/rich_presentation_launcher.py"
destination_dir_launcher="/home/$username/Desktop/"     
mv "$source_file_launcher" "$destination_dir_launcher"

if [ $? -eq 0 ]; then
    echo -e "\e[32m- Successfully moved rich_presentation_launcher.py.\e[35m"
else
    echo "Move failed."
fi   

mv richzip rich_presentations

cd /run/user
username=$(whoami)
directories=($(ls -d */))
if [ -z "$directories" ]; then
    echo "Samba does not appear to be mounted. Specifically, didn't find any directories in $(pwd).";
fi

for dir in "${directories[@]}"; do
    # Remove the trailing slash from the directory name
    dir=${dir%/}
    # Check if the directory name contains more than 5 digits
    if [[ "$dir" =~ [0-9]{6,} ]]; then
        usernumber=$dir
        break
    fi
done 

cd $usernumber
cd gvfs

if [ -z "$(ls)" ]; then
    echo "No samba shares appear to be mounted. Specifically, didn't find anything in $(pwd)";
    exit
fi

studentdir="$(ls | grep student || true)"

if [ -z "$studentdir" ]; then
    echo "Student samba share does not appear to be mounted. Specifically, didn't find anything containing the word student in $(pwd)";
    exit    
fi
# studentdir=$(ls -lt | grep "^d" | grep "student" | head -n 1 | awk '{print $NF}')
cd $studentdir # chooses just the student samba dir in the event the instructor is linked to both inst samba and student samba
samba_root=$(pwd)
source_file_python_slideshows="$samba_root/python_resources/python_slideshows/"
destination_dir_python_slideshows="/home/$username/Desktop/"  
  
cp -r "$source_file_python_slideshows" "$destination_dir_python_slideshows"

if [ $? -eq 0 ]; then
    echo -e "\e[32m- Successfully moved python slideshows folder to the Desktop.\e[35m"
else
    echo "Move failed."
fi 

source_file_sdr_slideshows="$samba_root/sdr_resources/sdr_slideshows/"
destination_dir_sdr_slideshows="/home/$username/Desktop/"  

cp -r "$source_file_sdr_slideshows" "$destination_dir_sdr_slideshows"

if [ $? -eq 0 ]; then
    echo -e "\e[32m- Successfully moved sdr slideshows folder to the Desktop.\e[35m"
else
    echo "Move failed."
fi 

source_file_sdr_angel_zip="$samba_root/sdr_resources/sdr_proot_env.tar"
destination_dir_sdr_angel_zip="/home/$username/Desktop/sdr_proot_env.tar"  
  
cp -r "$source_sdr_angel_zip" "$destination_dir_sdr_angel_zip"

if [ $? -eq 0 ]; then
    echo -e "\e[32m- Successfully moved SDR Angle zip to the Desktop.\e[35m"
else
    echo "Move failed."
fi 

source_file_sdr_slideshows="$samba_root/sdr_resources/sdr_slideshows/"
destination_dir_sdr_slideshows="/home/$username/Desktop/"  

cp -r "$source_file_sdr_slideshows" "$destination_dir_sdr_slideshows"

if [ $? -eq 0 ]; then
    echo -e "\e[32m- Successfully moved sdr slideshows folder to the Desktop.\e[35m"
else
    echo "Move failed."
fi 
# Cleanup

cd ~/Desktop/
echo "Would you like to delete the student_config_script.sh from the Desktop? (y|N)"
read delsetupscript
if [ y == $delsetupscript ]
then 
    echo "Deleting student_config_script.sh."
    rm student_config_script.sh
    if [ $? -eq 0 ]; then
        echo -e "\e[32m- Successfully removed student_config_script.sh.\e[35m"
    else
        echo "Deletion failed."
    fi   
else 
    echo "Ok we won't delete it even though it is of no further use."
fi

# You might need to restart Nautilus for changes to take effect

echo "You need to exit the file browser (Nautilus) for changes to fully take effect."
echo "Would you like to exit Nautilus now? (y|N)"
read exitnautilusnow
if [ y == $exitnautilusnow ]
then 
    echo "Exiting nautilus."
    nautilus -q
else 
    echo "Please restart the file browser when convenient."
fi
xrandr --output HDMI-2 --off
