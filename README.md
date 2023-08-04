# CodeBots
Automating Code Review Activities in Fork-Based Development

Datasets
----------
Reference: R. Tufan, L. Pascarella, M. Tufanoy, D. Poshyvanykz, and G. Bavota, “Towards automating code review activities,” in 2021 IEEE/ACM 43rd International Conference on Software Engineering (ICSE). IEEE, 2021, pp. 163–174. 

The dataset is in the ```data``` directory, which contains the source dataset and the processed dataset.

How to run
----------
### Setting parameters
Before model training, some parameters need to be set. 
You can adjust the values of these parameters in the ```config``` directory
### Training
``` bash
python main.py --name CodeBots
```
### Prediction
``` bash
python infer.py --name CodeBots
```

