$$
n = \frac {v}{D};\tag{5.7}
$$

that is, the one-way trip time t is 

$$
t = \frac {d}{v} = \frac {1}{2 n}.\tag{5.8}
$$

In one round trip one vehicle delivers 2w tons of freight; therefore, in one hour one vehicle would deliver 2nw tons. 

Now consider a fleet of vehicles. Let Q be the total number of vehicle round trips scheduled per hour and q the number actually accomplished (which may be different from the number scheduled). Then the maximum total volume that can be delivered by the fleet, the capacity volume, is 2qw. 

The price to be charged per one-way trip per ton, P, is set as an option. 

To formalize these relationships we add the following variables: T, the vector of transportation options; M, the vector of options specifying technological characteristics; and $V_{C}$ , the capacity volume (the maximum payload that can be carried in both directions, per hour, for the options T). For this system 

$$
\mathbf {T} = (\mathbf {M}, Q, P),\tag{5.9}
$$

where 

$$
\mathbf {M} = (w, v);\tag{5.10}
$$

the environment E is 

$$
\mathsf {E} = (d);\tag{5.11}
$$

and the capacity volume is 

$$
V _ {\mathrm{C}} (\mathsf {T}) = 2 w q.\tag{5.12}
$$

In this case we assume also that 

$$
q = Q.\tag{5.13}
$$

SERVICE-LEVEL RELATIONSHIPS 

We now consider the service variables: 

$$
t _ {\mathrm{w}}
$$

$h_{e}$ = average time interval between successive vehicles (headway), 

$t_{\mathrm{T}} =$ total one-way trip time, 

c = out-of-pocket price paid by traveler, 

$$
\mathbf {S} = (t _ {\mathrm{iv}}, t _ {\mathrm{w}}, t _ {\Gamma}, c).
$$

These are related to the options and other parameters as follows. First, c = P is set explicitly as a transportation option. Since each vehicle will cover the round-trip distance in 1/n hours, the one-way in-vehicle travel time will be 

$$
t _ {\mathrm{iv}} = \frac {d}{v} = \frac {1}{2 n}.\tag{5.14}
$$

We assume that the vehicles are scheduled to cycle continuously at a uniform rate over the route. The total number of vehicles passing any particular point per hour is q. The headway is thus 

$$
h = \frac {1}{q}.\tag{5.15}
$$

We assume that shipments arrive at random without knowledge of the schedule, so the average wait time experienced by a user is half the headway: 

$$
t _ {\mathrm{w}} = \frac {1}{2} h = \frac {1}{2 q}\tag{5.16}
$$

$$
\text { or,   since } q = Q,
$$

$$
t _ {\mathrm{w}} = \frac {1}{2 Q}.\tag{5.17}
$$

The total trip time is 

$$
\begin{array}{l} t _ {\mathrm{T}} = t _ {\mathrm{iv}} + t _ {\mathrm{w}} \\ = \frac {1}{2} \left(\frac {1}{n} + \frac {1}{Q}\right). \end{array}\tag{5.18}
$$

Let us look at the service level as a function of the options T. Specifically, we vary frequency Q over a range of values, holding M and P fixed; then we can vary M and P. The components of $\mathbf{S}(\mathbf{T})$ are shown in figure 5.7, parts a–c. Note that only $t_{w}$ and $t_{T}$ are actually influenced by Q; c and $t_{iv}$ depend only on P and M. 

## RESOURCES CONSUMED

Assume for this example that the resources can be expressed wholly in terms of vehicle-hours. The magnitude of resources consumed is then the total vehicle-hours per hour, or 


b


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/fc366feb-933b-4442-bcbf-4538c4ada340/a6410c90b6f2646a3349a5516b6b20bcd430110d597914d9ba4ab5f15a452c4c.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/fc366feb-933b-4442-bcbf-4538c4ada340/466bce9ab0dade49496aee361720921de03f92e9a84a628867bd6c2f409b7267.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/fc366feb-933b-4442-bcbf-4538c4ada340/4092177bcac606d7b2909c0649b888698985147a8fa39894f0d282cedcbff59c.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/fc366feb-933b-4442-bcbf-4538c4ada340/132dba1390eef2e4f47c6e7342b8eb64c9289493ac6b79711586e0fce8c0f93a.jpg)



Figure 5.7 Service and resource variations (for a given technology).


$$
R = \frac {Q}{n} = Q \frac {d}{v}.\tag{5.19}
$$

This is shown in figure 5.7d. 

## THE TRANSPORTATION PERFORMANCE FUNCTION

Thus this model expresses the performance function explicitly in terms of the options, as shown in table 5.3. 

## 5.4.2 Travel-Market Equilibration

In the general case finding the equilibrium volume $V_{E}$ that satisfies both service and demand conditions can involve complex calculations. In this performance model, however, the service level is a function of the options T only and does not vary as $V_{E}$ varies (there are no congestion effects). Thus travel-market equilibration is trivial (also because we are dealing with a single link and not a network), and, as in section 5.3.2, 

$$
V _ {\mathrm{D}} = f _ {\mathrm{D}} (\mathbf {S}),\tag{5.20}
$$

$$
V _ {\mathrm{E}} = \min (V _ {\mathrm{D}}, V _ {\mathrm{C}}).\tag{5.21}
$$

For this performance model 

$$
V _ {\mathrm{C}} = 2 w Q,\tag{5.22}
$$

so the load factor is 

$$
\lambda = \frac {V _ {\mathrm{E}}}{V _ {\mathrm{C}}} = \frac {V _ {\mathrm{E}}}{2 w Q}.\tag{5.23}
$$


Table 5.3 Performance model I


<table><tr><td>Options</td><td><eq>\mathbf{T} = (\mathbf{M}, Q, P)</eq><eq>\mathbf{M} = (w, v)</eq></td></tr><tr><td>Environment</td><td><eq>\mathbf{E} = (d)</eq></td></tr><tr><td>Basic relationships</td><td><eq>q(\mathbf{T}) = Q</eq><eq>V_{\mathrm{c}}(\mathbf{T}) = 2wq</eq><eq>n(\mathbf{T}) = \frac{v}{2d}</eq></td></tr><tr><td>Service level</td><td><eq>\mathbf{S}(\mathbf{T}) = (t_{\mathrm{iv}}, t_{\mathrm{w}}, t_{\mathrm{T}}, c)</eq><eq>c(\mathbf{T}) = P</eq><eq>t_{\mathrm{iv}}(\mathbf{T}) = \frac{d}{v}</eq><eq>t_{\mathrm{w}}(\mathbf{T}) = \frac{1}{2q}</eq><eq>t_{\mathrm{T}}(\mathbf{T}) = \frac{1}{2}\left(\frac{2d}{v} + \frac{1}{q}\right)</eq></td></tr><tr><td>Resources consumed</td><td><eq>R = \frac{q}{n}</eq></td></tr></table>

Thus $\lambda$ , $V_{E}$ , and $V_{C}$ are all functions of the options T. (Note that, consistent with our definition of $V_{C}$ , $V_{D}$ and $V_{E}$ are also the total payloads of one-way trips.) 

## 5.4.3 Evaluation

We now want to trace out impacts on users and operators. The user impacts are expressed in terms of the service levels and volume at equilibrium, $S_{E}$ and $V_{E}$ . For our present purposes $V_{E}$ is a sufficiently good measure of the impact on users. (In chapter 9 various economic formulations for expressing user impacts in terms of both service levels and volumes are considered. Since $V_{E}$ is a monotonically increasing function of the level of service, we shall use $V_{E}$ as a proxy for the more elaborate formulations.) 

From the operator's perspective, economic measures such as costs and revenues are often important. Users pay fares and thus provide revenues to the operator. The gross revenue from users, $I_{\mathrm{GR}}$ , is the product of $V_{\mathrm{E}}$ and the price charged, $P$ : 

$$
I _ {\mathrm{GR}} = P V _ {\mathrm{E}}.\tag{5.24}
$$

The magnitude of the resources consumed can also be expressed in monetary terms. The total cost incurred by the operator, $C_{T}$ , is 

$$
C _ {\mathrm{T}} = a R,\tag{5.25}
$$

where a is the unit cost in dollars per vehicle-hour. (This is a simple assumption; more general formulations will be explored in volume 2.) One useful measure of impact on the operator is the net revenue, $I_{NR}$ : 

$$
I _ {\mathrm{NR}} = I _ {\mathrm{GR}} - C _ {\mathrm{T}}.\tag{5.26}
$$

Other measures can be defined to reflect other objectives of the operator, but for our present, introductory discussion, this one measure will suffice. (More subtle and realistic evaluation approaches are described in chapter 9.) 

## 5.4.4 Summary: Methodology for Analysis

This gives us all that we need for a systematic exploration of the options open to this transportation operator. 

The step-by-step methodology is shown in figure 5.8. The methodology includes three basic activities of analysis: search, prediction, and evaluation. (Choice and implementation are not shown here.) The approach to prediction includes the basic elements defined in chapter 1 (except for activity shifts, in this case). Steps 5, 6, and 9 utilize the performance model defined in section 5.4.1. Travel-market equilibration reflects the assumption that there is no congestion (in chapter 7 we shall relax this assumption and introduce the loop indicated by the dashed line marked 1 in this figure to take into account the effects of volume on levels of service). Loop 2 indicates another step we could add later, in which resource consumption is also influenced by actual volumes. We have added a sensitivity analysis in step 12 and feedback loops to step 4 based on the results of prediction (loop 3) and evaluation (loop 4). 

## 5.5 AN AIR TRANSPORTATION EXAMPLE

To illustrate the use of a transportation performance function in a systematic analysis we consider in this section a simplified air transportation example. 

## 5.5.1 The Situation

The operator serves a single market between two cities with round-trip distance D. The options $\mathbf{T} = (\mathbf{M}, Q, P)$ , where M denotes choice of aircraft type, with corresponding maximum payload w, effective speed v, and cost structure a (in dollars per vehicle-hour). The level of service is, as before, $\mathbf{S} = (t_{\mathrm{iv}}, t_{\mathrm{w}}, t_{\mathrm{T}}, c)$ . 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/fc366feb-933b-4442-bcbf-4538c4ada340/095c1fe1d6f717634c0699cff37479d02ce0a9d9b81165e66ad264a41be3ab71.jpg)



Figure 5.8 A methodology for analysis.


## PERFORMANCE FUNCTION

The performance of the system, including available volume $V_{C}$ , resources consumed R, and level of service S, is determined as in section 5.4 and summarized in table 5.3. 

## DEMAND

The demand function is 

$$
V _ {\mathrm{D}} = f _ {\mathrm{D}} (\mathbf {S}) = f _ {\mathrm{D}} (t _ {\mathrm{iv}}, t _ {\mathrm{w}}, t _ {\mathrm{T}}, c)\tag{5.27}
$$

or specifically 

$$
V _ {\mathrm{D}} = Z \left(\frac {1}{1 + e ^ {U _ {0} - U}}\right),\tag{5.28}
$$

where 

$$
U = \alpha_ {1} t _ {\mathrm{iv}} + \alpha_ {2} t _ {\mathrm{w}} + \alpha_ {3} c,\tag{5.29}
$$

$$
U _ {0} = \alpha_ {0},\tag{5.30}
$$

$$
t _ {\mathrm{w}} = \frac {1}{2 q},\tag{5.31}
$$

the $\alpha$ s are empirically determined parameters, and $Z$ is some measure of the activity system's influence on total demand in the market. The behavior of this type of model is similar to that of figure 2.8. We take $\alpha_0 = -1.36$ , $\alpha_1 = -0.5$ , $\alpha_2 = -1.2$ , $\alpha_3 = -0.015$ , and $Z = 900$ . 

For all options (aircraft types and schedule frequencies) being considered, D and v are the same. Therefore $t_{iv}$ is constant. For this section we shall hold P constant also and assume there is no congestion; thus 

$$
c = P, \quad q = Q.\tag{5.32}
$$

Therefore $V_{D}$ is a function of schedule frequency only: 

$$
V _ {\mathrm{D}} = f _ {\mathrm{D}} (Q) = \frac {Z}{1 + \beta_ {1} e ^ {\beta_ {2} / Q}},\tag{5.33}
$$

where 

$$
\beta_ {2} = \frac {\alpha_ {2}}{2}, \quad \beta_ {1} = e ^ {\alpha_ {0} - \alpha_ {1} t _ {i v} - \alpha_ {3} P}.\tag{5.34}
$$

(Note that $V_{D}$ is the two-way volume in total one-way trips per hour.) 

For this example we take 

$$
d = 8 0 0 \mathrm{miles}, \qquad D = 2 d = 1, 6 0 0,
$$

$$
v = 4 0 0 \text {miles per hour}, \quad t _ {\mathrm{iv}} = 2 \text {hours},\tag{5.35}
$$

P = $60. 

Thus in (5.33) we have $\beta_{1} = 1.72$ and $\beta_{2} = 0.6$ . 

For any specific set of options $T^{i}$ , prediction is straightforward, following the equations in table 5.3 and the steps in figure 5.8: 

1. The available volume $V_{C}$ is determined from (5.22). 

2. The number of round trips per vehicle per hour is n = v/D = 0.25. 

3. For S, c and $t_{iv}$ are known, and $t_{w}$ is found by (5.31) and enters directly into the demand function (5.33). 

4. For R, vehicle-hours per hour are determined from $(5.19)$ . 

5. The demand volume $V_{\mathrm{D}}$ is determined from the demand function (5.33). 

6. Since there is no congestion, $V_{E} = \min(V_{D}, V_{C})$ . 

7. $I_{GR}$ is determined from (5.24). 

8. $C_{T}$ is determined from (5.25). 

9. Evaluation follows directly, too: $I_{NR}$ is determined from $I_{GR}$ and $C_{T}$ by (5.26). 

## 5.5.2 Systematic Analysis of the Options

To analyze the options we use the approach described in section 5.4: we systematically vary the options T over a range of values and trace out the impacts on the affected interests (in this case, users and operators), and we examine the predicted impacts and look for trade-offs among the affected interests. 

The options available include choice of vehicle type and schedule frequency (for this section we assume that fare is fixed, for example by regulatory policy). The first question is, for a particular vehicle type, What is the best frequency? From the point of view of the operator, we assume that the best frequency is the one that maximizes net revenue. From the point of view of the users, who want the maximum service, the higher the frequency the better. If net revenue increases as frequency increases, users and operator will both benefit; if net revenue decreases, they will clearly be in conflict. 

The second question is, What are the impacts of alternative vehicle types? Several alternative choices of vehicle are considered, as shown in table 5.4. 


Table 5.4 Three transportation technology options


<table><tr><td>Aircraft type</td><td>Payload (w, seats)</td><td>Cost per vehicle-hour (a)</td><td>Cost per available seat per hour</td></tr><tr><td><eq>M_{1}</eq></td><td>200</td><td>$2,800</td><td>$14</td></tr><tr><td><eq>M_{2}</eq></td><td>140</td><td>$2,240</td><td>$16</td></tr><tr><td><eq>M_{3}</eq></td><td>90</td><td>$1,620</td><td>$18</td></tr></table>

## VARYING OPERATING POLICY

Figure 5.9 illustrates a systematic analysis of operating policy: holding vehicle type fixed at $M_{2}$ , frequency Q is varied over a range. The corresponding variations in $V_{D}$ , $V_{E}$ , and $V_{C}$ are shown in part a of the figure. Part b shows the variation in load factor. Part c shows the monetary impacts on the operator, $C_{T}$ and $I_{GR}$ , and part d the net revenue $I_{NR}$ . For $Q = Q_{OPT}$ , net revenue is a maximum. Points B and D have $I_{NR} = 0$ ; point C, the frequency for maximum $I_{NR}$ , is different from A, the point of maximum load factor. The shaded area in part c has a positive $I_{NR}$ ; maximum $I_{NR}$ is achieved at point C, where the slopes of the $C_{T}$ and $I_{GR}$ functions are equal. 

Part e shows the resulting trade-offs between the users and the operator. Note that in the range B to C increases in frequency make both operator and user better off, while in the range C to D a change in frequency increases benefits to one group while decreasing them to the other. The range C to D thus represents an area of potential conflicts. 

This figure illustrates a systematic procedure for finding (graphically, numerically, or, under some conditions, analytically) the schedule frequency that gives maximum $I_{NR}$ for a particular market, a particular fare, and a particular vehicle choice. 

## EFFECT OF A CAPACITY CONSTRAINT

In some cases the capacity constraint may be binding, in that the point of maximum $I_{NR}$ occurs at a load factor of 1.0. This is illustrated schematically in figure 5.10 for vehicle $M_{3}$ . If there were no capacity constraint, the frequency for maximum net revenue would be $Q_{2}$ , where the slopes of the $C_{T}$ and $I_{GR}$ curves are equal. Since the capacity constraint is operative, net revenue is maximized at frequency $Q_{1}$ . 

## VARYING VEHICLE TYPE

In figure 5.11 the three alternative vehicle choices are compared. Note that there is one demand and gross revenue curve that applies to all three technologies, since at any Q they have the same service levels in all respects. However, there are different $C_{T}$ , $V_{C}$ , and $V_{E}$ curves for each of the three technologies. As a consequence the optimal frequency is different for each technology: $Q_{\mathrm{OPT}}(M_{1}) = 10$ , $Q_{\mathrm{OPT}}(M_{2}) = 12$ , $Q_{\mathrm{OPT}}(M_{3}) = 22$ . 


C


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/fc366feb-933b-4442-bcbf-4538c4ada340/397fa3d8c0d6e5a01e2a7957aa21b719d30592510c9119f693ed90baf0b4955d.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/fc366feb-933b-4442-bcbf-4538c4ada340/dc99644231b3eed70cc8ed784b8767ab7598053852706d976cc45f1c319686e0.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/fc366feb-933b-4442-bcbf-4538c4ada340/16fccc882b2ca1995b7526041dc614c8022fd30a7c30aa80b6346912d93e06a4.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/fc366feb-933b-4442-bcbf-4538c4ada340/b500d6c31acd01c5fb74d9b44a7aa8a474d8eba577eaab09876e49b3a74e6fb5.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/fc366feb-933b-4442-bcbf-4538c4ada340/f3639800b682086e3ef87834ce0433019a01e374c0dbfe7fce00998a8e0c72b6.jpg)



Figure 5.9 Basic analysis for an air transportation example.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/fc366feb-933b-4442-bcbf-4538c4ada340/6ee058ac410d45df332e6bbb36bffb481dae047b2673537788d82307a84880e3.jpg)



b


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/fc366feb-933b-4442-bcbf-4538c4ada340/57b06464a25a009c5ca285fb50a27c0e9de542b74036c40212a62cfd7afda520.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/fc366feb-933b-4442-bcbf-4538c4ada340/0e3e7e6b07b22b565f6047e72a904f4dd747347435a37a6f9df45d3b25f1a973.jpg)



Figure 5.10 Effect of a volume constraint.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/fc366feb-933b-4442-bcbf-4538c4ada340/5f9ace25b5be91f4dc4e4fa864f138fc698fc920368d909725065859b1637a58.jpg)



Figure 5.11 A comparison of three technologies.


## TRADE-OFFS BETWEEN USER AND OPERATOR

Clearly there are trade-offs between impacts on operators and on users, as shown in figure 5.9e. These are emphasized in figure 5.12. The frequencies that produce maximum net revenue for the operator are not those that are "best" from the user's perspective. From that perspective, the higher the value of $V_{\mathrm{E}}$ , the more attractive the system (since $V_{\mathrm{E}}$ is monotonically related to the service level and to other measures of user benefits). 

Figure 5.12 shows some of the trade-offs available. If point N represents the existing service, both users and operators could be made better off by shift to points A, B, or C. From point A, any point in the range A to R would be an improvement for users but a loss for operators relative to point A. Alternatively a shift to a new technology, $M_{2}$ or $M_{3}$ , would keep the same level of $I_{NR}$ for the operator as A but increase $V_{E}$ to points D or E. 

Again, maximum $I_{\mathrm{NR}}$ is not necessarily the operator's sole or even primary decision rule. In addition to the clear trade-off between operator and users, many other issues may enter into the operator's decisions, as well as into decisions from a broader perspective. 

## 5.6 EXTENDING THE ANALYSIS

The simplified air transportation example illustrated a basic style of systematic analysis using a performance function. In this section we show how this analysis can be extended to explore many significant questions. 

## 5.6.1 Effects of Price Variations

Consider the option of varying pricing policy. We assume explicitly that carrier $i$ is free to vary his own price while other carriers stick with their original sets of options. (In practice this is not a valid assumption in most air travel markets. Prices are usually regulated, so there are restrictions on a carrier's ability to vary prices, and competition in the industry is so keen that other carriers will usually respond to changes in carrier $i$ 's services by changing their own options.) 

Figure 5.13 illustrates schematically the structure of the expanded analysis. Part a shows that $V_{D}$ varies as P is varied (we assume that there is no volume constraint, so $V_{E} = V_{D}$ ). Since the elasticity of demand with respect to price is almost always negative, as P increases ( $P^{3} > P^{2} > P^{1}$ ), demand will increase. In part b the total cost $C_{T}$ is compared with the various gross revenue curves corresponding to the different prices. If demand is inelastic with respect to price (elasticity between 0 and -1), an increase in price will cause an increase in gross revenue, so $I_{GR}^{III}$ corresponds to $P^{1}$ , $I_{GR}^{II}$ to $P^{2}$ , and so on. If, however, demand is elastic (elasticity less than -1), a price increase causes a decrease in gross revenue, so $I_{GR}^{I}$ corresponds to $P^{3}$ , $I_{GR}^{II}$ to $P^{2}$ , and so on. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/fc366feb-933b-4442-bcbf-4538c4ada340/0722860af488d1afc833302ef95c2b081eb4aa24d3a6949612bcc65ada9c6aca.jpg)



Figure 5.12 User-operator trade-offs.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/fc366feb-933b-4442-bcbf-4538c4ada340/42bfc79683e53c92a7da5f293395e7cd8eae649e32d7dc9c951041739bc3556c.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/fc366feb-933b-4442-bcbf-4538c4ada340/8290e8b654e0c36acb0ea46cbff41d98c54c98afef1f9d3249b3a4228dc7a170.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/fc366feb-933b-4442-bcbf-4538c4ada340/40fc141fcfe2c10c7e879d7c0f12c81d3b7bff2878e38f0cf79aacf7a2a424ee.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/fc366feb-933b-4442-bcbf-4538c4ada340/e3c18d83fcdc7a2a6b20caf30c62b14313d741e01a32a6a85c32f7b670a6980b.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/fc366feb-933b-4442-bcbf-4538c4ada340/b9904f18679cdd9039264f25aab21c8eb92a624a3d51d6b45eba510d9dd96cdd.jpg)



Figure 5.13 The effect of price variations.


For each price level a schedule frequency that maximizes $I_{NR}$ can be found, as illustrated in part c. If P is continuously variable, then a curve such as the dashed one can be developed. As shown in part d, this curve gives the maximum $I_{NR}$ that can be achieved for a given Q. (In some cases the value of P that maximizes $I_{NR}$ for a given Q can be derived analytically.) Conversely, for every price there is an optimal frequency, as shown in part e (the dashed line emphasizes that the shape of the curve depends on the characteristics of the specific situation). 

This analysis can be repeated for a number of technologies. The result suggested in part d can be generalized to show the maximum net revenue as a function of Q, assuming that the optimum P is used at every Q. 

Thus, in general, there will be a different $(P, Q)$ combination that maximizes net revenue for each technology. This fact has important implications for the analysis of alternative transportation options. It is usually difficult or impossible to know beforehand which combination of pricing and operating policies will be optimal for a given technology. Therefore it is usually poor practice to establish a single price or schedule beforehand and compare technologies at that combination. While some technologies will perform better than others at that operating point, it may well be that the relative rankings of the technologies will change significantly at other $(P, Q)$ combinations. For example, one technology may perform well at a low price and a relatively low service level, whereas another system performs well at a high price and a relatively high service level. Thus it is essential that any comparison of transportation options include systematic variations in operating and pricing options in combination. 

An alternative way of visualizing this is illustrated in figure 5.14. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/fc366feb-933b-4442-bcbf-4538c4ada340/e65128e3ef9f8edc5042b673cbe6bc00ce96d4332d922880322a8ed17653fe06.jpg)



Figure 5.14 Trade-offs among options. $\lambda = 1$ along the dashed portion of the curves.


Here emphasis is placed on showing how options can be explored in $(P, Q)$ space, to trace out isoquants of major impacts—for example, combinations of $(P, Q)$ that give the same levels of $I_{GR}$ , $C_{T}$ , $I_{NR}$ , or $V_{E}$ . 

Two cautions must be voiced here. First, the actual relationships depend significantly on the demand functions and parameter values. The magnitude of the price elasticity is particularly important—specifically, whether demand is elastic or inelastic with respect to price, that is, whether $E_{\mathrm{P}}(V_{\mathrm{D}})$ is greater than or less than one in absolute magnitude (see section 4.5.3). Second, most analyses usually encompass several different market segments, and the responses of each segment will be different. 

## 5.6.2 Effects of Parameter Variations

It is important to recognize the degree of uncertainty that may exist in key elements of any analysis. In this type of analysis key elements of uncertainty include the parameter values used in the performance and demand functions. Since uncertainty is always present in any analysis to a greater or lesser degree, it is important to recognize this and to do appropriate sensitivity analyses. A sensitivity analysis simply involves repeating the analysis for several alternative assumptions about the values of specified parameters. (Sometimes analytical relationships can be derived and used to estimate sensitivities.) 

In any analysis of transportation options, significant uncertainty may exist about the optimal choice of options due to uncertainty in underlying parameter values. It is essential that appropriate studies be done to explore how sensitive the choice may be to likely variations in key parameters. If the results of a preliminary analysis indicate that the choice of options may be particularly sensitive to the values assumed for one or several parameters, this suggests that in later, more detailed analyses, proportionately greater effort should be devoted to detailed modeling and analysis of these components of the transportation performance function. 

The methodology of a sensitivity analysis is particularly important for the planning of new systems. 

## 5.6.3 Example: Setting Transportation Research and Development Priorities

The methodology outlined here can be especially valuable in establishing desired performance levels for new systems, for a specific situation, or for establishing priorities for a national transportation research and development program. The methodology would be applied in the style of a sensitivity analysis. For example, alternative assumptions can be made about design targets for such variables as speed, payload, or unit costs. Then, based on explicit analyses of the type described in this chapter, the impacts associated with alternative design targets can be predicted. Final selection of design targets can then be made with knowledge of their consequences. 

Such a methodology was utilized in a study to assist in establishing R&D priorities for a particular class of urban transportation systems (Kocur et al. 1977). “Dual-mode” systems are medium-size buslike vehicles that carry 12–50 passengers and operate in two modes: under automated control on a special guideway, and under the manual control of a driver on local streets. Utilizing Milwaukee as a prototype city, this study explored systematically some 240 different transportation alternatives. Each alternative consisted of a choice of the following options: technology, network characteristics, station locations, link and station characteristics, and operating and pricing policies. Flows were predicted by means of an explicit demand model, a modified version of standard urban transportation planning computer models, and specifically designed performance models. Particular attention was given to systematic exploration of a wide range of operating policies, since dual-mode systems can be operated in a spectrum of ways, ranging from fixed routes and fixed schedules (like conventional buses) to on-demand almost-direct service from a few origins to one or a few destinations (like a shared taxi or carpool). 

The style of this type of analysis is illustrated in figure 5.15. Consider aircraft type $M_{3}$ as defined in table 5.4. A proposal is under consideration for developing a new aircraft, $M_{4}$ . This aircraft is expected to have an increased speed such that its productivity over the route studied in section 5.5 is expected to increase by 20 percent, from 0.25 trips per hour to 0.30 (that is, instead of four hours for one trip, the new vehicle would do it in 3.3 hours). If the increase in cost were also 20 percent, would this vehicle be an attractive option for the operator, and therefore for the manufacturer? Figure 5.15 compares the net revenue in this market for $M_{3}$ and $M_{4}$ . Clearly $M_{4}$ would be attractive: it produces a net revenue about 50 percent higher than that of $M_{3}$ . 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/fc366feb-933b-4442-bcbf-4538c4ada340/1f28422ca3dd569d64995c27dd21773de59dc6d9d738aae88c0a56d977d068b4.jpg)



Figure 5.15 Examination of R & D objectives for two technology options.


## 5.6.4 Incremental Analysis

The preceding analyses could be applied to an incremental analysis of variations from an existing, “base-case” condition $T^{0}$ . Thus, for any changes $\Delta T = (\Delta Q, \Delta P)$ , the corresponding changes can be calculated for $C_{T}$ , $V_{E}$ , $I_{GR}$ , and $I_{NR}$ . To compute $\Delta V_{E}$ , the methods for incremental analysis of demand described in section 4.6 could be used. This formulation is demonstrated in the exercises and in chapter 10. 

## 5.6.5 General Applicability of Systematic Analysis

The idea of a systematic analysis of a range of options applies at any scale of concern in transportation systems analysis. For example, similar concepts have been applied in the analysis of highway projects in developing countries. In a pioneering work Soberman (1966a, b) demonstrated that there are significant trade-offs among the design elements of a highway. He showed that various combinations of road width and pavement design yield different traffic capacities and different construction and operating costs, and he demonstrated that the relative consumptions of domestic capital, foreign exchange, and labor can be varied by varying these design parameters. (See also Lago 1968.) Roberts and Deweese (1971) extended this type of analysis to explore alternative alignments and demonstrated the trade-offs between user and operator impacts achievable by variations in alignments. More recently Moavenzadeh et al. (1975) and Hide et al. (1975) (see also Robinson 1975) have further extended this type of analysis to the analysis of trade-offs among initial road design, staged construction, and alternative maintenance strategies. 

## 5.7 STYLES OF ANALYSIS

The preceding sections have illustrated an analytical style in which the options are stated explicitly; prediction of impacts is done using a performance function and with an explicit equilibrium analysis; the options are varied systematically over a range; and trade-offs among different interests are explicitly considered. 

There are a number of ways in which analyses can be carried out using less explicit procedures. Each such style of analysis has advantages and disadvantages. The analyst should be aware of these in order to make an informed judgment about which style to utilize in a particular application. In this section we shall begin a discussion that will be extended in later chapters. 

## 5.7.1 The Load-Factor Assumption

In some applications it is customary to assume a load factor and use it to estimate impacts. For example, one might assume $\lambda = \lambda^{*}$ and thereby estimate equilibrium volume: 

$$
V _ {\mathrm{E}} = \lambda^ {*} V _ {\mathrm{C}}.\tag{5.36}
$$

Costs and revenues are then predicted as in explicit analysis. 

This is a strong assumption, specifically that, over the range of options being explored, $\lambda = V_{D}/V_{C}$ is constant (see, for example, figure 5.9b). This may be a reasonable approximation in some situations, especially when the range of variations in T is small, but it must be carefully examined in each case. 

Note that the assumption of a load factor is a shortcut to avoid explicitly stating a demand function and calculating equilibrium. An alternative method would be to utilize an incremental approach: given present demand volume $V_{D}^{0}$ , estimate the change $\Delta V_{D}$ for the change in options and, considering the change in capacity $\Delta V_{C}$ , find the new load factor explicitly: 

$$
\lambda^ {\prime} = \frac {V _ {\mathrm{D}} ^ {0} + \Delta V _ {\mathrm{D}}}{V _ {\mathrm{C}} ^ {0} + \Delta V _ {\mathrm{C}}}.\tag{5.37}
$$

## 5.7.2 Service Level as an Input

In an explicit analysis service levels are predicted as functions of the options T. Alternatively an analysis may begin with an explicit statement of goals in terms of desired service levels $S^{*}$ (for example, a maximum waiting time). The performance function can then in principle be used in a search procedure to specify the values of some or all of the options. 

For example, consider a desired level of waiting time, $t_{w}^{*}$ . From performance model I we have 

$$
t _ {\mathrm{w}} = \frac {1}{2 q}, \quad q = Q.\tag{5.38}
$$

The schedule frequency $Q^{*}$ that achieves this service level is then 

$$
\dot {Q} ^ {*} = \frac {1}{2 t _ {\mathrm{w}} ^ {*}}.\tag{5.39}
$$

In general, however, a careful distinction must be made between the search and prediction steps. With more complex models, and especially with explicit consideration of congestion and/or network effects, a full prediction of impacts together with explicit equilibration may produce an equilibrium service level different from the desired goal. For example, consider a case in which congestion effects cause q to be different from Q: 

$$
q = f (Q).\tag{5.40}
$$

Then $t_{\mathrm{w}}(Q^{*})$ may be significantly different from $t_{w}^{*}$ . Thus, while (5.39) produces a good suggestion for an initial schedule frequency, in the general case it does not necessarily specify the value of Q that will achieve the desired service level. 

Therefore, while it is often useful to transform an explicit performance model into a form useful for search, it is always important to test the output of search (for example, $Q^{*}$ ) by doing explicit prediction of impacts with the explicit performance function and equilibration. 

## 5.7.3 Desired Capacity as an Input

In explicit analysis available capacity is predicted as a function of the options. Alternatively an analysis may begin with an explicit statement of a desired or “design” capacity $V_{C}^{*}$ . Again the performance function can in principle be used in a search procedure. 

In performance model I 

$$
V _ {\mathrm{C}} = 2 w q, \qquad q = Q,\tag{5.41}
$$

so the schedule frequency that achieves this capacity is 

$$
Q ^ {*} = \frac {V _ {\mathrm{C}} ^ {*}}{2 w}.\tag{5.42}
$$

The same comments apply to the use of this search procedure as to one with service levels as an input: the values of the options resulting from search must be tested in full-scale prediction to see what impacts they actually achieve. 

## 5.7.4 The Supply Function

In chapter 1 we identified the type 3 relationship as the adjustment of options T by the operators. We indicated that for most purposes we would not model this relationship, preferring to vary the options T explicitly. Sometimes, however, it is desirable to model this relationship. In such a case a supply function can be derived. 

200 Transportation System Performance 


Table 5.5 Impacts of alternative strategies


<table><tr><td colspan="4">Strategy</td><td colspan="4"><eq>Impacts^a</eq></td></tr><tr><td><eq>T^i</eq></td><td>=</td><td colspan="2"><eq>(P^i, Q^i)</eq></td><td><eq>V_E</eq></td><td><eq>I_{GR}</eq></td><td><eq>C_T</eq></td><td><eq>I_{NR}</eq></td></tr><tr><td>11</td><td></td><td>$1.50</td><td>2</td><td>4.1</td><td>6.2</td><td>2.0</td><td>4.2</td></tr><tr><td>12</td><td></td><td></td><td>4</td><td>6.3</td><td>9.4</td><td>4.0</td><td>5.4</td></tr><tr><td>13</td><td></td><td></td><td>6</td><td>8.0</td><td>12.0</td><td>6.0</td><td>6.0</td></tr><tr><td>14</td><td></td><td></td><td>8</td><td>9.5</td><td>14.2</td><td>8.0</td><td>6.2</td></tr><tr><td>15</td><td></td><td></td><td>10</td><td>10.8</td><td>16.3</td><td>10.0</td><td>6.3</td></tr><tr><td>16</td><td></td><td></td><td>12</td><td>12.1</td><td>18.1</td><td>12.0</td><td>6.1</td></tr><tr><td>17</td><td></td><td></td><td>14</td><td>13.3</td><td>19.9</td><td>14.0</td><td>5.9</td></tr><tr><td></td><td></td><td><eq>Q_{OPT} =</eq></td><td>9.4</td><td>10.4</td><td>15.7</td><td>9.4</td><td>6.3</td></tr><tr><td>21</td><td></td><td>$2.00</td><td>2</td><td>2.7</td><td>5.4</td><td>2.0</td><td>3.4</td></tr><tr><td>22</td><td></td><td></td><td>4</td><td>4.1</td><td>8.1</td><td>4.0</td><td>4.1</td></tr><tr><td>23</td><td></td><td></td><td>6</td><td>5.2</td><td>10.4</td><td>6.0</td><td>4.4</td></tr><tr><td>24</td><td></td><td></td><td>8</td><td>6.2</td><td>12.3</td><td>8.0</td><td>4.3</td></tr><tr><td>25</td><td></td><td></td><td>10</td><td>7.1</td><td>14.1</td><td>10.0</td><td>4.1</td></tr><tr><td>26</td><td></td><td></td><td>12</td><td>7.9</td><td>15.7</td><td>12.0</td><td>3.7</td></tr><tr><td>27</td><td></td><td></td><td>14</td><td>8.6</td><td>17.2</td><td>14.0</td><td>3.2</td></tr><tr><td></td><td></td><td><eq>Q_{OPT} =</eq></td><td>6.6</td><td>5.5</td><td>10.9</td><td>6.6</td><td>4.4</td></tr><tr><td>31</td><td></td><td>$2.50</td><td>2</td><td>1.9</td><td>4.8</td><td>2.0</td><td>2.8</td></tr><tr><td>32</td><td></td><td></td><td>4</td><td>2.9</td><td>7.3</td><td>4.0</td><td>3.3</td></tr><tr><td>33</td><td></td><td></td><td>6</td><td>3.7</td><td>9.3</td><td>6.0</td><td>3.3</td></tr><tr><td>34</td><td></td><td></td><td>8</td><td>4.4</td><td>11.0</td><td>8.0</td><td>3.0</td></tr><tr><td>35</td><td></td><td></td><td>10</td><td>5.0</td><td>12.6</td><td>10.0</td><td>2.6</td></tr><tr><td>36</td><td></td><td></td><td>12</td><td>5.6</td><td>14.0</td><td>12.0</td><td>2.0</td></tr><tr><td></td><td></td><td><eq>Q_{OPT} =</eq></td><td>5.0</td><td>3.3</td><td>8.3</td><td>5.0</td><td>3.3</td></tr><tr><td>41</td><td></td><td>$3.00</td><td>2</td><td>1.5</td><td>4.4</td><td>2.0</td><td>2.2</td></tr><tr><td>42</td><td></td><td></td><td>4</td><td>2.2</td><td>6.6</td><td>4.0</td><td>2.6</td></tr><tr><td>43</td><td></td><td></td><td>6</td><td>2.8</td><td>8.5</td><td>6.0</td><td>2.5</td></tr><tr><td>44</td><td></td><td></td><td>8</td><td>3.4</td><td>10.1</td><td>8.0</td><td>2.1</td></tr><tr><td>45</td><td></td><td></td><td>10</td><td>2.8</td><td>11.5</td><td>10.0</td><td>1.5</td></tr><tr><td></td><td></td><td><eq>Q_{OPT} =</eq></td><td>4.0</td><td>2.2</td><td>6.6</td><td>4.0</td><td>2.6</td></tr><tr><td>51</td><td></td><td>$3.50</td><td>2</td><td>1.2</td><td>4.1</td><td>2.0</td><td>2.1</td></tr><tr><td>52</td><td></td><td></td><td>4</td><td>1.8</td><td>6.1</td><td>4.0</td><td>2.1</td></tr><tr><td>53</td><td></td><td></td><td>6</td><td>2.2</td><td>7.8</td><td>6.0</td><td>1.8</td></tr><tr><td>54</td><td></td><td></td><td>8</td><td>2.7</td><td>9.3</td><td>8.0</td><td>1.3</td></tr><tr><td>55</td><td></td><td></td><td>10</td><td>3.0</td><td>10.6</td><td>10.0</td><td>0.6</td></tr><tr><td></td><td></td><td><eq>Q_{OPT} =</eq></td><td>3.3</td><td>1.2</td><td>5.4</td><td>3.3</td><td>2.2</td></tr><tr><td>61</td><td></td><td>$4.00</td><td>2</td><td>0.9</td><td>3.8</td><td>2.0</td><td>1.8</td></tr><tr><td>62</td><td></td><td></td><td>4</td><td>1.4</td><td>5.7</td><td>4.0</td><td>1.7</td></tr><tr><td>63</td><td></td><td></td><td>6</td><td>1.8</td><td>7.3</td><td>6.0</td><td>1.3</td></tr><tr><td>64</td><td></td><td></td><td>8</td><td>2.2</td><td>8.7</td><td>8.0</td><td>0.7</td></tr><tr><td>65</td><td></td><td></td><td>10</td><td>2.5</td><td>10.0</td><td>10.0</td><td>0</td></tr><tr><td></td><td></td><td><eq>Q_{OPT} =</eq></td><td>2.8</td><td>1.1</td><td>4.6</td><td>2.8</td><td>1.8</td></tr></table>


$^{a}$ In units of 1,000, rounded to one decimal place. 


To derive a supply function from a performance function it is necessary to have an explicit decision rule D that describes the objectives of the operator in completely operational terms. Then we can use the following procedure: 

1. Select a set of alternative strategies $T^{i}$ that the operator is assumed to consider. 

2. Using the full set of prediction models (including demand, performance, travel-market equilibration, and activity shifts), predict the impacts $I^{i}$ of each strategy $T^{i}$ . 

3. Apply the decision rule D to predict which strategy $T^{*}$ the operator will pick. 

As an example, consider the results shown in table 5.5. Assume the operator has the decision rule, “maximize net revenue.” Then assume that a regulatory agency is setting price. We might derive from table 5.5 a supply function that predicts the frequency $Q_{OPT}$ the operator would choose to offer as a function of this externally set price, and thus the capacity $V_{C}$ (proportional to $Q_{OPT}$ ) that would be available at each level of price. Figure 5.16 shows $Q_{OPT}$ as a function of price. This is the conventional supply function. Also shown is $I_{\mathrm{NR}}(Q_{\mathrm{OPT}})$ , a function of price also. 

## Note these important points:

1. Travel-market equilibration has to be done in order to develop each point of the supply function. 

2. The supply function depends explicitly on the choice of decision rule D. 

3. The service-function aspect of the performance function shows service as a function of volume for a fixed choice of T and always has service levels constant or decreasing (for example, travel time increasing) as volume increases. However, the supply function shows a family of choices of T and can have service levels increasing as volume increases. (In figure 5.16 service level is decreasing as price is increased. The shape of the relationship depends in a complex way on both demand and performance functions and on parameter values.) 

This is important and complex topic; indeed, the difference between a performance function and a supply function is often confused. For further discussion see Manheim (1978a) and also volume 2. 

## 5.8 CONCLUSIONS

We have demonstrated a basic approach to representing transportation system performance and analyzing transportation options. A simplified formulation of the decisions faced by an air transportation operator was used as an example. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/fc366feb-933b-4442-bcbf-4538c4ada340/bd5f83967d9f20a5e5514073fcfcc1036f0192650035fc183755a42a36912c03.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/fc366feb-933b-4442-bcbf-4538c4ada340/2f3463fec17c2f5580beec4a2bc2bcc89b47d734ad4a406461a44b5bdf37198a.jpg)



Figure 5.16 The supply function.


## 5.8.1 The Basic Approach

The primary elements of this approach are: 

1. representing the transportation system explicitly by a performance function so that both service levels and resources consumed are functions of the options and of the volume served; 

2. comparison of alternative options by explicit determination of equilibrium volumes with an explicit demand function; 

3. evaluation of impacts on operator and user in terms of equilibrium volumes, service levels, resources consumed, and monetary impacts such as costs and revenues; and 

4. systematic variation of options to trace out trade-offs among various impacts and various interests. 

The example demonstrated several key points: 

1. There are significant trade-offs achievable between resources consumed and levels of service; for example, by varying frequency, higher service levels can be achieved at greater costs. 

2. Actual volume at equilibrium is often very different from capacity volume; put another way, load factor is a variable and not a constant. 

3. Different transportation systems and different ways of operating a system will capture different portions of the market, that is, different values of equilibrium volume. 

4. For each system the actual volumes, resources consumed, costs, and gross and net revenues will depend on how the system is operated. 

5. The best way to operate a system—for example, the best schedule frequency—will generally be different for each system. 

6. The actual volume at which a system performs best will generally be different for each system. 

7. There will be different combinations of pricing and operating policies for which each system performs best. 

8. There are often important trade-offs between user and operator impacts. 

9. Uncertainty about values of performance or demand parameters may significantly affect the choice of options because of the influence of those parameters on costs and revenues. 

These observations have the following general implications for the analysis of alternative options and especially of different transportation systems: 

1. A range of options should be systematically explored for each system. 

2. An explicit equilibrium analysis should be done, with an explicit demand function. 

3. A range of actual volumes should be considered. 

4. The trade-offs between operators and users should be explicitly considered. 

5. Pricing and operating options should be systematically explored in combination. 

6. Systematic sensitivity studies should be done to identify effects of uncertainties in key parameters. 

While these principles apply generally, in each specific situation enough may be known from prior experience to allow substantial shortcuts in the analysis (such as assuming a load factor or setting a service-level target). 

The preceding sections have illustrated an analytical approach that might seem to imply a rigid structure leading invariably to the optimal policy an operator should follow. This is not our intent. We have described a style of analysis, not a rigid prescription. Many issues in a particular situation may cause an analyst to make significant simplifications. These are acceptable, provided the analyst understands the limitations thereby imposed on his results. In taking such shortcuts, however, the analyst must carefully weigh any resulting limitations on the usefulness of his analysis. 

The most important aspect of the approach presented here is explicit representation of service levels together with resources consumed. Characterizing a transportation system in terms of its level-of-service and resource-consumption trade-offs is fundamental to understanding system performance. 

## 5.8.2 Looking Ahead

Performance model I, while simple, has helped to establish the types of variables and relationships that must be included in such models and the ways in which performance models can be used in an analysis. In order to analyze service levels and resource consumption in more realistic and complex transportation systems, more detailed performance models will generally be required. 

To form a basis for deciding which factors should be included explicitly, which relationships should be modeled in detail, and which can be approximated in specific situations, we must begin to delve more deeply into the various elements of a transportation system. While the core of most performance analyses is the movement of vehicles through space and time, we must also consider a number of other elements: the various transportation options are often interrelated, can have widely varying implementation time scales, and may exhibit indivisibilities; the effective speed of a vehicle is influenced by many factors such as grades and en route stops; vehicle interactions produce congestion, which often significantly affects system performance; and the services provided to different markets in a large system interact in complex ways. 

The details of elements such as these significantly affect the performance of particular transportation systems in particular contexts. The actual resource and service relationships may vary greatly from one context to another. The analyst must understand each of these elements, their causes, their effects on service levels and resource consumption, and alternative ways in which they can be modeled. 

Chapter 6 will examine the vehicle cycle and some important economic concepts. Chapter 7 will consider the dimensionalities of options, congestion and its effects, and the spatial and temporal structure of services. Detailed examination of these and many other elements influencing system performance will, however, be deferred to volume 2. 

To understand these elements fully requires substantial additional background in a number of areas of theory and methods, including statics; kinematics; traffic flow theory; the physics and chemistry of such environmental aspects as air pollution, noise, and energy consumption; simulation, queuing theory, optimization, and other modeling methods that are applied to the analysis of performance of particular types of systems; and other areas of engineering, systems analysis, management, accounting, finance, labor relations, and so on, that bear on the understanding of system performance. These important topics are usually covered in transportation engineering or similar courses. They are not, however, in our view fundamental to understanding system performance, and so are not discussed in this volume. In volume 2, in a more detailed treatment of system performance, the relationships of these traditional areas of study to the concepts laid out in this volume will be discussed. 

## 5.9 SUMMARY

Transportation systems are complex and include many components: vehicles, guideways, stations, control and communication systems, maintenance systems, and management organizations and systems. 

The objective of this chapter has been to describe the key features that should be considered in developing an analysis of any particular system. 

Many options are available for changing any given transportation system. In general, both service levels (performance) and resources consumed vary as the options are varied and as the actual volume of usage of the system varies. A model of transportation system performance must explicitly represent these relationships. 

The actual volume is also a function of the service levels offered, as indicated by the demand function. Thus for any specified options the actual resources consumed and the actual service level can be found only after an equilibration of service level and volume through the demand function. 

Varying operating and other options can produce a wide range of variation in resources consumed and services produced for any given transportation system. As a consequence of this range of variation, different combinations of options can have significantly different impacts on various interests. Finding the best operating regime for each technology requires systematic analysis of a range of options and equilibration with explicit demand functions. 

Characterizing a transportation system in terms of its service-level and resource-consumption trade-offs is fundamental to understanding system performance. 

## TO READ FURTHER

The literature of technology is vast, but seminal material is sparse. New texts by Morlok (1978) and Daganzo (1978b) are useful, as is the proceedings volume edited by Florian (1978). See also Hay (1961), Haase and Holden (1964), Soberman (1966a, b, c), DeSalvo and Lave (1968), Morlok (1968), DeSalvo (1969), Bhatt (1971), Rea and Miller (1973), Simpson (1974), and Anderson (1977). 

For an example of the policy consequences of the concepts presented in this chapter see UMTA (1976a) and Manheim (1977b). 

For some of the practical problems in predicting service levels see, for example, Branston (1973), Johnson (1976), Terziev and Roberts (1976), Chiang and Roberts (1977), Samuelson and Lerman (1977), and Wilson, Roberts, and Kneafsey (1977). 

## EXERCISES

5.1(E) In exercise 1.4 we introduced the problem of deciding optimal train operating strategies. The capacity volume is $V_{C} = LQ$ , and the general cost function is (after Martland 1977) 

$$
C _ {\text { TRAIN }} (Q, L) = \alpha_ {1} D + \alpha_ {2} L \left(\frac {D}{v} + \frac {1 2}{Q}\right) + \alpha_ {3} D L ^ {2},
$$

$$
C _ {\mathrm{T}} (Q, L) = Q C _ {\mathrm{TRAIN}},
$$

where 

$Q =$ frequency (trains per day), $L =$ train length (cars per train), $C_{\mathrm{TRAIN}} =$ cost per train, $C_{\mathrm{T}} =$ total daily cost, $D =$ round-trip distance, $v =$ average speed, $\alpha_{1} =$ crew costs per train-mile, $\alpha_{2} =$ car costs per hour per car, $\alpha_{3} =$ train length costs, $P =$ freight rate (price per car per one-way trip). 

The first term represents labor costs for train operation, the second and third terms represent the costs per car for over-the-road travel time $(D/v)$ and for waiting time between trains $[(1/2Q) \times 24$ hours per day], and the last term represents those aspects of operating costs that go up more than proportionately to train length. 

The demand function is 

$$
V _ {\mathrm{D}} = \beta_ {1} \left(\frac {Q}{Q _ {0}}\right) ^ {\beta_ {2}}.
$$

Consider this situation: D = 200 miles, $Q^{0} = 2$ , $L^{0} = 90$ , $V_{D}^{0} = 180$ , P = 15, $\alpha_{1} = 2.40$ , $\alpha_{2} = 0.20$ , $\alpha_{3} = 2 \times 10^{-5}$ , $\beta_{1} = 180$ , $\beta_{2} = 0.5$ . a. Determine $C_{T}$ , $I_{GR}$ , $I_{NR}$ , $V_{E}$ , and $\lambda$ as functions of Q and L. Consider frequencies between 2 and 8 and a reasonable range of train lengths, including those lengths, $L_{OPT}$ , that provide just sufficient capacity to meet the demand. Display useful results in graphs and discuss (include $L_{OPT}$ ). 

b. What policies would you recommend from the operator's perspective? From the user's perspective? 

c. Consider the assumption $\beta_{2}=0$ . Predict impacts selectively. 

What would you recommend, and why? 

d. Explore the sensitivity of the results to alternative values of $\beta_{2}$ (use $\beta_{2}=0,0.8$ ) and cost (use $\pm10$ percent on all parameters). Discuss. 

e. Expand your previous results by considering a range of freight rates. 

f. A search strategy that is often proposed is as follows (see, for example, Martland 1977): Assume that the operator's objective is to minimize costs. For a given $Q$ , $C_{\mathrm{T}}$ is minimized by taking $L = L_{\mathrm{OPT}}$ , where $L_{\mathrm{OPT}}$ is found by setting $V_{\mathrm{C}} = V_{\mathrm{D}}$ : 

$$
L _ {\mathrm{OPT}} = \frac {V _ {\mathrm{C}}}{Q} = \frac {V _ {\mathrm{D}} (Q)}{Q}.
$$

When $\beta_{2}=0$ , so that $V_{D}=\beta_{1}$ , we can find the $Q_{OPT}$ for minimum total cost by calculus: 

$$
Q _ {\mathrm{OPT}} = \sqrt {\frac {\alpha_ {3}}{\alpha_ {1}} V ^ {2} + \frac {1 2 \alpha_ {2}}{\alpha_ {1} D} V}.
$$

Verify this result. Then calculate $Q_{OPT}$ , $C_{T}$ , $I_{GR}$ , and $I_{NR}$ for a range of values. Compare with previous results, especially for parts a and c. Discuss. What are the implications of using this type of search strategy? 

5.2(E) In the example in section 5.4, the alternative technologies all provided the same level of service at a particular frequency. This happens to be true at the current state of jet aircraft technology but is unlikely to be true in general. What would be the implications if the speeds of the three aircraft were different? Sketch a revised version of Figure 5.11. 

5.3(C) While many transportation studies require much more elaborate approaches than that reflected in performance model I, there is a surprisingly large number of policy-oriented studies in which the methodology employed is not much more detailed. It is useful to examine a particular transportation analysis and reformulate it (if necessary) in terms of the methodology described here, in order to better understand both the methodology and the reported policy analysis. Some suggestions (there are many others in the literature): 

1. A choice of shipping system technologies (Gilman 1977). 

2. An analysis of the economic potential of specialized wool shipping services (Chudleigh 1975). 

3. Comparative analyses of urban transit options (Meyer, Kain, and Wohl 1965, Bhatt 1976, Boyd, Asher, and Wetzler 1976; see also Vuchic 1976, Manheim 1977b). 

5.4(P) Select a transportation performance model for which documentation is available. 

a. Identify the key elements of the model: 

i. the general class of problems that the model is designed to address, 

ii. the options T, 

iii. the service variables S, 

iv. the cost variables C, 

v. the volumes V, 

vi. the environmental variables E, 

vii. other key data items (parameters) required, 

viii. the inputs required to operate the model, 

ix. the outputs produced by the model, 

x. the general logic of the model, including key assumptions, major limitations, and how it is related to demand models and equilibration. 

b. Discuss the model critically: what are its strengths and its weaknesses? 

5.5(P) Select an area of transportation system performance for potential development of a performance model. Prepare a preliminary design of a model and a User's Manual, that is, a document stating how the model is to be used. Include the following: 

a. an overview of the model, clearly spelling out the key elements listed in exercise 5.4a; 

b. a critical review of the relevant literature (where appropriate, specific references should be given to indicate where you have followed an approach taken by someone else or have explicitly decided to take a different approach); 

c. a general flow chart of the model's logic, a flow chart showing relations to other models, a glossary of variable names and symbols, and a concise list of needed data. 

You should, of course, include a clear description of options, parameters, and service, volume, resource, cost, and other impact variables. 

The manual should be arranged in a usable form; it should not resemble a stream-of-consciousness “core dump.” Some feeling for areas of uncertainty in model structure should be given, and you should also discuss how one might do sensitivity studies of key areas of uncertainty with the model. 

5.6(C) The discussions in this chapter have all assumed that the operator's goal is to maximize net revenue, $I_{\mathrm{NR}}$ . Formulate other possible operator goals and discuss how they might affect the results that have been presented. For example, consider the profit ratio $I_{\mathrm{NR}} / C_{\mathrm{T}}$ and the return on sales $I_{\mathrm{NR}} / V_{\mathrm{E}}$ (see Kneafsey 1974). 

5.7(C) We have limited ourselves to a single market segment in this chapter. How might the analysis be modified by explicit inclusion of two market segments (with different demand-function parameters)? How about five market segments? Five hundred? 

5.8(E) Consider the following demand and cost functions: 

$$
\begin{array}{l} {C _ {\mathrm{T}} = a Q,} \\ {V _ {\mathrm{D}} = \beta_ {0} P ^ {\beta_ {1}} Q ^ {\beta_ {2}}, \qquad \beta_ {2} > 0, \quad \beta_ {1} <   0.} \end{array}
$$

a. Assume that the operator's decision rule is to maximize net revenue. Show that, for an externally specified price (set by a regulatory agency perhaps), the operator's supply function is, for $\beta_{2} < 1$ , 

$$
Q _ {\mathrm{OPT}} = \left(\frac {a}{\beta_ {0} \beta_ {2} P ^ {\beta_ {1} + 1}}\right) ^ {1 / (\beta_ {2} - 1)}
$$

(Ignore possible capacity restraints, congestion effects, and the effects of network structure and travel-market equilibration.) Why must $\beta_{2}$ be less than one for this relationship to hold? 

b. We have 

$$
\frac {\partial Q _ {\mathrm{OPT}}}{\partial P} = - Q _ {\mathrm{OPT}} \left(\frac {\beta_ {1} + 1}{P (\beta_ {2} - 1)}\right).
$$

Under what conditions would $Q_{OPT}$ increase and under what conditions would it decrease with increasing P? Discuss the implications for operator behavior. 

c. Consider some of the factors that were ignored in part a. What effects do you think each would have on the derived relationship of $Q_{OPT}$ to P? 

d. Explore alternative decision rules for the operator and their implications for the supply function $Q_{\mathrm{OPT}}(P)$ . 

5.9(E) Refer to table 5.6, used in deriving the supply function of section 5.7 on the basis of the decision rule $\mathcal{D}_1 =$ "maximize net revenue." 

a. Considering only the strategies shown in that table, sketch supply functions for these alternative decision rules: 

i. $D_{2} = "maximize capacity"$ (assume that capacity is proportional to Q, that is, $V_{C} = 2wQ$ ); 

ii. $D_{3}$ = "maximize the ratio of net revenue to total cost"; 

iii. $D_{4}$ = "maximize capacity subject to a ratio of net revenue to total cost of at least 0.15"; 

iv. $D_{5}$ = “maximize volume served subject to a ratio of gross revenue to cost of at least 1.25.” 

b. Compare the results and discuss. 

c. How might the results be different if: 

i. congestion effects occurred? 

ii. the price elasticity were inelastic? 

iii. the demand function were linear or multinomial logit in $(P, Q)$ , rather than product-form? 

5.10(E) The supply function in section 5.7 was generated from the relationships in exercise 5.8, with the following parameter values: 

$$
a = 1, 0 0 0, \quad \beta_ {0} = 5, 0 0 0, \quad \beta_ {1} = - 1. 5, \quad \beta_ {2} = + 0. 6.
$$

Develop $Q_{\text{OPT}}(P)$ for $P$ in the range $1–$4 for these alternative sets of values of the parameters (all parameters not specifically mentioned stay at base-case values): 

$$
\begin{array}{l l} \text {a. Case I,} a = 1, 2 0 0; \\ \text {b. Case II,} \beta_ {0} = 3, 7 8 9, & \beta_ {1} = - 1. 1; \\ \text {c. Case III,} \beta_ {0} = 3, 0 7 8, & \beta_ {1} = - 0. 8; \\ \text {d. Case IV,} \beta_ {0} = 7, 1 5 5, & \beta_ {1} = - 1. 5, \quad \beta_ {2} = + 0. 4; \\ \text {e. Case V,} \beta_ {0} = 3, 4 9 4, & \beta_ {1} = - 1. 5, \quad \beta_ {2} = + 0. 8. \end{array}
$$

(Note that the values of $\beta_0$ are such that $V_{\mathrm{E}} = 5,180$ at $Q = 6$ and $P = \$2$ .) Plot, compare, and discuss. 

5.11(E) The treatment of the capacity restraint in this chapter has been relatively simple. A more realistic assumption is that the availability of a seat—that is, the load factor—has an influence on demand given by $x = f(\lambda)$ , where $\lambda$ is the load factor of the flight (average over a particular route) and x is the percentage of available flights over this route that were fully booked and closed to sale prior to departure. How would you modify the analysis of this chapter to incorporate such a function? One air carrier reports data (Borman 1977, Appendix D) that allows estimation of the following relationship: 

$$
x = \left\{ \begin{array}{l l} 0, & \lambda <   0. 3 7, \\ 1 8 6 (\lambda - 0. 3 7), & 0. 3 7 \leq \lambda \leq 0. 9 1, \\ 1 0 0, & \lambda > 0. 9 1. \end{array} \right.
$$

5.12(E) Various relationships can be derived to guide a systematic analysis of the options. For example: 

1. for a given frequency, the fare that maximizes net revenue is the P such that $E_{P}(V) = -1$ , if such a fare exists; 

2. for a given fare, the frequency that maximizes net revenue is Q such that 

$$
\frac {\partial V}{\partial Q} = \frac {1}{P} \frac {\partial C _ {T}}{\partial Q}
$$

or, alternatively, 

$$
E _ {Q} (V) = \frac {C _ {\mathrm{T}}}{P V} E _ {Q} (C _ {\mathrm{T}});
$$

3. for a constant level of $I_{NR}$ , Q and P can be varied together as 

$$
P = \frac {- Q}{E _ {Q} (V)} [ 1 + E _ {P} (V) ] + \frac {C _ {\mathrm{T}}}{V} \frac {E _ {Q} (C _ {\mathrm{T}})}{E _ {Q} (V)}
$$

or 

$$
Q = \frac {(C _ {\mathrm{T}} / V) E _ {Q} (C _ {\mathrm{T}}) - P E _ {Q} (V)}{1 + E _ {P} (V)}.
$$

Although results such as these are useful, they do have important limits: they assume a single market segment and ignore the capacity constraint. (For extensions and examples see Simpson 1974, Lion and Opperman 1977.) 

a. Verify these results. 

b. Discuss their limitations: How can they be useful? What are the limits and corresponding issues? 

c. For the case $C_{T} = kQ$ , the above results 1–3 become: 

4. $E_{P}(V) = -1$ ; 

5. $\frac{\partial V}{\partial Q}=\frac{k}{P};$ 

$$
6. P = \frac {Q}{E _ {Q} (V)} \left[ \frac {k}{V} - 1 - E _ {P} (V) \right]
$$

or 

$$
Q = \frac {P E _ {Q} (V)}{(k / V) - 1 - E _ {P} (V)}.
$$

Using these results, develop a plot of constant values of $I_{NR}$ for the example in section 5.5. 

5.13(E) One value of the load factor concept is that it is sometimes a useful surrogate for the relative profitability of a system, from the viewpoint of the operator. The revenues are related to the actual volume $V_{E}$ , whereas the costs are more directly related to the available volume $V_{C}$ . Thus operators can often establish a desired load factor as a target to achieve profitability. 

The concept of the break-even load factor, $\lambda_{B}$ , expresses this viewpoint: $\lambda_{B}$ is the minimum load factor required for break-even operations. 

The value of $\lambda_{B}$ can be determined as follows for the example of section 5.5. For a particular price P, the gross revenue $I_{GR}$ from users of the system will be 

$$
I _ {\mathrm{GR}} = P V _ {\mathrm{E}}.
$$

The total costs will be, as previously, 

$$
C _ {\mathrm{T}} = a R = a Q \frac {2 d}{v}.
$$

For break-even operations 

$$
I _ {\mathrm{GR}} - C _ {\mathrm{T}} = 0.
$$

Thus the break-even volume $V_{BE}$ would satisfy 

$$
P V _ {\mathrm{BE}} = C _ {\mathrm{T}},
$$

and the break-even load factor would be the load factor at this equilibrium volume: 

$$
\begin{array}{r} \lambda_ {\mathrm{BE}} = \frac {V _ {\mathrm{BE}}}{V _ {\mathrm{C}}} \\ = \frac {C _ {\mathrm{T}}}{P V _ {\mathrm{C}}}. \end{array}
$$

a. Show that for this case 

$$
\lambda_ {\mathrm{BE}} = \frac {k}{P w},
$$

$$
\text { where } k \equiv a d / v.
$$

b. Discuss the relationship between k and $\lambda_{BE}$ . 

c. Is $\lambda_{\mathrm{BE}}$ a constant or does it vary with $Q$ or with other elements of the options $\mathbf{T}$ ? 

5.14(E) Consider an operator whose objective is to maximize net revenue. If there is no capacity constraint, then the Q for maximum $I_{NR}$ can be found by elementary calculus, from the cost and demand functions. 

Given the cost function $C_{\mathrm{T}}(Q)$ and the demand function $V_{\mathrm{D}}(Q)$ , the point of maximum net revenue can be found by setting 

$$
\frac {\partial I _ {\mathrm{NR}}}{\partial Q} = 0
$$

or 

$$
\frac {\partial I _ {\mathrm{GR}}}{\partial Q} = \frac {\partial C _ {\mathrm{T}}}{\partial Q},
$$

provided the appropriate conditions on the second derivatives are also met: 

## 214 Transportation System Performance

$$
\frac {\partial^ {2} I _ {\mathrm{NR}}}{\partial Q ^ {2}} \leq 0
$$

or 

$$
\frac {\partial^ {2} I _ {\mathrm{GR}}}{\partial Q ^ {2}} \leq \frac {\partial^ {2} C _ {\mathrm{T}}}{\partial Q ^ {2}}.
$$

Consider the case where 

$$
C _ {\mathrm{T}} = a _ {0} + a _ {1} Q.
$$

Then 

$$
\frac {\partial C _ {\mathrm{T}}}{\partial Q} = a _ {1}
$$

and 

$$
\frac {\partial^ {2} C _ {\mathrm{T}}}{\partial Q ^ {2}} = 0.
$$

Show that the values of Q that maximize net revenue are as follows: 

a. Case I: $V = \alpha Q^{\beta}$ : 

$$
Q _ {\mathrm{OPT}} = \left(\frac {a _ {1}}{\alpha \beta P}\right) ^ {1 / (\beta - 1)}, \quad 0 <   \beta <   1.
$$

b. For Case I, what happens if $\beta > 1$ ? 

c. Case II: $V = \frac{\alpha_1}{\alpha_2 + (\alpha_3 / Q)}$ : 

$$
Q _ {\mathrm{OPT}} = \frac {- \alpha_ {3} \pm \sqrt {\alpha_ {1} \alpha_ {3} P / a _ {1}}}{\alpha_ {2}}.
$$

d. Case III: $V = \frac{\alpha}{1 + \gamma e^{\beta Q}}$ : 

$$
Q _ {\mathrm{OPT}} = \frac {\ln x}{\beta}, \quad x = \frac {\rho - 1 \pm \sqrt {\rho (\rho - 1)}}{\gamma}, \quad \rho = \frac {P \alpha \beta}{2 a _ {1}}.
$$

# Understanding Performance Functions I: The Vehicle Cycle and the Analysis of Cost Functions

## 6.1 INTRODUCTION

Chapter 5 introduced the basic conceptual structure we shall utilize in trying to understand the performance of transportation systems. That structure begins with the following premises: 

1. We are interested in both the service provided to the user and in the resources consumed: service because this is what influences demand and thus the benefits and revenues of a system; resources consumed because these are the costs and other undesirable consequences (air quality degradation, energy consumption) of a system. 

2. We are interested in how, for a particular system specification, the service levels provided and resources consumed vary with the volume using the system, especially with respect to the influence of congestion effects. 

3. We are also interested in how varying the options—the system specification—can change the performance of a system as reflected in service levels and resources consumed. 

To express these concepts symbolically we represent the transportation system by a performance function $\phi$ in which two sets of “outputs” are important: the resources consumed, R, and the service levels provided, S. Both S and R depend on the set of options T specifying the characteristics of the system, and both are influenced by the actual volumes using the system, V. Thus S and R are interrelated in ways that significantly influence decision making. 

Our objective in this chapter and chapter 7 is to begin a more detailed examination of the phenomena that underlie transportation performance functions. As noted in section 5.8.2, there are many topics that might be discussed; we have chosen to explore in these two chapters those concepts that in our view are fundamental to understanding transportation system performance. 

A key feature of transportation is the spatial and temporal structure of a system. This structure can affect the service-resource trade-offs in complex ways. From the perspective of the user, the key issue 

is the service level offered for the possible paths between a particular origin and possible destinations; different users perceive the system differently. From the perspective of the operator, the key issue is the overall performance of a system of services, in terms of revenues received and resources consumed. 

A system in general consists of fleets of vehicles moving over networks of facilities. The vehicles can have complex trajectories over space and time, as suggested by figure 5.4, and the vehicles and facilities can interact in several ways, as suggested by figure 5.3. Thus the structure of a transportation system, and especially the patterns of services offered to users and of impacts on the operators, may be quite complex. 

To dissect this complexity we shall begin our analysis by looking at the vehicle cycle—the performance of a vehicle over its total annual (or daily) operational pattern (section 6.2). We shall then examine some basic economic concepts that are especially useful in a systematic analysis of performance functions (sections 6.3–6.6). In sections 6.7 and 6.8 we shall apply these concepts to the analysis of vehicle cycles and see the implications in several examples. 

Vehicles do not operate in isolation, however, but over networks of facilities. Vehicles affect one another and are affected by facilities and by demand in a set of phenomena we call congestion. Sections 7.2 and 7.3 will explore various types of congestion and their implications for system performance. 

In chapter 1 we noted that changes in a number of types of options can be considered: technologies available, fixed facilities and network structure, vehicles, and organizational and operating strategies, including specifically the assignment of vehicles and personnel to routes, schedules, and pricing policies. The performance of a system depends on the system specification in terms of all of these options. Therefore, in any analysis of alternative specifications it is important to systematically explore all dimensions of T and to trace out impacts on different interests. Sections 7.4–7.6 will explore the implications of this dimensionality of options, especially the implications of their different time frames and indivisibilities and their interrelation with congestion. 

In section 7.7 we shall return to our basic theme of system performance in space and time and, through the concept of an operating plan, suggest how all of these factors interrelate to determine system performance. 

## 6.2 THE VEHICLE CYCLE AND ITS COMPONENTS

In most transportation systems (except those using continuous media such as pipelines or conveyors) the vehicle plays a major role. For this reason, understanding the anatomy of the vehicle's movements over time and space is very important. We shall look first at the cycle of a single vehicle; then in chapter 7 we shall explore the composite performance of a fleet of vehicles. 

## 6.2.1 A Trucking Example

In their study of truck operators who own their own vehicles ("owner-operators") Wyckoff and Maister (1975) developed the following estimate for a truck operator's cost function (see section 6.5.2): 

$$
C _ {\mathrm{T}} = 3 6, 0 0 0 + 0. 2 4 m _ {\mathrm{T}},\tag{6.1}
$$

$$
C _ {\mathrm{tmL}} = \frac {C _ {\mathrm{T}}}{\gamma w m _ {\mathrm{T}}},\tag{6.2}
$$

where 

$$
m _ {\mathrm{T}} = \text {total mileage driven per year},
$$

$$
w = \text { vehicle   payload },
$$

$\gamma =$ fraction of total mileage traveled on a loaded basis, 

$$
C _ {T} = \text { total   cost   per   year },
$$

$C_{tmL}$ = average cost per loaded ton-mile (that is, per ton-mile carried). 

Taking w = 20 tons and $\gamma = 0.8$ , we have 

$$
C _ {\mathrm{tmL}} = \frac {3 6 , 0 0 0}{0 . 8 (2 0) m _ {\mathrm{T}}} + \frac {0 . 2 4}{(0 . 8) (2 0)} = 0. 0 1 5 + \frac {2 , 2 5 0}{m _ {\mathrm{T}}}.\tag{6.3}
$$

Consider the following situation. A particular trucker serves two cities 600 miles apart on a regular basis. With two drivers, each round trip, or complete vehicle cycle, takes about 39 hours, including rest time, travel time, and time spent waiting to get into the terminal, loading, and unloading. Of this, about 9 hours per trip (4.5 hours each way) is spent in congested conditions: about 1.5 hours each way in each city moving over congested local streets and 1.5 hours at delivery waiting to get into the overcrowded truck terminals. Thus about 30 hours are spent in over-the-road travel with an average over-the-road speed of 40 mph. (We assume that there are no legal constraints on driver hours. Such constraints exist in most countries for safety reasons but are often violated.) 

This operator averages about 60 trips a year, so that $m_{\mathrm{T}} = 72,000$ . Thus his cost per ton-mile is $0.015 + $0.0313 = $0.0463. 

We now ask by how much the trucker would be able to reduce his cost per ton-mile carried if the following changes in the vehicle cycle occurred: 

a. New loading docks are built at one terminal, reducing delay time to essentially zero in that city. 

b. A new terminal is built nearer the outskirts of city A, and near intercity highways, reducing travel time over local streets to zero and waiting time to 15 minutes at most. 

c. A new intercity highway is built, allowing an average over-the-road speed of 50 mph. 

d. Both b and c occur. 

To analyze these changes we first note that the total time the truck and drivers are in service per year is (39 hours/trip) × (60 trips/year), or 2,340 hours. We assume that this figure remains constant. Then we can calculate the cost savings from the four cases as follows: 

a. If delay time were zero at the terminal, then the round-trip time would become 37.5 hours, and the number of round trips per year would increase to 2,340/37.5 = 62.4 with $m_{T}$ = 74,880 miles and a corresponding cost per ton-mile of $0.015 + $0.030 = $0.045. Thus a time reduction of 3.9 percent leads to a cost reduction of about 2.7 percent. 

b. If local travel time and delays were reduced by 4.25 hours by the new terminal in city A (saving 1.5 hours each way in local travel and 1.25 hours in delays), then the round-trip time would be reduced to 34.75 hours, a reduction of 10.9 percent. The resulting number of round trips would be 2,340/34.75 = 67.3 with $m_{T}$ = 80,805 and an average cost of $0.015 + $0.0278 = $0.0428 per ton-mile. This is a cost reduction of 7.5 percent. 

c. If the average speed increased to 50 miles per hour, then over-the-road travel time would be 1,200/50 = 24 hours and the total round-trip time would be 24 + 9 = 33 hours. This corresponds to 70.9 round trips and 85,090 miles per year, for an average cost of $0.015 + $0.0264 = $0.0414 per ton-mile. This is a cost reduction of 10.6 percent. 

d. If both b and c occurred, the round-trip time would be 24 + 4.75 = 28.75 hours, corresponding to 81.4 trips and 97,670 miles per year, for an average cost of $0.015 + $0.0230 = $0.0380 per ton-mile, a reduction of 17.9 percent. 

This example demonstrates the important influence of the vehicle cycle, as reflected in round-trip time and in total annual mileage. Improvements in the vehicle cycle can reduce monetary costs to the operator. Note that the user can benefit too: directly if travel or delay time is reduced or frequency is increased, and indirectly if the operator passes on a portion of his cost savings to the user by reducing prices. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/fc366feb-933b-4442-bcbf-4538c4ada340/c453892e3949027aa7ad8bf5c57e4f04a7f72f608528189185294ac618eb2b7f.jpg)



b Railcar cycle



←Movement empty to pick up laad


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/fc366feb-933b-4442-bcbf-4538c4ada340/9836978c8951826e8b3c22011d72f5783b0f494d2ba95495d40d2b3a6943522f.jpg)



Figure 6.1 Two examples of vehicle cycles.


## 6.2.2 Major Components of the Vehicle Cycle

The typical trajectory of a transport vehicle is illustrated in figure 6.1 (see also figure 5.4). The vehicle cycle has three major components: the operating cycle, the service cycle, and the annual cycle. 

The operating cycle begins and ends at an operational base, a temporary or permanent terminal where the vehicle rests when not in service. It includes travel time while loaded and unloaded, loading and unloading time, positioning time, operational servicing time, processing time, schedule slack, and other components (these terms are defined below). 

The service cycle begins and ends at a major maintenance base, where the vehicle is garaged and maintained. Each service cycle is composed of one or more operating cycles. For systems in which a vehicle returns to its maintenance base only after periods of months or years (for example, railcars and tramp ocean vessels), a service cycle can be quite long. 

The annual cycle consists of the total trajectory of the vehicle over the year. It includes the service cycle plus time spent in periodic (major) maintenance plus idle time. 

The relationships among these major components are illustrated in figure 6.2. 

## 6.2.3 Key Relationships in the Operating Cycle $^{1}$

In the operating cycle a number of segments can be identified: 

Positioning time ( $t_{\text{P}}$ ) is time spent moving from the vehicle's maintenance base to its operating base at the beginning of service and back at the end and/or time spent moving from the operating base to the first station on the route and from the last station back to the operating base. It is sometimes useful to distinguish $t_{\text{PC}}$ , positioning time in the operating cycle, and $t_{\text{PS}}$ , positioning time to and from the maintenance base. 

Travel time while loaded ( $t_{TL}$ ) is time spent actually carrying a productive (revenue-producing) load. As shown in figure 6.2, travel time is composed of acceleration/deceleration times, time at cruise speed, and delays due to congestion and other factors. 

Travel time while unloaded( $t_{TUL}$ ) is time spent in motion traveling between loads (from a point at which one load is discharged to another point at which a new load will be obtained). 

Load/unload time ( $t_{LULD}$ ) is time spent actually loading and/or unloading passengers or cargo. 

Operational servicing time ( $t_{OS}$ ) is time spent while in operation for fueling, cleaning, maintenance, supply replenishment, crew rests, crew changes, and other servicing. Often some, or even all, operational servicing is accomplished while the vehicle is being loaded or unloaded, so that only a fraction of the total operational servicing time impacts on the operational cycle time. 

Station stopped time ( $t_{STA}$ ) is time spent in operational servicing and in loading or unloading. Station stopped time is a function of $t_{OS}$ and $t_{LULD}$ . 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/fc366feb-933b-4442-bcbf-4538c4ada340/84f91a596d438c3424190a4bf380b6074c4cabfa1513dc045cbfb340861ed537.jpg)


Schedule slack ( $t_{SLK}$ ) is, for operations according to a schedule (timetable), the time spent idle while in operation to maintain adherence to the schedule. A slack period, or cushion, is often provided between operational cycles, or even between segments of a cycle, to accommodate random delays on one cycle without disrupting the schedule of the next cycle, and/or to provide a rest for the vehicle operator. For operations that are demand-responsive rather than prescheduled, $t_{SLK}$ is the time spent waiting between demands at rest (that is, it does not include travel time unloaded to the point of pickup of a new load). 

Movement processing time ( $t_{MP}$ ) is time spent in motion between two points for processing (for example, rail cars being processed through a classification yard and shifted from one train to another). 

Total vehicle operating-cycle time ( $t_{VC}$ ) is the sum of all of these components: 

$$
\boldsymbol {t} _ {\mathrm{VC}} = \boldsymbol {t} _ {\mathrm{PC}} + \boldsymbol {t} _ {\mathrm{TL}} + \boldsymbol {t} _ {\mathrm{TVL}} + \boldsymbol {t} _ {\mathrm{SLK}} + \boldsymbol {t} _ {\mathrm{STA}} + \boldsymbol {t} _ {\mathrm{MP}},\tag{6.4}
$$

where 

$$
t _ {\mathrm{STA}} = f (t _ {\mathrm{OS}}, t _ {\mathrm{LULD}}).\tag{6.5}
$$

If operational servicing is done simultaneously with loading and unloading, then the station stopped time is the maximum of $t_{OS}$ and $t_{LULD}$ ; if it is done sequentially, the station stopped time is the sum of the two. Thus 

$$
\max (t _ {\mathrm{OS}}, t _ {\mathrm{LULD}}) \leq t _ {\mathrm{STA}} \leq t _ {\mathrm{OS}} + t _ {\mathrm{LULD}}.\tag{6.6}
$$

Other useful characterizations of the vehicle cycle are total travel time (the time the vehicle is moving whether loaded or unloaded), $t_{T}$ , and total time in motion (the time spent either moving or stopped temporarily at a station for loading, unloading, or operational servicing), $t_{MVE}$ . By definition, 

$$
\boldsymbol {t} _ {\mathrm{T}} = \boldsymbol {t} _ {\mathrm{TL}} + \boldsymbol {t} _ {\mathrm{TUL}},\tag{6.7}
$$

$$
t _ {\mathrm{MVE}} = t _ {\mathrm{T}} + t _ {\mathrm{STA}} + t _ {\mathrm{MP}} = t _ {\mathrm{TL}} + t _ {\mathrm{TUL}} + t _ {\mathrm{STA}} + t _ {\mathrm{MP}}.\tag{6.8}
$$

Thus 

$$
\boldsymbol {t} _ {\mathrm{VC}} = \boldsymbol {t} _ {\mathrm{MVE}} + \boldsymbol {t} _ {\mathrm{PC}} + \boldsymbol {t} _ {\mathrm{SLK}}.\tag{6.9}
$$

These definitions and relationships are summarized in figure 6.2. It is, of course, possible to refine these definitions further for use in 

specific analyses. For example, in many traditional transportation engineering analyses, extensive studies are made of travel times, decomposing $t_{TUL}$ and $t_{TL}$ into components such as time spent at vehicle cruise speed, $t_{CR}$ , time spent accelerating or decelerating, $t_{ACD}$ , and delays due to congestion and other factors, $t_{D}$ . 

## 6.2.4 The Service Cycle

In an extended period of time between returns to a major maintenance base a vehicle accomplishes a number $n_{C}$ of operating cycles. The total time spent in these operational cycles, together with the positioning time to and from the maintenance base, is the in-service time, $t_{IS}$ : 

$$
t _ {\mathrm{IS}} = t _ {\mathrm{PS}} + \sum_ {i = 1} ^ {n _ {c}} t _ {\mathrm{VC}} (i).\tag{6.10}
$$

If $t_{V}$ is the average total vehicle operating-cycle time, so that 

$$
t _ {\mathrm{V}} = \frac {1}{n _ {\mathrm{C}}} \sum_ {i = 1} ^ {n _ {c}} t _ {\mathrm{VC}} (i),\tag{6.11}
$$

then 

$$
t _ {\mathrm{IS}} = t _ {\mathrm{PS}} + n _ {\mathrm{C}} t _ {\mathrm{V}}.\tag{6.12}
$$

## 6.2.5 The Annual Cycle

In addition to in-service time, over the course of a year a vehicle typically requires a certain amount of maintenance time, $t_{MNT}$ : this consists of scheduled maintenance, which may be required every x hours or y miles to maintain the vehicle in an operational state, and unscheduled major maintenance, such as occurs when the breakdown of a component requires the vehicle to be pulled out of service for a period of days or longer. The rest of the year is made up of idle time, $t_{IDLE}$ (though it should be emphasized that there are often substantial periods of time at rest during the in-service time, such as $t_{SLK}$ or $t_{STA}$ ). 

The basic relationship is, by definition (if times are measured in days), 

$$
t _ {\mathrm{IS}} + t _ {\mathrm{MNT}} + t _ {\mathrm{IDLE}} = 3 6 5.\tag{6.13}
$$

Usually $t_{MNT}$ is fixed by the vehicle design and especially by maintenance policy (sometimes it is not a constant but a function of the number of cycles or related variables such as vehicle-hours or vehicle-miles). From an operator's perspective, $t_{IS}$ is established by the assignment of routes and schedules—the operating plan (see chapter 7)—and thus the corresponding cycle times, $t_{\mathrm{VC}}(i)$ , leading to $n_{C}$ and $t_{V}$ and thus $t_{IS}$ . The idle time is then the residual. In general, the operator, in trying to maximize net revenue or pursuing other economic objectives, will also try to minimize $t_{IDLE}$ , but it is important to note that the minimum $t_{IDLE}$ may in fact produce lower net revenue than the optimum value. 

## 6.2.6 Examples of Vehicle Cycles

## A BUS CYCLE

For urban buses in public mass transit service, the maintenance base is usually the garage to which the vehicle returns at night (or sometimes more frequently). The operating base is the terminus where the bus rests between scheduled runs and may simply be a street corner. A typical vehicle cycle might have the following components. 

Positioning time: 10 minutes in the morning plus 10 minutes in the evening traveling from garage to starting point of route and return; so $t_{PS} = 20$ minutes for the daily service cycle. (We assume that the bus begins and ends each run at the same point on the route and does not change routes, so $t_{PC} = 0$ ; positioning occurs only at the beginning and end of the day.) 

Operating cycles: The route is such that the bus makes one round trip per hour. Since there are 16 operating hours (4 peak hours and 12 off-peak hours) in a day, $n_{C} = 16$ . 

Travel time: Each one-way trip takes 25 minutes in peak periods and 20 minutes in off-peak periods. Each one-way trip makes an average of 18 stops, at an average stopped time of 30 seconds for loading and unloading, so $t_{\mathrm{STA}}$ is $18 \times 0.5 \times 2 = 18$ minutes per operating cycle, or $16 \times 18 = 288$ minutes per day. The travel time $t_{\mathrm{T}}$ is $50 - 18 = 32$ minutes per round trip for peak hours and $40 - 18 = 22$ minutes for off-peak hours, or a total of $(4 \times 32) + (12 \times 22) = 392$ minutes per day, all (in general) loaded time (in revenue service, although the vehicle may be partially full or even empty at times). 

Operational servicing, processing: There is no requirement for operational servicing or movement processing. 

Schedule slack: For user convenience the trips are scheduled to depart from either terminus every half hour. Thus the time allowed for a one-way trip is 30 minutes, versus run times of 20 or 25 minutes, and schedule slack is 10 minutes per round trip in peak hours and 20 minutes in off-peak hours, for a total of $(4 \times 10) + (12 \times 20) = 280$ minutes per day. Note that on the last return trip 10 minutes slack is avoided because the vehicle can proceed directly from the last stop to the garage, so the total is 280 - 10 = 270. 

Total service cycle: The total time the vehicle is in operational service consists of the initial positioning time (10 minutes) plus the 16 hours in the operating cycles (travel, loading, unloading, slack) less the last 10 minutes of schedule slack at the end of the day plus the return positioning time (10 minutes), or 16 hours 10 minutes. 

(Note that several drivers may be assigned to the vehicle over the day.) 

The per-cycle averages of these components are 

$t_\mathrm{TL} = 392 / 16 = 24.5\mathrm{min / cycle},$ $t_\mathrm{STA} = 288 / 16 = 18.0\mathrm{min / cycle},$ $t_\mathrm{SLK} = 270 / 16 = 16.9\mathrm{min / cycle},$ $t_\mathrm{P} = 20 / 16 = 1.25\mathrm{min / cycle},$ $t_\mathrm{V} = 970 / 16 = 60.6\mathrm{min / cycle},$ $t_\mathrm{T} = t_\mathrm{TL} = 24.5\mathrm{min / cycle},$ $t_\mathrm{MVE} = t_\mathrm{T} + t_\mathrm{STA} = 24.5 + 18.0 = 42.5\mathrm{min / cycle}.$ Thus $t_\mathrm{T} / t_\mathrm{V} = 24.5 / 60.6 = 40$ percent, $t_\mathrm{MVE} / t_\mathrm{V} = 42.5 / 60.6 = 70$ percent, $t_\mathrm{IS} = n_{\mathrm{C}}t_{\mathrm{V}} = 970\mathrm{min} = 16\mathrm{hr}10\mathrm{min}.$ 

In this situation the vehicle is traveling only 40 percent of the time it is in service and is in motion only 70 percent of the time. Conversely 30 percent of the in-service time is spent in schedule slack or in positioning. 

## THE RAILCAR CYCLE

The movements of rail freight cars in typical services are quite illuminating (see figure 6.3, which was adapted from a study of freight car movements in the United States). The stages in an average car movement are given in table 6.1. Analysis of these figures yields the following values for the various time components of the cycle: 

$t_{\mathrm{VC}} = 25.5$ days, $t_{\mathrm{TL}} = 2$ days, $t_{\mathrm{TUL}} = 2$ days, $t_{\mathrm{T}} = 4$ days, $t_{\mathrm{MPL}}$ (total time spent in processing while loaded) = 6 days, $t_{\mathrm{MPUL}}$ (total time spent in processing while unloaded) = 8.5 days, 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/fc366feb-933b-4442-bcbf-4538c4ada340/e745e0b308e17ae77fda527429c96de11c12fe8fa8d788e4ec8ce031a1f39ff8.jpg)



Figure 6.3 Anatomy of the railcar cycle (thick rules indicate times of shipper control). Adapted from Reebie Associates (1972).


$$
t _ {\mathrm{MP}} = t _ {\mathrm{MPL}} + t _ {\mathrm{MPUL}} = 1 4. 5 \mathrm{days},
$$

$t_{SH}$ (total time spent under shipper control while being loaded or unloaded) = 6 days [line 7 plus line 13], 

$t_{RR}$ (total time spent under railroad control while being loaded or unloaded) = 1 day [line 8 plus line 2], 

$$
t _ {\mathrm{LULD}} = t _ {\mathrm{SH}} + t _ {\mathrm{RR}} = 7 \text { days },
$$

$$
t _ {\mathrm{VC}} = t _ {\mathrm{T}} + t _ {\mathrm{MP}} + t _ {\mathrm{LULD}} = 2 5. 5 \mathrm{days}.
$$

Thus the fraction of time actually spent traveling is 

$$
\frac {t _ {\mathrm{T}}}{t _ {\mathrm{VC}}} = \frac {t _ {\mathrm{TL}} + t _ {\mathrm{UL}}}{t _ {\mathrm{VC}}} = \frac {4}{2 5 . 5} = 1 5. 7 \text { percent };
$$

the fraction of time spent loaded is 

$$
\frac {t _ {\mathrm{TL}} + t _ {\mathrm{MPL}}}{t _ {\mathrm{VC}}} = \frac {1 4 . 5}{2 5} = 5 6. 9 \text { percent };
$$

the time spent in processing (being switched from one train to another, waiting for the next train) is 


Table 6.1 Stages in a railcar cycle (days)


<table><tr><td></td><td>Elapsed time</td><td>Cumulative elapsed time</td><td>Component</td></tr><tr><td colspan="4">Empty time</td></tr><tr><td>1. An empty car becomes available to be assigned to pick up a new load (car is released).</td><td>0</td><td>0</td><td>—</td></tr><tr><td>2. Empty car waits at point of release to be picked up (pulled) for movement to the terminal.</td><td>0.5</td><td>0.5</td><td><eq>t_{LULD}</eq></td></tr><tr><td>3. Empty car is processed at initial terminal (includes switching into outbound train, waiting time).</td><td>2</td><td>2.5</td><td><eq>t_{MPUL}</eq></td></tr><tr><td>4. Empty car moves over system to pickup point.</td><td>2</td><td>4.5</td><td><eq>t_{TUL}</eq></td></tr><tr><td>5. Empty car is processed at intermediate terminals (switching from one train to another, waiting time).</td><td>4.5</td><td>9</td><td><eq>t_{MPUL}</eq></td></tr><tr><td>6. Empty car is processed at final terminal and delivered to point of pickup of load (car is “placed”).</td><td>2</td><td>11</td><td><eq>t_{MPUL}</eq></td></tr><tr><td colspan="4">Loaded time</td></tr><tr><td>7. Empty car is loaded and released by the shipper for movement by the railroad.</td><td>3</td><td>14</td><td><eq>t_{LULD}</eq></td></tr><tr><td>8. Loaded car waits after release to be picked up for movement.</td><td>0.5</td><td>14.5</td><td><eq>t_{LULD}</eq></td></tr><tr><td>9. Loaded car is moved to and processed through initial terminal.</td><td>1</td><td>15.5</td><td><eq>t_{MPL}</eq></td></tr><tr><td>10. Loaded car moves to load delivery point.</td><td>2</td><td>17.5</td><td><eq>t_{TL}</eq></td></tr><tr><td>11. Loaded car is processed at intermediate terminals.</td><td>4</td><td>21.5</td><td><eq>t_{MPL}</eq></td></tr><tr><td>12. Loaded car is processed at final terminal and delivered to point of destination of load.</td><td>1</td><td>22.5</td><td><eq>t_{MPL}</eq></td></tr><tr><td>13. Loaded car is placed at delivery point, unloaded, and released by the recipient for pickup.</td><td>3</td><td>25.5</td><td><eq>t_{LULD}</eq></td></tr></table>

$$
\frac {t _ {\mathrm{MP}}}{t _ {\mathrm{VC}}} = \frac {1 0 . 5}{2 5 . 5} = 4 1. 2 \text { percent };
$$

and the fraction of time spent under shipper control being loaded or unloaded is 

$$
\frac {t _ {\mathrm{SH}}}{t _ {\mathrm{VC}}} = \frac {6}{2 5 . 5} = 2 3. 5 \text { percent }.
$$

From this we can see the basis for the frequently encountered statement that the average American railcar moves about 70 miles per day: even if the average train speed overall is about 19 mph, since a car is in traveling status only 15.7 percent of the time, its effective speed is $24 \times 0.157 \times 19 = 71.6$ miles per day. 

As we shall see shortly, the low fraction of time a vehicle spends in actual productive travel has significant economic implications. In the case of railcars, the U.S. railroads have undertaken a major research program aimed at developing a better understanding of car movement cycles and of how rail economics can be improved by increasing the amount of productive travel time relative to unproductive time. One key target is to reduce the time spent in loading or unloading under shipper control, which as we have seen is 23.5 percent of the vehicle cycle time. We shall return to this example in section 6.7. 

## 6.2.7 Opportunities to Affect the Vehicle Cycle

The following sections will demonstrate the economic importance of the vehicle cycle. There are a wide variety of points of leverage on the vehicle cycle and thus on the economics of system performance: 

1. Travel time ( $t_{T}$ ) can be affected by changes in the vehicle, enabling higher cruise speeds (lower $t_{CR}$ ) and more rapid acceleration or deceleration (lower $t_{ACD}$ ), changes in the guideway, enabling higher speeds or shorter distances, or strategies to reduce congestion delays ( $t_{D}$ ), such as control system improvements. 

2. The travel time while unloaded ( $t_{TUL}$ ) reflects the need to move from a point of unloading one load to the point of pickup of another load (the backhaul problem). Improvements in $t_{TUL}$ can be achieved through marketing strategies designed to increase demand in nonpeak directions and nonpeak periods and through vehicle-fleet management strategies designed to match the distribution of empty vehicles more closely (in time and space) to the distribution of demands. 

3. In modes such as rail, the time required for processing while in motion ( $t_{MP}$ ) can be quite significant. A wide variety of operational strategies can be utilized to reduce $t_{MP}$ , such as running more trains over longer distances to provide more direct services, increasing the frequency of service, improving schedule coordination, and improving travel-time reliability. 

4. The time required for operational servicing ( $t_{OS}$ ) can be reduced by more efficient servicing procedures or by changes in vehicle design to reduce operational servicing requirements or to allow more efficient procedures. 

5. The time required for loading and unloading ( $t_{LULD}$ ) can be affected by vehicle design, by terminal design, and by operational procedures. This has been a major aspect of the containerization revolution in marine transportation and is also important in aircraft operations. 

6. Since station stopped time ( $t_{STA}$ ) is a function of both $t_{OS}$ and $t_{LULD}$ , it can be affected by improvements in those components and especially by approaches that allow maximum overlap between them; it can also be affected by changing the number of stops, as by changing from local to express services. 

7. For scheduled modes slack time ( $t_{SLK}$ ) is set by policy but is based in part on expectations of the degree of variability in other elements of cycle time. Thus improvements in time reliability for any vehicle cycle components can lead to decreases in $t_{SLK}$ . For demand-responsive modes $t_{SLK}$ is the time spent waiting between demands; it reflects the variability of cycle time components in that the ability to assign vehicles to new loads is influenced, in part, by the degree of uncertainty in the time when loaded vehicles will be unloaded and available for a new load. 

8. The positioning time ( $t_{P}$ ) can be affected by the location of vehicle (maintenance) bases, the design of routes, and especially the positioning of starting and terminating points. 

Obviously all components of the vehicle cycle are affected in major ways by the design of routes, by scheduling decisions, and by vehicle assignments to operating bases and to routes and schedules. Clearly, too, changes in system strategies that affect the vehicle cycle will potentially impact both users and operators. Thus, in looking at the economics of the vehicle cycle, we must consider both costs and revenues to the operator as well as effects on users. First, however, we need to review some basic concepts of systematic analysis relevant to an economic analysis. 

## 6.3.1 Average and Marginal Products $^{2}$

In the analysis of change in a function $y = f(x)$ , several concepts are of interest, namely the average product of y with respect to x, 

$$
\bar {y} _ {x} \equiv \frac {y}{x} = \frac {f (x)}{x},\tag{6.14}
$$

and the marginal product of y with respect to x, 

$$
y _ {x} ^ {\prime} \equiv \frac {\partial y}{\partial x} = \frac {\partial f (x)}{\partial x}.\tag{6.15}
$$

Average and marginal products are particularly useful for analysis of various dimensions of resource consumption, and especially for resources that can be evaluated as monetary costs incurred by the operator. (Recall that there are many different types of resources consumed in producing transportation. Some of these lend themselves to ready evaluation in monetary terms, such as the direct costs borne by the operator; others cannot be so evaluated without the application of value judgments.) 

As the options T are varied, capacity volume $V_{C}$ will vary along with the amount of resources consumed. Consider air quality degradation, as measured by the number of milligrams of hydrocarbons emitted, r: 

$$
\bar {r} _ {V _ {\mathrm{c}}} \equiv \frac {r}{V _ {\mathrm{C}}}\tag{6.16}
$$

is the average hydrocarbon emission per unit of capacity; 

$$
r _ {V _ {\mathrm{c}}} ^ {\prime} \equiv \frac {\partial r}{\partial V _ {\mathrm{c}}}\tag{6.17}
$$

is the marginal increase in hydrocarbon emissions for each additional unit of capacity. 

A particularly useful application of average and marginal products is to the total cost incurred by the operator, $C_{T}$ : 

$$
\bar {C} _ {V _ {\mathrm{c}}} \equiv \frac {C _ {\mathrm{T}} (V _ {\mathrm{c}})}{V _ {\mathrm{c}}}\tag{6.18}
$$

is the average cost per unit of capacity; 

$$
C _ {V _ {\mathrm{c}}} ^ {\prime} \equiv \frac {\partial C _ {\mathrm{T}} (V _ {\mathrm{C}})}{\partial V _ {\mathrm{C}}}\tag{6.19}
$$

$^{2}$ See Henderson and Quandt (1958), section 3-1. Our terminology derives from, but differs from, the concepts of microeconomics. 

is the marginal increase in cost for each additional unit of capacity. For the simple cost function assumed in section 5.4, 

$$
C _ {\mathrm{T}} = \frac {a}{n} Q, \qquad V _ {\mathrm{C}} = 2 w Q.\tag{6.20}
$$

Thus 

$$
\bar {C} _ {V _ {\mathrm{c}}} = \frac {C _ {\mathrm{T}}}{V _ {\mathrm{C}}} = \frac {a}{2 w n},\tag{6.21}
$$

$$
C _ {V _ {\mathrm{c}}} ^ {\prime} = \frac {\partial C _ {\mathrm{T}}}{\partial V _ {\mathrm{C}}} = \frac {a}{2 w n}.\tag{6.22}
$$

In this simple case the average and marginal total operator costs, defined with respect to capacity volume, are equal and constant, independent of $V_{C}$ . Note, however, that the average and marginal costs with respect to equilibrium volume $V_{E}$ would not necessarily be equal or constant. For example (assuming that capacity never constrains $V_{E}$ ), with a demand function 

$$
V _ {\mathrm{D}} = \alpha_ {0} Q ^ {\alpha_ {1}}, \qquad \alpha_ {1} > 0,\tag{6.23}
$$

and 

$$
V _ {\mathrm{E}} = V _ {\mathrm{D}},\tag{6.24}
$$

so that 

$$
Q = \left(\frac {V _ {\mathrm{E}}}{\alpha_ {0}}\right) ^ {1 / \alpha_ {1}},\tag{6.25}
$$

(6.20) becomes 

$$
C _ {\mathrm{T}} = \frac {a}{n} \left(\frac {V _ {\mathrm{E}}}{\alpha_ {0}}\right) ^ {1 / \alpha_ {1}}.\tag{6.26}
$$

Then 

$$
\begin{array}{r l} \bar {C} _ {V _ {\mathrm{E}}} \equiv \frac {C _ {\mathrm{T}}}{V _ {\mathrm{E}}} & = \frac {a}{\alpha_ {0} n} \left(\frac {V _ {\mathrm{E}}}{\alpha_ {0}}\right) ^ {(1 / \alpha_ {1}) - 1} \\ & = \left(\frac {a}{\alpha_ {0} n}\right) Q ^ {1 - \alpha_ {1}}, \end{array}\tag{6.27}
$$

$$
\begin{array}{r l} C _ {V _ {\mathrm{E}}} ^ {\prime} & \equiv \frac {\partial C _ {\mathrm{T}}}{\partial V _ {\mathrm{E}}} \\ & = \frac {a}{\alpha_ {1} n \alpha_ {0}} \left(\frac {V _ {\mathrm{E}}}{\alpha_ {0}}\right) ^ {(1 / \alpha_ {1}) - 1} = \frac {a}{\alpha_ {1} n \alpha_ {0}} Q ^ {1 - \alpha_ {1}} \end{array}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/fc366feb-933b-4442-bcbf-4538c4ada340/512724457641f80c8c08817132e8378fbefe74556b28136a901c4e262609a582.jpg)



Figure 6.4 Relationship between average and marginal products.


$$
= \frac {1}{\alpha_ {1}} \bar {C} _ {V _ {\mathrm{E}}}.\tag{6.28}
$$

In this case the average and marginal costs with respect to equilibrium volume are unequal and vary with volume and with frequency. 

More generally we can define average and marginal products in terms of any of the impacts of interest. In particular, from the perspective of the user, we might examine average or marginal levels of service. From the perspective of the operator, average and marginal net revenues are useful, as well as many other constructs. Historically, particular attention has been paid to average and marginal monetary costs, but these are not by any means the only impacts of interest. 

Figure 6.4 illustrates a common functional relationship for $y = f(x)$ and the corresponding relationships of $\bar{y}_x$ and $y_x'$ . The point $x = x_A$ has particular importance (if it exists in a particular case): it is the point at which $\bar{y}_x = y_x$ . In this case, for values of $x > x_A$ , $y_x' > \bar{y}_x$ : the marginal product of $y$ is greater than the average product. For example, if $y$ is total cost, for $x > x_{A}$ each additional unit of x increases the total cost at a rate greater than the average total cost of each unit (see section 7.2). 

## 6.3.2 Choice of the Output Dimension: Cost Functions

It is important to understand the relationship between the foregoing concepts and those developed in chapter 5. There we traced out impacts as a function of options; for example, all of the graphical illustrations dealt with schedule frequency Q as the independent variable, representing the options T, and showed the variations of volumes, costs, revenues, and so on, as functions of Q. 

There are various ways in which the results of a systematic analysis can be displayed. Traditionally transportation analysts have dealt with costs and revenues as functions of "output," using the concepts of average and marginal products. 

In the notation of section 5.4, some possible output measures are: 

1. scheduled frequency of vehicle trips, Q, 

2. available capacity, $V_{C} = 2Qw$ , where w is a payload, 

3. "revenue" volume, $V_{\mathrm{E}}$ , 

4. available ton-miles per round trip, $V_{c}D = 2Qwd$ , where D = 2d 

is the round-trip distance, 

5. revenue ton-miles per round trip, $V_{E}D$ . 

Structurally the analyses would be the same regardless of the output dimension chosen. Following the pattern of the analyses in chapter 5, we vary the options T over a range. For each value of T, the value of the impact of interest (for example, total cost, net revenue, or volume of air pollutants) and the value of the chosen output dimension (for example, $V_{C}$ or $V_{E}$ ) are determined. Then the results can be displayed in tabular or graphic form and analyzed. 

A particularly common analysis is that of the cost function, in which total cost $C_{T}$ is expressed as a function of capacity volume $V_{C}$ . In the next section we shall explore such cost functions and see some of the policy implications that can be developed from their analysis. Here we should note that the choice of output unit can have a significant effect on the outcome of an analysis. For example, while $V_{C}$ has been a traditional basis of cost function analysis, $V_{E}$ is often a more appropriate measure because it reflects the actual usage of the system: “average cost per actual user” has more significance than “average cost per seat available.” Using $V_{E}$ does, however, require either explicit equilibration with a demand function or a judgment about the load factor and how it varies with T. 

It is important to recognize that different choices of measures may lead to different displays and possibly to different conclusions. The analysis in chapter 5 showed that different technologies may have different optimal schedule frequencies. For each technology there will thus be a different equilibrium volume at which that technology performs best, in the sense of maximizing $I_{NR}$ or any other objective. This is demonstrated in exercise 6.1. 

There has been substantial debate about which of the various possible output measures is the best measure to use (G. Wilson 1959). From our perspective, each measure has advantages and disadvantages. The analyst should use several measures, choosing the ones that appear to be most useful in a particular context. 

## 6.4 ANALYSIS OF COST FUNCTIONS

While variations in all dimensions of resource consumption are important, special attention is often focused on how costs, and specifically the total monetary cost incurred by the operator, vary as options are varied. The following discussion, while formulated in terms of monetary costs and volumes, could be generalized to include any element of S, R, or V. 

In general, the total cost will be a function of the volume, and we shall use $V_{E}$ for this discussion. Figure 6.5 shows the variety of forms this functional relationship may take. Consider the alternatives A, B, and E. All three express the hypothesis that a large initial cost is required to serve any volume at all and that, over a range of moderate volumes $V_{0}-V_{1}$ , the cost of serving an additional unit of volume is relatively constant. Curve B assumes that, after a certain point $V_{1}$ , the system becomes particularly efficient, so that each additional unit of traffic served costs less and less (economies of scale). Curve A assumes that the cost of serving additional units begins to increase rapidly (diseconomies of scale). Curve E assumes that the incremental cost remains constant. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/fc366feb-933b-4442-bcbf-4538c4ada340/a6272a1be9c0470a1988980369658cc0525a5ee080f1c041feccee6a29a52e4f.jpg)



Figure 6.5 General cost function. Adapted from Meyer et al. (1960).


Let us assume that we have the total cost as a function of volume for a particular transportation system: $C_{\mathrm{T}} = f(V)$ . Two additional quantities of interest are the average total cost, $\bar{C}_{V} = C_{T}/V$ , and the marginal cost, $C_{V}^{\prime} = \partial C_{T}/\partial V$ . The average total cost is precisely that: the share of the total cost per unit of volume, assuming that all units of volume bear the total cost equally. The marginal cost, on the other hand, reflects the incremental total cost incurred when a single unit of volume is added to the system. 

To explore the implications of these concepts we shall look at some general forms of the total cost function and study their properties. 

## 6.4.1 A Linear Cost Function

One simple form is the linear cost function: 

$$
C _ {\mathrm{T}} = a + b V = C _ {\mathrm{FC}} + C _ {\mathrm{VC}}.\tag{6.29}
$$

Here an initial cost a must be incurred before the system can begin operation, and the addition of a single unit of volume increases the cost by b. The portion $C_{FC} = a$ is often termed the fixed cost because it is independent of volume. The portion $C_{VC} = bV$ is similarly termed the variable cost. This cost function has the following properties: 

1. average total cost: 

$$
\bar {C} _ {V} = \frac {C}{V} = \frac {a}{V} + b,
$$

2. average fixed cost: 

$$
\bar {C} _ {\mathrm{FC/V}} = \frac {C _ {\mathrm{FC}}}{V} = \frac {a}{V},
$$

3. average variable cost: 

$$
\bar {C} _ {\mathrm{VC} / V} = \frac {C _ {\mathrm{VC}}}{V} = b
$$

4. marginal total cost: 

$$
C _ {V} ^ {\prime} = \frac {\partial C _ {\mathrm{T}}}{\partial V} = b,
$$

5. marginal fixed cost: 

$$
C _ {\mathrm{FC} / V} ^ {\prime} = \frac {\partial C _ {\mathrm{FC}}}{\partial V} = 0,
$$

6. marginal variable cost: 

$$
C _ {\mathrm{VC/V}} ^ {\prime} = \frac {\partial C _ {\mathrm{VC}}}{\partial V} = b.
$$

Understanding Performance Functions I 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/fc366feb-933b-4442-bcbf-4538c4ada340/b4ca4c7a8abfefbb455472543a437cf8457105451318ce72f327fb32d447be42.jpg)



Figure 6.6 Characteristics of a linear cost function.


These properties are illustrated in figure 6.6. 

## 6.4.2 Example: A Penetration Road

In underdeveloped countries a major transportation problem is to provide access to previously inaccessible areas. Often the traffic volumes to be expected are very low—perhaps only a few thousand vehicles per year. In this context there is a range of choices of transport technologies; each technology consists of the specification of the roadway to be provided and the vehicle type(s) to be operated over that roadway. 

We consider three alternative technologies (Guenther 1968): 

A: off-road tracked vehicles, operating on a "burro-path" or other cross-country track, 

B: vehicles with four-wheel drive, operating on a packed-earth roadway, 

C: heavy-duty two-axle vehicles, operating on an all-weather gravel road. 

The cost functions are shown in figure 6.7. They reflect the following relationships among the alternatives, going in order A, B, C, and for a specified volume level: 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/fc366feb-933b-4442-bcbf-4538c4ada340/968d94c336e58bc86d970102330c37551b38961d495291490b0ef724a0ea2c9d.jpg)



Figure 6.7 Three alternative technologies for a penetration road.


1. the initial construction cost of the roadway increases and the roadway maintenance cost decreases, 

2. the vehicle procurement and operating costs decrease, 

3. speeds increase, trip time decreases, and thus fewer vehicles are required to transport a given volume per time period. 

Thus 

$$
\bar {C} _ {\mathrm{FC/V}} ^ {\mathrm{A}} <   \bar {C} _ {\mathrm{FC/V}} ^ {\mathrm{B}} <   \bar {C} _ {\mathrm{FC/V}} ^ {\mathrm{C}}
$$

and 

$$
\overline {{C}} _ {\mathrm{VC/V}} ^ {\mathrm{A}} > \overline {{C}} _ {\mathrm{VC/V}} ^ {\mathrm{B}} > \overline {{C}} _ {\mathrm{VC/V}} ^ {\mathrm{C}}.
$$

These curves illustrate how the cost advantages of different systems change as the volume varies. For low volumes, between 0 and $V_{1}$ , system A has the lowest total cost and average total cost, because it requires no investment in roadway construction and the lowest level of roadway maintenance. That is, average fixed cost is low. Because the average variable cost for A is high, however, for volumes between $V_{1}$ and $V_{3}$ system B has the lowest cost. Above volume $V_{3}$ system C has the lowest cost; the heavier investment in the roadway (high average fixed cost) is spread over a large volume and is also offset by the lower vehicle costs (low average variable cost). 

If total cost or average total cost were the only relevant criterion (for example, if differences in levels of service were negligible, which is unlikely, or if demand were insensitive to service levels over this range), then the cost functions alone could be used as a basis for decision. Otherwise, the more general equilibrium analysis of chapter 5 would be required (see section 6.6). 

All of these alternatives are highway alternatives; taken as a family, they could be characterized by the single cost function in part c of the figure, which is the same as the dark boundary line in part b of the figure. 

This same curve is shown as $AA'$ in figure 6.8; it has been extended to higher volume ranges, with the successive peaks representing additional lanes of highway constructed. Curve $RR'$ represents an alternative technology, namely railroad. 

The two modal choices are abstracted in part b of the figure, where the relatively minor perturbations of the alternative choices within the spectrum of roadway–vehicle options have been smoothed out. For some purposes, where it is necessary only to understand the major differences between modes, it may be sufficient to determine only the broad trend of the cost function, as in part b. In other instances the choices within modes may become important, in which case the component curves must be determined as in figure 6.7. Occasionally it may be important to reach even more deeply into the detailed options of vehicles, link characteristics, and operating decisions and so to have even more detailed curves within the envelope of a single curve of figure 6.7—for example, different combinations of vehicle size, highway pavement width, and pavement thickness (see Soberman 1966a, Walters 1968, Niebur 1975). 


a


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/fc366feb-933b-4442-bcbf-4538c4ada340/d4cedd66c6f235f344fd29eb0f552c9db5bba1f6057defc03a7b97a70d0ef0e5.jpg)



b


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/fc366feb-933b-4442-bcbf-4538c4ada340/fc926ba467f2d467f666e648d25ea83ad29d902367d9195b00d07e67b52c34a3.jpg)



Figure 6.8 Two alternative modes.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/fc366feb-933b-4442-bcbf-4538c4ada340/e3353acff87171b528cfdf87c5b152d72034dc082abc4c8cf5652f01627ea779.jpg)



Figure 6.9 A composite cost function.


## 6.4.3 Nonlinear Cost Functions

Many, if not most, transportation systems exhibit cost behavior more complex than that implied by the simple linear cost function. In particular, many systems have the property of diseconomies of scale, as illustrated by curve A in figure 6.5. The general case is illustrated in figure 6.9. This function has the following properties. The average fixed cost decreases as volume increases, since the cost is spread over more units. However, the average variable cost decreases initially, is almost constant over a middle range, and then increases over high volumes. 

The phenomenon of increasing average variable cost is called the law of diminishing marginal productivity. The hypothesis underlying this law is that, as higher levels of volume are accommodated, the production process becomes inefficient in its use of resources, so that increasing proportions of some resources are required and/or the cost of the resources increase. For example, in building urban highways, going beyond six lanes of width often requires separated roadways, more median barriers, and more complex interchanges, which may result in diseconomies of scale under some conditions. In transportation one particularly important source of diminishing marginal productivity is the set of phenomena we call congestion (see chapter 7). 

As an example of a nonlinear cost function figure 6.10 shows a set of cost functions for pipelines. 

## 6.4.4 Implications: Variations in Transportation Performance Functions

The cost functions of most types of transportation systems have both fixed and variable components, and the variable components usually exhibit a range of diseconomies of scale. However, the relative influences of the fixed and variable components vary significantly among transportation systems, and such differences can be a major factor in the choice among systems (Heflebower 1965). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/fc366feb-933b-4442-bcbf-4538c4ada340/e014c67ed8986eac7a3afbc1ef21bb4732bac02356f47bb6f55060a8afbcebfe.jpg)



Figure 6.10 An example of cost functions for pipelines of various diameters. bbl = barrel. From Cookenboo (1955).


As a rough generalization, at one extreme are systems such as water or air transport and bus transit. Although there are significant investments in fixed facilities in each of these modes—port facilities, airports and maintenance facilities, and highways—the institutional structure is usually such that the transport operator—air carrier, ship owner, transit operator—pays for the infrastructure only indirectly. Some of the mechanisms used are port or airport landing fees, facilities rentals, and fuel taxes. Thus from the operator's perspective the fixed costs are basically those of owning or leasing vehicles, and variable costs therefore play a key role in the operator's cost function. 

At the other extreme are systems such as railroads. Here major infrastructure investments are borne directly by the operator, and so the fixed-cost component tends to be a high proportion of the average cost. 

Again we stress that these are generalizations and that the specifics of particular situations can vary greatly and need to be investigated individually in detail. 

## 6.5 USING COST FUNCTIONS FOR POLICY ANALYSIS

The analysis of cost functions can often lead to useful insights. As an example we shall examine a particular segment of the U.S. trucking industry. 

## 242 Understanding Performance Functions I

## 6.5.1 The Nonuniformity of Demand by Direction: Backhaul and Positioning

In almost every situation, in any time period, there are unequal flows in the two opposite directions on the same route. Freight flows are almost always unbalanced: raw materials move in one direction, finished goods in the opposite direction. For passenger movements the flows usually balance over a long enough period of time, such as a day or week (except for the rare situation of migratory movements), but over short periods of time the movements in two directions are unbalanced. For example, in peak periods in most urban areas there is a dominant movement toward the city's central area in the morning and in the reverse direction in the evening. 

These directional imbalances in demand lead to the backhaul problem—unequal load factors in the two directions, yielding an overall load factor lower than that in the direction of maximum flow. 

Closely related to the backhaul problem is that of positioning. When a load is dropped at A, the empty vehicle may have to move to B to pick up its next load. Thus a vehicle must spend time in empty movement. This was illustrated in general terms in section 6.2. 

The economics of the backhaul situation can be quite complex. In response to this market condition operators may vary pricing options or even route structures in order to reduce the disparity in demand directions. An analysis of cost functions can show the impact of these imbalances. 

## 6.5.2 Backhaul: A Trucking Example

Wyckoff and Maister (1975) analyzed the cost structure of a particular class of truckers: owner-operators operating on a lease basis, subcontracting to a larger carrier. They established high, medium, and low estimates of cost based on interviews and other data sources. These estimates show costs to be a roughly linear function of total vehicle mileage per year. Thus the cost equation is approximately 

$$
C _ {\mathrm{T}} = \alpha_ {0} + \alpha_ {1} m _ {\mathrm{T}},\tag{6.30}
$$

where $m_{T}$ is the total number of vehicle-miles driven per year and $\alpha_{0}$ and $\alpha_{1}$ are parameters. 

From this cost equation can be derived the average cost per mile $c_{m} \equiv \bar{C}_{T/m}$ and, for an average payload of w tons, the average cost per ton-mile $c_{tm} \equiv \bar{C}_{T/mw}$ : 

$$
c _ {\mathrm{m}} = \frac {C _ {\mathrm{T}}}{m _ {\mathrm{T}}} = \frac {\alpha_ {0}}{m _ {\mathrm{T}}} + \alpha_ {1},\tag{6.31}
$$

Vehicle Cycle and Analysis of Cost Functions 

$$
c _ {\mathrm{tm}} = \frac {C _ {\mathrm{T}}}{m _ {\mathrm{T}} w} = \frac {1}{w} \left(\frac {\alpha_ {0}}{m _ {\mathrm{T}}} + \alpha_ {1}\right).\tag{6.32}
$$

Some of the mileage traveled each year is empty mileage. This is referred to as empty backhaul—the mileage traveled without a load in the return or backhaul direction. This can also be thought of as positioning mileage: after dropping off one load, an operator may drive several hundred miles to pick up a load that he can carry back to his origin. Thus 

$$
m _ {\mathrm{T}} = m _ {\mathrm{L}} + m _ {\mathrm{E}},\tag{6.33}
$$

where $m_{I}$ , and $m_{E}$ are the numbers of miles driven while loaded and empty, respectively. 

The ratio of loaded to total mileage is 

$$
\gamma \equiv \frac {m _ {\mathrm{L}}}{m _ {\mathrm{L}} + m _ {\mathrm{E}}} = \frac {m _ {\mathrm{L}}}{m _ {\mathrm{T}}}.\tag{6.34}
$$

Thus the cost per loaded mile $c_{mL}$ and the cost per ton-mile loaded $c_{tmL}$ are determined by correcting (6.31) and (6.32) by $\gamma$ (note that empty miles are actually somewhat cheaper to operate than loaded miles, but this difference is small and will be ignored in this discussion): 

$$
c _ {\mathrm{mL}} = \frac {C _ {\mathrm{T}}}{m _ {\mathrm{L}}} = \frac {C _ {\mathrm{T}}}{\gamma m _ {\mathrm{T}}},\tag{6.35}
$$

$$
c _ {\mathrm{tmL}} = \frac {C _ {\mathrm{T}}}{\gamma m _ {\mathrm{T}} w}.\tag{6.36}
$$

Sometimes an alternative parameter is used: the ratio of empty backhaul to loaded miles, 

$$
\beta \equiv \frac {m _ {\mathrm{E}}}{m _ {\mathrm{L}}}.\tag{6.37}
$$

Thus 

$$
m _ {\mathrm{L}} = m _ {\mathrm{T}} \left(\frac {1}{1 + \beta}\right).\tag{6.38}
$$

Both $\beta$ and $\gamma$ can be expressed as fractions or as percentages and can range from 0 to 1 (0 to 100 percent). (Wyckoff and Maister use $\beta$ as an empty backhaul percentage. Sometimes a third parameter is used: the empty backhaul ratio $\rho$ defined as the percentage of the backhaul miles that are empty. If the backhaul miles are assumed to be half the total miles, then $\rho \equiv 2m_{E}/m_{T}$ .) 

The two parameters are related as follows: 

$$
\gamma = \frac {1}{1 + \beta},\tag{6.39}
$$

$$
\beta = \frac {1}{r} - 1.\tag{6.40}
$$

Thus (6.35) and (6.36) can also be expressed in terms of $\beta$ : 

$$
c _ {\mathrm{mL}} = \frac {C _ {\mathrm{T}}}{m _ {\mathrm{L}}} = \frac {C _ {\mathrm{T}}}{m _ {\mathrm{T}}} (1 + \beta),\tag{6.41}
$$

$$
c _ {\mathrm{tmL}} = \frac {C _ {\mathrm{T}}}{m _ {\mathrm{L}} w} = \frac {C _ {\mathrm{T}}}{m _ {\mathrm{T}} w} (1 + \beta).\tag{6.42}
$$

Combining (6.42) and (6.30) yields 

$$
c _ {\mathrm{tmL}} = \frac {1}{w} \left(\frac {\alpha_ {0}}{m _ {\mathrm{T}}} + \alpha_ {1}\right) (1 + \beta).\tag{6.43}
$$

Values of $c_{tmL}$ are shown in table 6.2 for a range of values of $\beta$ and for three sets of parameter values. The results are displayed in figures 6.11 and 6.12, with the average payload w taken as 20 tons. 

These results show that owner-operator costs are sensitive to assumptions about $m_{T}$ and $\beta$ as well as to alternative cost assumptions. While precise data are not available about any of these elements, the numerical results, together with informed judgments, do provide a basis for important policy conclusions. 

For example, in figure 6.12 the lines RR-1 and RR-2 correspond, respectively, to the estimated average rail rate for grain, coal, and canned goods and to the estimated average rail rate for iron and steel. An owner-operator who records 100,000 miles per year, a commonly occurring figure according to Wyckoff and Maister, and incurs approximately 10 percent empty backhaul or less can compete with rail for coal, grain, and canned goods if he is an efficient, low-cost-estimate operator. If he is very productive, covering 150,000 miles per year, he can still be competitive with 25 percent empty backhaul. Competing for steel traffic, even a medium-cost operator can be competitive with only 100,000 miles per year and a 30 percent empty backhaul (Wyckoff and Maister 1975, pp. 110–112). 

Wyckoff and Maister undertook this analysis “to examine the long-term viability of the owner-operator as a competitor to the railroads and other bulk-volume carriers” (p. 23). They concluded that “the owner-operator is able to provide transportation at costs that are directly 


Table 6.2 Owner-operator trucking cost as a function of major parameters


<table><tr><td rowspan="2">Cost estimate</td><td rowspan="2"><eq>\alpha_0</eq>($)</td><td rowspan="2"><eq>\alpha_1</eq>($/mile)</td><td rowspan="2">Total annual mileage (<eq>m_T</eq>)</td><td colspan="4"><eq>c_{tmL}</eq>(¢/ton-mile) for β =</td></tr><tr><td>0%</td><td>25%</td><td>50%</td><td>100%</td></tr><tr><td rowspan="3">Low</td><td rowspan="3">28,100</td><td rowspan="3">0.197</td><td>75,000</td><td>2.86</td><td>3.57</td><td>4.29</td><td>5.72</td></tr><tr><td>100,000</td><td>2.39</td><td>2.99</td><td>3.59</td><td>4.77</td></tr><tr><td>150,000</td><td>1.92</td><td>2.40</td><td>2.88</td><td>3.84</td></tr><tr><td rowspan="3">Medium</td><td rowspan="3">36,200</td><td rowspan="3">0.242</td><td>75,000</td><td>3.62</td><td>4.53</td><td>5.44</td><td>7.25</td></tr><tr><td>100,000</td><td>3.02</td><td>3.78</td><td>4.53</td><td>6.04</td></tr><tr><td>150,000</td><td>2.42</td><td>3.02</td><td>3.63</td><td>4.83</td></tr><tr><td rowspan="3">High</td><td rowspan="3">50,300</td><td rowspan="3">0.260</td><td>75,000</td><td>4.65</td><td>5.82</td><td>6.98</td><td>9.31</td></tr><tr><td>100,000</td><td>3.82</td><td>4.77</td><td>5.72</td><td>7.63</td></tr><tr><td>150,000</td><td>2.98</td><td>3.72</td><td>4.47</td><td>5.95</td></tr></table>


Source: Developed by linear regression on the results of Wyckoff and Maister (1975), table 3-3. Some numbers differ slightly because of approximations due to the linear cost function equation assumed here. Figures are for owner-operators operating on a lease basis. Costs are estimated for mid-1974. An average payload of 20 tons is assumed. 


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/fc366feb-933b-4442-bcbf-4538c4ada340/629b6db005cdbcb74786067d957624f1273ee736d42729c27d12aaebdc44a449.jpg)



Figure 6.11 Owner-operator cost per ton-mile as a function of mileage ( $\beta = 0$ , w = 20 tons).


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/fc366feb-933b-4442-bcbf-4538c4ada340/9b7036a5eeb1161bb89b715fa8dd595298867635aa78d9d28cf51f2f40d4f296.jpg)



Figure 6.12 A comparison of railroad and truck costs.


competitive with rates of rail-secure traffic" (p. 37). That is, since an owner-operator running 100,000 miles per year can offer his services at a rate of 2.5–3.0 ¢/ton-mile, he can compete effectively with railroads for such traffic as canned goods, for which the rate is 3.5 ¢/ton-mile for moves of 500–700 miles; steel moving at 3.7 ¢/ton-mile for moves up to 1,100 miles; and grain moving at 2.6 ¢/ton-mile up to 1,200 miles. 

It is a common assumption that trucking is an inherently more expensive mode of transportation than rail. In contrast to this conventional wisdom the Wyckoff-Maister analysis showed that certain types of truckers can, under certain conditions, become “price-competitive as well as service-competitive with railroads” (p. xviii). 

This example demonstrates the type of policy conclusion that can sometimes be drawn from an analysis of cost functions. Note also that the analysis is an approximation of an equilibrium analysis, in that $\beta$ is very similar to a load factor, reflecting what can be achieved in the market. 

## 6.6 THE LIMITS OF COST FUNCTION ANALYSIS

Analysis of cost functions, and particularly analysis of the marginal and average costs and the fixed and variable components of costs, can assist one in understanding how and why selected impacts vary as options are varied. The analyst should, however, keep in mind several cautions that have been raised throughout this discussion: 

1. Monetary costs are only a portion of the relevant impacts. It is useful to look at many other dimensions of resource consumption (grams of air pollutants, acres of land) with the same methodology. 

2. Various measures of output may be useful. In particular, use of equilibrium measures such as $V_{E}$ may give conclusions different from capacity measures such as $V_{C}$ . 

3. A cost function is not an acceptable basis for making a decision; that is, even if technology A has the least total monetary cost to the operator at volumes less than V, this does not mean that it is the optimal choice. A complete equilibrium analysis is necessary to take into account, for example, variations in service levels and their effect on actual volumes and thus net revenues. 

As an example figure 6.13 shows the net revenues of two technologies, A and B. If they both have the same service levels at all volumes, then they will have the same gross revenue curve $I_{GR}^{1}$ and the same net revenues at $V_{1}$ , where their costs are equal (and only at $V_{1}$ ); the points of maximum net revenue will be $V_{2}$ and $V_{3}$ , respectively. In this case the technology with the lowest average cost at any volume V will also have the lowest net revenue; for values less than $V_{1}$ technology B has lower total and average cost and higher net revenue than A. If, on the other hand, there are differences in service levels, then the volumes at which net revenues are equal will necessarily be different from the volumes at which costs are equal. For example, let the service levels be such that technology A produces $I_{GR}^{1}$ while B produces $I_{GR}^{2}$ . Then the point of equal net revenues shifts to $V_{5}$ , different from $V_{1}$ . (Note that the point of maximum net revenue shifts from $V_{2}$ to $V_{4}$ .) 

Thus, since in general no two technologies can have precisely the same service levels, analysis on the basis of cost functions alone can often be misleading. 

To overcome this limitation an important early comparison of urban transportation options (Meyer, Kain, and Wohl 1965) used what might be called an equivalent-service approach. In this approach all options are tailored to provide the same or equivalent levels of service. Then the options can be compared strictly on the basis of cost. For example, in the cited study various forms of bus rapid transit, rail rapid transit, and automobile were compared by developing the total cost as a function of volume for various geographic and demographic configurations: 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/fc366feb-933b-4442-bcbf-4538c4ada340/1672021da48f103d156b185173b706bcf9d69dc3f1f920b6b18b8af74e5e0af0.jpg)



Figure 6.13 A comparison of two technologies, showing the effect of differences in service levels and thus the limitations of an analysis on the basis of cost functions alone.


The reported costs of specific travel modes were computed while observing certain service constraints which, it was hypothesized, put all modes at about the same advantage or disadvantage and therefore permitted a determination of the “best” mode on the basis of cost considerations alone. This analytic approach is sound enough so long as we can assume that all travelers attach about the same values to travel time savings, avoidance of transfers, schedule frequency, and the like, and that the service standards established accord with these values. It is more realistic, however, to take human differences into account. Some travelers would pay dearly to save time on the work-trip; others would not. Some travelers highly value privacy, personal comfort, and convenience; others are relatively unconcerned. . . . In sum, aspects of cost, price, service, and the specific demand characteristics of the traveling public are vitally important and must be integrated and synthesized to arrive at the most effective and economic choice or combination of choices in any particular application. (Meyer, Kain, and Wohl 1965, pp. 305–306; emphasis added) 

This same approach has been used in a number of recent studies (Boyd, Asher, and Wetzler 1976, Bhatt 1976, Deen, Kulash, and Baker 1976). 

This approach can be useful under some highly specialized conditions, but it ignores the basic fact that each mode provides relatively unique service characteristics. This can lead to serious errors; the different service attributes offered by each option should be considered explicitly as they are perceived by users and reflected in the demand functions (Vuchic 1976, Manheim 1977b). The most generally valid approach remains that described in chapter 5, based on explicit options, systematic analysis, explicit travel-market equilibration, and explicit prediction of impacts on different interests and display of trade-offs. 

## 6.7 AN OVERVIEW OF VEHICLE CYCLE ECONOMICS

We now return to the vehicle cycle and apply the concepts developed in preceding sections. 

The characteristics of the vehicle cycle in a particular situation can profoundly influence the impacts on users and on operators, especially in terms of economics. The basic logic of this influence is straightforward, though it takes different forms in different contexts. In this section we shall explore the economics of the vehicle cycle and derive some basic relationships. These will be illustrated and extended in later sections. 

## 6.7.1 A Cost Perspective

First, we consider the cost to the vehicle operator. Let 

$C_{VA}$ = equivalent annual ownership cost of a vehicle, taking into account useful life, salvage value, and the cost of capital, 

a = all other costs per unit of available capacity, 

X = units of available capacity per year (for example, vehicle cycles, vehicle-miles, or ton-miles). 

Then the total annual cost per vehicle, including ownership and other costs (but excluding nonvehicle costs), is 

$$
C _ {\mathrm{T}} = C _ {\mathrm{VA}} + a X,\tag{6.44}
$$

and the average total cost per unit of available capacity is 

$$
\bar {C} _ {\mathrm{T}} = \frac {C _ {\mathrm{VA}}}{X} + a.\tag{6.45}
$$

Thus, as in all cases of fixed costs, the average cost per unit drops as the number of units of available capacity increases. 

The available capacity X is often called the utilization, especially when the sense is that available capacity is utilized for productive (revenue) service. As the examples will show, it is common in the analysis of rail systems to talk of the utilization of a freight car as the number of cycles or “turns” that can be accomplished per year; in the analysis of air systems the utilization is usually defined as the number of revenue flight hours per year (though sometimes total flight or “block” hours are used also). We see no reason to fix on a single definition of utilization. Different definitions will be useful in different analyses. Further, any simple definition can be misleading for some analytical needs. We shall use utilization as a generic concept, as in “the utilization of the available resources,” and shall employ more precise definitions as appropriate. 

## A RAIL EXAMPLE

Consider a railcar for which the annual cost of ownership is $C_{VA} = \$1,600$ . Rail analysts often use the number of car cycles as a measure of the number of loads that can be delivered in a year (implicitly, one full load is delivered for each cycle). Let $X_{CC}$ be the number of car cycles (or loads delivered) per year and assume that other costs of 


Table 6.3 Effects of railcar utilization


<table><tr><td>Utilization (cycles per year)</td><td>Total cost ($/year)</td><td>Average cost ($/cycle)</td><td>Vehicle ownership cost fraction <eq>\left( {{C}_{\mathrm{{VA}}}/{C}_{\mathrm{T}}}\right)</eq></td></tr><tr><td>12</td><td>8,800</td><td>733.33</td><td>0.18</td></tr><tr><td>15</td><td>10,600</td><td>706.67</td><td>0.15</td></tr><tr><td>18</td><td>12,400</td><td>688.89</td><td>0.13</td></tr><tr><td>21</td><td>14,200</td><td>676.19</td><td>0.11</td></tr><tr><td>24</td><td>16,000</td><td>666.67</td><td>0.10</td></tr><tr><td>27</td><td>17,800</td><td>659.26</td><td>0.09</td></tr><tr><td>30</td><td>19,600</td><td>653.33</td><td>0.08</td></tr><tr><td>33</td><td>21,400</td><td>648.48</td><td>0.07</td></tr><tr><td>36</td><td>23,200</td><td>644.44</td><td>0.01</td></tr></table>

operation amount to a = $600 per cycle. Then the total cost and average cost per cycle are 

$$
C _ {\mathrm{T}} = 1, 6 0 0 + 6 0 0 X _ {\mathrm{cc}},\tag{6.46}
$$

$$
\bar {C} _ {X _ {\mathrm{cc}}} = 6 0 0 + \frac {1 , 6 0 0}{X _ {\mathrm{cc}}}\tag{6.47}
$$

Table 6.3 shows the effects of changes in the number of productive car cycles per year. The table also shows the ratio $C_{VA}/C_{T}$ , which demonstrates the importance of utilization in the relative composition of costs. 

Consider a situation in which the utilization is 15 cycles per year and the average revenue is $700 per cycle, resulting in a loss of $6.67 per cycle. As the table shows, if the number of cycles were increased to 18 and if the average revenue per cycle remained the same, the operator would gain a net revenue of $700.00 – $688.89 = $11.11 per cycle. This illustrates the profound effect of the vehicle cycle on the economics of a system. 

## AN AIR EXAMPLE

Consider an aircraft for which the annual cost of ownership is $C_{VA} = \$500,000$ per year. Typically airline planners are interested in the number of hours per year an aircraft can be utilized in productive service (“airborne revenue hours”). Let $X_{HU}$ be the number of useful vehicle-hours per year and assume that other costs of operation amount to 


Table 6.4 Characteristics of three types of jet aircraft


<table><tr><td rowspan="2">Type</td><td rowspan="2">Seats</td><td colspan="2">Costs</td><td rowspan="2">Typical utilization (revenue hours per year)</td></tr><tr><td><eq>C_{\text{VA}}</eq> ($ × 106)</td><td>a ($ per useful vehicle-hour)</td></tr><tr><td>A</td><td>140</td><td>0.50</td><td>950</td><td>2,832</td></tr><tr><td>B</td><td>234</td><td>1.32</td><td>1,300</td><td>2,538</td></tr><tr><td>C</td><td>342</td><td>2.00</td><td>1,780</td><td>2,969</td></tr></table>


Source: Civil Aeronautics Board (1975). 


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/fc366feb-933b-4442-bcbf-4538c4ada340/6b38043ef1f091b4b7cbccb8a6a8aeb1d73b21f817c35f5366e13bd1c59ec160.jpg)



Figure 6.14 The effect of the utilization on the relative costs of three types of jet aircraft.


a = $950 per useful vehicle-hour. Then the total cost and average total cost per useful vehicle-hour are 

$$
C _ {\mathrm{T}} = 5 0 0, 0 0 0 + 9 5 0 X _ {\mathrm{HU}},\tag{6.48}
$$

$$
\bar {C} _ {X _ {\mathrm{HU}}} = 9 5 0 + \frac {5 0 0 , 0 0 0}{X _ {\mathrm{HU}}}.\tag{6.49}
$$

For example, at $X_{\text{HU}} = 2,500$ hours per year, $\bar{C}_{X_{\text{HU}}} = \$1,150$ and $C_{\text{T}} = \$2,880,000$ . 

Table 6.4 gives the characteristics of three types of jet aircraft. The average costs per seat per hour are shown for a range of utilizations in figure 6.14. Note that at low utilizations A has a lower cost per available seat per hour, but this is reversed at high utilizations. (A and B have the same cost per available seat per hour at a utilization of 1,682 hours.) 

## 6.7.2 A Net Revenue Perspective

As noted in chapter 5 and in section 6.6, a focus on costs and available capacity can be quite misleading. What is most important to the operator—and to the user too—is the actual usage (the equilibrium volume) and the implications of both costs and usage for net revenue (or similar measures from the operator's perspective). 

To extend the preceding discussion we define the following variables (note that we distinguish capacity available by subscripts C and capacity utilized or revenue units by subscripts E, denoting equilibrium volumes): 

$I_{NR}$ = net revenue per year for a fleet of vehicles, 

N = number of vehicles in the fleet, 

$X_{C}$ = number of units of available capacity per vehicle per year (cycles, flying hours, vehicle-miles), 

$X_{E}$ = number of revenue units (units of capacity actually utilized per vehicle per year), 

$\lambda = \text{load factor (fraction of available capacity actually utilized)},$ 

$r_{VE} = net revenue per vehicle per revenue unit,$ 

$r_{VC}$ = net revenue per vehicle per unit of available capacity, 

p = price charged per unit of utilized capacity, 

a = operating cost per unit of available capacity, 

$C_{VA}$ = equivalent annual vehicle ownership cost, 

$C_{\mathrm{T / V}} =$ total cost per vehicle, 

$I_{GR/V} = gross revenue per vehicle,$ 

$I_{\mathrm{NR / V}} =$ net revenue per vehicle. 

Then, as before, we have 

$$
C _ {\mathrm{T/V}} = C _ {\mathrm{VA}} + a X _ {\mathrm{C}},\tag{6.50}
$$

$$
I _ {\mathrm{GR/V}} = X _ {\mathrm{E}} p,\tag{6.51}
$$

$$
I _ {\mathrm{NR/V}} \equiv I _ {\mathrm{GR/V}} - C _ {\mathrm{T/V}} = X _ {\mathrm{E}} p - a X _ {\mathrm{C}} - C _ {\mathrm{VA}}.\tag{6.52}
$$

Since 

$$
\lambda \equiv \frac {X _ {\mathrm{E}}}{X _ {\mathrm{C}}},\tag{6.53}
$$

$$
I _ {\mathrm{NR/V}} = X _ {\mathrm{C}} (\lambda p - a) - C _ {\mathrm{VA}},\tag{6.54}
$$

and, for the fleet as a whole, 

$$
I _ {\mathrm{NR}} = N I _ {\mathrm{NR/V}} = N [ X _ {\mathrm{C}} (\lambda p - a) - C _ {\mathrm{VA}} ].\tag{6.55}
$$

It is useful to write this differently. We take 

$$
\begin{array}{r l} r _ {\mathrm{VE}} \equiv \frac {I _ {\mathrm{NR/V}}}{X _ {\mathrm{E}}} & = p - a \frac {X _ {\mathrm{C}}}{X _ {\mathrm{E}}} - \frac {C _ {\mathrm{VA}}}{X _ {\mathrm{E}}} \\ & = p - \frac {a}{\lambda} - \frac {C _ {\mathrm{VA}}}{\lambda X _ {\mathrm{C}}}, \end{array}\tag{6.56}
$$

$$
\begin{array}{r l} r _ {\mathrm{VC}} \equiv \frac {I _ {\mathrm{NR/V}}}{X _ {\mathrm{C}}} & = \lambda p - a - \frac {C _ {\mathrm{VA}}}{X _ {\mathrm{C}}} \\ & = \lambda r _ {\mathrm{VE}}. \end{array}\tag{6.57}
$$

Since 

$$
I _ {\mathrm{NR/V}} = r _ {\mathrm{VE}} X _ {\mathrm{E}} = r _ {\mathrm{VE}} X _ {\mathrm{C}} \lambda ,\tag{6.58}
$$

for the fleet as a whole we have 

$$
I _ {\mathrm{NR}} = N r _ {\mathrm{VE}} X _ {\mathrm{C}} \lambda\tag{6.59}
$$

and, comparing two alternative strategies $T^{0}$ and $T^{1}$ , 

$$
\frac {I _ {\mathrm{NR}} ^ {1}}{I _ {\mathrm{NR}} ^ {0}} = \frac {N ^ {1}}{N ^ {0}} \frac {r _ {\mathrm{VE}} ^ {1}}{r _ {\mathrm{VE}} ^ {0}} \frac {X _ {\mathrm{C}} ^ {1}}{X _ {\mathrm{C}} ^ {0}} \frac {\lambda^ {1}}{\lambda^ {0}}.\tag{6.60}
$$

These relationships will be used in the following discussions. 

## 6.7.3 Influence of the Vehicle Cycle on Costs and Revenues

The relationship presented above relates costs and revenues to general measures of available capacity and units of utilized capacity. We now focus specifically on the vehicle cycle, as illustrated by the railcar example of section 6.7.1, where the utilization is $X_{\mathrm{CC}}$ , the number of vehicle cycles per year. 

255 Vehicle Cycle and Analysis of Cost Functions 

Consider a possible change in transportation strategy from $T^{0}$ to $T^{1}$ , which will affect the vehicle cycle in one or more ways, resulting in changes in the total vehicle cycle time $t_{VC}$ . Changes in $t_{VC}$ can have several important effects: 

1. A decrease in cycle time can mean an increase in $X_{cc}$ . 

2. An increase in $X_{cc}$ can reduce the average cost per cycle by spreading the vehicle ownership cost $C_{VA}$ over a larger number of cycles. 

3. A reduction in average cost per cycle can result in an increase in net revenue per vehicle per cycle $r_{VC}$ if the average cost per cycle is decreased and/or if the additional cycles made available can be utilized for revenue service. 

4. An increase in demand (or more precisely equilibrium volume)—the number of cycles utilized in revenue service—can result from (i) the direct effect of the change in cycle time on service as perceived by users; (ii) changes in price made feasible or necessary by changes resulting from changes in cycle time; or (iii) the effect on other aspects of service quality of actions taken to implement the change in cycle time. 

5. Changes in demand, or in the cycles available per vehicle, can affect required fleet size N. 

Equation (6.60) demonstrates this. A change in $t_{VC}$ can bring about an increase in $I_{NR}$ if there is an increase in $r_{VE}$ , $X_{CC}$ , N, or $\lambda$ . These relationships are illustrated in figure 6.15. 

It should be emphasized that these relationships leave out factors that may be significant in a particular situation. For example, there may be costs incurred in implementing the change in vehicle cycles, such as a guideway improvement, that are not shown in the above formulas; moreover vehicle life, maintenance costs, and depreciation considerations may change. 

## 6.8 A RAIL SYSTEM CASE STUDY

## 6.8.1 The Burlington Northern Experience

In section 6.2.6 we examined the cycle of the typical U.S. railcar and showed the very small fraction of time the vehicle is actually in motion. One of many possible points of leverage on the railcar cycle is the amount of time during which a car is under control of the shipper or the receiver, waiting to be loaded or unloaded. A recent attempt to influence shipper behavior is illuminating. 

In December 1971 the Burlington Northern Railroad introduced incentive rates for the movement of grain in covered hopper cars (Burress 1975). These incentive rates offered shippers a substantially reduced price per load (with some reduced ancillary services by the railroad), if an empty car was loaded within 10 daylight hours after delivery to the shipper and the loaded car was unloaded within 48 hours after delivery to the receiver. The penalties for violating these time limits (called demurrage charges) were severe—$80 per day versus $5–$10 per day under then-current rates. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/fc366feb-933b-4442-bcbf-4538c4ada340/f3a295112761210081e2f4f67c2e41651885b68c84409fb5f0177f6d62a12371.jpg)



Table 6.5 Effect of incentive rate


<table><tr><td></td><td>Average time before incentive rate</td><td>Average time after incentive rate</td><td>Average time savings</td></tr><tr><td colspan="4">Time at origin</td></tr><tr><td>1. Daylight loading hours from placement to release</td><td>20:02a(0.83)</td><td>6:64(0.24)</td><td>13:1(0.55)</td></tr><tr><td>2. Total loading hours from placement to release</td><td>41:38(1.73)</td><td>11:38(0.48)</td><td>30:10(1.26)</td></tr><tr><td>3. Total hours from placement to departure from origin station (removal from shipper location)</td><td>68:17(2.85)</td><td>32:24(1.35)</td><td>35:53(1.50)</td></tr><tr><td colspan="4">Time in transit</td></tr><tr><td>4. Time from origin to destination terminal</td><td>89:29(3.73)</td><td>76:34(3.19)</td><td>12:56(0.54)</td></tr><tr><td colspan="4">Time at destination</td></tr><tr><td>5. Time from arrival at destination terminal to placement at receiverb</td><td>94:09(3.92)</td><td>44:10(1.84)</td><td>49:59(2.08)</td></tr><tr><td>6. Time from placement at receiver until unloaded and released</td><td>85:26(3.56)</td><td>47:02(1.96)</td><td>38:24(1.60)</td></tr><tr><td colspan="4">Total movement timec</td></tr><tr><td>(3 + 4 + 5 + 6)</td><td>337:26(14.06)</td><td>200:09(8.34)</td><td>137:16(5.72)</td></tr></table>


$^{a}$ Hours:minutes (days in decimal fractions in parentheses). 



$^{b}$ Or until placement at interchange to connecting carrier. 



$^{c}$ Excluding time spent for return move empty or times moving loaded over other carriers. Total cycle times went from 25 to 19 days, based on estimates from other sources.
Source: Burress (1975). Data two months after the introduction of rates. 


These changed incentives did lead to changed behavior on the part of customers (see table 6.5). Average total loaded movement time was decreased by 5.72 days out of an original time of 17 days, a reduction of 40.7 percent. This can be translated into a savings in the number of car-days required to move a given volume of grain. In 1971 Burlington Northern moved approximately 30,000 carloads of grain over the routes covered by these new rates. A saving of 5.72 days per load released more than 170,000 additional car-days during that period. These could have been used to carry other traffic, or alternatively Burlington Northern could have reduced its investment in this type of car. 

On first glance this seems like a very attractive move. But we must be careful: What steps were taken to implement this strategy? What were the overall impacts on costs and revenues? After all, the incentive rate offered was a reduction of 25 percent. Although the increased time savings resulted in a decrease in costs, did the net revenue increase or decrease with this drop in price? To answer these questions we need a more detailed analysis. 

It was reported that, after introduction of the incentive rates, the railroad's volume doubled (market share went from 40 to 80 percent) and the cycle time went from about 25 to 19 days, so 

$$
\frac {V _ {\mathrm{E}} ^ {1}}{V _ {\mathrm{E}} ^ {0}} = \frac {X _ {\mathrm{E}} ^ {1}}{X _ {\mathrm{E}} ^ {0}} = 2,\tag{6.61}
$$

$$
\frac {p ^ {1}}{p ^ {0}} = \frac {1 - 0 . 2 5}{1} = \frac {3}{4}.\tag{6.62}
$$

$$
\mathrm{Since} X _ {\mathrm{CC}} = 3 6 5 / t _ {\mathrm{VC}}, \text {we have}\tag{6.63}
$$

$$
\frac {X _ {\mathrm{CC}} ^ {1}}{X _ {\mathrm{CC}} ^ {0}} = \frac {t _ {\mathrm{VC}} ^ {0}}{t _ {\mathrm{VC}} ^ {1}} = \frac {2 5}{1 9} = 1. 3 2.\tag{6.64}
$$

If we assume that the fleet was fully utilized in both cases ( $\lambda^{1} = \lambda^{0} = 1$ ) and was expanded to meet the demand, then 

$$
N = \frac {V _ {\mathrm{E}}}{w X _ {\mathrm{CC}} \lambda},\tag{6.65}
$$

$$
\frac {N ^ {1}}{N ^ {0}} = \frac {V _ {\mathrm{E}} ^ {1} / V _ {\mathrm{E}} ^ {0}}{X _ {\mathrm{CC}} ^ {1} / X _ {\mathrm{CC}} ^ {0}} = \frac {2}{1 . 3 2} = 1. 5 2.\tag{6.66}
$$

Suppose the following unit values were applicable. (The numbers are hypothesized to illustrate the possible consequences of the reported relative changes in volumes, prices, and cycle times.) For the initial conditions, 

$$
\begin{array}{r l} t _ {\mathrm{VC}} ^ {0} & = 2 5 \text {days}, \\ p ^ {0} & = 1, 5 0 0 / \text {carload}, \\ a ^ {0} & = 6 0 0 / \text {cycle}, \end{array}
$$

$$
\begin{array}{r l} {V _ {\mathrm{E}} ^ {0}} & {= 3 0, 0 0 0 \mathrm{carloads/year},} \\ {C _ {\mathrm{VA}}} & {= 1, 6 0 0 / \mathrm{vehicle}.} \end{array}
$$

After the change, 

$$
t _ {\mathrm{VC}} ^ {1} = 1 9 \mathrm{days},
$$

$$
p ^ {1} = \frac {3}{4} p ^ {0} = 1, 1 2 5 / \text {carload},
$$

$$
a ^ {1} = 6 2 5 / \text {cycle},
$$

$$
V _ {\mathrm{E}} ^ {1} = 2 V _ {\mathrm{E}} ^ {0} = 6 0, 0 0 0 \text { carloads / year }.
$$

Then, with $\lambda = 1$ and w = 1 carload (1 cycle = 1 carload), 

$$
X _ {\mathrm{CC}} ^ {0} = \frac {3 6 5}{2 5} = 1 4. 6 \text { cycles / year },\tag{6.67}
$$

$$
N ^ {0} = \frac {V _ {\mathrm{E}} ^ {0}}{w X _ {\mathrm{CC}} ^ {0}} = \frac {3 0 , 0 0 0}{1 4 . 6} = 2, 0 5 5,\tag{6.68}
$$

$$
\begin{array}{l} r _ {\mathrm{VE}} ^ {0} = p ^ {0} - \frac {a ^ {0}}{\lambda} - \frac {C _ {\mathrm{VA}}}{\lambda X _ {\mathrm{CC}} ^ {0}} = (1, 5 0 0 - 6 0 0) - \frac {1 , 6 0 0}{1 4 . 6} = 9 0 0 - 1 0 9. 5 9 \\ =   \text {   } 7 9 0. 4 1 / \text {cycle}, \end{array} \tag {6.69}
$$

$$
I _ {\mathrm{NR/V}} ^ {0} = X _ {\mathrm{CC}} ^ {0} r _ {\mathrm{VE}} ^ {0} = (1 4. 6) (7 9 0. 4 1) = 1 1, 5 4 0 / \text {vehicle}.\tag{6.70}
$$

$$
I _ {\mathrm{NR}} ^ {0} = N ^ {0} X _ {\mathrm{CC}} ^ {0} r _ {\mathrm{VE}} ^ {0} = 2, 0 5 5 (1 1, 5 4 0) = 2 3. 7 1 \text { million }.\tag{6.71}
$$

For the new conditions, 

$$
X _ {\mathrm{CC}} ^ {1} = \frac {3 6 5}{1 9} = 1 9. 2 1 \text { cycles / year },\tag{6.72}
$$

$$
N ^ {1} = \frac {V _ {\mathrm{E}} ^ {1}}{w X _ {\mathrm{CC}} ^ {1} \lambda} = \frac {6 0 , 0 0 0}{1 9 . 2 1} = 3, 1 2 3,\tag{6.73}
$$

$$
\varDelta N = N ^ {1} - N ^ {0} = 3, 1 2 3 - 2, 0 5 5 = 1, 0 6 8,\tag{6.74}
$$

$$
\begin{array}{r l} r _ {\mathrm{VE}} ^ {1} & = \left(p ^ {1} - \frac {a ^ {1}}{\lambda}\right) - \frac {C _ {\mathrm{VA}}}{\lambda X _ {\mathrm{CC}} ^ {1}} = (1, 1 2 5 - 6 2 5) - \frac {1 , 6 0 0}{1 9 . 2 1} \\ & = 5 0 0 - 8 3. 2 9 =   \text {   } 4 1 6. 7 1 / \text {cycle}, \end{array}\tag{6.75}
$$

$$
I _ {\mathrm{NR/V}} ^ {1} = X _ {\mathrm{CC}} ^ {1} r _ {\mathrm{VE}} ^ {1} = (1 9. 2 1) (4 1 6. 7 1) = 8, 0 0 5 / \text {vehicle}.\tag{6.76}
$$

Thus 

$$
\frac {r _ {\mathrm{VE}} ^ {1}}{r _ {\mathrm{VE}} ^ {0}} = \frac {4 1 6 . 7 1}{7 9 0 . 4 1} = 0. 5 3,\tag{6.77}
$$

$$
\frac {X _ {\mathrm{CC}} ^ {1}}{X _ {\mathrm{CC}} ^ {0}} = \frac {1 9 . 2 1}{1 4 . 6} = 1. 3 2,\tag{6.78}
$$

$$
\frac {N ^ {1}}{N ^ {0}} = \frac {3 , 1 2 3}{2 , 0 5 5} = 1. 5 2,\tag{6.79}
$$

and, by (6.60), 

$$
\frac {I _ {\mathrm{NR}} ^ {1}}{I _ {\mathrm{NR}} ^ {0}} = (1. 5 2) (0. 5 3) (1. 3 2) = 1. 0 5.\tag{6.80}
$$

We also have 

$$
\frac {I _ {\mathrm{NR/V}} ^ {1}}{I _ {\mathrm{NR/V}} ^ {0}} = \frac {8 , 0 0 5}{1 1 , 5 4 0} = 0. 6 9.\tag{6.81}
$$

Thus, in this case: 

1. Net revenue increases. 

2. Net revenue per car per cycle decreases by a factor of 0.53, primarily because of the substantial price decrease. 

3. Even though cycles per car per year increase by a factor of 1.32, net revenue per car per year still decreases by a factor of 0.69 because of the substantial decrease in net revenue per car per cycle. 

4. The volume of cars that can be productively utilized increases by a factor of 1.52; net revenue of the fleet therefore increases even though net revenue per car decreases. 

This example demonstrates that improvements in cycle time can have significant economic effects. Whether or not these effects result in an increase in net revenue (or an improvement in other pertinent economic measures) can depend on some relatively subtle interactions (see, for example, Martland, Assarabowski, and McCarren 1977, sec. 2.3). 

The example also demonstrates that while the performance of a single vehicle is important, our primary concern should be the performance of the fleet as a whole, since net revenue for the fleet can increase even when net revenue per car decreases. We shall explore this idea further in chapter 7. 

## 6.8.2 Implications of Vehicle-Cycle Considerations for Railroad System Policy

We have now developed the relationship of the vehicle cycle to the economic issues relevant to the operator (and ultimately to the user) as reflected in costs and revenues. For most modes and most situations these relationships are of great importance. To illustrate we shall examine some current policy-oriented transportation systems research in the U.S. railroad industry. This research is a joint effort of the industry, the federal government, and a university research team (Industry Task Force 1975). 

In the United States the utilization of railcars has become a major political and economic issue. In some regions and for some seasons of the year, shippers have difficulty obtaining enough railcars to ship their commodities to market: 

Over the years, depending on the economic level of activity, shippers have not received the number of cars requested for certain commodities during peak loading periods of the year. Their expressions of concern have created a widespread conviction that there have indeed been extensive car shortages. Further, inflationary trends in the costs of purchasing new equipment and the debt financing associated with such purchases have added to the concern of the industry about replacing existing fleets of equipment. (Industry Task Force 1975, p. iv) 

Rapidly escalating freight car costs and interest rates have pushed the problem of car utilization to the fore in recent years. Given the current average turnaround times and rates, the return on new freight cars barely covers their capital costs. Many roads, not only the bankrupt roads, are no longer able to profitably finance even their minimum freight car needs. As a result, these roads are forced to rely heavily on foreign cars and the industry as a whole fails to satisfy the demand for cars during peak loading seasons. Although the problem of car supply has lessened during the current recession, there is no reason to believe it will not once again be common after the economy starts to recover. Further, the financial aspects relating to return on investment have worsened. When economic recovery does occur, the industry must decide whether to invest heavily in equipment, which at best is marginally profitable, or to attempt a comprehensive program for improving car utilization, which would have the same effective impact on car supply. (pp. 1–2) 

Utilization has at least four aspects important to shippers and rail operator management (p. 7): 

1. cycle time, or the average time between successive car loadings; 

2. capacity utilization, or the average degree to which a load fills a car; 

3. serviceability, or the fraction of time that a car is available for service; 

4. life time. 

## The Industry Task Force notes that

an improvement in car utilization could be achieved by reduction in the percent of time a car is unserviceable, a reduction in car cycle time, a decrease in empty line-haul miles, and an increase in the percentage of volume or weight capacity used by shippers. A quantitative assessment of the potential for improvement can be made when an adequate data base on car cycles is available. Analysis of these car cycles from load to load would reveal the fraction of time a car spends being moved by the railroad and being unloaded. These car cycles would also identify the time a car spends after unloading until it is spotted for loading at a shipper's dock. In each of these segments of the car cycle, a different set of changes in practice may be required to improve utilization. (p. iv) 

In response to this identification of a problem and realization of the importance of improving vehicle utilization as one approach to resolving the problem, a major research program is under way, focusing particularly on reliability of service and its impact on the car cycle. Reliability is “the amount of variability in rail trip times.” The reliability of rail system operations can have a significant impact on utilization, especially the cycle time. As illustrated in figure 6.16, an improvement in reliability 

will have both direct and indirect impacts leading to an increase in the level of car utilization. . . . Most actions that improve reliability will also reduce average trip times as well; this results in a shorter trip time for loads and allows the railroad to distribute empty cars more rapidly and effectively. These changes in rail performance, once they are perceived by shippers, should in turn lead to the indirect impacts noted in the [figure]. As a result of the shorter trip times and the higher degree of reliability, shippers and receivers will perhaps be able to plan loading and unloading operations more effectively, thereby shortening the time that cars remain in their control. If the service improvements persist, the railroad should also begin to capture a larger share of the traffic moving over the corridors affected by the change. With higher traffic levels, the railroad may be able to increase the frequency of some trains or to add new blocks to existing trains, thereby further reducing average trip times. Together, the direct and indirect impacts that promote better car utilization should lead to a reduced need for new freight cars or, if traffic conditions are favorable, to an ability to move more traffic with the same number of cars. Finally, the change in capital costs and in net railway operating income will, for a successful strategy, raise profitability. (pp. 9–11) 

This relationship between reliability and utilization has important implications for research strategy. Particular attention has been given to assessing rail system reliability in order to predict the effects of possible strategies that might lead to improvements in both mean trip time and trip time reliability: "The conceptual framework suggests the kinds of models that are needed to evaluate alternatives for improving reliability and car utilization. Models are needed to predict: 

- Reliability and trip time improvements as a function of changes in operations, investments, and institutional arrangements. 

- The impacts of service improvements on empty car distribution, shippers' detention of cars, and traffic levels. 

- Freight car utilization as a function of railroad and shipper policies. 

- Profitability as a function of the changes in capital costs, operating costs, and revenues" (pp. 9–11). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/fc366feb-933b-4442-bcbf-4538c4ada340/00f9c71c97f78ca9d72d583debd5291798dbb21c244ab2b9730a122228ecf575.jpg)



Figure 6.16 Influence of reliability on utilization. Adapted from Industry Task Force (1975).



Table 6.6 Possible mechanisms for improving reliability


<table><tr><td>Operating Alternatives</td></tr><tr><td>Runthrough trains</td></tr><tr><td>More frequent trains</td></tr><tr><td>Faster trains</td></tr><tr><td>Revised train schedules</td></tr><tr><td>Schedule adherence</td></tr><tr><td>Extra train policy</td></tr><tr><td>Blocking policy</td></tr><tr><td>Priorities</td></tr><tr><td>Local and interchange operations</td></tr><tr><td>Inspection policies</td></tr><tr><td>Revised power cycles</td></tr><tr><td>Capital Investment Alternatives</td></tr><tr><td>Additional power</td></tr><tr><td>Consolidation and modernization of yards</td></tr><tr><td>Construction of new yards</td></tr><tr><td>Right-of-way improvements</td></tr><tr><td>Better equipment design</td></tr><tr><td>Freight car control systems</td></tr><tr><td>Institutional and Commercial Alternatives</td></tr><tr><td>Work rule modifications</td></tr><tr><td>Hourly per diem system</td></tr><tr><td>New methods of local distribution such as unit trains or trailer or container on flatcar.</td></tr><tr><td>New operations control systems or procedures</td></tr></table>


Source: Industry Task Force (1975). 


As a result of analysis along these lines, the authors conclude that “numerous operating, investment, and institutional strategies will lead to more reliable railroad service. In fact, any railroad decision or action offers some potential for improving reliability, if, directly or indirectly, it: 

a. reduces the number of times cars are handled; 

b. improves the reliability of train connections at intermediate yards; 

c. improves the consistency of routing between origin and destination; 

d. improves the reliability of local service at the origin or destination; 

e. reduces the number of delays caused by unusual circumstances such as lost waybills, misroutes, and mechanical failures" (p. 17). 

Some of the possible mechanisms for improving reliability are shown in table 6.6 (see also Martland, Sussman, and Philip 1977). 

Focusing on the vehicle cycle and its implications has thus led to recognition of a very important area for policy influence on the rail transport system, namely strategies to improve reliability, and particularly operating strategies. 

## 6.9 SUMMARY

The vehicle cycle has three major components: the operating cycle, the service cycle, and the annual cycle. The operating cycle begins and ends at the operational base and includes positioning time, travel time while loaded and unloaded, load/unload time, operational servicing time, schedule slack, and movement processing time. The service cycle begins and ends at a major maintenance base and includes one or more operating cycles as well as positioning time from and to the maintenance base. The annual cycle includes the service cycle, time spent in periodic maintenance, and time spent in idle status. The total vehicle cycle time includes all of these components. Numerous points of leverage on the vehicle cycle can be identified. 

A number of basic concepts have been introduced: marginal and average products, marginal and average costs, and cost functions. The cost function is a useful way of displaying the results of a systematic analysis, although analysis of the cost function alone can be quite misleading. The only generally valid approach is an explicit analysis of the type described in chapter 5. 

These concepts were used to examine the economics of the vehicle cycle. The characteristics of the cycle in a particular situation can profoundly influence the behavior of users and operators, especially as they are reflected in monetary impacts. 

Changes in any of the components of the vehicle cycle can increase the utilization of a vehicle. In particular, changes in total vehicle cycle time can change the average cost per cycle, the net revenue per vehicle per cycle, the number of cycles available per vehicle, and the equilibrium volume; it can also allow productive changes in vehicle fleet size. All of these factors are interrelated and will affect net revenue to the operator and other economic measures. 

Improvements in the vehicle cycle create opportunities for economic gains. (Whether or not these gains are achieved depends, of course, on whether and how the opportunities are utilized.) Recognition of these relationships can be an essential factor in policy and planning decisions. 

## TO READ FURTHER

Whatever one's modal interests, the directions of contemporary rail systems research are quite illuminating: see Industry Task Force (1975), RAILROAD RESEARCH STUDY BACKGROUND PAPERS (1975), Martland, Sussman, and Philip (1977), C. E. Taylor (1977), and Williamson (1977). There are similar examples from other modes: see 

Frankel and Marcus (1973), Borman (1977), and Gilman (1977). 

For an analysis of transportation cost functions see Meyer et al. (1960), Heflebower (1965), Soberman (1966a, b), and Thomson (1974). 

## EXERCISES

6.1(E) Section 6.3.2 discussed alternative dimensions of output. Consider the results of sections 5.5 and 5.6 and the descriptions of three alternative technologies offered in table 5.4. 

a. Plot total cost and net revenue for each of the technologies as a function of: 

i. equilibrium volume $V_{E}$ , 

ii. capacity volume $V_{c}$ , 

iii. available seat-miles, 

iv. revenue seat-miles. 

b. Compare and discuss. 

6.2(E) Compare the explicit analysis in chapter 5 with the analysis on the basis of cost functions in exercise 6.1: 

a. Use the data of sections 5.5 and 5.6 (table 5.4). Discuss. 

b. Use the data of section 5.7 (table 5.5). Discuss. 

6.3(C) Review the discussions of cost function analysis by Vuchic (1976) and Manheim (1977b) and the analyses of Meyer, Kain, and Wohl (1965), Bhatt (1976), Boyd, Asher, and Wetzler (1976), and Deen, Kulash, and Baker (1976). 

a. Critically appraise the various analyses. 

b. Discuss critically the U.S. Department of Transportation's policy as expressed in UMTA (1976b). Draw on your answers to part a. 

6.4(P) Select a transportation operation for which data are available to you (for example, local bus transit, an air carrier, a shipping line). Describe typical vehicle cycles for this operator, making estimates of the times for each component. Analyze the possibilities for changes in the cycle. Estimate the cost and revenue consequences of alternative changes (indicate clearly any cost assumptions that you have to make). 

Understanding Performance Functions II: Congestion, Dimensionalities, and the Spatial Structure of Services 

## 7.1 INTRODUCTION

In this chapter we shall examine a number of basic characteristics of transport technologies and explore their implications for system performance. We start with a consideration of the phenomenon of congestion. Section 7.2 introduces the basic concept and several types of congestion, and section 7.3 describes the effects of congestion, using an extension of the performance model developed in chapter 5. Section 7.4 discusses the dimensionality of options, especially the implications of their different time frames and their indivisibilities, and section 7.5 introduces a performance model that includes these factors. Section 7.6 examines the combination of dimensionality of options and congestion, using the case of vehicle-facility congestion. Finally, section 7.7 explores system performance in space and time, returning again to the concept of vehicle cycles introduced in chapter 6. 

## 7.2 CONGESTION AND CAPACITY

## 7.2.1 Basic Concepts

We begin with the concept of capacity. For any system component the capacity is the maximum number of items, per unit of time, that can be processed through the component. In this definition capacity is a firm, "hard" number. 

Congestion arises out of the conjunction of two factors. The first is that every process has a finite capacity. The second is that every process has a stochastic character: there is some degree of randomness in both the demands placed on a process and the ability of the process to service those demands. 

Consider a system component with a capacity of $\mu$ units per unit of time. That is, each unit takes an average time $t_{P} = 1/\mu$ to be serviced. Units arrive at the component at a rate $\lambda$ per unit of time. If $\mu$ and $\lambda$ are both fixed, then the total time each arriving unit spends being processed is 

$$
t _ {\tau} = \left\{ \begin{array}{l l} t _ {P}, & \quad \lambda \leq \mu , \\ \infty , & \quad \lambda > \mu . \end{array} \right.\tag{7.1}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/fc366feb-933b-4442-bcbf-4538c4ada340/b15cfb0ccc6112166941feba8e35da6c37eea36abe3a0fed35f155bfe9c0ba7c.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/fc366feb-933b-4442-bcbf-4538c4ada340/681231dfb86e39bff03eeac41d7bb81dd5d0e3d2921996bb31afdb616c76b098.jpg)



Figure 7.1 Capacity and congestion. Part a shows a deterministic case; parts b and c show a more realistic case with congestion.


This is shown in figure 7.1a. 

If $\lambda > \mu$ , several alternative conditions can occur: (1) the system breaks down, in that there is a complete jam-up and no units are processed ( $t_{\tau} = \infty$ ); (2) a waiting queue is formed and grows ever longer (so that $t_{\tau} \to \infty$ ); or (3) under non-steady-state conditions, when $\lambda > \mu$ only for a finite period of time, the queue that builds up is eventually dissipated (see Yagar 1977). 

If either $\lambda$ or $\mu$ or both are random variables, then even when $\lambda < \mu$ , queues will occasionally build up. The time $t_{\tau}$ then depends on the nature of the probabilistic process controlling $\lambda$ and $\mu$ . 

The total processing time, per unit, is the processing time $t_{P}$ plus a delay time $t_{D}$ : 

$$
t _ {\tau} = t _ {\mathrm{P}} + t _ {\mathrm{D}}.\tag{7.2}
$$

In general, for probabilistic processes $t_{D}$ is an increasing function of $\lambda$ relative to $\mu$ : 

$$
t _ {\mathrm{D}} = f (\lambda / \mu).\tag{7.3}
$$

It is often useful to characterize processes by the ratio $\lambda/\mu$ and to normalize by defining 

$$
\rho \equiv \frac {\lambda}{\mu},\tag{7.4}
$$

so that 

$$
\frac {t _ {\tau}}{t _ {\mathrm{P}}} = 1 + \frac {t _ {\mathrm{D}}}{t _ {\mathrm{P}}} = 1 + g (\lambda , \mu) = 1 + g (\rho).\tag{7.5}
$$

The practical significance of congestion is shown in parts b and c of figure 7.1. The range of arrival rates between 0 and $\lambda_{A}$ (corresponding to $\rho$ between 0 and $\rho_{A}$ ) is the "uncongested" area: $t_{\tau} = t_{\mathrm{P}}$ over this range, since $t_{\mathrm{D}} = 0$ . Above $\lambda_{A}$ , however, $t_{\mathrm{D}} > 0$ and there is congestion. Thus congestion occurs when the average processing time per unit increases because of demand for service. That is, congestion occurs when $t_{\mathrm{D}} > 0$ or, equivalently, $t_{\tau} > t_{\mathrm{P}}$ . 

The capacity of a system is best understood by reference to figure 7.1. As the level of demand $\lambda$ rises, approaching the average service rate $\mu$ , the delay increases. The maximum throughput rate is a number infinitesimally smaller than $\mu$ : any level of demand greater than $\mu$ cannot be handled, and the queue will build up to infinity if the demand level stays constant (if it varies, then the queue will begin to dissipate when $\lambda$ drops below $\mu$ ). 

The problem with defining $\mu$ as the capacity is that, except in perfectly deterministic systems, the average delay per unit is very large at $\lambda$ very close to $\mu$ . Thus $\mu$ is sometimes called the physical capacity to emphasize that it is physically the maximum number of units that can be squeezed through the system per unit of time. In contrast, a practical capacity is usually chosen at a lower level such that the delays are still in some sense tolerable. 

For example, in a recent railroad simulation study the following comments were made on the estimation of capacity of a rail line: 

A number of definitions of capacity were considered in attempting to develop the most useful definition. Ultimate capacity, where absolutely no more trains can be forced through the line, is too unstable and dependent upon precisely how trains are scheduled and what failures occur. An economic capacity, where an optimal balance between operating and capital costs would occur, is not within the scope of the project and would probably be too site specific for a general analysis such as this. Other possible definitions, such as an arbitrary percent delay of total running time or an operationally stable capacity where a line could recover from a disruption in service of moderate length (e.g., 4 hours) and return to normal service levels, were also rejected as too arbitrary or unstable. The most useful and stable definition appears to be one based on the maximum allowable time for the most delayed train to traverse the line. It was discovered that maximum time could be related to average delay and would allow the user to define capacity constraints based on either minimum level of service (maximum acceptable trip time) or minimizing the need to recrew trains because of the 12 hour on-duty time limitation imposed by the Hours of Service Law. It should be noted that since the parametric runs were designed to represent “typical day” operations, this approach would not eliminate all trains that exceed the time limit. Unusual delays or catastrophic failures could still result in some trains exceeding the time limit. (Prokopy and Rubin 1975; emphasis added) 

In highway studies the approach has been to define six levels of service, designated A-F. Each level of service reflects a range of a number of factors, including not only travel time (or its inverse, speed) but also “traffic interruptions, freedom to maneuver, safety, driving comfort and convenience, and operating costs” (HIGHWAY CAPACITY MANUAL 1965, p. 7). Thus, while physical capacity corresponds to $\lambda \approx \mu$ , highway designers are encouraged to think in terms of essentially different levels of $t_{D}$ : this procedure “offers a choice of four [service] levels [A-D] below capacity [E, F], each of which is related to an operating speed [t]; these levels offer more freedom to the local administrator or engineer to select that type of operation most suitable for his local conditions” (p. 87). 

Although physical capacity is usually a well-defined concept, workable, practical definitions of capacity must be related explicitly to levels of delay. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/fc366feb-933b-4442-bcbf-4538c4ada340/09f9096c876f4f933e90e7269df5858e169ef79807082c37dadef9ae2890dcde.jpg)



Figure 7.2 a: Total service time as a function of arrival rate. b: Average and marginal total service times as functions of arrival rate.


## SIGNIFICANCE OF CONGESTION

Figure 7.2 shows the significance of congestion effects. Part a shows the total processing time y (for all units) as a function of arrival rate $\lambda$ : 

$$
y = \lambda \bar {t} _ {\tau},\tag{7.6}
$$

where $\bar{t}_{\tau}$ is the average value of $t_{\tau}$ for all units being serviced. Part b shows the average and marginal total processing times $\bar{y}_{\lambda}$ and $y_{\lambda}^{\prime}$ (note that $\bar{y}_{\lambda} = y/\lambda = \bar{t}_{\tau}$ ). For arrival rates less than $\lambda_{A}$ , the marginal and average processing times are equal. For arrival rates greater than $\lambda_{A}$ , however, the marginal total processing time is greater than the average total processing time. 

This has great significance. Above $\lambda_{A}$ each additional arrival per unit of time will experience a processing time equal to the average processing time $\bar{y}_{\lambda}$ . However, such additional arrivals increase the total pro-

cessing time of all other users of the system by an amount equal to $y_{\lambda}^{\prime}$ —an average increase of $y_{\lambda}^{\prime}/\lambda$ . Thus such additional arrivals may receive benefits, but they cause disbenefits to all other users of the system. 

This difference between average and marginal times (or, more generally, between average and marginal costs or composite service levels) leads to the important concept of adding an additional charge p so that the average cost plus p equals the marginal cost at equilibrium volume. In urban transportation, for example, it has often been proposed that automobiles entering the congested central area of a city be charged a “congestion toll” (see, for example, Walters 1961, Thomson 1974, URBAN TRANSPORTATION PRICING ALTERNATIVES 1976, Arrillaga 1978, McGillivray, Neels, and Beesley 1978). 

## TRANSIENT CONDITIONS

So far we have dealt only with the steady state, where $\lambda$ and $\mu$ are constant over time, and with $\lambda < \mu$ . In many practical situations $\lambda$ is a function of time, and sometimes $\mu$ is also. 

Consider the case where $\mu$ is constant but $\lambda$ is a function of time and $\lambda(t) > \mu$ for some period $\Delta t$ . Even while $\lambda(t) < \mu$ , congestion can occur due to the probabilistic nature of $\lambda$ and $\mu$ , but although queues build up, they also dissipate. Once $\lambda(t)$ becomes greater than $\mu$ , the queue continues to build at a rate faster than it dissipates, until such times as $\lambda(t)$ drops below $\mu$ again. At that time there still is a queue, or backlog, to be dissipated. In the discussion that follows we shall assume that such transient saturated systems ( $\lambda > \mu$ ) can be represented approximately by an equivalent unsaturated system ( $\lambda < \mu$ ) if we take a long enough time interval that the transient effect is averaged out. (This is not necessarily a good assumption in a practical analysis. In some cases it is very important to take into account the time dynamics; see Odoni and Kivestu 1976, May and Orthlieb 1976, Yagar 1977.) 

## 7.2.2 Models of Congestion

It will be useful to have some simple models of congestion. One useful class of models for these processes is provided by queuing theory; we shall use this theory here for expository purposes, but the reader should be aware that other probabilistic models may be more appropriate in particular applications. 

When the arrival rate or the service rate or both are randomly distributed, there is a certain probability that an arriving unit will have to wait before being serviced. As a standard result of queuing theory (Wohl and Martin 1967, Wagner 1969), the expected or average delay $t_{D}$ is (under the assumptions of a Poisson arrival distribution, exponential service-time distribution, and a single channel): 

$$
t _ {\mathrm{D}} = \frac {1}{\mu} \frac {1}{(\mu / \lambda) - 1} = \frac {1}{\mu} \frac {\lambda / \mu}{1 - (\lambda / \mu)}.\tag{7.7}
$$

Since the average service time without congestion is $t_{P} = 1/\mu$ , the average total processing time is 

$$
t _ {\tau} = t _ {\mathrm{P}} + t _ {\mathrm{D}} = \frac {1}{\mu} \left(1 + \frac {\lambda / \mu}{1 - (\lambda / \mu)}\right),\tag{7.8}
$$

and 

$$
\frac {t _ {\tau}}{t _ {\mathrm{P}}} = 1 + \frac {t _ {\mathrm{D}}}{t _ {\mathrm{P}}} = 1 + \frac {\lambda / \mu}{1 - (\lambda / \mu)} = 1 + \frac {\rho}{1 - \rho},\tag{7.9}
$$

where $\rho \equiv \lambda/\mu$ . The behavior of this function is shown in figure 7.3.
More general models can also be formulated. Following Davidson (as described in Hutchinson 1974, p. 128), we can write 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/fc366feb-933b-4442-bcbf-4538c4ada340/32e8a922faa464c213a8c52ad207d23fe30c8017c3d93abc83a9e4514fbe4e55.jpg)



Figure 7.3 Basic queuing model. After Wohl and Martin (1967).


## 274 Understanding Performance Functions II

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/fc366feb-933b-4442-bcbf-4538c4ada340/ec45dcf34d289093572c707adb13ae2944f007131a747c43b0bbadf2114110bb.jpg)



Figure 7.4 A general congestion model. After Hutchinson (1974).


$$
\begin{array}{r l} \frac {t _ {\tau}}{t _ {\mathrm{P}}} & = 1 + J \frac {\lambda / \mu}{1 - (\lambda / \mu)} \\ & = 1 + J \frac {\rho}{1 - \rho}. \end{array}\tag{7.10}
$$

This function is shown in figure 7.4 for various values of J. 

The value of the parameter J is derived from theoretical or empirical arguments to characterize a particular process. For example, for the case of Poisson arrivals and Erlang service times (Wohl and Martin 1967, p. 372; Wagner 1969), 

$$
J = \frac {k + 1}{2 k},\tag{7.11}
$$

so that 

$$
t _ {\mathrm{D}} = t _ {\mathrm{P}} J \frac {\rho}{1 - \rho} = t _ {\mathrm{P}} \frac {k + 1}{2 k} \frac {\rho}{1 - \rho}.\tag{7.12}
$$

Here the parameter $k = 1, 2, 3, \ldots$ characterizes the variability of the servicing time; as k increases, the variance of service time decreases, and the times become more regular. Correspondingly the average delay $t_{D}$ becomes smaller. 

We emphasize that, while the queuing model is a useful one for our present purposes, it is not necessarily the most appropriate model for every practical application. The roots of this model lie in a particular formulation of delay processes. Many other probabilistic formulations of delay processes are possible. In each application the analyst must carefully examine the probabilistic mechanisms in the congestion phenomena under study to determine which of the many alternative types of models is most appropriate. See, for example, Rallis (1967) for a variety of transportation applications of this class of models. For highway traffic applications see Drew (1968), chapter 10. 

## 7.2.3 Types of Congestion

Many types of congestion occur in transportation systems, but it is especially important to distinguish two major categories: 

1. Load-independent congestion occurs when system performance is degraded by the interactions of system components, even if the system is not utilized. For example, vehicles moving along guideways can experience congestion even if there are no passengers or cargo on the vehicles. In this case the demand that causes congestion is that of system components such as vehicles rather than passengers or cargo. 

2. Load-dependent congestion occurs when system performance is degraded by the volume of flow of loads (passengers or cargo). If the flow volume of passengers or cargo is zero, no degradation occurs. 

Within these categories there are a number of specific types of congestion that can occur in transportation systems, and we list below two examples from each category. 

## LOAD-INDEPENDENT CONGESTION

## Vehicle-facility congestion

Every facility, whether guideway or terminal, exhibits congestion effects. A terminal has a service rate at which it can handle arriving or departing vehicles. A guideway has a service rate at which vehicles can move over the facility. (The mechanism controlling congestion on guideways is the headway spacing-speed distribution.) As the volume of vehicles scheduled or otherwise attempting to move through a guideway approaches capacity, vehicle interactions cause speed reductions and thus delays. 

In this case $\lambda = q$ , the actual frequency (flow rate) of vehicles, while $\mu = q_{C}$ , the flow capacity of the facility. Note that vehicle-facility congestion can occur whether the vehicles are empty or full; the demand is not loads but vehicles. (For further discussion see section 7.6.) 

## Vehicle-schedule congestion

This type of congestion arises when the number of scheduled trips is large relative to the number that can be produced by the available fleet. Here the service rate is a function of the number of vehicle round trips that can be produced by a fleet of size N: $\mu = Nn$ , where n is the number of round trips per vehicle per time period. The demand rate is the number of round trips required to meet the schedule: $\lambda = Q$ , where Q is the scheduled frequency. 

## LOAD-DEPENDENT CONGESTION

## Load-vehicle congestion

This type of congestion arises when a stream of vehicles moves over a route past a terminal at which loads are waiting to board. The waiting time experienced by a passenger (or cargo load) at the terminal has two components: waiting time until the first vehicle arrives (after arrival of the passenger at the terminal) and the additional time (if any) until a vehicle with an empty space arrives. In this case, if q is the frequency at which vehicles move past the terminal and each vehicle has a payload capacity w, then the number of seats (or tons) available per unit of time is wq, and the service rate is $\mu = wq$ . (This is a crude model; a more realistic one would model the arrival of batches of seats of size w at a rate q.) The arrival rate $\lambda$ is the number of passengers (or tons) at the terminal ready to board (per unit of time). That is, the delay time reflects the probability of finding a seat. In the case of a grain shipper waiting for an empty railcar to be made available to him for loading by the rail carrier, the delay may be due to competing demands for the available vehicle capacity. $^{1}$ 

## Load-schedule congestion

A key element of a schedule is the time allowed for each detailed element of a vehicle's movement—for example, the time allowed for loading and unloading cargo or passengers at each stop. Congestion occurs when the actual volumes to be loaded require more time than originally scheduled. In this case the service rate is the quantity of passengers or cargo that can be loaded per unit time, and the arrival rate is the actual volume requiring loading. 

## DISCUSSION

We emphasize again that both vehicle-facility and vehicle-schedule congestion can occur even when there is no load—no passengers or cargo using the system. These two types of congestion arise solely from the performance interactions of vehicles and facilities; the demands for service that cause congestion are established by the operating schedules of the system. On the other hand, load-vehicle and load-schedule congestion can arise even when there is no vehicle-facility or vehicle-schedule congestion. 

This distinction has important practical implications. Load-dependent congestion effects enter directly into the process of travel-market equilibration. Load-independent congestion effects, on the other hand, can often be analyzed separately from, and prior to, travel-market equilibration. 

## 7.3 EFFECTS OF CONGESTION

Congestion can have significant effects on the performance and especially on the economics of a system, and each type of congestion has different effects. To illustrate these effects we shall examine load-vehicle congestion with a simple model. Then in section 7.6 we shall examine vehicle-facility congestion. We start by introducing a modification of performance model I, developed in chapter 5. 

For a schedule frequency Q, if we assume random arrivals of loads at a terminal, the average waiting time for the first vehicle to arrive after the load arrives is $t_{w1} = 1/2Q$ . The average waiting time $t_{w}$ for an empty seat (or empty unit of cargo capacity) may be greater than this, by $t_{w2}$ , since some arriving vehicles may be fully loaded. 

To represent this phenomenon we take as a first approximation to $t_{w}$ a queuing model with arrival rate equal to the demand volume $V_{D}$ . For the service rate we use the arrival rate of seats, 2Qw, where w is the vehicle payload capacity (alternatively we could treat each direction separately, taking into account such factors as load imbalances: see section 6.5). Thus 

$$
\rho \equiv \frac {V _ {\mathrm{D}}}{2 Q w} = \frac {V _ {\mathrm{D}}}{V _ {\mathrm{C}}},\tag{7.13}
$$

$$
\frac {t _ {\mathrm{D}}}{t _ {\mathrm{P}}} = \frac {t _ {\mathrm{w2}}}{t _ {\mathrm{P}}} = \frac {J \rho}{1 - \rho},\tag{7.14}
$$

$$
t _ {\mathrm{P}} = t _ {\mathrm{w1}} = \frac {1}{2 Q},\tag{7.15}
$$

and, combining terms, 

$$
t _ {\tau} \equiv t _ {w} = t _ {w 1} + t _ {w 2} = \frac {1}{2 Q} \left(1 + \frac {J V _ {D} / 2 Q w}{1 - V _ {D} / 2 Q w}\right) \text {   for   } V _ {D} <   2 Q w.\tag{7.16}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/fc366feb-933b-4442-bcbf-4538c4ada340/a5259b901558af254a0d3816ed3c841ef4e7ebc8c710cb93904ec907c1d71889.jpg)



Figure 7.5 Effects of congestion. D-D is the demand function. The solid lines are service functions for the indicated Q and J=0. The dashed curves are service functions for the indicated Q and J=0.10. Some equilibrium flows are also shown for J=0.05 and J=1.00.



Table 7.1 Performance model II


<table><tr><td>Options</td><td><eq>\mathbf{T} = (\mathbf{M}, Q, P)</eq><eq>\mathbf{M} = (w, v)</eq></td></tr><tr><td>Environment</td><td><eq>\mathbf{E} = (d)</eq></td></tr><tr><td>Basic relationships</td><td><eq>q(\mathbf{T}) = Q</eq><eq>V_{\mathrm{C}}(\mathbf{T}) = 2wq</eq><eq>n(\mathbf{T}) = \frac{v}{2d}</eq></td></tr><tr><td>Service level</td><td><eq>\mathbf{S}(\mathbf{T}) = (t_{\mathrm{iv}}, t_{\mathrm{w}}, t_{\mathrm{T}}, c)</eq><eq>c(\mathbf{T}) = P</eq><eq>t_{\mathrm{iv}}(\mathbf{T}) = \frac{d}{v}</eq><eq>t_{\mathrm{w}}(\mathbf{T}) = \frac{1}{2q} \left(1 + \frac{J\rho}{1 - \rho}\right)</eq><eq>\rho = \frac{V_{\mathrm{D}}}{2qw}</eq><eq>t_{\mathrm{T}}(\mathbf{T}) = t_{\mathrm{iv}} + t_{\mathrm{w}}</eq></td></tr><tr><td>Resources consumed</td><td><eq>R = \frac{q}{n}</eq></td></tr></table>

This function is shown by the dashed curves in figure 7.5 for J = 0.10. Each curve is the service function for the indicated values of Q. 

Our definition of performance model II is summarized in table 7.1. Referring back to the air transportation example in chapter 5, we can take the demand function 

$$
V _ {\mathrm{D}} = \frac {Z}{1 + e ^ {U _ {0} - U _ {\mathrm{A}}}}, \quad U _ {0} - U _ {A} = \alpha_ {0} - \alpha_ {1} t _ {\mathrm{iv}} - \alpha_ {2} t _ {\mathrm{w}} - \alpha_ {3} c,\tag{7.17}
$$

and reduce it, for purposes of travel-market equilibration, to a function of $t_{w}$ : 

$$
V _ {\mathrm{D}} = \frac {Z}{1 + \beta_ {1} e ^ {- \alpha_ {2} t _ {\mathrm{w}}}}, \quad \beta_ {1} = e ^ {\alpha_ {0} - \alpha_ {1} t _ {\mathrm{iv}} - \alpha_ {3} c}.\tag{7.18}
$$

Now we can apply the methodology of figure 5.8. Note that for a specific set of options $T^{i} = (M, Q, P)$ we must do an explicit travel-market equilibration to find equilibrium flows before we can compute the remaining impacts. The conditions to be met at equilibrium are (7.16) and (7.18). Numerical methods can be used to find the solution to these two simultaneous equations (this example was solved on a programmable pocket calculator using a general routine for finding the roots of an arbitrary function). 


Table 7.2 Effects of congestion on equilibrium


<table><tr><td rowspan="2">Q</td><td rowspan="2"><eq>V_C</eq></td><td colspan="4">J=0</td><td colspan="3">J=0.01</td></tr><tr><td><eq>V_E</eq></td><td><eq>t_w^E</eq></td><td colspan="2"><eq>I_{NR}</eq></td><td><eq>V_E</eq></td><td><eq>t_w^E</eq></td><td><eq>I_{NR}</eq></td></tr><tr><td>4</td><td>70</td><td>45(1.00)</td><td>2(1.00)</td><td colspan="2">471(1.00)</td><td>43.4(0.96)</td><td>2.03(1.02)</td><td>364(0.77)</td></tr><tr><td>8</td><td>140</td><td>134(1.00)</td><td>1(1.00)</td><td colspan="2">3,583(1.00)</td><td>123.9(0.92)</td><td>1.08(1.08)</td><td>2,954(0.82)</td></tr><tr><td>12</td><td>210</td><td>187(1.00)</td><td>0.67(1.00)</td><td colspan="2">4,485(1.00)</td><td>179.5(0.96)</td><td>0.71(1.06)</td><td>4,050(0.90)</td></tr><tr><td>16</td><td>280</td><td>218(1.00)</td><td>0.50(1.00)</td><td colspan="2">4,125(1.00)</td><td>214.6(0.98)</td><td>0.52(1.04)</td><td>3,916(0.95)</td></tr><tr><td colspan="3">J=0.05</td><td colspan="3">J=0.10</td><td colspan="3">J=1</td></tr><tr><td><eq>V_E</eq></td><td><eq>t_w^E</eq></td><td><eq>I_{NR}</eq></td><td><eq>V_E</eq></td><td><eq>t_w^E</eq></td><td><eq>I_{NR}</eq></td><td><eq>V_E</eq></td><td><eq>t_w^E</eq></td><td><eq>I_{NR}</eq></td></tr><tr><td>39.0(0.87)</td><td>2.13(1.07)</td><td>100(0.21)</td><td>35.6(0.79)</td><td>2.21(1.11)</td><td>-104(0.22)</td><td>19.0(0.42)</td><td>2.75(1.38)</td><td>-1,100(-2.34)</td></tr><tr><td>110.5(0.82)</td><td>1.19(1.19)</td><td>2,150(0.60)</td><td>101.7(0.76)</td><td>1.27(1.27)</td><td>1,622(0.45)</td><td>59.9(0.45)</td><td>1.75(1.75)</td><td>-886(-0.25)</td></tr><tr><td>165.5(0.89)</td><td>0.79(1.18)</td><td>3,204(0.71)</td><td>155.0(0.83)</td><td>0.86(1.28)</td><td>2,580(0.58)</td><td>100.4(0.54)</td><td>1.28(1.92)</td><td>-696(-0.16)</td></tr><tr><td>204.6(0.94)</td><td>0.57(1.14)</td><td>3,316(0.80)</td><td>195.6(0.90)</td><td>0.62(1.24)</td><td>2,776(0.67)</td><td>137.0(0.49)</td><td>0.98(1.96)</td><td>-740(-0.18)</td></tr></table>


Note: Numbers in parentheses are ratios relative to values at J=0. 


We can take the example of chapter 5, use performance model II, and solve for equilibrium at each alternative frequency. Table 7.2 and figure 7.5 show the results for J = 0 (no congestion), 0.01, 0.05, 0.1, and 1. The shifts in equilibrium flows can be quite significant. 

The economic significance of congestion is clear from the table. The presence of congestion causes significant losses to both user and operator over the uncongested conditions. 

## 7.4 DIMENSIONALITY, TIME FRAMES, AND INDIVISIBILITIES IN OPTIONS

Performance model I was very simple in many respects. Congestion effects were not included, and the number of types of options explicitly represented was artificially small. In general, in transportation there is a wide range of options, including fixed facilities, vehicle fleet size and mix, and operating, pricing, and organizational policies; different options are variable over different time frames, ranging from years for construction of new fixed facilities to weeks or days for schedule and route changes; and many of the options exhibit “lumpiness” or in-divisibilities. In this section we shall explore the implications of these multiple dimensions of options. 

## 7.4.1 Time Frames

The transportation analyst is often interested in examining the extent to which changes can be implemented at various points in time. For convenience we separate options into three groups according to the time it takes to implement a change in the system (Heflebower 1965): 

1. Long-run options: Changes in many aspects of a transportation system can occur only slowly because they require extensive planning, construction, and investment. These long-run options, $T_{LR}$ , generally involve the fixed facilities, such as links and terminals (rail tracks, highway lanes, airports), which take significant amounts of time to plan, design, and construct—often on the order of 7–12 years or more.
2. Short-run options: Some aspects of a transportation system can be changed fairly quickly. These short-run options, $T_{SR}$ , generally involve changes in the operations of specific services in the system—for example, changes in routes, schedules, prices charged and ancillary services offered, and taxes and subsidies (although in many contexts some of these options may be so constrained by institutional procedures, such as regulatory commissions, that the short run becomes several years). 

3. Intermediate-run options: Some changes to a transportation system fall between the short and long run and are worth distinguishing as "intermediate" in degree of rigidity. These options, $\mathbf{T}_{\mathrm{IR}}$ , generally involve changes in the vehicle fleet such as procurement of new or replacement vehicles or changes in vehicle characteristics, fleet mix, or fleet size. 

These groupings of options are general; in particular contexts very different groupings may be appropriate. Further, what is short-run in one analysis may be long-run in another, and vice versa. 

To explore the implications of these time frames we examine the cost function for a particular system. In part a of figure 7.6 we assume that long-run, intermediate-run, and short-run options are fixed at $T_{LR}^{\prime}$ , $T_{IR}^{\prime}$ , and $T_{SR}^{\prime}$ , respectively, and show how average total cost $\overline{C}$ might vary as a function of volume. (We assume the general case of both economies and diseconomies of scale.) In part b, we let the short-run options take three different values, $T_{SR}^{\prime}$ , $T_{SR}^{\prime\prime}$ , and $T_{SR}^{\prime\prime\prime}$ , while holding long- and intermediate-run options fixed. For each a different curve of $\bar{C}$ is generated. If $T_{SR}$ is varied over a wide enough range, we can consider each level of V and find the $T_{SR}$ for which $\bar{C}$ is lowest for that volume. We thus generate the envelope of $\bar{C}$ shown by the dashed line in the figure. This envelope gives the curve of lowest values of $\bar{C}$ achievable for the particular values of the (fixed) $T_{LR}$ and $T_{IR}$ . 


a


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/fc366feb-933b-4442-bcbf-4538c4ada340/9e68276ad40bbef6e76e37a4020bab478b82d77f91555d47be29903050eec851.jpg)



b


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/fc366feb-933b-4442-bcbf-4538c4ada340/714b653afcdb9e81fd40e331c8014104303cd2cd8d6f7fd48e3318b7c1289aab.jpg)



C


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/fc366feb-933b-4442-bcbf-4538c4ada340/3e1cfabd21bcadcbbbdcf086572e665a2a8551f2fc5f110cc0712e63c05ebbfa.jpg)



d


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/fc366feb-933b-4442-bcbf-4538c4ada340/a7c713c44f46565c4243f0137bc08825b36c3e3eb6c8a2e1756745c453af537c.jpg)



Figure 7.6 Effect of differing time frames of options.


In part c we continue to hold the long-run options fixed but now let the intermediate-run options take the values $T_{IR}^{\prime}$ , $T_{IR}^{\prime\prime}$ , and $T_{IR}^{\prime\prime\prime}$ ; for each of these we let the short-run options vary over a range. For each setting of $T_{IR}$ , the variation of $T_{SR}$ again generates an envelope of $\bar{C}$ ; this envelope results from taking the setting of $T_{SR}$ for each volume level which yields the lowest $\bar{C}$ for that volume, conditional on the level of $T_{IR}$ and $T_{LR}$ . If we now consider the variability of $T_{IR}$ as well as $T_{SR}$ , we generate the $\bar{C}$ envelope shown by the dot-and-dash curve. (Note that the scales of parts c and d are different from those of a and b, for clarity, as emphasized by the spacing of $V_{1}$ and $V_{2}$ .) 

In part d we consider $T_{LR}$ to be variable as well. The dashed curves mark the envelopes generated by varying $T_{SR}$ for $T_{IR}$ and $T_{LR}$ fixed. The dot-and-dash curves mark the envelopes generated by varying both $T_{SR}$ and $T_{IR}$ for $T_{LR}$ fixed. The dotted curve marks the envelope generated by varying $T_{LR}$ as well. 

Thus the distinction of long-, intermediate-, and short-run options allows us to distinguish a corresponding hierarchy of $\bar{C}(V)$ curves. In the technical literature, one often sees reference to long-, intermediate-, and short-run cost functions, corresponding to the outer envelopes in parts d, c, and b, respectively. 

This distinction is a relative one: what is long-run in one context may be short-run in another. The key issue is to determine, over any prespecified time frame, which options are variable and which must be considered fixed. 

The practical implications follow in a straightforward way. Part b of the figure gives the short-run average total cost function. The cost function can be shifted to match demand only over a range; to change the intermediate- and long-run options (from $T_{IR}^{\prime}$ and $T_{LR}^{\prime}$ ) takes time. Therefore, if a volume $V_{3}$ occurs, the operator is in relatively good position, since he can vary the short-run options to $T_{SR}^{\prime\prime}$ to produce the lowest average total cost for $T_{IR}^{\prime}$ and $T_{LR}^{\prime}$ . If, on the other hand, volume turns out to be substantially greater than expected, say $V_{2}$ 

(or, alternatively, substantially lower), then the operator's average total cost even with the best choice of short-run options ( $T_{SR}^{\prime\prime}$ , say) may be much greater than what it might have been if $T_{IR}$ or $T_{LR}$ could have been varied. If the operator has competitors, they may have a lower $\bar{C}$ , having made wiser past decisions, and may be able to offer a lower price and thus capture a larger share of the market. If the operator is a public agency and does not have competitors, then operator net revenues and/or user service suffer because higher costs are incurred than might otherwise be achievable. 

Thus the interrelationship of options with different time frames has a significant effect in reducing the effectiveness of transport, because with the time lags required to change intermediate- and long-run options, and with imperfect information about future demand, it is often difficult to choose the combination of options that is “best” (in the limited sense of minimum average total cost). For example, in the mid-1970s many air carriers had excess vehicle capacity and higher costs because demand was less than had been forecast at the time in the early 1970s when the decision was made to invest heavily in jumbo aircraft. 

We note that this type of analysis can be done with any measure of impact: resource consumption, service level, net revenue, and so forth. 

## 7.4.2 Indivisibilities

Most types of transportation systems are characterized by indivisibilities; that is, some options cannot be varied continuously over a range but must take discrete values. For example: 

1. Fixed facilities: The number of runways at an airport, the number of boarding gates or apron positions at a terminal, and the number of airports in a metropolitan area must be integers; the number of lanes in a highway or tracks in a railroad or transit stations can only take integral values. 

2. Vehicles: The number of aircraft, ships, trucks, railcars, locomotives, etc., owned or operated by a particular carrier must be integral. (When there is the option of short-term charters or of sharing of vehicles with another carrier, this is no longer strictly true.) 

3. Operating policy is not necessarily discrete and usually is continuously variable (frequency, price, taxes, subsidies). One exception occurs when a vehicle must return to its home base at fixed intervals; then the number of round trips per interval over a particular route must be integral. 

The indivisibility of options is an important aspect of transport costs. The major implication is that, for many transport technologies, the options cannot be varied so as to have precisely the right amount of capacity to serve a particular volume of demand. Rather, there is usually either too much capacity or too little. For example, if each lane of highway can carry 1,600 vehicles per hour, then a demand volume of 3,500 vehicles per hour must be served by more than two lanes; two is too little and three is more than sufficient. 

Thus the presence of indivisibilities, together with the different time frames of various options, usually make it impossible to tailor the choice of options to provide just that capacity which is “best.” 

## 7.5 AN EXPANDED PERFORMANCE MODEL

In this section we shall expand the simple performance model introduced in chapter 5 to take account of the multiple dimensions of options, their interrelations and varying time frames, and the presence of indivisibilities. Then we shall examine this expanded performance model and draw some conclusions. 

## 7.5.1 Defining the Model

As before, we assume that service is provided over a single route connecting two points, such that the round-trip distance (A to B and back to A) is D = 2d, with vehicles traveling at an average speed v at uniform constant headway h. Each one-way trip of one vehicle results in the delivery of a payload of w tons. In one hour a vehicle makes n = v/D round trips and delivers 2nw tons. 

We consider a fleet of vehicles. Let Q be the total number of vehicle round trips scheduled per hour and q the number accomplished. Then the total volume delivered by the fleet is a function of q, namely 2qw. 

## CONSTRAINTS

Two kinds of constraints may apply. First, the vehicles operate over fixed facilities whose capacities may limit the number of round trips they can accomplish. Second, the size of the vehicle fleet may not be sufficient to implement the Q scheduled trips. 

To explore the first constraint we let K indicate the number of units of fixed facilities, such that each unit can accommodate $q_{C}$ round trips per hour. (For example, K might be the number of highway lanes or airport runways.) Then $Kq_{C}$ is the maximum number of round trips per hour that can be accommodated. 

As for the second constraint, if there are N vehicles in the fleet, each of which can make at most n round trips per hour, then the maximum number of round trips N vehicles can make per hour is Nn. 

The transportation options T are now the expanded set (M, K, N, Q, P), where $\mathbf{M} = (w, v, q_{\mathrm{C}})$ . Here M specifies the basic characteristics of the technology chosen, K indicates the amount of investment in fixed facilities, N the amount of investment in vehicles, Q the frequency at which the vehicles are scheduled to operate over the route, and P the price to be charged. 

We now consider q, the actual frequency at which vehicles are able to operate over the route. We know from the foregoing arguments that the maximum frequency is constrained by two factors, the capacity of the fixed facilities, set by K, and the size of the vehicle fleet, N: 

$$
q \leq K q _ {\mathrm{C}},\tag{7.19}
$$

$$
q \leq N n.\tag{7.20}
$$

The actual frequency is thus 

$$
q = \min (Q; K q _ {\mathrm{C}}; N n).\tag{7.21}
$$

The total volume that can be delivered per hour is then 

$$
V _ {\mathrm{C}} (\mathbf {M}, K, N, Q, P) = 2 q w.\tag{7.22}
$$

Defining 

$$
Q _ {\max} ^ {i} = \min (K q _ {\mathrm{C}}; N n),\tag{7.23}
$$

we can rewrite (7.21) as 

$$
q = \left\{ \begin{array}{l l} Q, & \quad Q \leq Q _ {\max} ^ {i}, \\ \text { undefined }, & \quad Q > Q _ {\max} ^ {i}. \end{array} \right.\tag{7.24}
$$

## SERVICE RELATIONSHIPS

The service relationships were given in section 5.4: 

$$
c (\mathbf {T}) = P,\tag{7.25}
$$

$$
t _ {\mathrm{iv}} (\mathbf {T}) = \frac {d}{v} = \frac {1}{2 n},\tag{7.26}
$$

$$
t _ {\mathrm{w}} (\mathsf {T}) = \frac {1}{2 q},\tag{7.27}
$$

$$
t _ {\mathrm{T}} (\mathbf {T}) = \frac {1}{2} \left(\frac {1}{n} + \frac {1}{q}\right).\tag{7.28}
$$

## RESOURCES CONSUMED

The resources consumed can be assumed to fall into the following categories: 

$R_{F}$ (fixed facilities): resources required to build and operate the fixed facilities; proportional to the number of units of fixed facilities (for example, lane-miles), that is, to K (for given d); 

$R_{V}$ (vehicles): resources required to acquire a vehicle fleet and maintain it in operating condition; proportional to N; 

$R_{0}$ (operations): resources required to operate the scheduled service; proportional to the number of vehicle-hours, per hour, that is, to Q/n. 

Thus we can write 

$$
R _ {\mathrm{F}} = b _ {\mathrm{F}} K,\tag{7.29}
$$

$$
R _ {\mathrm{V}} = b _ {\mathrm{V}} N,\tag{7.30}
$$

$$
R _ {0} = b _ {0} \frac {Q}{n},\tag{7.31}
$$

where the bs are appropriate constants. 

## COST RELATIONSHIPS

The monetary costs incurred by the operator in providing transportation are assumed to fall into three groups and are, in general, functions of the technology, M: 

$$
\begin{array}{r l} c _ {\mathrm{FK}} ^ {\prime} & = \text {cost of fixed facilities per unit of capacity (for example, per lane- mile)} \\ & = f (q _ {\mathrm{C}}, v, d), \\ c _ {\mathrm{VN}} ^ {\prime} & = \text {cost to procure one vehicle} \\ & = g (w, v), \\ c _ {\mathrm{OQ}} ^ {\prime} & = \text {operating cost of one vehicle (per vehicle - hour)} \\ & = k (w, v, d). \end{array}
$$

In other words, the investment in fixed facilities depends on the design standards that determine $q_{C}$ , the average speed, and the distance; the cost of a vehicle depends on its characteristics, and the operating cost depends on the characteristics of both the vehicle and the fixed facilities. 

The total cost is given by 

$$
C _ {\mathrm{T}} = C _ {\mathrm{TF}} + C _ {\mathrm{TV}} + C _ {\mathrm{TO}},\tag{7.32}
$$

where 


Table 7.3 Performance model III


<table><tr><td>Options</td><td><eq>\mathbf{T} = (\mathbf{M}, K, N, Q, P)</eq><eq>\mathbf{M} = (w, v, q^c)</eq></td></tr><tr><td>Environment</td><td><eq>\mathbf{E} = (d)</eq></td></tr><tr><td>Basic relationships</td><td><eq>n(\mathbf{T}) = \frac{v}{2d}</eq><eq>q(\mathbf{T}) = \min(Q; nN; q_cK)</eq><eq>V_c(\mathbf{T}) = 2wq</eq></td></tr><tr><td>Service levels</td><td><eq>\mathbf{S}(\mathbf{T}) = (t_{\text{iv}}, t_w, t_T, c)</eq><eq>c(\mathbf{T}) = P</eq><eq>t_{\text{iv}}(\mathbf{T}) = \frac{d}{v}</eq><eq>t_w(\mathbf{T}) = \frac{1}{2q}</eq><eq>t_T(\mathbf{T}) = \frac{1}{2}\left(\frac{2d}{v} + \frac{1}{q}\right)</eq></td></tr><tr><td>Resources consumed</td><td><eq>\mathbf{R} = (R_F, R_V, R_O)</eq><eq>R_F = b_F K</eq><eq>R_V = b_V N</eq><eq>R_O = b_o \frac{Q}{n}</eq></td></tr><tr><td>Evaluation component(monetary costs incurred by operator)</td><td><eq>C_{\text{T}}(\mathbf{T}) = C_{\text{TF}}(\mathbf{T}) + C_{\text{TV}}(\mathbf{T}) + C_{\text{TO}}(\mathbf{T})</eq><eq>C_{\text{TF}}(\mathbf{T}) = c_{\text{FK}} K</eq><eq>C_{\text{TV}}(\mathbf{T}) = c_{\text{VN}} N</eq><eq>C_{\text{TO}}(\mathbf{T}) = c_{\text{oQ}} \frac{Q}{n}</eq></td></tr></table>

$$
\begin{array}{r l} {C _ {\mathrm{TF}} (\mathsf {T})} & {= \mathrm{totalcostoffixedfacilities}} \\ & {= c _ {\mathrm{FK}} ^ {'} R _ {\mathrm{F}}} \\ & {= c _ {\mathrm{FK}} K (c _ {\mathrm{FK}} = c _ {\mathrm{FK}} ^ {'} b _ {\mathrm{F}}),} \end{array}\tag{7.33}
$$

$$
\begin{array}{r l} {C _ {\mathrm{TV}} (\mathbf {T}) = \mathrm{totalcostofvehicles}} \\ & {= c _ {\mathrm{VN}} ^ {\prime} R _ {\mathrm{N}}} \\ & {= c _ {\mathrm{VN}} N (c _ {\mathrm{VN}} = c _ {\mathrm{VN}} ^ {\prime} b _ {\mathrm{V}}),} \end{array}\tag{7.34}
$$

$$
\begin{array}{r l} {C _ {\mathrm{TO}} (\mathbf {T})} & {= \mathrm{totalcostofoperations}} \\ & {= c _ {\mathrm{OQ}} ^ {\prime} R _ {\mathrm{O}}} \\ & {= c _ {\mathrm{OQ}} Q / n (c _ {\mathrm{OQ}} = c _ {\mathrm{OQ}} ^ {\prime} b _ {\mathrm{O}}).} \end{array}\tag{7.35}
$$

Thus the total cost is 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/fc366feb-933b-4442-bcbf-4538c4ada340/759d55c0284aa75be8d5761771a2386c1c971ffa575502e044d761364ab5c172.jpg)



Figure 7.7 Effect of a frequency constraint.


$$
C _ {\mathrm{T}} (\mathsf {T}) = c _ {\mathrm{FK}} K + c _ {\mathrm{VN}} N + c _ {\mathrm{OQ}} Q / n.\tag{7.36}
$$

This performance model III is summarized in table 7.3. 

7.5.2 Implications: Indivisibilities and Interrelations of Options
The implications of this model are shown in figure 7.7. Part a shows actual schedule frequency q, as a function of planned schedule frequency Q, for a particular set of options $(K^{i}, N^{i})$ and a particular vehicle type. This capacity constraint has the effect on total cost $C_{T}$ shown in part b: $C_{T}$ is a function of Q for $Q \leq Q_{max}^{i}$ . As the options are varied, both the costs and the capacities shift, generating the family of cost curves shown in part c. From these total cost curves can be derived the average cost curves shown in part d. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/fc366feb-933b-4442-bcbf-4538c4ada340/4979c52f59ff7bfefae2933af6c55025c951c85a48b2aafe99eee5eadfd7defe.jpg)



Figure 7.8 Effects of variations in interrelated options.


Congestion, Dimensionalities, Spatial Structure of Services 

Figure 7.8 shows three possibilities for three alternative sets of options $T^{i}$ , $T^{j}$ , and $T^{k}$ . In part b the average total costs at each $V_{C}^{\max}$ are equal, in part a they increase, and in part c they decrease. 

Consider part a of the figure, where curves $i, j, k$ correspond to different choices of the options $K$ and/or $N$ . Assume for the moment that levels of service are equal or demand is inelastic, and thus that the operator's objective is to minimize average cost. If the volume anticipated is $V^{B}$ , then to achieve a minimum average total cost, the options $(K^{i}, N^{i})$ would be chosen. If several years later the volume $V^{A}$ were actually observed, rather than $V^{B}$ , the average total cost $\bar{C}_{\mathrm{T}}^{i}(V^{A})$ would be greater than the average total cost $\bar{C}_{\mathrm{T}}^{j}(V^{A})$ that would have been incurred if the more desirable options $(K^{j}, N^{j})$ had been chosen. Because $K$ and $N$ are relatively long-term options, the operator would have no choice but to live with this higher cost until such time as these options could be adjusted. (This is in fact what happened in the international air travel market in the mid-1970s, when airlines collectively bought too much capacity.) 

Thus the fact that K, N and Q have different time frames means that the options cannot usually be precisely tailored to the volume demanded. This problem is further compounded by the lumpiness of the options—the fact that K and N can, in general, take only integral values. 

## 7.5.3 Service-Oriented Analysis

So far we have varied the options explicitly and found that sometimes target values of Q are infeasible because they exceed the capacity set by K and/or N. An alternative approach is to set Q and then choose whatever values of K and N are required to allow sufficient guideway capacity and a sufficient number of vehicles to meet the desired level of service. This approach is found in many types of models in the literature. To demonstrate the implications of this approach we shall reformulate the model defined in section 7.5.1. 

Service-oriented analysis begins with the specification of a desired service policy, reflected in the schedule frequency Q and fare P, together with the technology $\mathbf{M} = (w, q_{\mathrm{C}}, v)$ . Then the required values of K and N, $K_{R}$ and $N_{R}$ , are found. 

The logic of this type of analysis is as follows: 

1. Specify service policy $(Q, P)$ and technology $(\mathbf{M})$ to establish $\mathbf{T} = (\mathbf{M}, Q, P)$ . 

2. Determine design requirements for K and N to provide enough physical capacity to satisfy Q: 

$$
K _ {\mathrm{R}} (\mathsf {T}) = \Big \langle \frac {Q}{q _ {\mathrm{C}}} \Big \rangle ,\tag{7.37}
$$

$$
N _ {R} (T) = \left\langle \frac {Q}{n} \right\rangle .\tag{7.38}
$$

The brackets indicate “next-highest-integer value”; that is, $K_{R}$ equals the quantity in brackets rounded up to the next highest integer. 

3. Predict the available volume capacity: 

$$
V _ {\mathrm{C}} (\mathsf {T}) = 2 Q w.\tag{7.39}
$$

4. Predict the level of service. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/fc366feb-933b-4442-bcbf-4538c4ada340/9b4131e4d0f1295462ec65d5afa71d508b7718c54a2886a6558b5051b5a8da5a.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/fc366feb-933b-4442-bcbf-4538c4ada340/ca1b30f5b348dc3ffcfc8581c4f66fe5cfef9631d7c07ee11141f6ea677ba188.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/fc366feb-933b-4442-bcbf-4538c4ada340/ab6dc5c43364d4e73fa098142aeaf8ef06e515d4e0dc1fa25c73a0f05d892253.jpg)



Figure 7.9 A service-oriented analysis.


Congestion, Dimensionalities, Spatial Structure of Services 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/fc366feb-933b-4442-bcbf-4538c4ada340/3cc81ed3898854c39713aff39d0b05638ab39b7e2e652657042e0a92a30afa2e.jpg)



Figure 7.10 Average total cost function for a service-oriented analysis.


5. Predict the resources consumed. 

6. Predict the total cost. 

The significance of this formulation can be seen in figure 7.9. Here the indivisibilities of K and N show up clearly—for example, to achieve a service frequency of Q = 3.5n, $N_{R} = 4$ since $N_{R}$ can take only integral values. 

The implications for the average total cost function are shown in figure 7.10. These curves demonstrate the effects of long-, intermediate-, and short-run options and of indivisibilities on total cost. Further, we can see that very different kinds of technologies can be represented by this model; by varying the magnitudes of w, $q_{C}$ , and v, and of $c_{FK}$ , $c_{VN}$ , and $c_{OQ}$ , we can greatly affect the shape of the $\bar{C}_{T}$ curve. 

The indivisibility of components is reflected by discontinuities in the cost curves. The costs suddenly jump when an additional fixed facility or vehicle is acquired (figure 7.11). Jump $J_{1}$ represents the acquisi-

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/fc366feb-933b-4442-bcbf-4538c4ada340/1914595fbc7c91fbd98f53c4e443c5dae9c8e26f79a89fe9acffaa0f94e417f9.jpg)



Figure 7.11 Effect of indivisibilities on average total cost. Jump $J_{1}$ represents acquisition of a vehicle; $J_{2}$ represents construction of a unit of fixed facilities. After Bhatt (1971).


tion of an additional vehicle; $J_{2}$ represents an additional unit of capacity of fixed facilities. Jump $J_{2}$ is much larger in magnitude because the unit vehicle acquisition cost is small compared to the unit cost of a fixed facility. 

The magnitudes of the discontinuities depend on the technological and cost characteristics of the particular system. In some cases the envelope of the cost curve (dashed line) is a satisfactory approximation to the true cost curve. For example, if vehicle acquisition cost is a small percentage of the total cost, $J_{1}$ will be small. Systems with high fixed facility costs relative to vehicle costs show such characteristics. If the vehicle acquisition cost accounts for a large percentage of the total cost and is large compared to the unit cost of the fixed facility, then the jumps will be prominent and the envelope will not approximate true costs very closely. 

It is important to recognize that this formulation represents a specific premise about the objectives to be achieved. These objectives are sufficient capacity in fixed facilities and in vehicle fleet to fully accommodate the desired schedule frequency Q. Many other objectives can be considered, such as choosing K and N to maximize net revenue for a given Q. The results will, in general, be different. 

## 7.6 VEHICLE-FACILITY CONGESTION

So far we have examined the dimensionality of options without considering the congestion effects introduced in section 7.2. To illustrate the interactions of these characteristics of transportation performance functions we shall consider vehicle-facility congestion. 

v (mph) 

## 7.6.1 A Simple Model

Using the queuing analogy, which was a useful modeling approach in the early development of traffic flow theory (see Baerwald 1976), we take for the service rate 

$$
\mu = K q _ {\mathrm{C}},\tag{7.40}
$$

where $q_{C}$ is the capacity in vehicles per unit of time per unit of fixed facilities and K is the number of fixed facilities, and for the arrival rate 

$$
\lambda = q.\tag{7.41}
$$

Thus 

$$
\rho \equiv \frac {\lambda}{\mu} = \frac {q}{K q _ {\mathrm{C}}},\tag{7.42}
$$

$$
\frac {t _ {\tau}}{t _ {\mathrm{P}}} = 1 + J \frac {\lambda / \mu}{1 - \lambda / \mu} = 1 + J \frac {q / K q _ {\mathrm{C}}}{1 - q / K q _ {\mathrm{C}}},\tag{7.43}
$$

$$
\frac {t _ {\tau}}{t _ {\mathrm{P}}} = 1 + J \frac {1}{(K q _ {\mathrm{C}} / q) - 1}.\tag{7.44}
$$

In the highway engineering field relationships of this type are widely studied (Wohl and Martin 1967, Drew 1968, Pignataro 1973); an example, in the form of a speed-volume curve, is shown in figure 7.12. (Speed is, of course, proportional to $1 / t_{\tau}$ .) The quantity $\rho$ is called the volume-capacity ratio. Empirically determined variations on (7.44) have included, for highways (FHWA 1973b), 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/fc366feb-933b-4442-bcbf-4538c4ada340/8272245e76ea8fd0c62ed94354f67539fed06fd03a0a25f7fc578228aad0e0aa.jpg)



Figure 7.12 Typical highway congestion function. From HIGHWAY CAPACITY MANUAL (1965).


$$
\frac {t _ {\tau}}{t _ {\mathrm{P}}} = 1 + 0. 1 5 \left(\frac {q}{K q _ {\mathrm{C}}}\right) ^ {4}\tag{7.45}
$$

and, for arterial streets (prevailing speed 30 mph, three intersections with signals per mile, $t_{P} = 3.05$ minutes per mile) (Davidson as cited in Hutchinson 1974), 

$$
\frac {t _ {\tau}}{t _ {\mathrm{P}}} = 1 + 0. 1 7 1 1 \frac {q / 8 4 1}{1 - q / 8 4 1},\tag{7.46}
$$

where in both cases q is in passenger-cars per hour and $t_{\tau}$ is in minutes per mile. Similar relationships have been developed for other modes for vehicle and nonvehicle links (Rallis 1967, Hengsbach and Odoni 1975). 

## 7.6.2 Effects of Congestion on Costs and Revenues

The effect of vehicle-facility congestion is shown in figure 7.13. Part a shows how $t_{\tau} / t_{\mathrm{P}}$ increases as $q$ approaches the capacity, $Kq_{\mathrm{C}}$ , for each value of $K$ . Part b shows the effect of the congestion on speed relative to the free speed, $v_{\tau} / v_{\mathrm{P}}$ , where $v_{i} = d / t_{i}$ . Part c shows the effect of the reductions in speed on relative productivity, where $n_i = v_i / 2d$ and $n_{\mathrm{P}}$ is the productivity in trips per vehicle per time period at uncongested conditions: 

$$
\frac {n _ {\tau}}{n _ {\mathrm{P}}} = \frac {t _ {\mathrm{P}}}{t _ {\tau}}.\tag{7.47}
$$

From (7.36) we have 

$$
C _ {\mathrm{T}} (\mathbf {T}) = c _ {\mathrm{FK}} K + c _ {\mathrm{VN}} N + c _ {\mathrm{OQ}} \frac {Q}{n _ {\tau}}.\tag{7.48}
$$

For simplicity we assume that the vehicle fleet size is adequate at all times. 

Figure 7.14a shows the cost function for $q = Q$ and different values of $K$ . As $n$ decreases, cost increases. Because $n$ decreases as $q$ approaches capacity for a given $K$ , the total cost increases (as shown by the solid curves) faster than in the previous, uncongested case (shown by the dashed lines). As a result, crossover points for the different cost functions for various options $K$ shift: for example, for values of $q$ between $q_1^*$ and $q_C$ , $K = 2$ has a lower $C_T$ than $K = 1$ . This is demonstrated more clearly by part b, which shows the average total cost $\overline{C}_T$ . The congestion effect causes the average cost functions to become U-shaped. 

In the general case we would consider more than just the cost function: we would examine the effects of congestion and of variations in the options on service levels, equilibrium volumes, gross revenues, and user and operator impacts such as net revenues. Congestion affects not only the costs but also the service levels and thus the equilibrium volume, thereby reducing net revenues below those at uncongested conditions. Thus we would expect that from a net revenue perspective, the frequency at which an additional increment of capacity (in this case, fixed facilities) is desirable may be substantially lower than it would be from a cost perspective alone. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/fc366feb-933b-4442-bcbf-4538c4ada340/e56f3680a8e0a355084731bae6a130d8c6d901a26df9bcba5ac285bcd6fd4eb1.jpg)



Figure 7.13 Effect of vehicle-facility congestion on travel time, speed, and productivity.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/fc366feb-933b-4442-bcbf-4538c4ada340/94e4c960ac361e5a444e3bcf4eb92a8f0abe4352f238135d1bbbdaf5eba13ea8.jpg)



Figure 7.14 Effect of vehicle-facility congestion on cost functions.


From the perspective of capacity alone, in designing a system one wishes ideally to match all of the options so that there is just the right amount of capacity to meet the projected demand. This leads to the service-oriented formulation of a performance function. This is not always practical or desirable for several reasons: the lumpiness of the options, their different time frames, the influence of congestion effects, and the difference between design and actual (equilibrium) volumes. Because of congestion effects (even ignoring demand equilibration), the most attractive options may be different from the ones that just provide sufficient capacity to meet a specified demand level. Further, when demand functions are explicitly considered, the choices may be even more significantly different, since actual volumes may be significantly different from design volumes or capacities (see sections 5.7 and 6.6). 

## 7.7 SYSTEM PERFORMANCE IN SPACE AND TIME

In chapter 6 we explored the basic economics of the vehicle cycle. In this chapter we have examined congestion effects and the dimensionality of options. We shall now look at the full system of services offered in a network and suggest how all of these elements interact. 

## 7.7.1 Some Basic Concepts and Definitions

We start by introducing some basic definitions that are essential in understanding the structure of transportation services over space and time. 

## AN EXAMPLE

Consider the transportation system shown in figure 7.15. Services can be provided, potentially, at three locations, designated A, B, and C in part a. The services would use the network of facilities shown in part b, consisting of seven links. Links 1-3, 3-5, and 1-5 are movement links; links 1-2, 3-4, and 5-6 are transfer links. Link 4-7 connects the 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/fc366feb-933b-4442-bcbf-4538c4ada340/9adce6ab3fe6afe44415cb7030ea7062d35135fe4dc3ca68860369326197e72a.jpg)



Figure 7.15 A simple transportation system.



Table 7.4 Characteristics of five options for the transportation system of figure 7.15


<table><tr><td colspan="2"></td><td><eq>T^{0}</eq></td><td><eq>T^{1}</eq></td><td><eq>T^{2}</eq></td><td><eq>T^{3}</eq></td><td><eq>T^{4}</eq></td></tr><tr><td colspan="7">Routes</td></tr><tr><td colspan="2"><eq>R_{0}:A-B-A</eq></td><td>x</td><td></td><td>x</td><td>x</td><td>x</td></tr><tr><td colspan="2"><eq>R_{1}:A-B-C-B-A</eq></td><td></td><td>x</td><td></td><td></td><td></td></tr><tr><td colspan="2"><eq>R_{2}:B-C-B</eq></td><td></td><td></td><td>x</td><td></td><td>x</td></tr><tr><td colspan="2"><eq>R_{3}:A-C-A</eq></td><td></td><td></td><td></td><td>x</td><td>x</td></tr><tr><td>Markets</td><td colspan="6">Paths</td></tr><tr><td rowspan="3">A-B</td><td>Direct nonstop</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td></tr><tr><td>Direct one-stop</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Connecting,one transfer</td><td></td><td></td><td></td><td></td><td>x</td></tr><tr><td rowspan="3">B-C</td><td>Direct nonstop</td><td></td><td>x</td><td>x</td><td></td><td>x</td></tr><tr><td>Direct one-stop</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Connecting,one-transfer</td><td></td><td></td><td></td><td>x</td><td>x</td></tr><tr><td rowspan="3">A-C</td><td>Direct nonstop</td><td></td><td></td><td></td><td>x</td><td>x</td></tr><tr><td>Direct one-stop</td><td></td><td>x</td><td></td><td></td><td></td></tr><tr><td>Connecting,one-transfer</td><td></td><td></td><td>x</td><td></td><td>x</td></tr></table>

terminal at A with the operating base at O. If this were an airline network, the movement links would represent the controlled airways among cities and the transfer links would represent the airports (including the controlled approach zones, runways, and so forth). For a rail network, the movement links would represent the intercity rail lines, and the transfer links would represent the stations and associated rail yards. 

At present service is being offered between A and B, designated as option $T^{0}$ . This service has the characteristics shown in table 7.4. 

The possibility of extending service to C is being raised. Several alternatives are available: 

Plan $T^{0}$ : Maintain present service. 

Plan $T^{1}$ : Extend service from terminal B to C, operating vehicles from A through B to C and return. 

Plan $T^{2}$ : Operate present service between A and B, and operate a sep-

a A single raute (O-A-B-C-A-O) 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/fc366feb-933b-4442-bcbf-4538c4ada340/962572822dfc6720c443262575cfccef0da91f7f4408eb1587e114bfc96a3a90.jpg)


b Multiple rautes (movements ta operating base nat shown) 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/fc366feb-933b-4442-bcbf-4538c4ada340/a7153933bad0f93f7681f5a3e4d486cf365c5a119acf353d7355d86a0c5b094f.jpg)


c Paths connecting markets A and C 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/fc366feb-933b-4442-bcbf-4538c4ada340/096ecf7e976eb12df0c25d31b464b9e62db66ff032e59b722cc0bc826dfd748f.jpg)



Figure 7.16 Relation of definitions.


Understanding Performance Functions II 

arate service with different vehicles between B and C; thus passengers going between A and C would have to change vehicles at B. 

Plan $T^{3}$ : Operate present service between A and B, and operate a service between C and A. 

Plan $T^{4}$ : Combination of $T^{0}$ , $T^{2}$ , and $T^{3}$ . 

The general logic of the basic analysis introduced in chapter 5 applies here, but we must add significantly to the detail. 

## DEFINITIONS

The following concepts must be distinguished (the relationships among these definitions are shown in figure 7.16). 

A market is a potential set of flows that might be served, specified in terms of their origins and destinations. In the example there are three potential markets (for two-directional flows): B-A, A-C, B-C. 

A route is the path followed by one or several vehicles as each moves from its origin station through one or more way stations and back to the origin. In the example the four routes shown in table 7.4 are under consideration. 

A link is a facility over which vehicles may move. In the example the possible links are 1-2, 3-4, 5-6, 1-3, 3-5, 1-5, and 4-7. Note that, in general, the links are not the same as the markets. 

A path is the route or routes used by a passenger in moving from an initial origin to a final destination. The possible paths in the example are shown in table 7.4. 

For convenience we shall assume that passengers follow the same path in both directions. In general, there will be several paths available in each market, and some paths may require transfers between routes. In the example the available paths depend on which options are implemented. This is shown in the table. 

## THE USER'S PERSPECTIVE

Each user has a different view of the system. Each sees a set of alternative paths $p_{kdp}$ from an origin k to each destination d; and each path $p_{kdp}$ is characterized by a service vector $S_{kdp}$ . Some of the paths may involve direct nonstop services, some direct one- or multistop services, and some one- or multiple-transfer services; further, these paths may use routes of one or several modes. The service attributes characterizing the paths reflect the differences in these services (for example, the effects of en route stops or transfers). 

Any of the demand functions discussed in chapters 2–4 can be used to represent user behavior. The essential point is that the probability of an individual choosing path p should be a function of the service attributes of that path relative to those of alternative paths (see chapter 12). 

There are a variety of ways in which the differences between one- and multistop or between direct and transfer services could be included. At the simplest level the increments of in-vehicle and waiting time due to a stop or transfer could be added to those for other trip components, without any special treatment. More realistic formulations might include the number of en route stops or the number of transfers as explicit service attributes, or might even try to distinguish qualitative aspects of these attributes (for example, in international air travel a three-hour transfer time at a modest tropical airport with minimum facilities might influence traveler behavior differently from a three-hour transfer time at a major international center with extensive tax-free tourist shops and related services). 

## THE OPERATOR'S PERSPECTIVE

Users view the system primarily (perhaps exclusively) from a dis-aggregate perspective: what matters to them is the services available in the markets in which they are interested. Operators, on the other hand, are interested almost solely in the aggregate performance of their portions of the system. For a private-sector operator the total net revenue and other measures of profitability are of primary interest. Even a public-sector operator is mainly concerned with maintaining maximum effectiveness. (Both obviously do pay some attention to the degree of service in disaggregated markets, if for no other reason than to understand which parts of the system are relatively weak or strong contributors to profitability.) 

From the operator's perspective the basic question is, What are the alternative strategies for implementing and/or operating the system and what are the costs and revenues associated with these strategies? A fully specified strategy includes the fixed facilities and their characteristics; the types and numbers of vehicles and their characteristics; the structure of routes on which services will be offered; for each route, the schedule (or frequency of service), the vehicle(s) to be assigned, the fixed facilities to be traversed; and for each path in each market, the price to be charged. Thus the operator must specify a complex and detailed pattern of services over space and time. (Figure 5.4 illustrates just how complex the route of a single vehicle can be.) 

At the core of this specification is the assignment of vehicles to routes, since each assigned vehicle operates according to the prescribed schedule. Correspondingly, for each vehicle there is a vehicle cycle, or pattern of use, involving operational cycles, service cycles, and the annual cycle. The economics of each vehicle cycle can be viewed in isolation, but that can be misleading. In the context of operations in space and time, the economic performance of a strategy is likely to be significantly different from the simple addition of independent vehicle cycles. This happens because of the ways in which the parts of the system are interrelated and the ways in which the system operates to deliver different services to different markets (Taylor 1977). Figure 7.16 shows just how different the views of users and operators are; indeed the paths taken by users are often very different from the routes of vehicles (for example, compare the one-transfer path in part c with the vehicle movement over routes $R_{0}$ and $R_{2}$ , which may be only portions of the routes flown by the respective vehicles). 

In order to understand the economics of vehicle performance we must therefore understand the ways in which several vehicles on several routes perform as a system, delivering different services in different markets. To develop this understanding in this introductory discussion we shall build on our previous analysis of the vehicle cycle and its economic implications. 

## 7.7.2 The Operating Plan

An operator typically utilizes a fleet of vehicles over a number of routes. In the simplest cases each vehicle is assigned to a specific route and shuttles back and forth over that route at regular intervals. In general, however, the efficient utilization of a fleet of vehicles will involve the integrated use of a number of vehicles on a number of routes. The specification of an operating plan includes: 

1. a list of the vehicles to be utilized; 

2. a list of the routes to be served; 

3. a timetable of services over each route; 

4. an assignment of each vehicle to a schedule such that the set of routes is covered and the timetable is met; and 

5. an assignment of operating labor (crews) to vehicles and services. 

## AN AIRFREIGHT EXAMPLE

Figure 7.17 shows an operating plan for a London-based fleet of seven freighter aircraft. These are European short-haul services to 24 cities 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/fc366feb-933b-4442-bcbf-4538c4ada340/97dee652333717afe9df1d45eb25d60f37b8442e8d722658aca47bdcb245f568.jpg)



Figure 7.17 An airfreight operating plan. Letters represent cities. From P. S. Smith (1974), p. 88.


over 19 routes. The following features of this plan should be noted (P. S. Smith 1974, p. 88ff.): 

1. Six aircraft are assigned to operational cycles and the seventh is retained on standby reserve in case of unexpected problems with the other aircraft or weather problems. 

2. Each operational cycle covers the seven-day week and is unique. 

3. The assignment of specific aircraft to the seven operational cycles is changed each week. 

4. Service to any given market is provided by a different aircraft on different days. 

5. Much of the maintenance is scheduled early in the week, since the bulk of the flying time occurs in the evening, at night, and late in the week when demand is greatest. 

6. Operational servicing occurs during the operational cycles, generally at the periods of lowest demand. 

7. Some services are provided at the same time throughout the week to provide regularity to shippers. 

8. There appears to be spare capacity in the fleet (see cycle 6) in that there do not seem to be any opportunities for sufficiently productive use of this capacity. 

In discussing the vehicle cycle in chapter 6, we noted that one measure of productive utilization of a vehicle is the number of hours it is utilized. The utilization achieved by this particular operating plan varies by operational cycle, as shown in table 7.5. The average utilizations are 45.8 hours for the first six aircraft and 39.3 hours for the fleet of seven (corresponding to annual utilizations of 2,407 and 2,063 hours, respectively). Note that the average for the fleet as a whole is significantly lower than the maximum achievable by a single vehicle on a single cycle. 


Table 7.5 Variations in utilization by operating cycle


<table><tr><td rowspan="2">Cycle</td><td colspan="2">Utilization in hours</td></tr><tr><td>Per week</td><td>Per year</td></tr><tr><td>1</td><td>64.2</td><td>3,371</td></tr><tr><td>2</td><td>51.0</td><td>2,678</td></tr><tr><td>3</td><td>49.8</td><td>2,615</td></tr><tr><td>4</td><td>36.5</td><td>1,916</td></tr><tr><td>5</td><td>54.8</td><td>2,874</td></tr><tr><td>6</td><td>18.8</td><td>987</td></tr><tr><td>7</td><td>0</td><td>0</td></tr></table>


Source: P. S. Smith (1974). 


This example demonstrates the complexity that can enter into an operational plan. It also demonstrates that the effective utilizations of specific vehicles can vary widely, so that the estimation of the effective utilization of a fleet, or of an "average" vehicle, is often difficult if one does not actually construct a detailed operating plan. Since the economics of the system depend significantly on the utilization achieved, as illustrated in section 6.7.1, it is clearly important to examine the utilization of the fleet rather than that of a single vehicle. 

## OTHER RESOURCES

In the foregoing example we explicitly mentioned only vehicles. In general, there are several types of resources that are assigned in the process of developing an operating plan: 

1. vehicles; 

2. vehicle crews (the driver or pilot and other personnel traveling with the vehicle); 

3. other labor (for example, at terminals or maintenance facilities); and
4. facilities. 

Since the capacities of fixed facilities are limited, in many contexts the scheduling of these facilities is an important part of the operating plan, as in the case of boarding gates at airports. 

The treatment of operating labor (vehicle crews) is often particularly complex. In many contexts historical practices and negotiated agreements on work rules result in quite detailed and complex constraints on how crews can be utilized. For example, there may be limits on maximum working hours per shift, maximum in-travel hours, maximum distance traveled, minimum time between successive shifts, and so forth. As a result, the development of an operating plan with an efficient utilization of personnel resources is a difficult task, usually requiring intimate knowledge of specific working practices in a particular system. As we have seen, the influence of fixed facilities and various types of congestion effects can also be important. 

Various mathematical models and computer programs have been developed for use in preparing portions of an operating plan (Simpson 1969, 1977, Ehrlich 1977; see especially the journal Transportation Science and the operations research literature). 

## 7.8 SUMMARY

In this chapter we have examined three sets of factors that can significantly influence the performance of a system. 

Congestion in a transportation system occurs when the average processing time per unit increases as demand for service increases. The level of demand at which congestion becomes important is determined by the capacity of the system. The physical capacity is the maximum number of units that can be processed by a system under any circumstances, but this may well involve very long delays. In contrast, various definitions of practical capacity can be chosen such that delays are within more tolerable limits. 

The significance of congestion is that the marginal time (or cost) is greater than the average time (or cost). 

Many types of congestion occur in transportation systems. It is especially important to distinguish load-dependent and load-independent congestion. The first category includes load-vehicle and load-schedule congestion. The second category includes vehicle-facility and vehicle-schedule congestion, which can occur regardless of the load (passengers or freight) moving through the system. 

Using simple models of congestion, we modified performance model I to demonstrate the effects of congestion on user and operator impacts. 

In general, transportation system planners are faced with a wide variety of options that offer a range of implementation time frames and show various forms of indivisibilities. These interrelationships among options have a significant effect on user and operator impacts in that it often becomes difficult to choose a precise combination of options that is "best" for a particular situation. A third performance model was used to demonstrate these effects.

As an example of the combined effects of congestion and the dimensionality of options, vehicle-facility congestion was explored through traditional highway facility models. The effect of congestion was shown in the cost functions, which became U-shaped.

The spatial structure of a transportation system can be quite complex. A wide variety of different service strategies can be implemented in the same network. Each user sees a set of alternative paths from an origin to a set of possible destinations. Some paths may involve non-stop or one- or multiple-stop direct services; other paths may require one or more transfers. User choice of alternative paths is a function of the service levels of the paths.

While users see the system from a disaggregate perspective, operators are interested primarily in the aggregate performance of a total system, as reflected in economic and other measures.

Complete specification of a system from the operator's perspective requires identification of the fixed facilities, the vehicles, the set of routes; for each route, the vehicles assigned and the schedule; and for each path, the prices. The assignment of vehicles to routes is at the heart of this specification; the economics of a system are related to the characteristics of each vehicle cycle over each route. The relationships are not simply additive. Because of the interrelations of vehicle routes and markets, evaluation of the economic performance of a system strategy is likely to be significantly different from a simple addition of independent vehicle cycles.

The operating plan of a system is the description of how vehicles are utilized to provide services. The detailed specification of an operating plan includes the vehicles to be used, the routes to be served, the timetable of services over each route, and the assignment of vehicles, facilities, and operating labor to the scheduled services.

In the working out of a practical operating plan, numerous deviations from a nominal optimum may be required. For example, the utilizations in a fleet of vehicles in international airfreight service may range from 64 to 19 hours per week, with one aircraft kept in reserve (0 hours per week). Thus the average effective utilization for the fleet as a whole is 40 hours.

Congestion, Dimensionalities, Spatial Structure of Services 

## TO READ FURTHER

The various formulations and models of congestion comprise a large body of material: see, for example, Rallis (1967), Gazis (1974), and Daganzo (1978b). For applications to port and airport planning see De Weille and Ray (1974), Robinson and Tognetti (1974), Wilmes and Frankel (1974), and Hengsbach and Odoni (1975). For models of systems interrelations see Simpson (1969, 1977), Pollack (1974), Ehrlich (1977), and the large body of literature in operations research on optimization and simulation applications. 

## EXERCISES

7.1(E) At present, a regularly scheduled shipping route is operated by operator A with direct service to both ports X and Y, on the same coast, from port Z, 5,000 miles across the ocean. Operator A thinks it might be financially advantageous to eliminate port Y from the route; then cargo from Y would be transshipped to X, either by truck or by other water carrier, and loaded there for shipment to Z. Thus the ship from Z would no longer call at port Y. The carrier is prepared to absorb the cost of the inland transportation between X and Y if the savings are great enough. 

Will the elimination of the separate port call at Y be profitable if demand is constant? if demand varies? 

Define the necessary variables and relationships and indicate the analysis you would do to answer these questions. 

7.2(E) In exercises 1.6 and 5.1 we considered the issue of optimal train operating strategies under the assumption that service levels were independent of demand. In fact, the time a car spends waiting at a railyard to be placed on an outgoing train is an example of vehicle-load congestion. Let 

$$
\mathbf {S} = (t _ {\mathrm{iv}}, t _ {\mathrm{w}}),
$$

$$
t _ {\mathrm{iv}} = \frac {D}{v},
$$

$$
t _ {\mathrm{w}} = \frac {2 4}{2 Q} \left(1 + \frac {J \rho}{1 - \rho}\right), \quad \text { where } \rho = \frac {V _ {\mathrm{D}}}{V _ {\mathrm{C}}} \text { and } V _ {\mathrm{C}} = Q L.
$$

Incorporate this service function with congestion into exercise 5.1. 

Assume J = 0.1 and then 0.001 and discuss the results. 

7.3(C) The relationships developed in this chapter ignore a number of elements that are sometimes important: 

1. fixed facilities costs and utilization 

2. general overhead and administrative costs 

3. relationships of vehicle usage (for example, miles per year) to serviceable life, maintenance requirements, depreciation, and salvage values (see De Weille 1966, Annex I). 

a. Extend the relationships developed in this chapter to include consideration of elements 1, 2, and 3, separately and together. 

b. Take a particular mode or context and develop specific relationships and numerical examples for that situation, incorporating elements 1, 2, and 3 separately and together. 

7.4(C) Compare the “fundamental diagram” of traffic flow theory (Drew 1968, Pignataro 1973, or Baerwald 1976) with figure 7.13 and discuss. 

7.5(C) The Bay Area Rapid Transit System (BART) was heralded as a major innovation in rail rapid transit. Soon after the system opened, however, it became clear that innovation involves many problems. One of the key problem areas turned out to be vehicle reliability. 

Planners of BART anticipated that in due course at least 80 percent of the cars in the fleet would be available for service at any given time. Instead, for a number of reasons that are still the subject of active investigation and litigation, car availability for revenue service during 1974 and 1975 varied between 45 and 60 percent (Ellis and Sherrett 1976). What impact would this have on system performance? How would you incorporate this factor in a performance model? 

## 8.1 THE SCOPE OF EQUILIBRATION

In the prediction step of transportation analysis we consider both human behavior and system performance. We represent human behavior (primarily as consumer behavior) by means of demand and activity-shift models. We represent the performance of the transportation system through resource and service models. 

Equilibration involves creating an interface between these two factors. The interactions between human behavior and system performance are resolved over several different time frames and through several different mechanisms. Three major groupings of these interactions were identified in chapter 1: travel-market equilibrium, activity-system equilibrium, and transportation-operator equilibrium. 

In the short range the transportation-system options T and the activity-system options A are fixed. Thus the service function S can be interfaced with the travel demand function D to determine an equilibrium flow pattern. This is the type 1 relationship. There are two key methodological issues in this travel-market equilibration. The first is how to take into account the service function, and especially the congestion effects introduced in chapter 7. The second involves the spatial distribution of services, the topological structure of networks, and the behavioral bases of choice of travel routes. 

In the long range the activity system will, in general, change. The nature of the change in any period will be affected in part by the equilibrium flow patterns that have existed in each prior period and in part by forces internal to the activity system, such as economic and social changes in a society. The time lags are an important part of this process, and it may be more correct to describe long-run activity-system equilibrium as a direction toward which the system is continually adjusting rather than as a state that is ever reached. Metaphorically the travel demand function D can be described as shifting over time, thus causing shifts in travel-market equilibrium which then bring about further activity shifts, and so on. This is the type 2 relationship. Because of the time lags and the complex interrelationships, developing good models of this activity-system equilibration process is very difficult. 

In the long range also, each transportation operator can, in principle, adjust the options within his control to achieve a travel-market equilibrium at each point in time that maximizes the achievement of his own objectives. In principle, one could construct models for predicting the behavior of operators under various conditions if a number of special conditions are met. As demonstrated in section 5.7, the result would be the supply function of classical economics. Then one could also predict the equilibrium conditions of the transportation operators. In practice, however, these conditions are not met, and for many additional practical reasons it is difficult to model the process of transportation-operator equilibration except under special and usually highly idealized conditions. (In volume 2 we shall analyze in greater detail operator equilibration and the relationship between the classical supply function and the transportation system performance function.) 

In this chapter we shall explore the concept of travel-market equilibrium, with particular emphasis on alternative computational approximations, and the implications of actions defined over time for the relationships between travel-market and activity-system equilibration. In chapter 12 we shall expand our consideration of travel-market equilibration to include the spatial structure of networks. 

## 8.2 TRAVEL-MARKET EQUILIBRATION

Given a demand function, one is tempted to use it for predicting flows by assuming that the transportation-system service levels are known at the outset of the analysis and do not change. In general this is not the case; at least some of the service attributes will vary according to the number of users of the system. For example, travel time over a highway or bus route, or processing time through a rail classification yard, will depend on a level of usage. This often makes prediction of an actual level of usage difficult even if the demand function is known. The level of usage will be a function of the service provided, as specified by the demand function; but the service will be affected in turn by the level of usage. This second dependency is reflected by a service function S of the form 

$$
\mathbf {S} = \mathbf {J} (\mathbf {V}, \mathbf {T}),\tag{8.1}
$$

where T represents the characteristics and V the volumes of the transportation system. 

## 8.2.1 Equilibrium Conditions

In general, both service and demand functions must be used, and the volume is determined by the equilibrium of service and demand. Prediction of flows requires consideration of the interactions of demand (consumer behavior) and service (technology) through finding the equilibrium flow pattern in the travel market. 

In the general case travel-market equilibration requires a computational process that explicitly determines a flow pattern—volumes and levels of service—that meets both service and demand conditions. Specifically, at equilibrium, the service levels $S_{i}$ on each facility i in the system are those that would occur at the predicted volumes, 

$$
\mathbf {S} _ {i} = \mathbf {J} _ {i} (\mathbf {V} _ {i}) \quad \text {   for   all   } i;\tag{8.2}
$$

and the volumes $V_{i}$ on all facilities i are those that would occur at the predicted service levels, 

$$
\mathbf {V} _ {i} = \mathbf {D} (\mathbf {S} _ {i}) \quad \text { for   all } i.\tag{8.3}
$$

This approach of explicit equilibration is the most general one. Prediction of volumes and service levels under a new set of transportation system options using the demand function alone generally leads to errors, because the service level assumed may be inconsistent with the volume predicted by the demand function alone. The service function, if taken into account, will ensure this consistency. The importance of these effects is shown in the following example. 

## 8.2.2 An Example

Consider travel by air between two cities in a densely populated region. The volume of travel in the base year, 1960, is 6,000 persons per day. The demand is forecast to increase by 1,000 per year each year (about 15 percent per year, not compounded). (In the mid-1960s typical forecasts envisioned 14–17 percent per year increases in air passenger travel, compounded annually.) We consider three ways in which demand could be forecast. 

In the first approach demand is simply assumed to grow by 1,000 per year. 

In the second approach we recognize that demand depends on travel time and formulate an explicit demand function: 

$$
V = a - b t.\tag{8.4}
$$

In 1960 a is 10,000, and it increases by 1,000 each year. Also in 1960, t is 2 hours. The coefficient b equals 2,000 persons per day per hour of travel time. If we assume that travel time remains constant, independent of volume, we get the same forecasts as in the first approach. 


Table 8.1 Comparison of forecasts


<table><tr><td>Year</td><td>(a) Volume for constant travel time</td><td>(b) Volume with congestion considered</td><td>(c) Overestimate of volume</td><td>(d) Time with congestion</td></tr><tr><td>1960</td><td>6,000</td><td>6,000</td><td>0</td><td>2.00</td></tr><tr><td>1962</td><td>8,000</td><td>8,000</td><td>0</td><td>2.00</td></tr><tr><td>1964</td><td>10,000</td><td>9,000</td><td>1,000</td><td>2.50</td></tr><tr><td>1966</td><td>12,000</td><td>10,000</td><td>2,000</td><td>3.00</td></tr><tr><td>1968</td><td>14,000</td><td>11,000</td><td>3,000</td><td>3.50</td></tr><tr><td>1970</td><td>16,000</td><td>12,000</td><td>4,000</td><td>4.00</td></tr><tr><td>1972</td><td>18,000</td><td>12,400</td><td>5,600</td><td>4.80</td></tr></table>

In the third approach we recognize that travel time is affected by volume; that is, after a certain volume congestion builds up in the system. This is reflected in the service function. We assume an explicit function made up of three linear segments: 

$$
t = \left\{ \begin{array}{l l} 2, & 0 \leq V \leq 8, 0 0 0, \\ \frac {V}{2 , 0 0 0} - 2, & 8, 0 0 0 \leq V \leq 1 2, 0 0 0, \\ \frac {V}{5 0 0} - 2 0, & V \leq 1 2, 0 0 0. \end{array} \right.\tag{8.5}
$$

At V = 12,000 the time has doubled to four hours; from this point on the system is very close to capacity, and travel time increases at the rate of two hours for every additional 1,000 passengers per day. 

The effects of congestion are shown in table 8.1. Column a indicates the results with constant travel times, and column b the results when congestion effects are considered. The amount of overestimation due to neglect of the service effects is shown in column c. Column d shows how the equilibrium travel time changes from the initial value t = 2 hours. The results are shown graphically in figure 8.1. 

The implications are clear: service effects can be ignored only under special conditions. In general, omitting the service effects results in serious errors in forecasting flows. For example, consider the year 1966. If congestion is not considered, the estimate of flows would be a volume of 12,000 persons per day and a travel time of 2 hours—point A in the figure. When congestion effects, reflected in the service function, are considered, the estimate would be 10,000 persons per day and 3 hours, as shown by point B (see also section 7.3). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/fc366feb-933b-4442-bcbf-4538c4ada340/00f7e614d40682cc93908b13d2ed5323d5a3d081aa08d8e51302e00c47ef1f04.jpg)



Figure 8.1 Effects of congestion on demand.


## 8.3 SOME PRACTICAL APPROXIMATIONS TO TRAVEL-MARKET EQUILIBRATION

The preceding discussion has indicated why an explicit treatment of the interaction of service and demand is important in an equilibration procedure. By “explicit” we mean that the analyst explicitly considers alternative approaches and the implications of simplifying assumptions. In particular situations approximations may well be desirable. 

## 8.3.1 Alternative Assumptions

Sometimes it may be acceptable, practical, or even essential to reduce the complexity of the general problem by making one of several assumptions. Either of the assumptions we shall now describe may be appropriate in a particular context. The analyst must, however, carefully weigh the limitations introduced by making such assumptions, as illustrated in section 8.2.2. If the assumptions are acceptable, equilibration is greatly simplified. 

## KNOWN-SERVICE-LEVEL ASSUMPTION

Sometimes the analyst may feel that congestion effects are sufficiently insignificant that the level of service resulting from an equilibrium analysis can be estimated beforehand, either because it is essentially the same as that assumed prior to equilibration (as when operating in the flat portion of the service function) or because there is a good basis for an estimate of the change. 

## KNOWN-VOLUME ASSUMPTION

Sometimes demand effects are sufficiently insignificant that the volume predicted by an equilibrium analysis can be estimated beforehand, either because it is essentially the same as that for a prior condition (as when demand elasticities are close to zero) or because there is a good basis for estimating the magnitude of the demand without an elaborate analysis. 

## 8.3.2 Using the Known-Service-Level Assumption

If the service levels can be easily estimated, then equilibration is simplified, and priority is placed on the demand function: 

Step 1: Estimate new service levels, $S_{i}^{\prime}$ . 

Step 2: Using the demand function, find $V_{i}^{\prime} = D(S_{i}^{\prime})$ . 

Step 3: Check against the service functions: 

$$
\mathbf {S} _ {i} ^ {\prime \prime} = \mathbf {J} _ {i} (\mathbf {V} _ {i} ^ {\prime}),
$$

$$
\Delta \mathbf {S} _ {i} \equiv \mathbf {S} _ {i} ^ {\prime \prime} - \mathbf {S} _ {i} ^ {\prime}.
$$

If the $\Delta S_{i}$ are sufficiently small, terminate; if not, revise estimates of $S_{i}^{\prime}$ and repeat step 2. 

This approach is especially useful when it is believed that congestion or other volume-related influences on service levels are minimal or insignificant and that the major effects are changes in the level of demand. It was used in the demand chapters (2, 3, and 4) and in much of the technology chapters (5 and 6), and its limitations were illustrated in section 8.2.2. 

This assumption is often made in practice. For example, in assessing urban transportation systems, analysts often assume that transit travel times are constant and independent of volumes. In many freight system analyses in which a demand function is used, this assumption has also been made. 

The approach is illustrated in figure 8.2b, where $J^0$ is the initial service function and $J'$ the new service function. Both are constant and independent of volume over the range of volume of interest. ( $J'$ is shown dashed to indicate that it may be the same as $J^0$ .) 

o Generol cose 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/fc366feb-933b-4442-bcbf-4538c4ada340/3660e585dc650c648cc235c78ca9508cd265b53645d06dde2677496eaab59c3c.jpg)



b Known-service-level assumption


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/fc366feb-933b-4442-bcbf-4538c4ada340/97cb44293dcf88082eb99ddd3a7ccac8258695e95639b063b2269131c5e43f9b.jpg)


c Known-volume assumption 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/fc366feb-933b-4442-bcbf-4538c4ada340/59e28430246512753604ff92b35abb021168c9e714bf1f6670ce61a5598716ff.jpg)



Figure 8.2 Two simplifying equilibration assumptions.


## 8.3.3 Using the Known-Volume Assumption

If the volume of demand can be easily estimated, then once again equilibration is simplified, and priority is now placed on the performance function: 

Step 1: Estimate new volumes $V_{i}^{\prime}$ . These may be assumed the same as the prior volumes $V_{i}^{0}$ or set by a load-factor assumption ( $V_{i}^{\prime} = \lambda V_{C}^{\prime}$ ) or set as a design goal (see section 5.7). 

Step 2: Using the service function, find service levels $S_{i}^{\prime} = J_{i}(V_{i}^{\prime})$ . 

Step 3: Check against the demand function: 

$$
\mathbf {V} _ {i} ^ {\prime \prime} = \mathsf {D} _ {i} (\mathbf {S} _ {i} ^ {\prime}),
$$

$$
\varDelta \mathbf {V} _ {i} \equiv \mathbf {V} _ {i} - \mathbf {V} _ {i} ^ {\prime \prime}.
$$

If the $\Delta V_{i}$ are acceptable, terminate; if not, repeat step 2 with some appropriate revised estimate of $V_{i}^{\prime}$ . 

This approach is especially useful when it is believed that demand is relatively insensitive to the changes being analyzed. It is often used (implicitly) where the primary emphasis is on appraising the operational performance of a given system under various operating policies, for example, when a stochastic simulation model is used for port or terminal analysis. Often the only check against demand is whether the system has sufficient capacity to serve the estimated (assumed) volumes $V_{i}$ . As shown in figure 8.2c, this amounts to assuming constant demand over the range of service levels being examined. ( $D'$ is shown dashed to indicate that it may be the same as $D^{0}$ .) 

## 8.4 INFLUENCE OF MARKET STRUCTURE

Several features of demand influence how a set of options performs in an equilibrium context. 

Demand is not uniform in several key respects (see, for example, Hill, Tittemore, and Gendell 1973, Campbell 1977, Taylor 1977). First, the actual volume using a particular service will vary with time: time of day, day of the week, and week of the year. Second, volumes in the two opposite directions on the same route will usually be unequal during a given time period. Third, performance of a system is a composite of performance over many different routes. Fourth, demand is often random; that is, it is a stochastic variable distributed with means exhibiting the properties of temporal and directional variation indicated above. Stochastic variation in demand also affects the average conditions achieved and the economic impacts on the operator. In this section we shall examine the first two elements; the third and fourth will be explored in volume 2. 

The cumulative result of all of these market factors is an average or overall economic picture (costs, operator revenues, user benefits) substantially different, in many situations, from “typical” or peak conditions. Further, the overall economic viability of a particular operator may be substantially dependent on the responses it makes to these variations, especially to the off-peak and backhaul conditions. 

In general, the demand functions at different times and in different directions are interdependent. For example, peak-period congestion may influence some users to shift their travel to other time periods. Ideally, in a complete analysis all of these effects would be included in the demand functions and in the travel-market equilibration procedures. However, this is not often feasible. For approximate analyses specific parameters can be defined to summarize these effects, such as the backhaul ratio or a peaking factor. 

## 8.4.1 The Nonuniformity of Demand over Space

The nonuniformity of demand over space was discussed in section 6.5.1. There we showed how a backhaul ratio could be defined to approximate the effect of directional imbalances. This parameter was used in a manner analogous to a load-factor estimate as an approximation to equilibration. In that analysis we showed that the ability of owner-operator truckers to compete for rail traffic depended in part on the value of this parameter. 

## 8.4.2 The Nonuniformity of Demand over Time:

## The Peaking Problem

The demand for transportation varies with time and with direction. If we take any fixed period of time as a base, we find that throughout the period the magnitude of demand varies even if the same level of service is offered at all times. For example, in an urban transportation situation the volume traveling inbound to the central business district in the peak morning rush hour will usually be much greater than the volume at midday in the middle of the week. 

Because of this variation, the equilibrium volume varies. Thus the average load factor achieved is a composite of varying load factors achieved for different time periods. For example, there are peak and off-peak periods in almost all transportation contexts. All other impacts—costs, revenues, and so on—also vary with time. 

A major factor influencing these variations is the fact that the transportation operator usually adjusts the options to provide different levels of service in different time periods. For example, peak-period service frequencies may be greater than off-peak frequencies. Thus the net economic effect of time variations can be quite complex, particularly when labor rules or other factors introduce cross-linkages among costs in different time periods or when demand cross-elasticities produce complex equilibration effects. 

To take these variations into account one can explicitly formulate different demand functions for different time periods and directions. For example, to represent these variations in an urban situation we might distinguish the following categories: 

1. trip purpose, p: work, school, other (shopping, social, recreational); 

2. market segment categorized, for example, by income group, i: high, medium, low; 

3. time period, t: weekday peak (A.M. or P.M.), weekday off-peak, evening or weekend; 

4. direction, d: inbound, outbound; 

5. day of week and season of year, h. 

In principle, a set of demand functions can be defined corresponding to the various possible combinations $(i, p, t, d, h)$ . Thus there would be a specific demand function for trips from home to work by high-income travelers in the A.M. peak period inbound to the central area on spring weekdays. This would lead to a large number of demand functions. (It is important to realize that since time of trip is a traveler choice, there should ideally be linkages among the time-of-day models such that there is a cross-elasticity among time periods; see chapter 11 and the discussion in Kraft and Wohl 1967.) This approach is often taken in large-scale regional studies, although some of the effects may be represented by factors rather than separate models. Travel-market equilibration would then have to include all of these. 

For small-scale studies it is often reasonable to simplify the analysis quite a bit. In the simplest approach one or a few demand functions are formulated explicitly. Travel-market equilibration is done with this function, and the volumes for other combinations of the set are derived from the resulting equilibrium flow. This is illustrated in case study II, chapter 10, where the approach used is to predict peak and off-peak trips in the dominant direction of flow and then to predict trips in the reverse direction as a fixed fraction of these trips. Even more simply, many transportation studies predict explicitly only peak-period flows and then estimate off-peak flows as a fixed ratio to peak volumes. 

In predicting impacts from user and operator perspectives, one must consider the different services offered and impacts achieved in each time period. The overall evaluation of a transportation plan must often include consideration of these different impacts in different time periods. The relation between peak and nonpeak periods is particularly important; when sufficient capacity is provided for peak periods, there is excess capacity for other periods. This leads to questions of allocation of costs, differential pricing by time of day, and related issues. 

## 8.5 ACTIVITY-SYSTEM EQUILIBRATION AND THE DYNAMICS OF PREDICTION (OPTIONAL READING)

We start with some definitions: 

$T^{t}$ = the state of the transportation system at time t, 

$\mathbf{A}^t =$ the state of the activity system at time $t$ , 

$T^{t} = \text{a set of actions taken at time } t \text{ to change the transportation system (defined in terms of the transportation options),}$ 

$A^{t} = \text{a set of actions taken at time } t \text{ to change the activity system (defined in terms of the activity options),}$ 

$E^{t}$ = the exogenous events that occur during time period t. 

Then a particular plan (or policy or program) P consists of a sequence of actions implemented over n time periods: 

$$
\mathcal {P} = \left(\mathcal {T} ^ {1}, \mathcal {A} ^ {1}; \mathcal {T} ^ {2}, \mathcal {A} ^ {2}; \dots ; \mathcal {T} ^ {n}, \mathcal {A} ^ {n}\right).\tag{8.6}
$$

To predict the impacts associated with this plan requires the explicit interrelationship of travel-market equilibration and activity-system equilibration over time. 

## 8.5.1 Scenarios

The evolution of the activity system over time will be a function of that system's own internal dynamics (including factors such as population growth and the changing structure of the economy), the influences of transportation (as reflected in changing service levels over time), and the influences of exogenous events. A scenario $\mathcal{E}$ is a statement of the set of exogenous events that occur over $n$ time periods: 

$$
\mathcal {E} = (\mathsf {E} ^ {1}, \mathsf {E} ^ {2}, \dots , \mathsf {E} ^ {n}).\tag{8.7}
$$

An explicit scenario is required for every model system; there are always some exogenous variables that must be defined as inputs, such as population growth rate or energy prices. 

## 8.5.2 Linkages

Potentially a model system can incorporate all three types of equilibration. Initially we shall assume the general case in which travel-market and activity-system equilibration are explicitly included, but with no operator equilibration. Then we shall consider the special case where operator equilibration is included. 

An activity-shift model represents the type 2 relationship and is used to predict the changes in the activity system that will occur as a consequence of activity-system actions, the flow patterns in the transportation system, and the resource consumption by transportation. Given the activity system $A^{t-1}$ , the flow pattern $F^{t-1}$ , and the resource consumption $R^{t-1}$ at time t - 1 and the actions $A^{t}$ to be taken in time period t, the activity-shift model predicts the state of the activity system at time t, as indicated in figure 8.3. This prediction also includes the effects of exogenous changes in environmental variables, $E^{t-1}$ ; this might represent international commodity prices external to the country being simulated, or the influence of the national economy on employment levels and distribution by industry type. 

For expository purposes we combine the other four basic types of prediction models (service, resource, demand, and travel-market equilibration) into a single block called the transport model. This terminology was used in the Harvard-Brookings Model System (Kresge and Roberts 1971). Given an activity system $A^{t}$ and transportation system $T^{t}$ at time t—or alternatively the transportation system $T^{t-1}$ at time t - 1 and the actions $T^{t}$ to be taken in time period t, resulting in a changed system $T^{t}$ —the transport model predicts the flow pattern $F^{t}$ during time period t—that is, service levels $S^{t}$ and volumes $V^{t}$ —and the resources $R^{t}$ consumed by transport during that period, as indicated in figure 8.3. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/fc366feb-933b-4442-bcbf-4538c4ada340/47e8193fc03c1871d45662e41e438585baf72d89aae40dbca2d9717ae89a1f3f.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/fc366feb-933b-4442-bcbf-4538c4ada340/53b071a31eca8ecc70ef1b729680a3a22d0539389cc66960001ef0484acaade1.jpg)



Figure 8.3 Flow charts showing inputs and outputs of (a) an activity-shift model and (b) a transport model.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/fc366feb-933b-4442-bcbf-4538c4ada340/3b959aa5be02452865c3db3097f6e2a67062cc8f4930e77adcceedd711fb7b32.jpg)



Figure 8.4 Time-dependent forecasts, showing the linkage of activity-shift and transport models.


The linkage of the two blocks of models is shown in figure 8.4. The activity-system actions in time period t are assumed to influence the activity system and thus to affect the demand for travel in the transport model in that time period. This is the approach used in the Harvard-Brookings Model System (HBMS). Alternatively activity-system actions in time period t are assumed to affect the activity system in the following time period, and thus the demand for travel in time period t is based on the activity-system changes since the last time period. This approach is often used in urban transportation land-use models. 

The integrated combination of transport and activity-shift models allows simulation of the evolution of the transportation and activity systems over time. This is especially important in representing the time lags in transportation impacts on the activity system; an action at time t may take several time periods to impact fully on the activity system. Further, such a time-staged simulation model is essential for testing alternative sequences and timings for implementation of a set of transportation actions. This is illustrated in figure 8.5, where $I^{t}$ represents all of the impacts predicted to occur in time period t (flows, user impacts, operator impacts, etc.). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/fc366feb-933b-4442-bcbf-4538c4ada340/5c6b689239c5f5d7c59bfee246f5455fc9f562b2fa6db25a139d36b80e0cd7b8.jpg)



Figure 8.5 Prediction of time-staged strategies over n time periods.


Operator equilibration is sometimes included in the process. For this an operator decision logic is assumed, and the transportation system actions in period t are divided into two groups. Some of the actions are established as part of the specification of the plan being tested; these are external to the model and are denoted by $T^{te}$ . Other actions are determined internally, by logic within the model reflecting the operator decision logic assumed, and are denoted by $T^{ti}$ . (This internal selection of transportation actions represents the type 3 relationship in the models.) 

For example, in the HBMS the internally determined decisions are primarily decisions on transport prices and on vehicle-fleet sizes and service frequencies. The decisions on investment in facilities are external. Functionally the operator logic is often an integral part of the transport-model block. For example, the required fleet size and schedule frequency may well be calculated after equilibrium flow volumes have been predicted, using design logic as described in section 5.7. 

## 8.5.3 Models versus Scenarios

There is an interesting controversy over the relative importance of scenarios and models (see, for example, Luchtenberg 1976). In most situations the emphasis of an analysis will be on utilizing a set of models to predict impacts over time, conditional on one or more alternative scenarios. In this case scenarios represent alternative assumptions about the future course of exogenous events. In other situations, however, the range of uncertainty about exogenous events may be considered so great that priority is placed on the development and analysis of alternative scenarios. In this case a set of predictive models may be used primarily to test the internal consistency of each scenario. There may even be situations where so much attention is given to the scenarios that no formal predictive models are used at all, other than informal judgment. 

## 8.6 OPERATOR EQUILIBRATION

The analyst usually wants to explore explicitly variations in the transportation options T. This means that the type 1 and type 2 relationships must be modeled explicitly in order to predict the impacts of the options. On the other hand, no attempt is made to model the type 3 (operator-equilibration) relationship. 

There are several conditions under which an analyst may wish to depart from this general practice: 

1. when there are operators that control some options that are not in the control of the analyst's agency or firm, and the analyst wishes to predict the response of those other operators to actions under consideration by his organization (for example, one airline wishing to predict the competitive response of another airline to a new service, or a government agency wishing to predict the responses of trucking companies to new taxes or to deregulation of entry into the market); 2. when the analyst wishes to determine which options would be most attractive from his organization's perspective under a hypothesized decision rule; 

3. when the analyst wants to employ mathematical optimization methods as search procedures. 

In such cases explicit assumptions can be made about the operator's decision rule, and then powerful tools such as mathematical programming can be exploited as search methods. There is an extensive literature on these approaches. 

As pointed out in section 5.7, travel-market equilibration always involves service functions in which the level of service either is constant or decreases as volume increases; there does not appear to be any type of transportation facility or service for which the service level improves with increasing volume when the options remain fixed. However, for applications in which it is desirable to assume an operator decision rule and perform operator equilibration to derive the corresponding supply function—so that options are allowed to vary—the service level may be increasing, constant, or decreasing as volume increases. 

## 8.7 SUMMARY

Three basic types of equilibrium relationships are important in transportation systems analysis. 

Travel-market equilibration is central to the prediction of flows. In general, both service and demand conditions must be met to find equilibrium flows. In special cases simplifying assumptions can be made, such as assuming that demand is known or that service levels are known. 

Activity-system equilibration reflects the long-term interactions of transportation and activity systems. A full set of prediction models would simulate the evolution of transportation and activity systems over time. 

To model operator equilibration requires explicit assumptions about the behavior of the operator. When such assumptions are made, a classical supply function can be derived. 

## TO READ FURTHER

See chapters 11 and 12 and also Ruiter and Kocur (1976). For examples of simplified equilibrium models see Lerman and Wilson (1974), Manski and Wright (1976), and Talvitie and Hasan (1978). A useful discussion of operator decision rules can be found in Kneafsey (1974), p. 102ff. On time-staging see Manheim (1969), Pecknold (1970), Neumann and Pecknold (1973), and UMTA (1976b). 

## EXERCISES

8.1(E) What kind of equilibration procedure was used in case study I (chapter 3)? 

8.2(C) Consider the following five options and four conditions. How reasonable is the approximation in exercise 8.1 for each option or condition? (Classify simply as "reasonable," "likely to produce serious error," or "intermediate.") Discuss your answers. 

Options 

1 = change in automobile parking price 

2 = change in transit service frequency 

3 = rerouting of transit over an exclusive lane on a freeway formerly used by automobiles 

4 = rerouting of transit over a new transit-only expressway 

5 = construction of an extensive new transit network in the region 

Conditions 

A = next month 

B = a few years from now, in a rapidly changing society 

C = a few years from now, in a stable society 

D = 25 years from now 

8.3(C) Review a model system from the technical literature and describe its equilibrium structure in terms of the concepts introduced in this chapter. Examples include the Harvard-Brookings Model System (Kresge and Roberts 1971) and various model systems used in particular urban or regional transportation studies (Kocur et al. 1977, Tober 1977, Morlok 1978). 

8.4(C) Manhattan Island is the core of New York City. Long Island lies east of Manhattan; it is 116 miles long and about 12 miles wide. Two boroughs of New York City (Brooklyn and Queens) occupy the west tip of Long Island and are densely populated; the rest of the island is relatively sparsely developed, especially the easternmost portion. The following extracts discuss the effects of two major transportation projects in the New York area: 

1. The Triborough Bridge was the fifth bridge constructed over the East River to connect Manhattan to Brooklyn and Queens. It opened on 11 July 1936. Before it opened the man who got it built, Robert Moses, 

had estimated that eight million vehicles would use the bridge during its first year of operation. Within four months, the estimate was increased to nine million. Three months later it was ten million. . . . But traffic on the four other East River bridges was not falling off at anything near a comparable rate. The eight million cars and trucks that Moses had forecast would use the Triborough each year were supposed to be cars and trucks that had previously used the other bridges. . . . Otherwise where would these cars and trucks come from? Yet traffic on the other bridges, down about 15 percent immediately following Triborough's opening, was creeping higher again month by month—back, within two years, almost to the pre-Triborough level. Traffic between Long Island and New York had, before Triborough's opening, flooded the twenty-two lanes available on the four old bridges; suddenly the traffic between Long Island and New York had become so heavy that it was also flooding eight new lanes, the new lanes of the Triborough Bridge . . . and it was hardly any lighter than before on the old bridges. (Caro 1974, p. 518) 

2. In 1955 Long Island's population was 6.2 million, concentrated mostly in the western quarter of the island. Under the direction of Robert Moses, construction of the Long Island Expressway (LIE) began in 1955; by 1970 it had reached Riverhead near the eastern tip of the island. 

As each section of the superhighway opened, it was jammed—with traffic jams of immense dimensions. . . . Year by year, the huge road bulled its way eastward. . . . As each section opened . . . the congestion grew worse. The Long Island Expressway's designed daily capacity was 80,000 vehicles. By 1963, it was carrying 132,000 vehicles per day, a load that jammed the expressway even at "off" hours—during rush hours, the expressway was solid with cars, congested with them, chaos solidified. The drivers trapped on it nicknamed Moses' longest road "the world's longest parking lot." (Caro 1974, p. 949) 

a. Summarize the effects described in these extracts in terms of the concepts presented in this chapter. Sketch service and demand curves at several points in time and describe the shifts in these curves in terms of the type 1, 2, and 3 relations as appropriate. Relate your description to figure 8.5. Do figures 8.1 and 8.2 have any relevance to these questions? 

b. If you were designing a system of models to be used in planning projects such as these, what features would you want to be sure to include? 

c. Discuss the policy implications of these examples. What considerations developed in this chapter did the planners of the projects not consider adequately? How did this affect their planning? 

d(P). Assume simple functions and construct a simulation of the phenomena discussed in part a. 

## 9.1 THE PURPOSE OF EVALUATION

## 9.1.1 The Objective of Analysis

Like transportation itself, analysis is a means, not an end. Significant changes in transportation will occur only when conscious decisions are taken by organizations and individuals with the responsibility, authority, and capability for taking action. These decisions may be to make specific changes in the transportation system and services to be offered—for example, to introduce new technologies; to change routes, schedules, or prices; or to make infrastructure changes. The decisions may also be to take no action, to defer a decision. 

Analysis is successful only if the results of analysis are useful in the process of reaching these decisions concerning the implementation of change. Thus the objective of analysis is to clarify the issues that should be considered by decision makers, to assist them in reaching a decision on a course of action. This definition is in direct and explicit contrast to the cynical view of analysis, which sees the purpose of analysis as being to justify and explain a previously reached decision. 

## 9.1.2 The Role of Evaluation in the Process of Analysis

The major steps in the process of analysis were described in section 1.6. There we defined search as the activity in which alternative actions are generated, described in terms of the various transportation and activity-system options. Prediction is the activity in which estimates are developed of the likely impacts of each of the actions generated in search; the preceding chapters have introduced the basic concepts used in prediction. The activity of goal formulation and revision involves the formulation of critical statements of goals and revision of these goals as the analysis evolves. 

Evaluation begins with the outputs of prediction (the actions and their impacts) and of goal formulation and revision (the statements of goals). 

Since the objective of analysis is to clarify the issues that should be considered, at some point in analysis the potential actions must be evaluated with respect to the goals to be achieved by transportation. Evaluation is that point. Evaluation is the activity of examining the available alternative actions in light of the possible goals, assessing the relative desirability of each action, and summarizing the key issues to be considered by interested parties in reaching a decision. Choice is the activity of reaching a conscious decision as to which of the alternative actions (if any) to implement; choice takes as input the results of evaluation. The actions available should include no action—the “null” or “status quo” alternative—as well as various forms of deferring the decision (for example, “continue analysis”). 

## 9.1.3 Relationship between Evaluation and Choice

In general, the distinction between evaluation and choice is clear: evaluation is performed by analysts, usually interacting with various interested parties, while choice is performed by one or more decision makers, often interacting in complex institutional environments. Sometimes, however, the interaction of evaluation and choice may be sufficiently complex that they are difficult to separate—for example, when a decision maker looks at the data on the predicted impacts of several actions and reaches an immediate decision on which to implement, or when the decision maker is the analyst. Often, too, the analyst and decision makers interact intensively and frequently so that the choice and evaluation activities are closely intertwined and the decision maker has already reached a decision by the time the analyst has completed a formal evaluation. Even in these cases, however, the distinction between evaluation and choice is a useful one. 

One assumption that is often made is that evaluation is an objective technical activity whereas choice is basically political, in that it involves value judgments. This is not true: evaluation is more technical than choice, but it is not value-free; value judgments are inescapable in evaluation, as we shall discuss shortly. 

There is also a close interaction between evaluation and the activity we call goal formulation and revision. In general, the initial formulation of goals will change as a result of analysis. The activity of evaluation in particular will often stimulate a reappraisal and revision of the goals initially posed. 

## 9.1.4 The Product of Evaluation

The evaluation activity plays a key role in the process of analysis. It is in this activity that the analyst must pull together all of the information developed through the various activities of the analysis, examine it to increase his understanding of the issues, and then summarize the insights gained in this examination: The primary product of evaluation should be a summary of the key issues to be considered by interested parties in reaching a decision on a course of action; this summary should be in a form that can be readily understood by laymen such as elected officials, managers, and the general public. 

The summary can be written or verbal, formal or informal. For convenience we shall call this summary an evaluation report and describe it as if it were a written document. Written documents are required in many situations, in public or in private agencies, to gain approval for funding, to document for the record the bases of decision, and to meet the requirements of environmental legislation (see section 9.2.5). 

We shall place great stress on the readability and understandability of the evaluation report. Most participants in most decision processes are not technically trained or analytically oriented; nor are they comfortable reading lengthy technical documents. They want to know the key issues about which they should be concerned, and they want to find this out quickly. They want documents that are concise and understandable. An evaluation report might also include technical appendixes that provide the details necessary to understand the facts and judgments presented in the summary; but the summary should be able to stand alone as a concise, readable statement of the major issues. 

## 9.1.5 The Issues to Be Clarified

In deciding which change (if any) to implement, the responsible decision makers will wish to have before them a summary of the key issues they should consider in reaching a decision. (While the decision makers will often be interested in the personal and professional views of the analyst as to the most attractive course of action, they will almost always wish to reserve the final choice to themselves.) In reaching this decision, they will be concerned with such issues as these: 

1. What are the major alternatives that should be considered? 

2. What are the major interests that are benefited or adversely affected by each alternative? 

3. What are the views of those interests? 

4. What are the most important uncertainties that should be considered? 

5. Consequently, what are the major advantages and disadvantages of each course of action? 

This list of issues places particular stress on the incidence of impacts. Generally changes in a transportation system will have many different impacts on different groups and interests. Some interests will benefit from a particular change, whereas others will be adversely affected. Different groups will have different views as to the relative desirability of particular alternatives. Thus the problem of evaluation is difficult not only technically but ethically as well. How should gains to one group be balanced against losses to others? 

Consider, for example, the construction of a new highway in a densely developed urban area. A highway provides many benefits: it improves service for traffic and relieves some of the congestion on local streets. A highway can create greater accessibility for some areas, thereby stimulating development. On the other hand, this development might otherwise have occurred elsewhere, and so areas that are now relatively less accessible may suffer. Location of a highway along one particular route may serve some groups of travelers well, but at the same time, because it might have been located elsewhere, other groups are served not as well as they might have been. The choice of a mass transit link rather than a highway can result in greater accessibility for still other groups, such as those who do not have access to an automobile for some or all of their trips. The construction of a highway can be, at least in the short run, a disruptive force in the community; it can cause the displacement of families or jobs, form a physical barrier separating people from parks or schools or churches, create a visual barrier or despoil a scenic area, or take parkland or other community facilities out of public use. Construction of highways can change the pattern of air pollution and groundwater flow and can affect land values in a variety of ways. Construction of a highway along one alignment can cause a loss of tax base for some communities while bringing development potential and thus an increased tax base to other communities; construction along an alternate alignment might have reverse effects. 

Highways are not unique in this respect. Consider these other examples: 

I. Several sites are being considered for a new airport in a metropolitan area. Sites close in to the core of the city will be very convenient for access by air travelers but will subject local communities to aircraft Evaluation 

noise and increased road congestion. Sites farther out either are quite distant for air traveler access or destroy a portion of a major wildlife refuge. 

II. A federal agency is reviewing its budget for transportation research and development. There are three major programs being considered. Program A, development of a new supersonic air transport, would provide a 30 percent reduction in air travel times for international air travelers, although only a 10 percent reduction in overall door-to-door time; the effects of the sonic booms and the extent of possible depletion of atmospheric ozone are largely unknown, in that even experts do not agree on the magnitudes of effects. Program B, development of a railroad subsidy program, would preserve intercity rail passenger service in some metropolitan corridors and suburban commuter services in a few urban regions. Program C, provision of operating subsidies to urban transit agencies, would support special services for inner-city residents and a revision of routes to better serve the young, the elderly, and the handicapped who need access to health centers and recreational facilities. If only one of these programs can be funded, which one should be selected? 

III. A shipping company is planning to introduce major changes in service on its routes, utilizing a new type of ship and new techniques for loading, stowing, and unloading freight. This will result in economies of operation, thus allowing lower costs to shippers and/or higher profits for the ship operator. Because of certain characteristics of the new technology, changes will be made in the service over many routes: some ports will receive much lower frequency of service than before or even get no service at all, while other ports will receive higher frequency of service than before and some new ports will be served. Thus the relative economic growth rates of certain areas will be affected. There will also be some changes in labor requirements: fewer personnel of certain skills will be required, and changes in seniority, work rules, and other labor practices appear likely; these will be of great concern to the workers affected. 

Thus every decision about transportation potentially involves a need to balance gains to some interests against losses to others. A major change in any of the transportation facilities, services, or policies of a region can have far-reaching effects and can constitute a major intervention in the fabric of society. Many different people and interests are affected. The total set of effects on all groups and interests must be considered, with particular attention paid to the differential effects (which groups gain, which lose). 

In almost every transportation analysis a key issue will be, Whose interests should be served? Which groups should gain and which should lose? 

It is essential that the processes of planning, designing, implementing, and operating transportation systems explicitly recognize such issues and take them into account. The planning and design of transportation systems is as much a sociopolitical as a technical and economic problem. 

This is true in the private as well as in the public sector. Management of a private firm such as a shipping company or airline may wish to consider only its own financial benefits in reaching a decision, but as a practical political matter it cannot ignore issues such as those in example III above. Public-spirited management would not wish to; pragmatic management cannot afford to. 

It is very tempting to ignore these problems by assuming that evaluation is basically a technical problem or that somehow the political process will deal with these issues. In transportation, however, one cannot make this assumption because the great majority of transportation decisions must in the end be political decisions in which the conflicting goals of different groups must be balanced. As analysts, if we wish to be effective in bringing about change, our analyses must be relevant to these sociopolitical issues, and our evaluation reports must address these issues of who gains and who loses. 

## 9.1.6 Evaluation as a Management Tool

Evaluation reports can be produced periodically throughout the process of analysis as well as at the conclusion, to summarize the key issues as they are understood at key points in the analysis. These interim evaluation reports are especially useful in reviewing and revising the relative priorities for further technical work and in focusing public involvement in a constructive way during the analysis process. 

This use of evaluation reports suggests the addition of a sixth issue to the above list: 

6. Should further analyses be done? If so, what are the relative priorities for further analysis? 

## 9.2 THE EVALUATION METHOD

Producing an evaluation report is a difficult task. The analyst must clarify the issues in a manner that is concise, relevant, clear, and understandable to laymen. To do this he must first organize and examine the available data in ways that help him to isolate and understand the most important issues. 

There is no algorithm or formula that produces the evaluation report automatically from the data. There are, however, heuristic procedures that the analyst can use as an aid in understanding the issues. There are also some technical procedures, such as economic analysis, that can be useful in supporting the heuristic procedures. 

In this section we shall describe the basic structure of the evaluation method; we shall start with some definitions. 

## 9.2.1 Basic Definitions

An actor is a group of one or more individuals who are essentially similar in their relationship to the issues under study. The major types of actors we shall be concerned with include the technical team, the group of professionals entrusted with the responsibility for analyzing a transportation problem; the decision makers, the individual or group of individuals that has the final authority for making a decision (for example, a mayor, a city council, a governor, a president of a transportation company such as an airline or shipline, a minister or secretary of transportation, a port authority, a state highway commission); and the community, the set of all other individuals and interest groups affected by the transportation decisions under consideration. 

The actors relevant to a particular transportation issue may be fairly numerous. For example, the Los Angeles, California, metropolitan area has been considering major investments in a regional rapid transit system for many years. Debate about regional choices reached a climax with a referendum in November 1974 about financing such a system. (It was defeated.) During the months preceding the referendum, a list of key actors was put together, extracts from which are shown in table 9.1. This list demonstrates the variety of actors and interests that may be important in a transportation decision. Note that, as extensive as it is, the list excludes many important interests, such as local and state elected officials, businessmen, and citizens' groups formed for purposes other than transportation, such as neighborhood and environmental groups. 

The impacts of a set of decisions are those aspects of the consequences of the decisions that may be of concern to one or more actors (that is, there is at least one actor who has some preference about the level and kind of impact that might occur). Table 9.2 shows an illustrative list of impacts of alternative urban transportation systems that might be important issues in a particular situation. Im-

Table 9.1 Some of the agencies, organizations, and committees concerned with the planning and development of transportation in the Los Angeles region (1974) 

I. Summary
A. City of Los Angeles
1. City Council Ad Hoc Committee on Rapid Transit
2. Technical Advisory Committee to Ad Hoc Committee on Rapid Transit (TAC AD HOC)
3. City Council Industry and Transportation Committee
4. City Council Planning Committee
5. City Council Traffic and Off-Street Parking Committee 

6. Mayor's Ad Hoc City Employee Transportation System Committee 

7. General Plan Advisory Board
8. Transportation Committee 

7. Transportation Committee
8. Aviation Commission 

C. Interagency: Southern California Association of Governments (SCAG)
1. General Assembly
2. Executive Committee 

3. Comprehensive Transportation Planning Committee (CTPC) 

4. Transportation Technical Advisory Committee (TTAC)
5. Los Angeles Regional Transportation Study (LARTS) 

6. Transit Advisory Committee (TAC)
7. Metropolitan Transportation Engineering Board (MTEB) 

10. Impact Task Force  
11. Modeling Task Force  
12. Implementation and Finance Task Force 

13. Airport Authority
14. Council of Airport Administrators 

D. Southern California Rapid Transit District
1. Board of Directors 

2. Board of Control for Alternative Transit Corridors and Systems Technical Study
3. Technical Advisory Committee (TAC) 

E. Local Agency Transportation Advisory Committee (LATAC) 

F. Los Angeles County Association of Planning Officials (LACAPO) 

G. Citizens' Advisory Committee on Rapid Transit (CACORT) 

H. Southern California Aviation Council Inc. (SCACI) 

II. Memberships and affiliations (selected examples) 

1. City Council Ad Hoc Committee on Rapid Transit: Created by the city council for review of the SCRTD Alternative Transit Corridor and Systems Technical Study and related matters. Membership: 6 council members. 

2. Technical Advisory Committee to Ad Hoc Committee on Rapid Transit (TAC AD HOC): Created by the City Council to advise the Council Ad Hoc Committee on the SCRTD Alternative Transit Corridors and Systems Technical Study and related matters. Reports to the Council Ad Hoc Committee on Rapid Transit. Membership: Chairman, Planning Department representative; Representatives of Harbor Department, Police Department, 

Department of Airports, City Administration Officer, Department of Public Utilities and Transportation, Chief Legislative Analyst, City Traffic Engineer, City Engineer. 

4. City Council Planning Committee: Hears items concerning the Planning Department including transportation planning, and makes recommendations to the full Council. Membership: 3 council members. 

5. City Council Traffic and Off-Street Parking Committee: Hears items concerning the Traffic Department and Off-Street Parking Agency. Membership: 3 council members. 

7. General Plan Advisory Board: Advises the Director of Planning in matters relating to the City General Plan. Membership: Chairman, Planning Department; Mayor; Councilman; City Administrative Officer; City Engineer; Housing Authority; Community Redevelopment Agency; Building and Safety; Department of Environmental Quality; Fire Department; Police Department; Public Utilities and Transportation; Recreation and Parks; Traffic Department; Department of Water and Power; Harbor Department; Department of Airports; Mayoral Appointees (2). 

8. Transportation Committee: Considers transportation matters affecting the City General Plan and advises the General Plan Advisory Board. Membership: Planning Department, Traffic Department; City Administrative Office; Public Utilities and Transportation; Bureau of Engineering; Department of Transportation of California; Southern California Rapid Transit District. 

## B. County of Los Angeles

1. Regional Planning Commission (RPC): Functions as an official hearing body and recommends county-wide comprehensive, general planning policies to the Board of Supervisors. Also responsible for highway protection through subdivision and zoning administration. 

2. General Plan Policy Review Board (GPPRB): Advises the RPC on development policies and priorities and coordinates the goals, policies, programs, and projects of individual County Departments which affect the General Plan. Membership: Agricultural Commissioner, Air Pollution Control Officer, Assessor, Director of Beaches, Chief Administrative Officer, County Engineer, Chief Engineer of the Flood Control District, Forester and Fire Warden, Director of Health Services, Executive Director of the Human Relations Commission, Director of Parks and Recreation, Director of Planning, Director of Public Social Service, Director of Real Estate Management, Road Commission, Director of Urban Affairs. 

3. Transportation Sub-Committee: Develops policy recommendations to the GPPRB on the Transportation Element and provides departmental input pertinent to development of the Element. Membership: Air Pollution Control District, County Engineer, Human Relations Commission, Regional Planning Commission, Road Department, Department of Senior Citizens Affairs (not on GPPRB). 

4. Interdepartmental Engineering Committee (IEC): Advisory technical body responsible for recommending to the Regional Planning Commission changes to the County Highway Master Plan. It also reviews and approves precise alignments for these highways as well as resolving problems encountered by any involved parties. Membership: Road Department, Regional Planning Commission, County Engineer, other departments when affected. 

6. Citizens Planning Council (CPC): Comprised of 50 members appointed by the County Board of Supervisors for three-year terms. The primary function of the Council is to help determine content of the County General Plan with respect to goals, policies, plans, and programs. This Committee of private, interested citizens is advisory to the RPC.
7. Transportation Committee of the CPC: Provides citizen input to aid the Road Department in the formulation of the Transportation Element of the Los Angeles County General Plan. 

C. Interagency: Southern California Association of Governments (SCAG) 

1. General Assembly: The policy body of SCAG, comprised of an elected delegate from each member county and city plus three additional delegates from the City of Los Angeles (the Mayor and 2 Councilmen). 

2. Executive Committee: The official day-to-day policy-making and supervisory body of SCAG as designated in the SCAG bylaws. The committee meets on the second Thursday of each month. Membership: 18 total. Three from the City of Los Angeles are the same as the delegates to the General Assembly (Mayor and 2 Councilmen); one from each of the 6 member counties (Imperial County, Los Angeles County, Orange County, Riverside County, San Bernardino County, Ventura County); one from each of the collective member cities within each county (Camarillo, Burbank, San Bernardino, Torrance, Santa Anna, Riverside, Brawley, Long Beach, and Fullerton and 3 members at-large). 

3. Comprehensive Transportation Planning Committee (CTPC): One of 9 policy committees established by the Executive Committee of SCAG on different aspects of urban planning. The CTPC advises the Executive Committee on all transportation matters. Membership: representatives of Orange, Riverside, San Bernardino, and Los Angeles counties; cities of Ontario, Torrance, Palmdale, Baldwin Park, Arcadi, Cypress, San Bernardino, Los Angeles, Oxnard, La Habra, Montebello; and California Department of Transportation. 4. Transportation Technical Advisory Committee (TTAC); Members of the committee are appointed by the President of SCAG and represent city and county road and traffic departments, airports, transit operations, state highways, and planning departments. 5. Los Angeles Regional Transportation Study (LARTS): Staff is provided by the State Division of Highways under the direction of TTAC; functions as an arm of SCAG and also performs the work on the Los Angeles Regional Transportation Study, a continuous program of comprehensive transportation planning. 

6. Transit Advisory Committee (TAC): Meets on call of the chair at least bimonthly. TAC was established by SCAG in July 1971 to coordinate the planning and operations of transit systems in the region in accordance with the Mass Transportation Planning Guide of 1966 and the California Transportation Development Act of 1971, as amended. The committee is composed of representatives of public transit operating agencies in the region and helps to prepare, update, and review progress on the SCAG Transit Development Program. 7. Metropolitan Transportation Engineering Board (MTEB): The MTEB acts as technical reviewers in street, highway, and freeway transportation planning. This committee, consisting of city and county engineers, the Director of RPC, Los Angeles City Planning, Small City Planning, SCAG, and Division of Highways representatives, acts as advisor to the SCAG CTPC 

8. Critical Decisions Task Forces: Review and coordinate investigations by the SCAG staff required to place the region in a position to adopt critical transportation decisions. The task forces function as advisory units to the SCAG staff. 

12. Implementation and Finance Task Force: Coordinates the preparation of implementation analysis and recommendations for the alternative transportation proposals and systems. The task force provides guidance and reviews analysis of fiscal capabilities and proposed fiscal actions associated with the above proposals and systems. Membership: representatives of Orange County Transit District (OCTD), Los Angeles City Planning, Los Angeles City Mayor's Office, Los Angeles County Road Department, CALTRANS, Los Angeles County, and Southern California Rapid Transit District. 

D. Southern California Rapid Transit District (SCRTD) 

1. Board of Directors: The policy body of SCRTD. Conducts the affairs of the district in accordance with the laws established by the State of California. Membership: 11, including appointees by each of 5 County Supervisors; 2 appointees of Los Angeles City Mayor; and 4 representatives of corridors elected by City Selection Commission. 

3. Technical Advisory Committee (TAC): Created at the request of SCRTD to meet UMTA requirements for a technical liaison and review of their Alternative Transit Corridors and Systems Technical Study with affected agencies. Membership: representatives of SCRTD, City Mayor's Office, L.A. City Planning, L.A. City Administration Office, L.A. City Airports, L.A. Public Utilities and Transportation, L.A. City Legislation Analysis, L.A. City Traffic, L.A. City Engineering, L.A. County Planning, L.A. County Road Department, L.A. County Administration Office, League of California Cities, California Transportation Department, City of Burbank, Southern California Transportation Department, Southern California Association of Governments, Orange County Transit Department, Commission for Central City Planning, Community Redevelopment Agency, UMTA Regional Office, and consultants doing the study. 

## Table 9.1 (continued)

F. Los Angeles County Association of Planning Officials (LACAPO): Encourages cooperation between local governmental jurisdictions in the development of a countywide General Plan, reasonable uniformity in standards, and joint studies. Membership: members of the Board of Supervisors, the City Councils, planning commissions, and each of the planning directors (or officials responsible for planning). 

G. Citizens' Advisory Committee on Rapid Transit: Immediate goal is to help SCRTD determine a final rapid transit proposal to present to the voters at the general election in November 1974. The committee will conduct a campaign effort and fund raising to achieve voter approval of taxes to fund the rapid transit proposal. Membership: Presidents of major local industry; Mayoral Appointees, County Supervisor Appointees, City Council Appointees, and representatives of the community at-large; expected to reach 150 members. 

Table 9.2 Possible impacts of urban transportation actions 

Community development and growth
Neighborhood cohesion
Neighborhood stability
Community aspirations
Transportation facilities as barriers in the community
School districts disrupted
Parish districts disrupted
Other impacts on religious institutions
Parkland taken
Vacant land taken
Access to employment opportunities
Access to educational opportunities
Access to recreational opportunities
Access to areas of natural beauty
Local land development
Community facilities
Preservation of historic and cultural sites
Displacement of persons and businesses
Effect on welfare and unemployment expenditure
Effect on commercial property values and sales
Effect on residential property values
Tax loss through displacements
Tax gain through increase in land values
Conduct and financing of governments
Creation of unpleasant visual effects
Fiscal efficiency
Maintenance and other nonvehicle operating costs
Right-of-way costs
Facility construction costs
Vehicle costs
Fuel consumption
System operating costs: labor
System operating costs: materials
Maintenance of design standards
Weather reliability
User trip time
User trip cost 

Comfort and convenience of users
Vehicle wear and tear
Multiple use of space
Access to and egress from roadways
Congestion on neighboring streets
Regional growth and development
Effect on distribution of economic activity
Changes in retail market area
Effect of construction on the economy
Public health and safety
Noise pollution
Air pollution
Conservation of natural resources
Accident rate
Complexity of demands on drivers
Flow congestion
System efficiency
Accessibility
Serving maximum population
Consistency with local land-use planning objectives
Consideration for future transportation needs
Coordination with other transportation facilities during and after construction
Disruption caused by construction
Integration with existing transportation facilities
Access to recreational and cultural sites
Access to fire and police services
Sequence of perceptions
Aesthetic experience of movement over highway
Aesthetic value of the view of the road
Ease of orientation of drivers
User monotony
Equity 

pacts can be described operationally by defining corresponding goal variables; such goal variables express the level of one or more impacts of a particular action on one or more actors. Goal variables may be defined qualitatively or quantitatively. The types of impacts can also be described in terms of the actors on whom those impacts are incident; in chapter 1 we grouped the impacts of transportation generally in terms of several groups: user, operator, physical, functional, and governmental impacts. 

The actions are the alternative transportation plans being considered. These are defined in terms of a set of options, which consist of choices of technologies, networks, links, vehicles, and operating and organizational policies. The actions may be simple or complex. Examples include alternative highway route locations; alternative bus or airline routes; comprehensive development plans for a transportation corridor, 

Table 9.3 Sample impact tableau: nine alternative alignments for the California Route 42 freeway 

Length (miles) 9.5
Cost (10 $^{6}$ $)
Construction 51.1
Right of way 57.6
Total 108.7
Traffic impact: 20-year user benefit (10 $^{6}$ $) 340
Benefit/cost ratio 3.1
Land-use impacts
Number of parcels affected:
Single family 1,588
Multiple family 309
Industrial 43
Commercial 66
Vacant 69
Parks, churches, schools 4
Miscellaneous 9
Total 2,088
Living units displaced, by community:
Compton Single family 0
(23,190) Multiple family 0
Total 0
Downey Single family 615
(31,220) Multiple family 368
Total 983
Lynwood Single family 75
(16,530) Multiple family 7
Total 82
Norwalk Single family 32
(24,140) Multiple family 0
Total 32
Paramount Single family 0
(11,000) Multiple family 0
Total 0
South Gate Single family 515
(23,360) Multiple family 217
Total 732 including highway location and design, transit facility location and design, a relocation housing program, and a recreational and community facilities program; or regional transportation programs such as the railroad reorganization plan in the northeastern United States. The set of actions must always include the null action. 

<table><tr><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td></tr><tr><td>9.6</td><td>9.2</td><td>9.3</td><td>9.3</td><td>8.8</td><td>8.9</td><td>8.9</td><td>8.9</td></tr><tr><td>52.5</td><td>53.6</td><td>54.8</td><td>49.5</td><td>42.3</td><td>46.0</td><td>48.7</td><td>50.8</td></tr><tr><td>55.2</td><td>59.6</td><td>57.0</td><td>57.7</td><td>55.6</td><td>54.6</td><td>53.2</td><td>51.9</td></tr><tr><td>107.7</td><td>113.2</td><td>111.8</td><td>107.2</td><td>97.9</td><td>100.6</td><td>101.9</td><td>102.7</td></tr><tr><td>330</td><td>370</td><td>360</td><td>275</td><td>280</td><td>275</td><td>275</td><td>275</td></tr><tr><td>3.1</td><td>3.3</td><td>3.2</td><td>2.6</td><td>2.9</td><td>2.7</td><td>2.7</td><td>2.7</td></tr></table>

<table><tr><td>1,464</td><td>1,873</td><td>1,760</td><td>1,899</td><td>1,685</td><td>1,475</td><td>1,997</td><td>1,579</td></tr><tr><td>296</td><td>293</td><td>284</td><td>330</td><td>294</td><td>329</td><td>230</td><td>311</td></tr><tr><td>57</td><td>35</td><td>49</td><td>34</td><td>44</td><td>58</td><td>23</td><td>30</td></tr><tr><td>50</td><td>72</td><td>57</td><td>72</td><td>52</td><td>46</td><td>39</td><td>42</td></tr><tr><td>74</td><td>54</td><td>60</td><td>55</td><td>32</td><td>43</td><td>36</td><td>47</td></tr><tr><td>4</td><td>7</td><td>7</td><td>6</td><td>5</td><td>7</td><td>7</td><td>5</td></tr><tr><td>8</td><td>5</td><td>5</td><td>6</td><td>9</td><td>10</td><td>2</td><td>8</td></tr><tr><td>1,953</td><td>2,339</td><td>2,222</td><td>2,121</td><td>1,968</td><td>2,334</td><td>2,334</td><td>2,022</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>183</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>94</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>277</td><td>0</td></tr><tr><td>439</td><td>613</td><td>433</td><td>411</td><td>413</td><td>413</td><td>412</td><td>412</td></tr><tr><td>540</td><td>315</td><td>496</td><td>236</td><td>236</td><td>236</td><td>236</td><td>236</td></tr><tr><td>979</td><td>928</td><td>929</td><td>647</td><td>649</td><td>649</td><td>648</td><td>648</td></tr><tr><td>75</td><td>75</td><td>75</td><td>361</td><td>529</td><td>427</td><td>462</td><td>452</td></tr><tr><td>7</td><td>7</td><td>7</td><td>239</td><td>323</td><td>595</td><td>292</td><td>663</td></tr><tr><td>82</td><td>82</td><td>82</td><td>600</td><td>852</td><td>1,022</td><td>754</td><td>1,115</td></tr><tr><td>99</td><td>32</td><td>99</td><td>201</td><td>201</td><td>201</td><td>201</td><td>201</td></tr><tr><td>0</td><td>0</td><td>0</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td></tr><tr><td>99</td><td>32</td><td>99</td><td>206</td><td>206</td><td>206</td><td>206</td><td>206</td></tr><tr><td>0</td><td>0</td><td>0</td><td>16</td><td>78</td><td>78</td><td>274</td><td>274</td></tr><tr><td>0</td><td>0</td><td>0</td><td>91</td><td>162</td><td>162</td><td>162</td><td>165</td></tr><tr><td>0</td><td>0</td><td>0</td><td>107</td><td>240</td><td>240</td><td>436</td><td>439</td></tr><tr><td>515</td><td>776</td><td>776</td><td>537</td><td>151</td><td>151</td><td>8</td><td>8</td></tr><tr><td>217</td><td>285</td><td>285</td><td>152</td><td>36</td><td>36</td><td>68</td><td>68</td></tr><tr><td>732</td><td>1,061</td><td>1,061</td><td>689</td><td>187</td><td>187</td><td>76</td><td>76</td></tr></table>


Table 9.3 (continued)


<table><tr><td colspan="2"></td><td>1</td></tr><tr><td>City of Los Angeles (Watts)</td><td>Single family</td><td>114</td></tr><tr><td>(8,160)</td><td>Multiple family</td><td>244</td></tr><tr><td></td><td>Total</td><td>358</td></tr><tr><td>County of Los Angeles</td><td>Single family</td><td>129</td></tr><tr><td>(Willowbrook)</td><td>Multiple family</td><td>254</td></tr><tr><td>(8,710)</td><td>Total</td><td>383</td></tr><tr><td colspan="3">Effect on local tax base of land acquired (106$ and % of city total)</td></tr><tr><td colspan="2">Compton</td><td>—</td></tr><tr><td colspan="2">($87 million)</td><td></td></tr><tr><td colspan="2">Downey</td><td>3.8</td></tr><tr><td colspan="2">($157 million)</td><td>(2.4%)</td></tr><tr><td colspan="2">Norwalk</td><td>0.5</td></tr><tr><td colspan="2">($85 million)</td><td>(0.6%)</td></tr><tr><td colspan="2">Paramount</td><td>—</td></tr><tr><td colspan="2">($46 million)</td><td></td></tr><tr><td colspan="2">South Gate</td><td>3.2</td></tr><tr><td colspan="2">($117 million)</td><td>(2.7%)</td></tr><tr><td colspan="2">City of Los Angeles</td><td>0.4</td></tr><tr><td colspan="2">County of Los Angeles</td><td>0.7</td></tr><tr><td colspan="2">Total</td><td>8.9</td></tr></table>


Source: Adapted from California Division of Highways data, April 1968. 



City totals in parentheses. 


An impact tableau shows, for each of the actions that have been developed, the consequences for each actor, by type of impact. Both beneficial and adverse consequences are shown. The impact tableau may contain some quantitative information such as construction costs, travel times, and numbers of families displaced, but it can also contain qualitative information such as verbal or even graphical descriptions of certain impacts (for example, a description of the ability of a particular community to adjust to social disruption caused by alternative facility locations). The impact tableau presented in table 9.3 shows the effects of alternative alignments for a freeway in the Los Angeles metropolitan area (this particular tableau shows only quantitative impacts). 

<table><tr><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td></tr><tr><td>114</td><td>114</td><td>114</td><td>114</td><td>2</td><td>2</td><td>2</td><td>2</td></tr><tr><td>244</td><td>244</td><td>244</td><td>244</td><td>13</td><td>13</td><td>13</td><td>13</td></tr><tr><td>358</td><td>358</td><td>358</td><td>358</td><td>15</td><td>15</td><td>15</td><td>15</td></tr><tr><td>129</td><td>129</td><td>129</td><td>129</td><td>244</td><td>167</td><td>333</td><td>167</td></tr><tr><td>254</td><td>254</td><td>254</td><td>254</td><td>180</td><td>183</td><td>355</td><td>183</td></tr><tr><td>383</td><td>383</td><td>383</td><td>383</td><td>424</td><td>350</td><td>688</td><td>350</td></tr><tr><td colspan="8"></td></tr><tr><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>0.9(1.0%)</td><td>—</td></tr><tr><td>3.6(2.3%)</td><td>3.9(2.5%)</td><td>3.7(2.4%)</td><td>2.2(1.4%)</td><td>2.2(1.4%)</td><td>2.2(1.4%)</td><td>2.2(1.4%)</td><td>2.2(1.4%)</td></tr><tr><td>0.5(0.6%)</td><td>1.2(1.5%)</td><td>1.2(1.5%)</td><td>3.0(3.7%)</td><td>4.2(5.1%)</td><td>4.2(5.1%)</td><td>2.2(3.5%)</td><td>4.1(5.0%)</td></tr><tr><td>—</td><td>—</td><td>—</td><td>0.4(0.9%)</td><td>0.8(1.7%)</td><td>0.8(1.7%)</td><td>1.2(2.6%)</td><td>1.2(2.6%)</td></tr><tr><td>3.2(2.7%)</td><td>3.8(3.3%)</td><td>3.8(3.3%)</td><td>2.4(2.1%)</td><td>0.7(0.6%)</td><td>0.7(0.6%)</td><td>0.2(0.2%)</td><td>0.2(0.2%)</td></tr><tr><td>0.4</td><td>0.4</td><td>0.4</td><td>0.4</td><td>—</td><td>—</td><td>—</td><td>—</td></tr><tr><td>0.7</td><td>0.7</td><td>0.7</td><td>0.7</td><td>0.9</td><td>0.9</td><td>1.2</td><td>0.9</td></tr><tr><td>8.7</td><td>10.3</td><td>10.1</td><td>9.8</td><td>9.5</td><td>9.5</td><td>9.3</td><td>9.3</td></tr></table>

Goals are the values or preferences or desires of any actor. Goals may be manifest (expressed explicitly in some way) or latent (not yet expressed). Goals may be expressed in terms of impacts or in terms of specific actions. For example, an actor may prefer that the number of families displaced be minimized or, alternatively, that a particular highway route be chosen. A goal statement is an expression of the goals of an individual or group of individuals. Such goal statements may or may not be internally consistent (observing such conditions as transitivity) and may be partial or complete, depending upon whether a statement of goals is clearly formulated over every possible combination of impacts. A ranking or preference order over a specific set of actions indicates the relative desirability of the various actions. 

Just as information on impacts can be organized into an impact tableau, information about the goals of various actors can be organized as a value information file. This file can contain for each actor and impact type what is known by the technical team about the manifest and latent goals of that actor. 

With these definitions we can reformulate the definition of an actor. An actor is any individual or group of individuals who for all practical purposes are homogeneous with respect to the impacts on them of any actions and their values concerning those impacts and actions. The term affected interest is used synonymously with actor; an affected interest is an individual, group of individuals, institution, or resource valued by society which is actually or potentially affected by any of the actions being considered. It is also often useful to distinguish spokesmen from the groups or interests they represent (since the question of who represents whom is often an issue). 

## 9.2.2 Evaluation: The Technical Problem

Evaluation operates on two sets of information—information about actions and information about values. The information about actions is summarized in the impact tableau, in which, for each of the available actions, the impacts on each affected interest are displayed. These data may be quantitative or qualitative, and there may be uncertainty about some impacts of some of the actions. Information about values is represented by the manifest preferences that have been expressed by spokesmen for various affected interests and by additional inferences that may be made about latent preferences. This information is assembled in a value information file. 

The task of evaluation is to operate on these two sets of information—the impact tableau and the value information file—to assess the relative desirability of alternative actions and to summarize the key issues (figure 9.1). 

Several features make this a difficult problem: 

1. There are generally many alternative actions. 

2. Each action has many impacts on many interests. 

3. The information on impacts is rarely complete or known with certainty. 

4. While there is available to the technical team some information about the goals of various interests, as expressed by spokesmen for those interests, this information is almost never complete and is rarely totally consistent. 

5. Most important of all, beneficial and adverse impacts typically fall onto different groups: some interests gain and some lose for each alternative action. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/fc366feb-933b-4442-bcbf-4538c4ada340/eca57ca1ebb1c8d87cc00b13a78332447bd81ca1eb079445b1382f9ce870947e.jpg)



Impact Tableau


<table><tr><td rowspan="2" colspan="2"></td><td colspan="4">Action</td></tr><tr><td>A</td><td>B</td><td>C</td><td>......</td></tr><tr><td>Interests</td><td>Impact Types</td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="3">U</td><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td>2</td><td></td><td></td><td></td><td></td></tr><tr><td>...</td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="3">V</td><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td>2</td><td></td><td></td><td></td><td></td></tr><tr><td>...</td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="3">X</td><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td>2</td><td></td><td></td><td></td><td></td></tr><tr><td>...</td><td></td><td></td><td></td><td></td></tr></table>

<table><tr><td rowspan="2" colspan="2"></td><td colspan="4">Impact Type</td></tr><tr><td>1</td><td>2</td><td>3</td><td>......</td></tr><tr><td colspan="2">Interests Spokesman</td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="5">U</td><td>a</td><td></td><td></td><td></td><td></td></tr><tr><td>b</td><td></td><td></td><td></td><td></td></tr><tr><td>c</td><td></td><td></td><td></td><td></td></tr><tr><td>d</td><td></td><td></td><td></td><td></td></tr><tr><td>...</td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="3">V</td><td>a</td><td></td><td></td><td></td><td></td></tr><tr><td>b</td><td></td><td></td><td></td><td></td></tr><tr><td>...</td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="3">X</td><td>a</td><td></td><td></td><td></td><td></td></tr><tr><td>b</td><td></td><td></td><td></td><td></td></tr><tr><td>...</td><td></td><td></td><td></td><td></td></tr></table>


Figure 9.1 Evaluation.


These differences in impacts are illustrated in the impact tableau in table 9.3. Note, for example, the differences in dwelling units displaced and in tax-base losses among the various communities affected by the alternative alignments for the Route 42 freeway. These differences in the incidence of beneficial and adverse effects cannot be ignored. It is morally unacceptable to ignore such distributional issues; and it is politically impractical to do so. 

Recognition of these five factors has strongly influenced the design of the evaluation method to be laid out in section 9.2.3. The rationale behind the method will be described in detail in section 9.3. 

The steps of the method are designed to assist the analyst in distilling out of the data an understanding of the issues and in communicating this understanding to laymen in terms they can understand. One way for the analyst to visualize this objective is to ask himself these questions: If I were limited to ten pages of text and five pages of figures, what would I say, and how would I say it, to communicate to lay readers my understanding of the issues? What are the key issues they must consider, in order to reach a decision about which alternative should be chosen? How can I express these issues in ways that they can understand and that bring out the importance of the decisions to be made? 

To prepare such a statement the analyst must understand not only the technical issues—the alternatives and their effects—but also the value issues—the interests that will be affected and how each is likely to feel about the technical issues. 

The detailed evaluation procedure laid out in the next section begins with the information on alternatives and their effects and on potential value issues. This procedure is one approach by which the analyst can work toward producing the kind of summary statement we have described. (For more detailed discussions see Manheim et al. 1975b, Cohen 1975.) Section 9.5 will describe additional concepts and techniques that are useful in expanding the basic procedure for application to the evaluation of complex system plans. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/fc366feb-933b-4442-bcbf-4538c4ada340/3ac2e55635047ac748323632ebc07f509f88e6febedef7f26c3dc087ac6c0495.jpg)



Figure 9.2 Steps in the evaluation method.


## 9.2.3 Steps of the Evaluation Method

The evaluation method can be described as a series of steps. As suggested by the dotted line in figure 9.2, it is likely that the activities in the various steps will be iterated several times in producing an evaluation report. 

The first step involves assembling the basic data in a form appropriate for analysis. The next steps deal with the data in its disaggregated form. In step II the current alternative actions are viewed from the perspective of each affected interest in turn, in order to anticipate the likely preferences of each interest. In step III each alternative action is viewed as a whole, to assess its strengths and its weak points. 

Since it is rare that any single action will appear to be preferred to all others by all affected interests, further analyses are usually necessary. In step IV the data are treated in more aggregated form. The objective in this step is to develop a further understanding of the issues by searching for various patterns in the data. In step V the analyst sets down his understanding of the issues in the form of a summary evaluation report. 

## STEP I: ORGANIZE BASIC DATA AND REVIEW

Two basic sets of data are required as inputs to evaluation: the impact tableau and the value information file. Much of the necessary information is developed in the course of the technical team's various activities. However, the data are usually scattered among the many individuals on the team and in various physical locations, and some of it is stored only in people's heads. Thus it is often a major task to assemble the data in one place for use in evaluation (for a discussion of some of the practical problems see Cohen 1975). Often, too, simply organizing a large volume of data physically in an efficient way requires thought. 

The first and most difficult task is to develop a list of all parties that might be affected by any of the alternatives being considered. Each such party, or interest, should be relatively homogeneous with respect to values and likely impacts. In many projects the sheer number of such interests will make this task difficult. 

The value information file should be organized with a separate record for each interest—one or more pages, or sections of a standard file system. This record should contain all the relevant data collected by the technical team: the obvious economic, demographic, and land-use data for such interests as neighborhoods or communities; and other appropriate background information on commercial and business interests. The file should also contain relevant expressions of attitudes or opinions that may be useful in understanding the needs or values of an interest: newspaper articles, public expressions of positions on transportation or other issues, and especially records of direct communications with the technical team, such as correspondence and memoranda by staff summarizing meetings with representatives of the affected interest. 

In short, this file should contain any information that will assist the analysts in understanding the affected interests. The best source of such understanding is direct and extensive communication with the interest, but indirect information is a partial substitute and a useful supplement. 

The impact tableau can be visualized as a table in which each row represents a particular type of impact on a particular interest: for example, number of residences displaced, traffic noise level, and accessibility are among the important impacts alternative highway locations can have on a neighborhood, so there would be a row for each impact type for each neighborhood. The columns represent the actions that have been developed. Thus the impact tableau is simply a format for displaying all of the data available to the analysts about the alternative actions being considered and their potential impacts on the various affected interests. 

Some of these data would come from the prediction models discussed in previous chapters—data on such impacts as travel times, volumes, noise levels, and accessibility. Other data would come from other types of models or expert judgment—such as the effects of disruption during construction on the viability of local retail stores, the effects of alternative facility locations on community social structure, and aesthetic impacts. While some of the data would be numerical, especially those produced by computer models, other data would be available only in verbal or perhaps in graphical form, such as effects on community cohesion or the visual impact of a facility as seen in the neighborhood. All such data should be included, because some of the impacts most important to some groups, such as social or aesthetic impacts, are those most resistant to quantification. 

The impact tableau should be cast in whatever physical form is most usable. While conceptually it is a single table, in almost all situations the numbers of rows and columns will be too great to fit on a single page or even a display board on the wall of a conference room. For working purposes it may be useful to organize the impact tableau as a series of pages in a loose-leaf notebook, perhaps with one page for each affected interest. 

Data derived as output from computer models can be organized by alternatives instead of by interests (for example, the matrices of inter-zonal travel times and volumes for a particular network); but care must be taken to put these data into proper perspective. Computer-generated data should not overshadow other less quantitative data, and the analyst should be careful to examine those data from the point of view of each interest affected, not simply from that of the system as a whole. 

The following steps may be useful in the initial development of these two sets of data (see also Manheim et al. 1975b, pp. 64–77): 

1. Develop a checklist of interests potentially affected, including all of the groups, institutions (public agencies, private businesses, organizations), and resources valued by society (air quality, cultural and historical sites, and so forth) that might be affected, positively or negatively, by the various alternatives under consideration (it is often useful to identify these by location on a map). 

2. Develop a checklist of types of impacts, that is, the effects (both positive and negative) about which the various interests might be concerned (see table 9.2). 

3. For each interest, assemble available data and establish a value information file. 

4. For each interest, identify which types of impacts will be matters of concern, using information in the file and judgment where necessary.
5. Review the alternative actions developed to date. Consider each interest in turn: Are all the impacts of each alternative that are likely to be of concern to that interest on the list of step 4? If not, add the missing impact types to the list. Consider each action in turn. Are there interests potentially affected by any action that are not on the list developed in step 1? If so, add them to the lists of steps 1 and 4.
6. Construct an impact tableau. Be sure to include in the set of actions the null alternative. 

7. Assemble and review all available data on the impacts of the alternatives—from travel prediction models, from other models, and from expert judgment. 

8. Place these data in the impact tableau. Show for each prediction the range of uncertainty in the level of impact. 

## STEP II: VIEW THE ISSUES FROM THE PERSPECTIVE OF EACH AFFECTED INTEREST

In this step the analyst attempts to view the issues from the perspective of each affected interest. 

1. Examine each affected interest, in turn, by going through the following steps. 

2. Review the data in the impact tableau. Consider each action in turn. How is the interest affected by the action? Does it benefit? Is it adversely affected in any way? If there are adverse effects, does the action include steps that will adequately compensate the interest for the adverse effects? 

3. Review the data in the value information file and the results of step 2. Consider each action in turn. What would be the attitude of the interest toward this action? Has the interest expressed any opinions on this action? Would the interest support the action? Oppose it? Be neutral? Why? Is there uncertainty about the likely attitude of the interest toward this action? If so, is this because the interest really consists of several interests with different values (so that it should be separated into several different interests)? 

4. Appraise the actions in the impact tableau from this interest's perspective. Which actions would the interest support? Oppose? Be neutral toward? How would the interest rank the actions? 

5. Explore possible new actions. Are there modifications of any particular action in the impact tableau that would make it much more attractive to the interest? Are there other actions, not in the impact tableau, that the interest has proposed or might propose that would be more attractive to it? 

6. Review the uncertainties in the impact data. Consider the data in the impact tableau and their ranges of uncertainty. Are there impacts for which the interest would want more, or more accurate, information? Are there additional types of impacts not yet included in the tableau that the interest is likely to consider important? 

## STEP III: VIEW THE ISSUES FROM THE PERSPECTIVE OF EACH ACTION

In this step the analyst appraises in a preliminary way the major strengths and weaknesses of each action. 

1. Examine each alternative action, in turn, by going through the following steps. 

2. Issues of community concern: How does the proposed alternative respond to people's concerns? To transportation issues? To related issues? How can an alternative be changed to make it more responsive to such concerns? Do other agencies or governmental bodies have jurisdiction over some issues being raised? 

3. Issues of feasibility: Is the action feasible technically? Legally? Administratively? Financially? If not feasible in some respect, why not? What steps might be considered to make it feasible? Not only changes in the action but also changes in administrative decisions or laws or other constraints should be carefully considered. 

4. Issues of equity: Compare this action with the null alternative. Review the results of step II. Which affected interests would receive benefits from this action relative to the null alternative? Which would receive adverse effects? Are any of these adverse effects inadequately compensated? Why? Which interests would not be affected significantly? Which would receive both beneficial and adverse effects?
5. Issues of potential acceptability: 

i. Which interests would be likely to support the action? To oppose it? To be neutral? 

ii. For which interests is there uncertainty as to their likely attitudes? Why? Does the uncertainty arise because the information about impacts is uncertain, or because the attitudes of the interest are uncertain, or for some other reason? 

iii. Would additional information on the effects of this action be desirable or useful? Which effects? What are the relative priorities for impact prediction? 

iv. Would additional information on the feelings or reactions of any interests be desirable or useful? Which interests? What are the relative priorities for learning more about the values of various interests?
v. Are there modifications of the action that would increase its desirability from the point of view of particular interests? What are they? What are the relative priorities? 

6. Summarize the major assets and liabilities of the action as revealed by this preliminary analysis. 

## STEP IV: VIEW THE ISSUES FROM THE PERSPECTIVE OF THE PROCESS AS A WHOLE

In steps II and III two different views are taken of the process: how each interest would view the process (as reflected in its views on each of the actions), and how each action compares to the null alternative. Each of these views provides important insights. In this step, in order to gain further insights, the analyst considers all the actions together in a search for patterns or relationships extending across several, many, or all actions and/or interests. 

1. Review the results of the preceding steps. 

2. Issues of undesirability: Are there actions for which the disadvantages are sufficiently great that they should be removed from further active consideration (for example, because they are infeasible and there is little potential for modifying them to make them feasible, or because they have significant adverse effects on some interests that are unacceptable to those interests and cannot be compensated)? 

3. Issues of potential acceptability: Examine the results of steps II and III. 

i. Are there groups of affected interests that share similar views (support, opposition, neutrality) about each of a group of several actions? All actions? 

ii. Are there affected interests that have opposing views about a single action? Some groups of actions? 

iii. For interests in conflict over some actions, are there other actions on which they would not conflict, but which they would support or at least not actively oppose? (If so, these actions are potential compromises.) Is there any way in which compromises among the affected interests might be reached through modification of available actions to change some impacts (or to provide compensation for adverse impacts) or through development of new actions? 

iv. Are there any actions that would have or do have substantial acceptance by all affected interests? Which actions have the greatest potential for such acceptance? 

## STEP V: PREPARE SUMMARY EVALUATION REPORT

1. Review results of previous steps. 

2. Summarize the major alternative actions and the most important issues: 

i. What are the major advantages and disadvantages of each of the major alternatives, with particular emphasis on the issues as viewed by specific interests? 

ii. What are the major issues that have been identified, especially the areas of conflict among interests and among alternative goals? 

iii. What are the major priorities for further work on development of additional alternative actions? On development of additional information on impacts? On development of additional information about the views or attitudes of specific interests? 

3. Write, review, and edit the evaluation report to ensure that it can be understood by the audience for whom it is intended. 

## 9.2.4 Features of the Method

The key features of this evaluation method are as follows: 

1. an emphasis on the differential incidence of adverse and beneficial impacts on different interests; 

2. explicit recognition of the fact that different interests place different relative values on various objectives and impacts; 

3. explicit emphasis on comparing differences among alternative actions to identify trade-offs (especially differences between the null action and others); 

4. recognition of the need to consider qualitative information as thoroughly as quantitative information; 

5. recognition of the need to identify uncertainties explicitly; 

6. explicit concern for using evaluation as a management tool to assist in establishing work priorities for the technical team. 

Basically the method consists of a systematic examination of each alternative action, in light of the available information on impacts and values, to determine whether each affected interest becomes better or worse off. The method explicitly considers the views of each interest separately. It stimulates the technical team to explore possible modifications of specific actions to shift the incidence of gains and losses by modifying actions; and it also encourages the team to think carefully about other priorities for further analysis. 

The emphasis throughout the method is on creating a style of analysis in which the analyst ponders questions and confronts the actual data instead of a formal mathematical algorithm. (For an application of this method see Manheim et al. 1975b.) 

## 9.2.5 Relation of the Evaluation Report to Environmental Impact Statements

In many countries legislation requires the preparation of a statement of the environmental impacts of proposed projects. In the United States section 102(2)(c) of the National Environmental Policy Act of 1969 requires that, before decisions are made on major federal actions (such as transportation projects with federal financial assistance), a state-

ment be prepared and circulated to other agencies and to the public summarizing the environmental impacts of the proposed action. This environmental impact statement (EIS) must describe 

1. the environmental impact of the proposed action; 

2. any adverse environmental effects which cannot be avoided should the proposal be implemented; 

3. alternatives to the proposed action; 

4. the relationship between local short-term uses of man's environment and the maintenance and enhancement of long-term productivity; and 

5. any irreversible and irretrievable commitments of resources which would be involved in the proposed action should it be implemented. 

In our view the evaluation report produced by the method described above would be identical with the EIS and would meet the corresponding legal requirements. Both formats are concerned with identifying all significant impacts and discussing trade-offs among alternatives, especially relative to the null alternative. Both reports should be circulated in draft form so that interested parties can comment on them. 

Where substantial detail is required for a full and comprehensive treatment of impacts, the report may reach hundreds or, for very large projects such as the Alaska oil pipeline, thousands of pages. The logical structure should be the same, however, in that the summary section should be concise and readable and identify the key issues. The summary section should be produced by the recommended evaluation method. To meet any specific format requirements for an EIS (see, for example, Council on Environmental Quality 1973) there are several approaches possible: either the combination of the evaluation report plus the associated technical appendixes can follow the specific format requirements, or alternatively the evaluation report section itself can be written to meet the format requirements. An example of this second approach may be found in Manheim et al. (1975b), pp. 40–48, where the summary section within the evaluation report fulfills the EIS requirements. 

## 9.3 WHY THIS METHOD?

The evaluation method described in this chapter differs from the evaluation procedures recommended in other transportation-related textbooks. In this section we shall explain the view of evaluation that led 

to the formulation of this approach and examine the techniques usually recommended. 

## 9.3.1 Evaluation: A Broader View

Our objective in this section is to step back from the technical details of evaluation and examine the kinds of issues with which the evaluation of transportation alternatives must deal. 

To do this we shall return to one of the themes of chapter 1, namely, the fact of rapid change in demand, in technology, and in values. We do not turn to this theme lightly: the pressures of a changing world pose a great challenge to the analyst who would work openly and professionally to use transportation to improve society. 

The rapidity of change is particularly critical in the area of public and private values. In many countries, and particularly in the United States, recent years have brought rapid changes in the desires and values of many groups. The evolution in values has been particularly important in transportation and has had many implications for the problem of evaluation. 

First of all, the issues that must be considered in transportation decisions have changed. In the past the major issues considered for public decisions about transportation were the impacts on users and on operators. For example, in evaluations of highway, airport, or waterway investments, the impacts on operators were considered to be the costs of construction or acquisition of the new facilities, the operating and maintenance costs, and the revenues from fares, tolls, or other sources. The impacts on users were considered to be measured by improvements in travel time, travel costs, and other aspects of the level of service (American Association of State Highway Officials 1960, Department of the Environment 1972, De Weille 1966). (Occasionally the transfer of user benefits to the economy in so-called indirect benefits were also considered.) 

This view of the issues to be considered is no longer adequate. For example, no longer is it sufficient to design transportation systems simply to serve “users” or operators. Instead we must identify which groups are served well and which groups poorly by a particular transportation system proposal. Thus we have begun to focus on the needs for transportation of those who are too poor or too ill or too young or too old to have ready access to automobile transportation. We have also become deeply concerned with the social, aesthetic, and environmental effects of transportation, particularly in built-up areas (Bridwell 

1969, Organization for Economic Cooperation and Development 1969, Webber and Angel 1969). 

A second critical change in values is the increased recognition of the diversity of values that exists in our society. This diversity has probably always existed; what is new is the increased degree to which these differences are actively expressed. Public attitudes have changed, shifting from apathy and indifference to concern and political activism; with greater public awareness has come more effective articulation of values. While most evident in the United States and in Great Britain, such changes are occurring in many other countries as well, particularly as the public interest in environmental issues increases (see, for example, Okita 1972, Simcock 1972, Mauch 1973). The result has been, in many instances, polarization and conflict. These changes in the political realities of transportation are reflected in the term “the freeway revolt” and the image it conjures in some minds: conflict between those who want highways for the greater mobility they provide, and those who oppose highways because of their effects on the quality of life in the communities they traverse. Opposition has also emerged in many countries to major new airports and to other kinds of transportation projects. The increased emphasis on such issues as air and noise pollution and better public transportation is, in part, a reflection of rapid change in the values held by some, if not all, sectors of the public. 

A third change in values is a belated recognition that the effects of transportation are pervasive in a society: 

Depending on the skill with which we exploit its potential, transportation can be either an instrument of desirable social change or a disruptive force against human development. It can both enhance and damage the quality of the environment. It can either act as a stimulus or act as a brake on urban growth and development. Thus, the ability to make enlightened transportation decisions may to a large extent determine government's success in achieving wider policy objectives. (Organization for Economic Cooperation and Development 1969) 

Professionals concerned with transportation decision making have usually been cognizant of these effects of transportation in a general sort of way. These effects were not, however, considered critical by the professionals or by others until recently, and so these perceptions did not influence the actual decisions being made. Now they can no longer be treated superficially or ignored altogether. 

A fourth change in values has been a change in the way the public views the professionals to whom it has previously turned for advice and guidance. This is a consequence of the other changes and of the failure of the professionals to respond to these changes in values quickly enough. 

The highway engineer and the urban planner provide good examples. The urban planner, once seen as a somewhat utopian dreamer struggling to create a habitable urban environment, is now seen by some groups as the instrument of established interests, destroying viable social communities of low-income residents to erect office towers and luxury housing. Similarly the highway engineer is now seen by many as the servant of the automobile, pushing highways across the country without regard for preservation of urban community or rural amenities. Whether or not these views of the motives and values of planners and engineers are valid is not as important as the fact that a large segment of the public no longer feels confidence in professionals or in their judgments and is no longer willing to follow their recommendations without question. 

As a consequence of these changes in values, the traditional approaches to transportation decision making are no longer adequate. For example, an international panel recently concluded that, in urban transportation planning, 

a new conceptual approach . . . is emerging—one which gives increased emphasis to human values and to the social and economic goals of urban development. In this approach economic and engineering efficiency, “demand” for transportation and profitability no longer serve as the only guiding principles for investment decisions. These conventional criteria are weighed against the social, economic, environmental, and aesthetic needs of urban residents: personal mobility, accessibility to urban opportunities, comfort and convenience, clean air, open spaces, pleasing surroundings, the preservation of neighborhoods and urban diversity. Underlying this shifting emphasis is the growing conviction that transportation is not an end in itself but a tool for bettering the total condition of urban life; that its objective is not just to move people but to enhance the quality of cities and to improve the social well-being of their residents; and that planning concerned only with the effects on transportation itself has too often resulted in transportation systems that have failed to contribute effectively to these objectives. 

. . . There is a need for a methodology which is more sensitive to the important issues facing urban society and more effective in helping to reach socially responsive decisions. . . . (Organization for Economic Cooperation and Development 1969) 

Several conclusions can be drawn from this discussion of changing values: 

1. There are many different kinds of impacts of transportation systems—not only on the users and operators but also on nonusers. Many of these are difficult to describe precisely, much less to quantify in numerical terms. Yet impacts that can be treated only qualitatively must nevertheless be fully considered. All of these effects must be considered in evaluating and choosing among transportation alternatives. 

2. Alternative actions for transportation system change differ not only in the kinds and magnitudes of their impacts but also in the incidence of those impacts. Each alternative action bestows beneficial effects on some groups and interests and causes adverse effects on others. These differences in incidence must be explicitly considered in evaluation and choice. 

3. Society is not homogeneous but is composed of a variety of different groups with different needs, desires, and values. This, together with the fact of the differences in incidence, makes decisions about most transportation system changes essentially political issues. Conflict is almost inevitable: some groups will favor actions that others oppose. This makes progress very difficult unless the analyst explicitly recognizes and addresses the probability of conflict. 

4. We can expect values to continue to change. We should never presume that values are static. As the options available change, as the political system and process evolves, and as our knowledge of the effects of various actions grows, values will continue to change. The issues that seem important today may or may not be the issues that seem important tomorrow. 

## 9.3.2 Classical Approaches to Evaluation

The evaluation techniques that have been used in the past fall into three major groups: pure judgment, economic analysis, and rating schemes. 

In the first approach the basic method of evaluation is judgment. In some cases the judgment is that of a professional engineer, planner, or economist, using technical data on the costs and feasibility of a project. In other cases the judgment is that of a political decision maker (or manager of a private firm), perhaps with some attention to technical data, perhaps weighing only the political or financial advantages and disadvantages of a project. Our stress on “pure” judgment reflects the fact that, while some judgment enters into all evaluation methods, this method relies solely on judgment. Another way of putting this is that evaluation and choice are tightly intermingled; as the issues are weighed, the decision is made. 

In the second approach the evaluation of projects is based upon an economic analysis. For public-sector decisions the basic approach has often been that of benefit/cost analysis, considering primarily user benefits. For example, in the highway field in the United States and many other countries the methods are largely those outlined originally in the “AASHO Red Book” (American Association of State Highway Officials 1960, Wohl and Martin 1967). In this approach the impacts of a highway project are divided into two groups. The costs are the capital costs of investment (land acquisition, construction) and the operating costs (maintenance, administration). The benefits are those received by users of the facility (further reductions in travel times or in vehicle operating cost); using dollar prices, such as a value of travel time in dollars per hours, all the benefits to users are measured in economic (dollar) terms. Through the use of appropriate interest rates and other factors (see section 9.4.2), costs and benefits at different times are made comparable (for example, by evaluating them on an equivalent annual basis). Then each alternative project is evaluated by determining the total costs and the total benefits for the project and computing a benefit/cost ratio; projects are compared on the basis of these ratios. This approach, with numerous variations and modifications, has been used in highway planning, in the United States and elsewhere, and for other kinds of public-sector transportation investments as well (Dawson 1968, Wohl and Martin 1967, De Wielle 1966). 

For private-sector decisions (that is, investment by a private firm) economic concepts are also applied. Costs are handled in much the same way as in the public-sector context (except that tax and financing considerations may significantly change the details of the analysis). The benefits are obviously the gross revenues to the firm from increases in traffic, higher charges, and so forth. The total gross revenues are then compared with the total costs, and net revenue, a rate of return on investment, or other economic criteria are computed. Alternative projects are evaluated on the basis of the relative values of these criteria. 

In the third type of approach procedures are established for weighing the various impacts of a project and computing a score for each alternative. The various alternatives are then compared on the basis of their scores. One special case illustrating the approach is the linear scoring function (LSF) (M. D. Hill 1967, Riedesel and Cook 1970). In this approach the total score for alternative i is 

$$
S _ {i} = \sum_ {j, k} w _ {j k} x _ {i j k},
$$

where $x_{ijk}$ is the level of impact type k on affected interest j for alternative i and $w_{jk}$ is the weight placed on impact type k by interest j. The values of $x_{ijk}$ are the data in the impact tableau. Once we have these data, the LSF approach requires us to establish a set of weights, which are then used to compute the total score $S_{i}$ for each alternative. Alternatives are then compared on the basis of the relative values of their scores. 

It is instructive to review the evolution of these three techniques and to put them in perspective. The pure-judgment approach has been used throughout history. In the mid-1950s the economic-analysis approach was first applied to public-sector projects in transportation, beginning with highway projects, as a result of its previous successful use for water-resource projects. Particularly popular was the variation termed benefit/cost analysis. (The use of economic analysis for private-sector transport investment decisions has a longer history. See, for example, Wellington 1891.) 

The economic-analysis approach should be seen in historical perspective. When benefit/cost analysis was introduced, it represented a professional approach to the evaluation of alternatives. Because this approach appeared to be an objective technical procedure, decisions about transportation projects could be removed from the domain of “political” judgments: arguments for particular alternatives on political grounds could (at least in principle) be countered by the results of an economic analysis, and a more rational basis for decision established. In the highway and urban transportation fields especially, the economic-analysis approach became the prescribed evaluation procedure in the 1950s and 1960s (see, for example, Department of the Environment 1972). 

In some ways the emphasis on economic analysis as an evaluation procedure went too far. To see why, it is useful to examine the rating-scheme approach represented by the linear scoring functions. (The economic-analysis approach is a special case of the LSF approach in which the weights used are the unit prices of benefits and costs.) We shall consider five issues. (These are useful questions to ask of any evaluation method, including the ones recommended in this volume!) 

1. What impacts are considered explicitly and what are omitted? 

2. What alternative actions are evaluated and what are omitted? 

3. Whose values do the weights represent? 

4. How are the weights determined? 

5. What is the significance of the total score as a basis for choosing among alternative actions? 

The impacts considered. To use the LSF all impacts must be expressed in numerical terms. This is obviously a strict requirement. Many significant social, aesthetic, and environmental impacts are difficult, if not impossible, to quantify and so must be omitted from the analysis. In economic analysis the restrictions are even more severe: only those impacts can be considered for which dollar prices can be obtained as weights (see Mishan 1970). In light of present values, omission of qualitative impacts is not acceptable. 

The alternative actions considered. Typically, when the LSF or the economic-analysis approach is used, evaluation comes at the end of the process of analysis, after the alternative actions to be considered have been developed. There is then a danger that the choice will be among equally unattractive alternatives. As indicated by the model of the process of analysis in chapter 1, evaluation should be an integral part of the cycle of analysis. It is particularly important that evaluation stimulate search; for example, it should suggest priorities for finding alternatives that modify or shift specific types of impacts on specific affected interests. (In a highway location study this might involve identification of an adverse effect such as displacement of a number of families in a specific neighborhood, thereby focusing effort on developing modifications of the location to reduce the displacement and developing a replacement housing program to ameliorate the adverse effects.) While nothing in the LSF or economic-analysis approaches prevents their being used in a manner more integrated with the process of analysis, they have conventionally not been so used and are not particularly effective (without modification) in this role. 

Whose weights? From our discussion of changing values, it should be clear that many different groups, with very different values, are affected by and concerned about transportation alternatives, and that most often there will be conflict and disagreement among these groups as to which alternatives are most desirable. In the LSF approach it is assumed that a single set of weights will be obtained and used. The presumption is that this set of weights represents the values of society. But recent experience indicates that different groups cannot agree on values because their values are different (at least at the operational level, though they may well share common values of a more abstract sort). The location for a new airport preferred by air travelers would be different from that preferred by residents of adjacent communities; the attitudes of management and of workers will differ on a proposed change in the structure of a transportation carrier such as a trucking or shipping company. Therefore the basic presumption of a single set of weights in the LSF approach avoids the very important question of whose weights—which group's values—should be used. 

The same presumption is made in the economic-analysis approach. It is further presumed in this case that the weights to be placed on various impacts should be the prevailing market prices (except when shadow prices are used: see Little and Mirrlees 1974). This involves a number of critical assumptions, including the assumption that people know the consequences of their present choices and approve of the present distribution of income, and that the action being considered would not significantly alter present conditions (see de Neufville and Stafford 1971, chapters 8–11). 

Determination of weights. Even if the problem of whose weights to use could be resolved, there would still remain the practical problem of determining those weights. Assume that we want to obtain values for a particular group with relatively homogeneous interests (air travelers or a residential neighborhood directly adjacent to a potential transportation project). To use the LSF approach we need to know what impacts are likely to be important to this group, and what their preferences are for various combinations of levels of different impacts. Some practical techniques have been developed for use in determining preferences. For example, multidimensional utility functions establishing weights over various impacts can be determined by asking a number of questions of an individual (see, for example, Keeney 1972). 

Such an effort is time-consuming for a single individual, however, and would be prohibitive for many individuals representing many groups—not only because of the cost in analyst time but also because of reluctance to expend the necessary effort by the affected individuals. Further, there are many critical assumptions in such an approach: that the individual’s values are static and will not be changed by any information presented to him; that all relevant impacts are included in the questions and that no new ones will surface later; that the individual’s preferences are independent of external conditions; and that the preferences expressed in such an introspective exercise with abstract, hypothetical alternatives are those he would express when actually making a choice among real alternatives. 

An evaluation technique that makes such assumptions is of limited value. Moreover, the number of impacts to be considered and the number of groups with different values are sufficiently large that such techniques would have limited practical use. 

The most practical way to determine a group's values is not by constructing abstract functions or weights but by asking members of the group to choose among specific real alternatives. People can express their values best when they are confronted with real alternatives whose impacts they can perceive and understand, when they understand the range of feasible options that are available, and when they are stimulated to clarify their own values through the process of learning about the alternatives and their consequences. 

Significance of the total score. Finally, and perhaps most important of all, there is the issue of using a single score as a measure for making a decision. When this is done, the presumption is that only the overall score of the alternative is important; the distributional effects—the incidence of adverse and beneficial impacts—is unimportant. For example, when a benefit/cost ratio is used as a basis for decision, the assumption is made that only the net benefits and the net costs, to whomsoever they might accrue, are relevant to the decision. Thus the benefit/cost ratio measures the efficiency of the investment but ignores the distributional aspects (see Walsh and Williams 1969, Nwaneri 1970, Pearce 1971). As our discussion of changing values stressed, however, it is the incidence of effects with which society has become concerned. Therefore, the use of a single score in evaluation as a basis of decision is directly opposed to the concerns of society today. The use of a single score hides the differential incidence of effects, whereas evaluation should strive to bring out the differences in incidence among various alternatives. 

Thus the LSF and economic-analysis approaches involve a number of serious assumptions. Clearly such technical approaches should not be abandoned completely in favor of a return to the pure-judgment approach. Neither extreme is appropriate today. A more subtle approach to evaluation is required, one that combines the positive attributes of both judgment and technical analysis (see Heymann 1965). 

We do not reject the LSF and economic-analysis approaches completely: these techniques can have useful, if somewhat minor, roles in a broader, more desirable evaluation process, provided their assumptions and limitations are clearly understood and counterbalanced. Economic analysis in particular can be an important tool for evaluation, so long as it is put in perspective and used in the context of the method outlined in this chapter. 

## 9.4 EXTENDING THE BASIC EVALUATION METHOD

The basic procedure of section 9.2 is generally applicable to all types of transportation problems. As described, however, it is most effective with project-scale issues, that is, the location and design of specific projects such as highways, transit lines, airports, or changes in operations over a single route. In these projects the alternative actions are relatively few and easy to understand and the number of affected interests and impact types is also relatively small. Thus the basic approach can be used, as outlined, with manual procedures—that is, the analyst can work almost solely with pencil and paper. 

For systems planning problems such as a metropolitan or national transportation plan, or the total network of a rail or air carrier, the inherent complexity demands additional techniques. The numbers of affected interests, impact types, and alternatives are much greater than they are at the scale of a single project. The alternative actions themselves are much more complex, since they consist of various combinations of specific projects and thus overlap to a considerable extent (that is, the alternatives are not mutually exclusive) and since differences in the time-stagings of the projects are often important features of the alternative plans. Furthermore, the impacts often extend over much longer time periods than do the impacts of a single project, are more uncertain, and in many respects are more difficult for laymen to understand. 

The same basic method is still applicable for large complex actions such as systems plans, but additional techniques become important in applying the approach efficiently (some of these techniques would also be required for the traditional evaluation approaches). These techniques are useful for steps II and III of the basic method but are especially valuable at step IV. 

In this section we shall describe briefly two specific techniques: the use of economic constructs to define goal variables and trade-off analysis. We shall assume some familiarity with the basic economic concepts of project appraisal (see McKean 1968, de Neufville and Stafford 1971, Mishan 1971, or any basic text in engineering or managerial economics). 

## 9.4.1 Economic Concepts as Goal Variables

A variety of procedures can be used to develop a set of goal variables for any given analysis. One important method uses economic concepts to construct aggregate measures summarizing some of the impacts important to particular interests, from the perspectives of those interests. 

Economic concepts can be used to develop a number of different goal variables. Several principles are common to all economic goal variables. First, impacts are described in terms of monetary values (prices); thus only impacts that can be quantified and for which monetary prices can be established are included in economic goal variables. Second, impacts incurred at different points in time are made commensurable by means of appropriate discount or interest rates. Third, it is possible to construct economic goal variables that combine positively valued impacts (benefits or revenues) with negatively valued impacts (costs or disbenefits) in additive or ratio forms. 

In constructing economic goal variables, several points should be kept in mind. 

1. Each actor has a different point of view, with different goals and values. Thus one or more goal variables should be constructed to represent the viewpoint of each actor, even in purely economic terms. 

2. The impacts of a particular alternative will be different on each actor, and each actor will have different values with respect to the desirability of various impacts. Thus the prices and definitions of economic goal variables may appropriately be different for different actors. 

3. Mechanisms for shifting the distribution of impacts among actors can and should be considered. Thus the economic goal variables should be defined in such ways that economic measures to shift the incidence of impacts can be explored—for example, through pricing policies, taxes, subsidies, or compensation payments. 

## 9.4.2 Some Basic Concepts

## THE TIME DIMENSION

Significant impacts occur at different points in time. For example, when a transportation operator builds a new facility or acquires a new vehicle, an initial investment of capital is made and then this cost is recovered by revenues that accrue in later time periods. One important issue in evaluation is how to balance the values of impacts that occur at different points in time. Economic methods provide one approach. 

The basic concept is that of the time value of money. A sum of money H can earn interest at some rate r, either by deposit in a bank account or by being loaned out in some other manner. Thus at the end of one year, if r is the annual interest rate, the sum H would grow to 

$$
G = H (1 + r).\tag{9.1}
$$

Conversely, if someone were to ask us how much we would pay now for a contract that offered a sure payment of G dollars at the end of one year, then we should be willing to pay H dollars. From this reasoning can be developed the following relationships: The value at end of year n of a present amount H is 

$$
G _ {n} = H (1 + r) ^ {n}.\tag{9.2}
$$

The value at present of a future amount $G_{n}$ to be received at end of year n is 

$$
H = G _ {n} (1 + r) ^ {- n}.\tag{9.3}
$$

The value at present of a series of future amounts $G_{n}$ that would be received at the end of the year in years $n = 1, 2, \ldots, N$ is 

$$
H = \sum_ {n = 1} ^ {N} G _ {n} (1 + r) ^ {- n}.\tag{9.4}
$$

The value at present of a series of future equal amounts G that would be received at the end of the year in years $n = 1, 2, \ldots, N$ is 

$$
H = G \sum_ {n = 1} ^ {N} (1 + r) ^ {- n}\tag{9.5}
$$

or, using properties of geometric series, 

$$
H = \frac {G}{\operatorname{CRF} (r , N)},\tag{9.6}
$$

where the capital recovery factor is defined by 

$$
\operatorname{CRF} (r, N) = \frac {r (1 + r) ^ {N}}{(1 + r) ^ {N} - 1}.\tag{9.7}
$$

The value of equal payments G, paid at the end of the year in years $n = 1, 2, \ldots, N$ , that would be received from an amount H invested at present is 

$$
G = H \times \operatorname{CRF} (r, N).\tag{9.8}
$$

These relationships can be used to establish various kinds of economic goal variables. For example, if an operator invests an amount C at the beginning of year 1 and receives revenue each year for N years in the amount B at the end of each year, then his net return can be computed in either of two ways. In the equivalent-annual-cost method all costs and revenues are put on an equivalent annual basis. Given the annual revenue payment B and the initial investment C transformed by (9.8) into an equivalent annual payment of 

$$
c _ {\mathrm{a}} = C \times \mathsf {C R F} (r, N),\tag{9.9}
$$

the equivalent annual cost EAC is 

$$
E A C = - B + c _ {a} = - B + [ C \times \operatorname{CRF} (r, N) ].\tag{9.10}
$$

In the net-present-value method all costs and revenues are represented by their values at the beginning of year 1. Given that the present value of the investment cost is C and the net present value of the revenue stream of B each year is, by (9.6), 

$$
b = \frac {B}{\operatorname{CRF} (r , N)},\tag{9.11}
$$

the net present value NPV of the total stream of benefits and costs is 

$$
\mathrm{NPV} = \frac {B}{\mathrm{CRF} (r , N)} - C.\tag{9.12}
$$

A comparison of $(9.10)$ and $(9.12)$ indicates that the EAC and NPV are directly related: 

$$
E A C = - C R F (r, N) \times N P V.\tag{9.13}
$$

Thus either measure can be used as a basis for comparing economic impacts at different points in time. (These are examples; many other types of measures are possible.) 

## CHOOSING A DISCOUNT RATE

An interest rate r can thus be used to establish equivalencies of economic impacts at different points in time, and the choice of a specific value for r can greatly influence the relative weights of present versus future costs and revenues. Table 9.4 shows this effect. 

There are a number of possible bases for the selection of an appropriate discount rate: 


Table 9.4 CRF factors


<table><tr><td rowspan="2">Year (N)</td><td colspan="5">Interest rate (r)</td></tr><tr><td>1%</td><td>5%</td><td>10%</td><td>15%</td><td>20%</td></tr><tr><td>1</td><td>1.01</td><td>1.05</td><td>1.10</td><td>1.15</td><td>1.20</td></tr><tr><td>2</td><td>0.51</td><td>0.54</td><td>0.58</td><td>0.62</td><td>0.65</td></tr><tr><td>5</td><td>0.21</td><td>0.23</td><td>0.26</td><td>0.30</td><td>0.33</td></tr><tr><td>10</td><td>0.11</td><td>0.13</td><td>0.16</td><td>0.20</td><td>0.24</td></tr><tr><td>20</td><td>0.06</td><td>0.08</td><td>0.12</td><td>0.16</td><td>0.25</td></tr><tr><td>30</td><td>0.04</td><td>0.07</td><td>0.11</td><td>0.15</td><td>0.20</td></tr></table>


Note: These figures are approximate; for detailed analyses the appropriate tables in standard references should be consulted. 


1. the actual current cost of borrowing money; 

2. the "opportunity cost" of capital, based upon the return that could be achieved from alternative investments of the resources; 

3. the "risk" in the proposed project, that is, the degree of uncertainty in future revenues and costs; or 

4. an explicit value judgment as to the relative desirability of impacts at different points in time, based on the values and preferences of those responsible for making the decision. 

There is a substantial literature on the choice of an appropriate discount rate, with the various views expressed depending, in part, on the context (see the discussion in de Neufville and Stafford 1971). 

It is our belief that the relative weighting given to present versus future impacts should be an explicit value judgment, as should the relative weights placed on any other types of impacts. These relative values would vary with the viewpoints of most if not all actors. The interest rates operating in the capital market at a given time are not necessarily the values that every interest group would place on impacts at that time. A choice of a discount rate should be made only in the context of the specific action alternatives available, with an awareness of their implications. Therefore, when economic goal variables are used, several alternative values for the discount rate should be established reflecting the perspectives of different interests, and a sensitivity analysis should be done to determine the effect on the economic goal variables (such as NPV) of these alternative values. 

## 9.4.3 Some Useful Economic Constructs

A number of types of economic goal variables can be constructed for comparison of alternative courses of action. Consider courses of action i, j, k, characterized by: 

1. initial investment costs $I_{i}$ , $I_{j}$ , $I_{k}$ ; 

2. annual costs to operate the system $A_{i}, A_{j}, A_{k}$ (all costs except that of the capital in the initial investment); and 

3. annual gross revenues from the system $R_{i}$ , $R_{j}$ , $R_{k}$ . 

For simplicity we assume that these are the only major categories of costs and revenues and that annual costs and revenues are constant over the life of each system. In actual applications these conditions would not be met; different items would have different useful lives, different salvage values, and perhaps different applicable interest rates, different rates of growth in annual costs and revenues, and so forth: 

We consider five categories of economic goal variables: 

1. Equivalent annual cost: 

$$
\mathsf {E A C} _ {i} = \left[ I _ {i} \times \mathsf {C R F} (r, N) \right] + A _ {i} - R _ {i}.\tag{9.14}
$$

2. Annual net operating revenue: 

$$
\mathrm{ANOR} _ {i} = R _ {i} - A _ {i}.\tag{9.15}
$$

3. Annual net revenue: 

$$
\mathsf {A N R} _ {i} = R _ {i} - A _ {i} - \left[ I _ {i} \times \mathsf {C R F} (r, N) \right] = - \mathsf {E A C} _ {i}.\tag{9.16}
$$

4. Net present value of costs and revenues: 

$$
\mathrm{NPV} _ {i} = - I _ {i} + \frac {R _ {i} - A _ {i}}{\operatorname{CRF} (r , N)} = \frac {\operatorname{ANR} _ {i}}{\operatorname{CRF} (r , N)}.\tag{9.17}
$$

5. Ratio of annual net revenue to investment: In this case the payoff of the investment is measured in terms of increasing annual net revenue, that is, the gain in gross revenue less the operating costs. For a single project one way of defining this is as annual net return on investment: 

$$
\mathrm{ANRI} _ {i} = \frac {R _ {i} - A _ {i}}{I _ {i}}\tag{9.18}
$$

or, for comparison of two projects i and j: 

$$
\mathrm{ANRI} _ {i, j} = \frac {\Delta \text { ANOR }}{\Delta I} = \frac {(R _ {i} - R _ {j}) - (A _ {i} - A _ {j})}{I _ {i} - I _ {j}}.\tag{9.19}
$$

This type of incremental measure is particularly useful when projects are ranked in order of increasing investment cost. It can then be used to answer the question, Is an increment of investment $\Delta I$ above the level $I_{j}$ worthwhile in terms of the increment of return? 

It is important to realize that much judgment goes into the choice of items to be included in the various terms of these measures. The actual financing mechanisms, taxes, and subsidies have significant implications. For example, if the investment the operator is considering involves buying an additional vehicle, it is quite likely that that investment will be financed by a mortgage or a similar mechanism through a bank or other source of capital. In this case the operator's investment may be only a down payment $d_{i}$ , and the major cost of the investment will be an annual charge $c_{i}$ to pay off the interest and principal on the mortgage. Thus / would be replaced by $d_{i}$ in the above relationships. 

Therefore, for each actor, a mix of measures with practical definitions should be developed which most effectively reflect the viewpoint of that actor. To illustrate we shall examine some specific forms of measures useful to various actors. 

## 9.4.4 Economic Goal Variables to Reflect the Viewpoints of Operators

Economic goal variables are especially useful in summarizing impacts from the viewpoints of transportation operators. For most private operators, and many public or semipublic operators, such economic measures directly reflect the impacts that are of greatest concern. Even in these circumstances, however, it will often be necessary to define several economic measures to reflect fully the different issues important to an operator, and there may be some important impacts that cannot be subsumed into any economic variables. 

The gross benefits to operators are the gross revenues from fares (or other user charges) and other sources, such as advertising, parking facilities, or concessions such as restaurants and other facilities in terminals. The costs to operate the system include direct operating costs such as fuel, labor, and spare parts and indirect operating costs such as management and administration (exclusive of the cost of capital investment). 

Some of the goal variables most often used are functions of these gross revenues $R_{i}$ and total direct and indirect operating costs $A_{i}$ ; these include the ones defined in section 9.4.3. The specific form used in chapters 5–7 was the annual net revenue: 

$$
\mathrm{ANR} _ {i} \equiv R _ {i} - A _ {i} - [ I \times \operatorname{CRF} (r, N) ] = I _ {\mathrm{GR}} - C _ {\mathrm{T}} \equiv I _ {\mathrm{NR}},\tag{9.20}
$$

where 

$$
C _ {\mathrm{T}} \equiv A _ {i} + [ I \times \operatorname{CRF} (r, N) ],\tag{9.21}
$$

$$
I _ {\mathrm{GR}} \equiv R _ {i}.\tag{9.22}
$$

Many different measures are used in particular sectors of the transportation industry, reflecting the variety of financing, tax, and organizational situations of decision makers (see, for example, Frankel 1977). 

9.4.5 Economic Goal Variables to Reflect the Viewpoints of Users The major impacts of system changes on users are through changes in the levels of service, which may be reflected in changes in the volumes of freight shipped or the numbers of users making particular travel choices. (For simplicity we consider a one-dimensional volume representing passengers.) While users do incur monetary costs, such as fares or operating costs of a private vehicle, these are just a portion of the impacts important to them. The basic premise underlying the use of economic variables to reflect impacts on users is that the demand function for a group of users shows the values they place on different levels of service. Thus the demand function expresses the users' relative "willingness to pay" for different service levels. 

## WILLINGNESS TO PAY

The argument for this is as follows (see figure 9.3) in the case of a single service variable, price. Based on the demand function D, a change in price from $p_{i}$ to $p_{i} + \Delta p$ will cause a change in volume from $V_{i}$ to $V_{i} + \Delta V$ ( $\Delta V$ will in general be negative for positive p, and vice versa). The $\Delta V$ users who leave the system are the ones who got just enough “benefit” or “value” out of using the system at price $p_{i}$ to make it attractive to them; at the higher price $p_{i} + \Delta p$ , the benefits are no longer sufficient to attract them. Therefore the benefit of using the system for these $\Delta V$ users lies between $p_{i}$ and $p_{i} + \Delta p$ , or for small $\Delta p$ , the benefit is approximately $p_{i}$ . Thus if we rewrite the demand function 

$$
V = D (p)\tag{9.23}
$$

as 

$$
p = g (V),\tag{9.24}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/fc366feb-933b-4442-bcbf-4538c4ada340/5c5e7263933ab54f8447049b71e68868f17562d48aee8546c4d9a47ce2765b9f.jpg)



Figure 9.3 The demand function as a measure of users' willingness to pay.


where g is the inverse function of D, we can measure the benefit to a small volume of users between $V_{i}$ and $V_{i} + \Delta V$ as 

$$
B _ {i} \approx g (V _ {i}).\tag{9.25}
$$

More generally, if $p_{0}$ is the actual price charged uniformly to all users, with a resulting volume $V_{0}$ , then integration over all volumes between 0 and $V_{0}$ gives the total benefit or value to users of that level of price. This gross user benefit is 

$$
\operatorname{UBG} (p _ {0}) \equiv \int_ {0} ^ {V _ {0}} g (V) \mathrm{d} V, \quad \text { where } V _ {0} = D (p _ {0}).\tag{9.26}
$$

On a graph this is the area under the demand curve from the vertical axis to the line $V_{0} = E$ . It is finite if the demand curve intersects the axis; if not, while the integral itself may not be bounded, the difference in UBG between two prices $p_{0}$ and $p_{i}$ is finite and can still be found. 

## APPLYING THE WILLINGNESS-TO-PAY CONCEPT

Now consider a change from $p_{0}$ to $p_{1}$ . We shall discuss three cases. First, assume there is only one service attribute, price, and that volume is a constant, $V_{0}$ . For a price change from $p_{0}$ to $p_{1}$ , from (9.26), 

$$
\varDelta \mathsf {U B G} _ {0 1} \equiv \mathsf {U B G} _ {0} - \mathsf {U B G} _ {1} = (p _ {0} - p _ {1}) V _ {0}.\tag{9.27}
$$

There is an improvement in service that is received wholly by the users $V_{0}$ . The magnitude of $UBG_{01}$ corresponds to the shaded area in figure 9.4. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/fc366feb-933b-4442-bcbf-4538c4ada340/7d9cf4243f28465117e672624a94bacbffdf478a98f63ba2cdb79c5818fab848.jpg)



Figure 9.4 User benefit under constant volume.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/fc366feb-933b-4442-bcbf-4538c4ada340/59ac7d3e3a4f5b9cde3b40b6f257ef8fa4ca4a51c1f259c1af54a9257cf491f6.jpg)



Figure 9.5 User benefit under changing volume.


The price p may be an explicit charge such as a railroad or air fare or bridge or highway toll, an expense such as automobile operating costs (oil, maintenance, and so forth), or the sum of a number of such items. In any of these cases the user benefit can be interpreted as the total cost savings to all users. 

Now let service volume vary with price according to a demand function D, as in (9.23). The problem is more difficult in this case for both conceptual and practical reasons. The conceptual issues can be illustrated by reference to figure 9.5. When price changes from $p_{0}$ to $p_{1}$ , volume changes from $V_{0}$ to $V_{1}$ . The original $V_{0}$ users benefit from the price decrease, but there are also benefits accruing to the $V_{1} - V_{0}$ new users of the system. There are three alternative views on how to measure benefit to users. 

i. Gross-benefit view. In this view, corresponding to the willingness-to-pay argument, the total benefit to users is given by the area under the demand curve. In the figure, for price $p_{0}$ and corresponding volume $V_{0}$ this integral corresponds to the area $E + A + D$ . The difference in gross user benefit between two actions would be 

$$
\varDelta \mathsf {U B G} _ {0 1} = \mathsf {U B G} (p _ {1}) - \mathsf {U B G} (p _ {0}) = \int_ {V _ {0}} ^ {V _ {1}} g (V) d V\tag{9.28}
$$

or, in the figure, the area $B + C$ . 

ii. Consumer-surplus view. A second point of view is that the benefits should exclude the amount actually paid out. The amount paid out is the total user cost, 

$$
\mathsf {U C} (p _ {0}) = p _ {0} V _ {0}.\tag{9.29}
$$

The consumer surplus is that amount of benefit received by users beyond what they actually pay: 

$$
\begin{array}{r l} \mathsf {U B C S} (p _ {0}) & \equiv \mathsf {U B G} (p _ {0}) - \mathsf {U C} (p _ {0}) \\ & = \int_ {0} ^ {V _ {0}} g (V) d V - p _ {0} V _ {0}. \end{array}\tag{9.30}
$$

In the figure this is area E (which may not be finite if the demand curve does not intersect the vertical axis). 

In comparing two alternative actions, the difference in consumer surplus would be used as a measure of user benefits: 

$$
\begin{array}{l} \varDelta \mathsf {U B C S} _ {0 1} = \mathsf {U B C S} (p _ {1}) - \mathsf {U B C S} (p _ {0}) \\ \qquad = \mathsf {U B G} (p _ {1}) - \mathsf {U B G} (p _ {0}) - \mathsf {U C} (p _ {1}) + \mathsf {U C} (p _ {0}) \\ \qquad = \int_ {V _ {0}} ^ {V _ {1}} g (V) d V - p _ {1} V _ {1} + p _ {0} V _ {0}. \end{array}\tag{9.31}
$$

In the figure this is the area $A + B$ . 

iii. User-cost view. A third point of view is expressed in either of two ways, each leading to the same result. From one perspective the benefit to users should reflect only the reduction in actual prices paid, that is, the reduction in user cost. This user-cost benefit is given by 

$$
\begin{array}{r l} \varDelta \mathsf {U B U C} & \equiv \varDelta \mathsf {U C} \\ & = p _ {0} V _ {0} - p _ {1} V _ {1}. \end{array}\tag{9.32}
$$

From another perspective the argument is made that the user benefit should be the gross benefit less the consumer surplus (Wohl and Martin 1967): 

$$
\begin{array}{r l} \mathsf {U B Y} & \equiv \mathsf {U B G} - \mathsf {U B C S} \\ & = \mathsf {U B G} - (\mathsf {U B G} - \mathsf {U C}) \\ & = \mathsf {U C}. \end{array}\tag{9.33}
$$

The result is the same. In comparing two alternatives, the difference in total user cost (9.32) would be used as a measure of user benefits. This corresponds to the difference between areas A and C in the figure. 

iv. Trapezoidal approximations. To visualize the differences among these measures, it is useful to assume that the demand function can be approximated by a linear relation in the region of interest. Then the integrals can be replaced by explicit areas. These are summarized in table 9.5. 


Table 9.5 Three measures of user benefit: comparison of differences in benefit for a change from $(p_{0}, V_{0})$ to $(p_{1}, V_{1})$


<table><tr><td>Measure</td><td>Differential areas in figure 9.5</td><td>Value of trapezoidal approximation</td></tr><tr><td>Gross benefit</td><td><eq>B + C</eq></td><td><eq>\frac{1}{2}(p_0 + p_1)(V_1 - V_0)</eq></td></tr><tr><td>Consumer surplus</td><td><eq>A + B</eq></td><td><eq>\frac{1}{2}(p_0 - p_1)(V_1 + V_0)</eq></td></tr><tr><td>User cost</td><td><eq>A - C</eq></td><td><eq>V_0p_0 - V_1p_1</eq></td></tr></table>


Source: Based on Wohl and Martin (1967). 


A comparison of the various measures shows that, except under very special conditions, each offers a different description of user benefit, and they may give different results on an incremental comparison of two actions. 

In the special case of constant volume 

$$
\Delta \mathrm{UBG} = 0,\tag{9.34}
$$

$$
\Delta \mathrm{UBCS} = \Delta \mathrm{UBUC},\tag{9.35}
$$

so that at least two of the measures give the same result. 

The conceptual difficulties in developing measures of user benefit involve arguments over appropriateness. At present the consumer-surplus and user-cost measures are the most commonly used (Wohl and Martin 1967, de Neufville and Stafford 1971, McIntosh and Quarmby 1972). 

The practical difficulties lie, in this case, in the measurement of areas under the demand curve. The linear assumption leading to the trapezoidal approximation to the areas must be used with caution; for significant changes in p, the approximation may introduce large errors. 

The units of these areas are the product of volume and price (for example, dollars per hour if volume is in passengers per hour and price is in dollars per passenger). 

In the third case we shall consider, the level of service is a vector S and volume varies according to a demand function D: 

$$
V = D (\mathbf {S}).\tag{9.36}
$$

The problems in measuring user benefit in this situation are compounded from those in the case of a single service attribute. In addition to the conceptual and practical problems noted already (different views on which measures to use and the practical problem of computing areas for nonlinear demand functions), there arises the important problem that the units of consumer surplus become complex and specific to the form of the demand functions. 

## RELATED ISSUES

## The value of time

In much of the literature of transportation engineering, a “user-cost” approach is recommended; as pointed out by Wohl and Martin, however, this is actually a consumer-surplus approach (when generated traffic is considered correctly). In this literature substantial effort is often devoted to establishing a “value of time”—a dollar value to be used to convert user travel time savings into equivalent monetary benefits (standard values of $1.375 per hour and, later, $1.75 per hour have been advocated). It should be clear from the preceding discussion that the value of time should be determined explicitly from the demand function; more directly, the demand function itself, together with all service attributes included in that function, should be used explicitly in determining the magnitude of user benefits, rather than a monetary valuation of time savings calculated from some standard independent of the demand function. (Only in the case of a linear demand function will the two approaches give the same result.) Further, since different market segments will have different demand functions, their values of time will be different. 

## Willingness to accept willingness to pay

Another important limitation of these measures of user benefit is that, if used carelessly, they are biased toward upper-income travelers. 

To see this, consider two market segments, one high-income and the other low-income, and assume that a linear demand function applies to each group. The high-income group will place a higher value on travel time than the low-income group; a ten-minute reduction in travel time would therefore result in a greater increase in volume of high-income travelers (all else being equal) than of low-income travelers. Two projects, A and B, are being considered, and each has the same investment cost: A provides a travel time reduction of 10 minutes only for high-income travelers; B provides a reduction of 10 minutes only for low-income travelers. Project A would have a higher value of $\Delta$ UBGB or $\Delta$ UBCS (though a lower value of $\Delta$ UBUC). From 