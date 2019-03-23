# Bouncing Ants 

Some ants are displaced of a table. They all walk at speed $1$, that is, in a unit of time they walk out one unit of distance in their direction, where the width of the table is $W$ units of distance, with $W$ an even natural number.
Initially, some of them are directed rightward and the others are directed leftwards, but each one of them starts from a different coordinate which is an even natural number in the interval $[0,W]$.
While time passes, it may happen that two ants walking in opposite directions bump their heads (actually, sense each other through the antennas). When this happens, that is, when their two coordinates coincide, then the two ants bounce on each other and immidiately flip their directions of march.  

We ask you to report in which order (and times) the ants fall off of the table, or the history of one single ant (simulations), but also to express bounds on how long such a process can last by adopting a wider view on the process.

Note: in reporting what happens, we need having named the ants. Ants are named according to their original settings: the rightwards get even numbers, the leftwards get odd numbers: the number 1 is the (originally) leftward moving ant of smalles coordinate, the number 2 is the (originally) rightward moving ant of smalles coordinate.

ITALIAN:
Delle formiche sono disposte su un tavolo. Esse si muovono tutte a velocità $1$, ossia, ad ogni unità di tempo, percorrono un unità di distanza nella loro direzione, dove il tavolo sia largo $W$ unità di distanza con $W$ un numero naturale pari.
Inizialmente, alcune delle formiche si muovono verso destra ed altre verso sinistra, partendo tutte da una coordinata che è un numero pari nell'intervallo $[0,W]$.
A processo avviato potrà accadere che due formiche che si stanno muovendo in direzioni opposte si scontrino (o entrino in contatto con le antenne). Quando questo succede, ossia quando le coordinate delle due formiche coincidiono, entrambe le formiche invertono istantaneamente il loro senso di marcia.
Chiediamo di riportare l'ordine (ed i tempi) in cui le formiche cadono giù dal tavolo, o la storia di una singola formica (simulazione).
Ma ti chiediamo anche di esprimere limiti superiori su quanto a lungo questo processo possa durare (siamo sicuri che termini sempre? Perchè?) adottando una più ampia visione di insieme sull'intero processo.


### Goals 

Questo problema prevede i seguenti goal, ossia obbiettivi che puoi prefiggerti di raggiungere (se ne vedi altri di interessanti facci sapere che arricchiamo il problema):

- `simulate_process_small`: al più $N=10$ formiche, $W <= 100$.
- `simulate_process_big`: al più $N=10$ formiche, $W <= 100000000$.
- `simulate_one_ant_small`: al più $N=20$ formiche, $W <= 100$.
- `simulate_one_ant_middle`: al più $N=20$ formiche, $W <= 1000000000$.
- `simulate_one_ant_big`: al più $N=1000000$ formiche, $W <= 1000000000$.
- `upper_bound_on_end_of_process`: al più $N=1000000$ formiche, $W <= 1000000000$, answer within $0.5$ sec.
- `precise_end_of_process`: al più $N=1000000$ formiche, $W <= 1000000000$, answer within $0.5$ sec.
- `upper_bound_on_end_of_process_without_knowing_the_initial_disposition_of_the_ants`: al più $N=1000000$ formiche, $W <= 1000000000$, answer within $0.01$ sec.
