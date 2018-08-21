In [1]: import pandas as pd

In [2]: ds=pd.read_csv('Game_medal.csv',encoding="ISO-8859-1")

In [3]: ds.describe()
Out[4]: 
            Edition
count  29216.000000
mean    1967.713171
std       32.406293
min     1896.000000
25%     1948.000000
50%     1976.000000
75%     1996.000000
max     2008.000000

In [5]: ds.head()
Out[5]: 
     City  Edition     Sport Discipline             Athlete  NOC Gender                       Event Event_gender   Medal
0  Athens     1896  Aquatics   Swimming       HAJOS, Alfred  HUN    Men              100m freestyle            M    Gold
1  Athens     1896  Aquatics   Swimming    HERSCHMANN, Otto  AUT    Men              100m freestyle            M  Silver
2  Athens     1896  Aquatics   Swimming   DRIVAS, Dimitrios  GRE    Men  100m freestyle for sailors            M  Bronze
3  Athens     1896  Aquatics   Swimming  MALOKINIS, Ioannis  GRE    Men  100m freestyle for sailors            M    Gold
4  Athens     1896  Aquatics   Swimming  CHASAPIS, Spiridon  GRE    Men  100m freestyle for sailors            M  Silver

In [6]: ds.tail()
Out[6]: 
          City  Edition      Sport       Discipline               Athlete  NOC Gender       Event Event_gender   Medal
29211  Beijing     2008  Wrestling  Wrestling Gre-R        ENGLICH, Mirko  GER    Men   84 - 96kg            M  Silver
29212  Beijing     2008  Wrestling  Wrestling Gre-R  MIZGAITIS, Mindaugas  LTU    Men  96 - 120kg            M  Bronze
29213  Beijing     2008  Wrestling  Wrestling Gre-R       PATRIKEEV, Yuri  ARM    Men  96 - 120kg            M  Bronze
29214  Beijing     2008  Wrestling  Wrestling Gre-R         LOPEZ, Mijain  CUB    Men  96 - 120kg            M    Gold
29215  Beijing     2008  Wrestling  Wrestling Gre-R        BAROEV, Khasan  RUS    Men  96 - 120kg            M  Silver

In [7]: ds.head(10)
Out[7]: 
     City  Edition     Sport Discipline                Athlete  NOC Gender                       Event Event_gender   Medal
0  Athens     1896  Aquatics   Swimming          HAJOS, Alfred  HUN    Men              100m freestyle            M    Gold
1  Athens     1896  Aquatics   Swimming       HERSCHMANN, Otto  AUT    Men              100m freestyle            M  Silver
2  Athens     1896  Aquatics   Swimming      DRIVAS, Dimitrios  GRE    Men  100m freestyle for sailors            M  Bronze
3  Athens     1896  Aquatics   Swimming     MALOKINIS, Ioannis  GRE    Men  100m freestyle for sailors            M    Gold
4  Athens     1896  Aquatics   Swimming     CHASAPIS, Spiridon  GRE    Men  100m freestyle for sailors            M  Silver
5  Athens     1896  Aquatics   Swimming  CHOROPHAS, Efstathios  GRE    Men             1200m freestyle            M  Bronze
6  Athens     1896  Aquatics   Swimming          HAJOS, Alfred  HUN    Men             1200m freestyle            M    Gold
7  Athens     1896  Aquatics   Swimming       ANDREOU, Joannis  GRE    Men             1200m freestyle            M  Silver
8  Athens     1896  Aquatics   Swimming  CHOROPHAS, Efstathios  GRE    Men              400m freestyle            M  Bronze
9  Athens     1896  Aquatics   Swimming          NEUMANN, Paul  AUT    Men              400m freestyle            M    Gold

In [8]: ds.tail(10)
Out[8]: 
          City  Edition      Sport       Discipline               Athlete  NOC Gender       Event Event_gender   Medal
29206  Beijing     2008  Wrestling  Wrestling Gre-R      MINGUZZI, Andrea  ITA    Men   74 - 84kg            M    Gold
29207  Beijing     2008  Wrestling  Wrestling Gre-R         FODOR, Zoltan  HUN    Men   74 - 84kg            M  Silver
29208  Beijing     2008  Wrestling  Wrestling Gre-R       MAMBETOV, Asset  KAZ    Men   84 - 96kg            M  Bronze
29209  Beijing     2008  Wrestling  Wrestling Gre-R         WHEELER, Adam  USA    Men   84 - 96kg            M  Bronze
29210  Beijing     2008  Wrestling  Wrestling Gre-R    KHUSHTOV, Aslanbek  RUS    Men   84 - 96kg            M    Gold
29211  Beijing     2008  Wrestling  Wrestling Gre-R        ENGLICH, Mirko  GER    Men   84 - 96kg            M  Silver
29212  Beijing     2008  Wrestling  Wrestling Gre-R  MIZGAITIS, Mindaugas  LTU    Men  96 - 120kg            M  Bronze
29213  Beijing     2008  Wrestling  Wrestling Gre-R       PATRIKEEV, Yuri  ARM    Men  96 - 120kg            M  Bronze
29214  Beijing     2008  Wrestling  Wrestling Gre-R         LOPEZ, Mijain  CUB    Men  96 - 120kg            M    Gold
29215  Beijing     2008  Wrestling  Wrestling Gre-R        BAROEV, Khasan  RUS    Men  96 - 120kg            M  Silver
