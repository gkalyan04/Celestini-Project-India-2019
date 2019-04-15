### Section D


##### Problem statement selected : 
Analytics and alerts on women safety using mobile microphone and public area cameras.

##### Solution
Idea is to have a decentralised security for car pooling and generate trust by the blend of Machine learning and Blockchain. Also, preventing the crime by having real time responses rather than post crime responses by authorities.
We propose to have the device integrated with various modules like GSM, GPS, Camera, Microphone, Wifi etc. Such device would be fit in the cars linked with car owner’s account. Car owners would buy the device to earn by sharing the travel with co-passengers. For co-passengers, it would cut down their cost to 25% to 50% of their initial cabs (Ola, Uber etc.). Also, middle man like Ola, Uber are removed from the scenario.

##### Flow of working:

Car owner enters the car, switches on the device and enters his route where he is going.
The co-passenger willing to travel same route is matched.
During the travel, the device remains on and could not be shut down. It does following functionality:
GPS values are constantly noted, sent to the local database during the whole travel. There is no tracking of the car in normal cases.
Microphone in the device helps in the audio processing and does scream detection. It will work for human frequency, hence, making it resistant towards inhuman sources. Whenever this system will detect that somebody is yelling or shouting for help, emergency system would be triggered.
Camera in the device allows video processing and constantly have an eye over passengers offline. Classification of real time video for various activities and actions like strangling, beating etc.
The co-passenger pays the amount to car owner decided and exits safely.

Note: Here, we are focusing on both women and men safety, basically the safety of everyone travelling.

##### What happens during emergency?

During emergency, the location of car/ victim is sent via internet & GSM of device. It is happening via cloud architecture. Nearest police stations can be notified instantly. The photo/ video & audio evidences are put on blockchain (ideally their IPFS hash) so that they become untamperable. The GSM helps transfer the details like GPS values, hashes etc. which get transacted on blockchain instantly via our server. So, device may even work if offline. Note, during the false triggers, the passengers can shut down the alert in a given time span via their app.

##### How we would be better than Ola / Uber?
They do not have any solid realtime mechanism to handle any mishap with passengers like audio/video processing (due to lack of trust for the same). Centralised organisations may not reveal all the cases filed against them (women cases mostly), as it may defame their name. The evidences are either not present or may get tampered easily. They are costlier too. Hence, our system may be well off in both social and economic background.

##### Architecture:
<img src= "https://github.com/piyush-98/Cesltine_TEST/blob/master/Section%20D/architecture.png">

##### Datasets/ Data acquisition for training:
The algorithm 
There will be two parts in this,we will be starting with the behavioral learning, it is a type of learning in which the algorithm learns to detect some particular behaviors, in the case of women security this can be any violent or abrupt action in the car against her. After searching for the datasets we came across [C-F violence Dataset](https://www.openu.ac.il/home/hassner/data/violentflows/) , Violent Flows Dataset, these two work upon learning violent as well as non-violent behavior.

The second Audio (scream Detection) is simple audio analysis by making spectrogram of the audio received and screening it’s pitch, amplitude and frequency. The inhuman voices would not be taken into account. Also, searching for datasets we found [MIVIA audio events dataset](http://www.cs.rug.nl/~nick/datasets/). Depending on processings after integrating (since, there are various other processings in parallel) and accuracy, we will decide what method to employ.  



##### Machine Learning algorithm (running offline):
We will be working upon video analysis for behavioral learning part of the product, it is a type of learning in which a machine learns a particular set of behaviour of human beings for example in our case whether any violent or non violent behaviour has taken place or not in a cab , this will be useful to know any potential crime against women is taken place or not , A lot of algorithms have been used for this type of learning but SVM is considered the best after applying various computer vision techniques that is finding out set of features which would help us classifying the result.

The second part is Audio Analysis we will be using Librosa(a python library) to find out the spectrogram of input audio, we are basically thinking to learn the set of values for (frequency, pitch, amplitude) of the women or any human being for example we will only be working upon the human frequency and the pitch or amplitude in which a women could possibly scream.   

##### Platform to run Machine Learning algorithm:

JeVois-A33 may be used for video processing. JeVois smart machine vision camera has an Allwinner A33 quad-core Cortex A7 processor, running at 1.34 GHz married to a 1.3-megapixel camera, with 256 MB of RAM, that can analyze scenes at 120 frames per second. It would work offline and quite efficiently. Considering the complexity to integrate GSM, GPS and microphone capabilities to it, we might use arduino Nano in parallel. This will even serve us the benefit that in case any wrong person tries to destroy the camera, other things will still work (which we can keep hidden in cars). Beaglebone Black may also be considered.




