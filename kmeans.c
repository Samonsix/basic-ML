#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <math.h>
#include <random>

int main()
{
    float x[10000][2];
    float u00 = 10,u01 = 9;
    float u10 = 9,u11 = 8;
    int s = 6;

    srand((unsigned)time(NULL));

    for(int i = 0; i < 5000; i++)
    {
        x[i][0] = u00 + rand()/(RAND_MAX+1.0) + rand()%s - s/2.0;
        x[i][1] = u01 + rand()/(RAND_MAX+1.0) + rand()%s - s/2.0;
    }

    for(int i = 5000; i < 10000; i++)
    {
        x[i][0] = u10 + rand()/(RAND_MAX+1.0) + rand()%s - s/2.0;
        x[i][1] = u11 + rand()/(RAND_MAX+1.0) + rand()%s - s/2.0;
    }

    srand((unsigned)time(NULL));
    float centor0[2],centor1[2];
    centor0[0] = x[rand()%10000][0];
    centor0[1] = x[rand()%10000][1];

    centor1[0] = x[rand()%10000][0];
    centor1[1] = x[rand()%10000][1];

    printf("centor:(%1.1f, %1.1f), (%1.1f, %1.1f)\n",centor0[0],centor0[1],centor1[0],centor1[1]);

    float dis[10000][2];
    for(int i = 0; i < 50; i++)
    {
        float x_t0[2]={0,0}, x_t1[2] = {0,0};
        int t0 = 0, t1 = 0;
        float dis_mean = 0;
        //step1, calc distance
        for(int j = 0; j < 10000; j++)
        {
            dis[j][0] = distance(x[j],centor0);
            dis[j][1] = distance(x[j],centor1);

            if(dis[j][0] < dis[j][1])
            {
                x_t0[0] += x[j][0];
                x_t0[1] += x[j][1];
                t0++;
                dis_mean += dis[j][0];
            }
            else
            {
                x_t1[0] += x[j][0];
                x_t1[1] += x[j][1];
                t1++;
                dis_mean += dis[j][1];
            }
        }
            
        //step2, calc means, centor
        if(t0 > 0)
        {
            centor0[0] = x_t0[0]/t0;
            centor0[1] = x_t0[1]/t0;
        }

        if(t1 > 0)
        {
            centor1[0] = x_t1[0]/t1;
            centor1[1] = x_t1[1]/t1;
        }

        printf("step:%d , dis = %f\n",i, dis_mean/10000);
    }
	
    printf("centor:(%1.1f, %1.1f), (%1.1f, %1.1f)\n",centor0[0],centor0[1],centor1[0],centor1[1]);
    system("pause");
}