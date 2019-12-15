#include <iostream>
#include <ctime>
#include <cstdlib>
using namespace std;





int main(){
    int width = 5;
    int height = 5;
    int state[height][width];
    srand(time(NULL));

    for (int i = 0; i < height; i++){
        for (int j = 0; j < width; j++){
            state[i][j] = 0;
        }
    }

    cout << "before randomizing\n";

    for (int i = 0; i < height; i++){
        for (int j = 0; j < width; j++){
            cout << "state[" << i << "][" << j << "]: " << state[i][j] << endl;
        }
    }

    int r = 0;
    for (int i = 0; i < height; i++){
        for (int j = 0; j < width; j++){
            r = rand() % 10 + 1;
            if (r > 5){
                state[i][j] = 1;
            }else{
                state[i][j] = 0;
            }
        }
    } 

    cout << "after randomizing\n";

    for (int i = 0; i < height; i++){
        for (int j = 0; j < width; j++){
            cout << "state[" << i << "][" << j << "]: " << state[i][j] << endl;
        }
    }
    return 0;
}