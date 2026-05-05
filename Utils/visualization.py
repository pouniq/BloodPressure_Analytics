
def Plot_L(datasets, names):
    
    import matplotlib.pyplot as plt


    for data, name in  zip(datasets, names):
        fig, ax = plt.subplots(3,1,figsize=(10,7))

        ax[0].plot(data['morning'], color = 'red')
        ax[0].set_title(f'Morning, Left Hand {name}')

        ax[1].plot(data['noon'])
        ax[1].set_title(f'Noon, Left Hand {name}')

        ax[2].plot(data['night'])
        ax[2].set_title(f'Night, Left Hand {name}')
        plt.tight_layout()
        plt.show()



def Plot_R(datasets, names):
    

    import matplotlib.pyplot as plt
    for data, name in  zip(datasets, names):
        fig, ax = plt.subplots(3,1,figsize=(10,7))

        ax[0].plot(data['morning'], color = 'red')
        ax[0].set_title(f'Morning, Right Hand {name}')

        ax[1].plot(data['noon'])
        ax[1].set_title(f'Noon, Right Hand {name}')

        ax[2].plot(data['night'])
        ax[2].set_title(f'Night, Right Hand {name}')
        plt.tight_layout()
        plt.show()
