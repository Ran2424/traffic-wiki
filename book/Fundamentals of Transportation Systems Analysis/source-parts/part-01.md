![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/a9a45185-cfa1-407d-8a96-209400065f95/fe19e5c8225b9f7b951a0df835efc9a67e38534486141517046dd55cea7d59d1.jpg)


-LIBRARY-

PITTSBURG STATE UNIVERSITY 

Pittsburg, Kansas 66762 

Marvin L. Manheim is Professor of Civil Engineering at MIT. This book is included in the MIT Press Series in Transportation Studies. 

## WITHDRAWN

Fundamentals of Transportation Systems Analysis 

MIT Press Series in Transportation Studies
Marvin L. Manheim, editor
Center for Transportation Studies, MIT 

1. The Automobile and the Environment: An International Perspective, edited by Ralph Gakenheimer, 1978 



2. The Urban Transportation System: Politics and Policy Innovation, Alan Altshuler with James P. Womack and John R. Pucher, 1979 



3. Planning and Politics: The Metro Toronto Transportation Review, Juri Pill, 1979 

4. Fundamentals of Transportation Systems Analysis. Volume 1: Basic Concepts, Marvin L. Manheim, 1979 

Fundamentals of Transportation Systems Analysis
Volume 1: Basic Concepts 

Marvin L. Manheim 

## Copyright © 1979 by The Massachusetts Institute of Technology

All rights reserved. No part of this book may be reproduced in any form or by any means, electronic or mechanical, including photocopying, recording, or by any information storage and retrieval system, without permission in writing from the publisher. 

This book was printed and bound in the United States of America. 

## Library of Congress Cataloging in Publication Data

Manheim, Marvin L
Fundamentals of transportation systems analysis. 

Bibliography: p. 

Includes index. 

CONTENTS: v. 1. Basic concepts. 

1. Transportation planning. 2. Transportation— 

Mathematical models. 3. System analysis. I. Title. 

HE199.9.M34 380.5 78-11535 

ISBN 0-262-13129-3 

380.5 

m3146 

To Margaret and Susannah, who share with me the sheer delight that this volume is finally done 

The image provided is completely blank and contains no text or visible content. Therefore, there is no OCR result to output. 

Acknowledgments xiv 

Prologue
The Profession of Transportation Systems Analysis 3 

1
The Challenge of Transportation Systems Analysis 10 

## 2

The Demand for Transportation 58 

3 Case Study I: Disaggregate Prediction of Behavior 91 

4 Aggregate Prediction of Behavior 114 

## 5

Transportation System Performance 163 

6 Understanding Performance Functions I: The Vehicle Cycle and the Analysis of Cost Functions 216 

## 7

Understanding Performance Functions II: Congestion, Dimensionalities, and the Spatial Structure of Services 268 

8 Equilibration 312 

## 9

Evaluation 330 

10 Case Study II: Carrier Operations Planning 390 

11 The Dimensions of Consumer Choice 415 

12
Travel-Market Equilibration in Networks 464
13
Case Study III: A Network Analysis 505
14
Choice 540
15
The Role of the Professional 559
16
Designing an Analysis: An Introduction 583
Epilogue
The Ethics of Analysis 589
Appendix A
Values of Exponentials and Reciprocals 595
Appendix B
Basic Probability Formulas 597
Standard Abbreviations and Sources 598
Bibliography 602
Index 635 

This textbook provides a basic introduction to the field of transportation systems analysis. We shall treat this subject as a coherent field of study and shall employ an approach that will be applicable to many different types of transportation systems problems. This approach incorporates concepts from economics, engineering, operations research, and public policy analysis. Our hope is that the resulting synthesis will be intellectually coherent and stimulating, comprehensive, and pragmatic. 

Enough details and numerical examples will be provided to build understanding of the concepts and to indicate how they can be applied in practice to various modes and problems. We have not, however, attempted to survey all of the models and analytical techniques that have been developed in recent years. Rather, our objective is to provide the reader with a basic framework onto which many different areas of specialization can be added by later coursework and practical experience. 

Our approach integrates a number of methods from diverse areas of analysis that are now widely accepted in the profession. For example, the techniques that have been employed in most urban transportation planning studies are here described in the context of more fundamental methods of travel forecasting. Similarly, transportation systems technologies are viewed from the perspective of a unified theory, without undue concentration on the specific details of vehicle kinematics or traffic flow theory. 

The theory presented in this book builds upon many current research results. For example, the approach to travel demand modeling is based upon techniques now moving from the frontiers of research into the arena of professional practice. Thus the material is sufficiently new in its perspective that professionals already working in transportation—whether their backgrounds are in engineering, economics, or other fields—should find it useful. 

We expect the book to be used primarily for introductory courses in transportation systems analysis for undergraduate or graduate students. 

No prerequisites are assumed except a facility with mathematical notation. 

Since 1967 more than seven hundred such students have used versions of this material as it has evolved. Typical classes have included students majoring in transportation systems analysis with engineering or systems analysis preparations and also students with backgrounds in political science, urban studies, economics, management, and other fields. As we shall emphasize throughout the text, this mixture of backgrounds is an essential and exciting part of the field. 

The material has also been used in intensive training programs for midcareer professionals. Two-week courses taught annually at MIT since 1970 have been taken by over five hundred professionals from more than thirty countries. Attendees have come from national, state, and local governments and from private industry. In addition, special versions of this material have been presented in intensive courses in Israel, Spain, and Switzerland. 

We have not endeavored to give uniform coverage to all aspects of transportation systems analysis in this text. Our primary consideration was, rather, to identify and present concepts that are truly fundamental, in that understanding them is a prerequisite for any serious work in the field. 

Our secondary consideration was to emphasize, through more detailed treatment, certain topics which are basic yet are treated insufficiently or even erroneously in much of the technical literature. These topics include transportation demand and performance and the processes of evaluation and choice. Particular attention is given to demand for several reasons. First, it is very important. Second, there is a substantial behavioral component to the determination of demand, and this has often been slighted in transportation courses in favor of more technical matters that build on the engineering or systems analysis backgrounds of most present students and practitioners in the field. 

In contrast, topics that are covered briefly here—or not at all—because they are treated effectively in other texts or in the technical literature include optimization models, especially for network analysis, such as minimum-path and related algorithms; statistics; economic evaluation methods; and the details of present urban transportation forecasting models. Instead, key references are supplied at appropriate points. 

The development of models is an important part of any analysis, but we have here chosen just a few basic models to illustrate the concepts we present. In the case of demand and technology models, this approach is justified by the sheer abundance and diversity of available models, so that a comprehensive inventory would require an effort quite outside the range of the book. In the case of activity-shift models, on the other hand, there is an abundant and diverse technical literature but no outstanding synthesis, so we have chosen to leave this important and complex topic for a later volume. 

In order to emphasize the range of the field, we have deliberately chosen examples from a wide variety of modes and problem contexts. Even in courses on particular fields such as urban transportation, we believe that it is important for the student to understand that the methods he or she is learning are general and applicable to many other contexts. Instructors are encouraged to modify examples to fit local circumstances and the particular problems in which the class is most interested. The bibliography and guides to further reading found at the end of each chapter should provide useful starting points for such adaptations. 

This volume is self-contained. Volume 2 will present in-depth coverage of selected topics and is intended as an advanced and supplementary text. 

The text has been designed to be used flexibly for a variety of teaching and self-study approaches, as indicated on the accompanying figure. For example, one sequence of chapters (prologue, 1–5, 8–10, epilogue) covers fundamentals plus two case studies; this would be suitable for a one-semester introductory course. The remaining chapters form two additional sequences, one modeling-oriented (6, 7, 11–13) and one policy-oriented (14–16). The material can also be used for specialized courses: for example, a course on transportation engineering or transportation technology might include the prologue, chapters 1–3, 5–8, 10, and the epilogue plus portions of volume 2, which will present in-depth coverage of selected topics. 

The three case study chapters form the bases for practical exercises. Although they focus on urban transportation, applications to other modes and contexts are stressed in the exercises. The first case study, on disaggregate prediction (chapter 3), provides an elementary introduction to predicting consumer response to system changes. Especially useful is the introduction of the idea of employing worksheets to organize calculations. 

The second case study, on carrier operations planning (chapter 10), complements the concepts presented in the fundamentals sequence and 

Modeling-oriented: 

Policy-oriented: 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/a9a45185-cfa1-407d-8a96-209400065f95/74763b2482147fd8cc89a3e8fed232b286bda63c845bd6c50ba131dce8366ab1.jpg)



Teaching paths.


demonstrates the application of these concepts without elaborate computer models. It also demonstrates an operator's perspective. This study is designed so that the early portions can be done after chapters 1 and 2 and prior to, or in the course of, chapters 5 and 9. 

The third case study, on network analysis (chapter 13), complements the modeling-oriented chapters (especially chapters 11 and 12). In order to focus the student's attention on the substance of the concepts rather than on calculational details, a simple Fortran program is used (see the Teacher's Manual). The case study includes a sequence of questions. The reader studying the volume alone should pause at each question, study it, and write out an answer before proceeding. In a class, the questions can be used as a basis for discussions. 

A variety of study materials are included to further the goal of establishing a style of thinking about transportation systems problems. Aside from the case studies and self-checking questions included in the text, there are a number of exercises at the end of most chapters. Some of these exercises are relatively straightforward, requiring either algebraic manipulations or numerical calculations and judgments; these are meant to reinforce or test basic analytical concepts. To assist students to begin thinking about broader issues, many of the exercises are relatively open-ended and more qualitative than quantitative. To differentiate the exercises, we use the following symbols: 

E: Simple exercises, usually involving numerical calculations. 

C: Conceptual exercises, usually requiring substantial thought. 

P: Projects, usually requiring a substantial amount of independent work. 

We believe that transportation systems analysis is a single field of study and practice, with a unified theoretical foundation and a diversity of practical applications. As our acknowledgments indicate, in our search for this unified intellectual core we have learned a lot from our colleagues and associates. We see you, the readers of this work, as additional collaborators in our search. The present work is a snapshot of a rapidly evolving body of knowledge and so should evolve rapidly itself. We invite you to contribute to this effort. We look forward to getting your comments and ideas, and especially your reactions, as you test, apply, refine, and accept or reject the concepts presented here. 

This work has grown out of the teaching and research activities of the transportation systems program at MIT. I have learned much from my colleagues and students. 

Some of the material included here has evolved from joint efforts, initially presented in papers and technical reports. Where possible, specific acknowledgments of these debts have been made in the text. In particular, the material on demand draws heavily on the work of Moshe E. Ben-Akiva; that on choice and the role of the professional on joint works with Elizabeth Deakin, Arlee T. Reno, and John Suhrbier; and the case studies on work of George A. Kocur and Earl R. Ruiter. I have also benefited from the insights and comments of Wayne M. Pecknold, Steven R. Lerman, Jorge Barriga, Clint Heimbach, Frank S. Koppelman, Thomas Larson, and Kumares N. Sinha, as they have struggled to teach with this material in its earlier, more primitive forms. 

Among those who have contributed substantially to the development of the exercises are Mark Abkowitz, Richard L. Albright, Moshe E. Ben-Akiva, Kiran U. Bhatt, Daniel Brand, Harry Cohen, Mark Daskin, Greig Harvey, George A. Kocur, Steven R. Lerman, Mary McShane, Jacques Nahmias, Wayne M. Pecknold, Leonard Sherman, and William Swan. Earl R. Ruiter developed the original case study in chapter 13, using DODOTRANS. Mark Abkowitz, Greig Harvey, and Steven Lerman were responsible for the development of TTP-1, Mark Abkowitz converted the case study to that format, and Mary McShane made later modifications. 

In addition, less tangible but nevertheless important influences have come from Lowell K. Bridwell, Carlos Daganzo, Michael Florian, Ernst G. Frankel, Stuart Hill, Michael Lash, Brian V. Martin, Lance Neumann, C. Kenneth Orski, Paul O. Roberts, Robert W. Simpson, Richard M. Soberman, Joseph H. Stafford, and Martin Wohl. 

Particular thanks are extended also to those at MIT and elsewhere who made it possible for me to spend substantial time developing this material and provided other support: at MIT, C. L. Miller, Peter S. Eagle-son, Frank Perkins, and Joseph Sussman; at the Institut de Recherche des Transports, Paris, Michel Frybourg and Alain Bieber; at OECD, Paris, C. Kenneth Orski; and at the Israel Ministry of Transport and the Israel Institute for Transportation Planning and Research, Uri Ben-Efraim and Gideon Hashimshony. 

Responsible for the production of the many preliminary and final editions over the years have been Carol Walb, Charna Garber, Gilbert High, and Janet Brown, assisted by Steven Kahn, Gary Garrels, Nancy Pfund, and Colleen Keough. 

I especially want to acknowledge the guidance and inspiration of A. Scheffer Lang, who over the past twenty years has influenced so significantly not only this work but also the whole direction of our transportation systems activities at MIT. 

Needless to say, the author alone is responsible for the imperfections of this material. 

Fundamentals of Transportation Systems Analysis 

The image provided is completely blank and contains no text or visible content. Therefore, there is no OCR result to generate. 

# Prologue The Profession of Transportation Systems Analysis

## THE FIELD TODAY

In the last ten years the field of transportation systems analysis has emerged as a recognized profession. More and more government agencies, universities, researchers, consultants, and private industrial groups around the world are becoming truly multimodal in their orientation and are adopting a systematic approach to transportation problems. Specialists in many different disciplines and professions are working together on multidisciplinary approaches to complex issues. 

The field of transportation systems analysis has the following characteristics: 

It is multimodal, covering all modes of transport (air, land, marine) and both passengers and freight. 

It is multisectoral, encompassing the problems and viewpoints of government, private industry, and the public. 

It is multiproblem, ranging across a spectrum of issues that includes national and international policy, the planning of regional systems, the location and design of specific facilities, operational issues such as more effective utilization of existing facilities, carrier management issues, and regulatory, institutional, and financial policies. The objectives considered relevant often include national and regional economic development, urban development, environmental quality, and social equity, as well as service to users and financial and economic feasibility. 

It is multidisciplinary, drawing on the theories and methods of engineering, economics, operations research, political science, psychology, other natural and social sciences, management, and law. 

Transportation systems analysts are professionals who endeavor to analyze systematically the choices available to public or private agencies in making changes in the transportation system and services in a particular region. They work on problems in a wide variety of contexts, such as: 

- urban transportation planning, producing long-range plans (5–25 years) for multimodal transportation systems in urban areas as well as short-range programs of action (0–5 years), including operational improvements in existing facilities and services and location and design decisions for new facilities and services; 

- regional passenger transportation, dealing primarily with intercity passenger transport by air, rail, and highway and possible new modes (as in the Northeast Corridor Study in the United States or Project 33 in Western Europe; see Grëvsmahl 1978, Wheeler 1978, Wilken 1978);
- national freight transport, in developed countries such as the United States, where issues of truck-rail-water competition are of particular importance, as well as in developing countries, where the magnitude of investments in the transport sector, its spatial distribution, and its allocation among modes are all important components of the overall problem of national economic development planning; 

- international transport, where issues such as containerization, competition between sea and air, and intermodal coordination are important for freight shippers and carriers in an era of increasing international trade. 

The field of transportation systems analysis began with the application of systems analysis methods to urban transportation studies. Most of these early applications were concerned with long-range planning, were public-sector-oriented, and used similar methodological approaches. Now, many different variations in methodologies are being used in a wide variety of operational, planning, design, and policy applications, in both private and public sectors, and involving short-range as well as long-range perspectives, in all of the contexts indicated above. 

Today, transportation systems analysis is a mature profession, with a unified theoretical basis and many and diverse practical applications. It is an exciting field in which the concerns extend from abstract theory and complex models to politically important policy questions and institutional change strategies. Our objective in this volume is to show the unity and the diversity of this field. We also hope to impart some of the excitement and satisfaction of practicing this profession. 

## UNITY AND DIVERSITY

The field today is characterized by a diversity of problem types, institutional contexts, and technical perspectives. But underlying this tremendous diversity is a central intellectual core: a body of theory and a set of basic principles to be utilized in every analysis of a transportation system. The elements of this core are introduced in chapter 1 and amplified in later chapters. 

The intellectual core provides a set of unifying themes. As a consequence of the historical development of the field, however, there is a rich variety of ways in which analysts can draw on this core in performing a practical analysis of a specific set of issues. While the same basic theory and principles apply to each problem, very different types of models and methods of analysis are appropriate in different situations. 

## THE CHALLENGE

The focus of transportation systems analysis is on the interaction between the transportation and activity systems of a region. The substantive challenge of transportation systems analysis is to intervene, delicately and deliberately, in the complex fabric of a society to use transport effectively, in coordination with other public and private actions, to achieve the goals of that society. To know how to intervene, analysts must have substantive understanding of transportation systems and their interactions with activity systems; this requires understanding of the basic theoretical concepts and of available empirical knowledge. 

To intervene effectively, and actually bring about change, analysts must also have a proper perspective on their role. The methodological challenge of transportation systems analysis is to conduct a systematic analysis in a particular situation which is valid, practical, and relevant, and which assists in clarifying the issues to be debated. 

An analyst will often use models and other technical means to assist in developing the analysis. There is a wide spectrum of modeling approaches available, ranging from complex computerized simulation models, to very simple algebraic models, to no formal models at all. 

A key task for the analyst is to select a process of analysis, including a choice of model, that will help to produce an analysis that is relevant, valid, and practical, and that helps to clarify the issues. To implement this process effectively may involve the analyst in public participation and even in institutional change. An important element of the design of a process of analysis may be inclusion of activities that stimulate constructive and timely involvement of affected interests in an open, participatory process designed to recognize explicitly potential value conflicts and to promote constructive resolution of those conflicts. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/a9a45185-cfa1-407d-8a96-209400065f95/db3d0ddafaa8cc5b9495d66331fb063af544cb9b5b4bfbad59313234a809b651.jpg)



Figure P.1 The scope of transportation systems analysis.


Figure P.1 presents symbolically the image we have been describing. At the core of the field is the prediction of flows, which must be complemented by the prediction of other impacts. Prediction, however, is only a part of the process of analysis; and technical analysis is only a part of the broader problem, namely the role of the professional transportation systems analyst in the process of bringing about change in society. 

Today, transportation systems analysis is a field so broad and diverse that few individuals can remain competent in all its aspects; rather, many specialties are emerging, such as demand analysis, evaluation, policy, and the development of new systems. It is an exciting field, spanning the range from abstract theory and sophisticated mathematics to important public policy questions and issues of political strategy. 

Within this broad spectrum of intellectual styles and problem applications, each individual, building on the same basic foundations, can develop his or her own unique potential as a transportation systems analyst. 

## PROFESSIONAL TRAJECTORIES

An education in transportation systems analysis can lead to many different professional careers (figure P.2). Transportation systems analysts 

## Application specialties

highway engineering
flight transportation
marine transportation
transportation management
traffic engineering
urban transportation planning
developing country transportation
rail transportation
port development and planning
airport planning
transit operations
trucking
transportation regulation
transportation and economic development
transportation engineering
transportation economics
national transportation policy
transportation environmental analysis
and others 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/a9a45185-cfa1-407d-8a96-209400065f95/3c8cf5a51b0d17d311ac144e34fb312df31542ab2a58378cca09409087e2dd10.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/a9a45185-cfa1-407d-8a96-209400065f95/f4ba735aa5be3d2d9fe9dabcdab6ff66db7cff80c71708909a1c1e58336455dc.jpg)



Figure P.2 Careers in transportation systems analysis.


## Methodological specialties

demand
transportation system performance evaluation
policy analysis and implementation
institutional change strategies
urban planning and development management
systems analysis methods
environmental impacts
economics
activity systems analysis and others 

work for private firms and for public agencies; for carriers such as airlines, steamship companies, railroads, or transit agencies and for other operators such as airport or seaport authorities or highway departments; for government agencies at local, state, and federal levels, as analysts, planners, and policy makers, as traffic engineers, highway engineers, transit planners, airport planners, or railroad analysts; and for private firms involved in the design and operation of facilities, in the manufacture of equipment, or in consultation work. 

Professionals in the field can take many different roles: technical analysts, working primarily with quantitative methods in any or all of the varied methodologies of the field; project managers, managing groups of technical professionals; community interaction specialists, at the interface of technical analysis and political action; policy analysts, providing technically oriented support to elected officials, legislators, and others; policy makers, such as heads of transportation firms or agencies, or ministers or secretaries of transportation; and, of course, educators and researchers. 

Thus transportation systems analysts can follow a wide variety of professional careers. We like to use the term “trajectory” because, as suggested by the upper right-hand corner of figure P.2, an individual’s career is rarely a predictable “linear” progression up a well-defined career ladder. 

Transportation is a rapidly changing profession in a rapidly changing world. The careers of most transportation systems analysts are likely to resemble the randomness of Brownian motion more than a simple linear progression. Each individual's career will evolve in unpredictable ways: new jobs, new events, changing external forces, development of new personal skills, all contribute to a largely unpredictable professional trajectory. 

This uncertainty suggests that an individual must acquire a broad professional base as well as specialized training in particular aspects of the field. From this basic grounding in the fundamentals of transportation systems analysis, one will usually go on to acquire more specialized training through academic coursework and on-the-job experience. As the individual acquires this more specialized training and advances from job to job, he or she becomes more “expert.” This is valuable and natural, but it is also a source of concern. 

As one acquires more and more technical expertise, one also acquires a set of attitudes, values, and perspectives peculiar to a particular subculture—the community of related specialists. While this has positive features, it also has serious dangers. The dangers arise from the loss of a sense of perspective and increasing rigidity in one's professional approaches—the belief that there is a "right way" to do something, or a "right solution" to a particular problem, or, most dangerous of all, that "the expert knows best." 

As one enters into a career in transportation systems analysis, one needs to be conscious of the balance to be achieved between "expertise" and "flexibility." Specialization and increasingly deeper knowledge of one's specialty are important; but personal flexibility, the ability to modify one's capabilities in response to the needs and challenges of new opportunities in one's unpredictable professional trajectory, is equally important. (These themes are taken up in chapters 14 and 15 and in the epilogue.) 

# The Challenge of Transportation Systems Analysis

## 1.1 A WORLD OF CHANGE

We live in a world of rapid change. This is particularly significant for transportation systems analysis because of the strong interactions between transportation and the rest of society. 

We can identify three critical dimensions of change relevant to transportation. The first is change in the demand for transportation. As the population, income, and land-use patterns of metropolitan areas and states change, so do the patterns of demand for transportation—both the amount of transportation desired and the spatial and temporal distribution of that demand. 

The second dimension of change is in technology. For example, in urban transportation, until just a few years ago the only actively considered alternatives were highways and rapid rail transit. Now we are able to consider such alternatives as lanes or even whole expressways restricted to buses; basically new technologies such as "dual-mode" systems, in which vehicles operate under individual control on local streets and automatically on tracked interurban guideways; and a variety of policy options designed to improve the efficiency of use of existing technology, such as incentives for carpools and van pools, "dial-a-ride" small buses, road pricing strategies, disincentives for automobile use, and auto-restricted zones (UMTA 1975, Smith, Maxfield, and Fromovitz 1977, TRANSPORTATION SYSTEM MANAGEMENT 1977). These new technologies provide a rich market basket of alternatives, from which a wide variety of transportation systems for metropolitan areas can be developed. 

Change has been rapid in other areas of transportation technology as well, as exemplified by the development of freight containerization, "jumbo" jet aircraft, vertical or short takeoff and landing (V/STOL) aircraft, and air-cushion vehicles for water and land transport. 

The third dimension of change is in the values, public and private, that are brought to bear on transportation decision making. It has become clear that many different groups are affected by decisions made about transportation. No longer is it sufficient to design transportation systems simply to serve the “users,” in some aggregate sense. Rather, we must identify which groups are served well and which groups poorly by a particular facility or system; and so we have begun to focus on the needs of those who are too poor or too ill or too young or too old to have ready access to automobile transportation. We have also become deeply concerned with the social and environmental effects of transportation: air pollution, noise pollution, community disruption, and ecological effects are given increasing weight in transportation decision making. 

These three dimensions of change—in demand, in technology, and in values—form the background against which we shall develop the basic concepts of transportation systems analysis. 

## 1.2 THE SCOPE OF THE PROBLEM

The first step in formulating a systematic analysis of transportation systems is to examine the scope of the analytical task. We shall start by setting out the basic premises of our approach, namely, the explicit treatment of the total transportation system of a region and of the interrelations between transportation and its socioeconomic context. We shall then identify those aspects of the system that can be manipulated—the “options”—and those aspects that are relevant to decision making—the consequences, or “impacts,” of the options. Given this framework, we can proceed to discuss the problem of prediction (section 1.3). 

## 1.2.1 Basic Premises

Two basic premises underlie our approach to the analysis of transportation systems: 

1. The total transportation system of a region must be viewed as a single, multimodal system. 

2. Consideration of the transportation system cannot be separated from consideration of the social, economic, and political system of the region. 

## THE TOTAL TRANSPORTATION SYSTEM

In approaching the analysis of a transportation systems problem, initially we must consider the total transportation system of the region: 

1. All modes of transportation must be considered. 

2. All elements of the transportation system must be considered: the persons and things being transported; the vehicles in which they are conveyed; and the network of facilities through which the vehicles, passengers, and cargoes move, including terminals and transfer points as well as line-haul facilities. 

3. All movements through the system must be considered, including passenger and goods flows from all origins to all destinations.
4. For each specific flow, the total trip, from point of origin to final destination, over all modes and facilities must be considered. 

For example, in a study of intercity passenger transport in a megalopolitan region, initially we must consider railroads, airplanes, buses, private automobiles, and trucks as well as new and innovative modes such as tracked air-cushion vehicles (TACV) and V/STOL aircraft. We must consider not only the direct intercity line-haul links but also the vehicles that will operate over these links, the terminals, en route stations, and other transfer points, and such means for access to, and egress from, the intercity portion of the system as taxis, limousines, automobiles, local transit, and other means of intracity transport. We must consider the diverse patterns of origins and destination of movements as well as how passenger and goods flows may use the same facilities. In examining each movement, we must consider the service provided on access and egress portions of each trip as well as on the line-haul portion. 

After this initial comprehensive definition of the transportation system has been made, the analyst, as he defines more finely the primary objectives of his analysis, can narrow his focus to those elements of the system that are of direct concern. This procedure will force him to consider explicitly the assumptions introduced by eliminating individual elements of a highly complex and interrelated system. 

## THE INTERRELATION OF TRANSPORTATION AND ACTIVITY SYSTEMS

The transportation system of a region is tightly interrelated with the socioeconomic system. Indeed, the transportation system will usually affect the way in which the socioeconomic system grows and changes. And changes in the socioeconomic system will in turn call forth changes in the transportation system. This interrelationship is fundamental to our view of transportation systems analysis. 

The system of interest can be defined by three basic variables: T, the transportation system; A, the activity system, that is, the pattern of social and economic activities; and F, the pattern of flows in the transportation system, that is, the origins, destinations, routes, and volumes of goods and people moving through the system. Three kinds of relationships can be identified among these variables (see figure 1.1): 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/a9a45185-cfa1-407d-8a96-209400065f95/49a4afe62a5e71b0142ca284a436d45cd884c6779dd7d65b4e5046f2c4ad697a.jpg)



Figure 1.1 Basic relations.


1. The flow pattern in the transportation system is determined by both the transportation system and the activity system. 

2. The current flow pattern will cause changes over time in the activity system: through the pattern of transportation services provided and through the resources consumed in providing that service. 

3. The current flow pattern will also cause changes over time in the transportation system: in response to actual or anticipated flows, entrepreneurs and governments will develop new transportation services or modify existing services. 

Though we label the activity system with the single symbol A, we must not assume that this system is as simple as the symbol suggests. On the contrary, the activity system of a metropolitan area or a megalopolitan region or a developing country consists of many subsystems, overlapping and interrelated—social structures, political institutions, housing markets, and so on. Transportation is only one of these subsystems. 

The evolution of the activity system is determined by a large number of forces and pressures. The internal dynamics of this system are very complex, and our understanding of these dynamics is very incomplete. 

Transportation plays a role in influencing the evolution of the activity system, but, except in very special situations, it is not the sole determinant of that evolution. The development of automobiles and of extensive systems of freeways does not alone cause suburbanization and dispersal of metropolitan areas, but it does interrelate closely with the dynamics of rising income, changing housing and labor markets, and other subsystems. Even the provision of access roads to a hitherto virgin area of an underdeveloped country will not by itself stimulate agricultural development. There must be a market for the produce, and there must be an array of adequate incentives to development. 

The interrelation between transportation and the activity system is fundamental to our approach. The challenge of transportation systems analysis is to intervene, delicately and deliberately, in the complex fabric of a society to use transport effectively, in coordination with other public and private actions, to achieve the goals of that society. Responding to this challenge is not easy. We must understand transportation as a technology, a system of physical elements managed by human organizations to move people and goods. We must also understand transportation as a subsystem of the complex of social, economic, political, and other forces we so tersely summarize as “the activity system.” Most important of all, we must know how to use this understanding effectively. 

## 1.2.2 The Major Variables

Now that we have defined in broad terms the nature of the system with which we are dealing, we must explore the major variables needed in an analysis. In the last section we characterized the system in terms of three major, interrelated variables—T, A, and F. The questions we now address are: What options are available for influencing the system? What impacts should be considered in evaluating alternative courses of action? 

## INTERVENING IN THE SYSTEM: OPTIONS

There are many individuals, groups, and institutions whose decisions interact to affect the transportation system, the activity system, and thus the pattern of flows. The user of transportation, whether a shipper of goods or a passenger, makes decisions about when, where, how, and whether to travel. The operator of particular transportation facilities or services makes decisions about vehicle routes and schedules, prices to be charged and services offered, the kinds and quantities of vehicles to be included in the fleet, the physical facilities to be provided, and so on. Governments make decisions on taxes, subsidies, and other financial matters that influence users and operators, on the provision of new or improved facilities, and on legal and administrative devices to influence, encourage, or constrain the decisions of operators or users. 

It is often important to identify which groups have control over particular decisions, particularly when it is time to implement a selected course of action. We shall often ignore this question, however, in order to clarify the task of analysis. In other words, we shall attempt to identify all the possible decisions that might be made, without regard to who has the power to make a specific decision in a particular context. 

Options, or decision variables, are those aspects of the transportation and activity systems that can be directly changed by the decisions of one or several individuals or institutions. The options available can be divided into two groups: those dealing with the transportation system itself and those dealing with the activity system. 

## Transportation options

Many aspects of a transportation system can be varied. Not all of these are open to a single decision maker, nor are all open at the same time. This spectrum of options, or “decision variables,” may be summarized as follows: 

Technology The development and implementation of new combinations of transportation components enable transportation demand to be satisfied in ways not previously available. Examples are containers, container ships, and piggyback trucks and railcars; the supersonic transport; and new urban mass transportation concepts, such as dual-mode and “dial-a-ride” systems. 

Options involving technology include fundamental decisions about the means of propulsion, the medium through which the vehicle travels, supporting way and suspension systems, vehicle size and shape characteristics, typical route and network structure, and general mode of operations. Decisions must be made about these options within the constraints of technological feasibility, but there is a wide range of 

options nevertheless, and we have seen very rapid growth in the variety of specific technologies available for urban, interurban, and developing country contexts. 

Networks Options involving networks include their general configurations and the approximate geographical locations of their links. Examples are the grid systems typical of many of our present cities versus radial links and concentric circles. 

Link characteristics Networks consist of links and nodes. Links correspond to facilities, such as highways, rail lines, or urban streets. Where it is necessary to model the characteristics of intersection points within a single mode (highway intersections, rail yards) and of transfer points between modes (airports, rail terminals, bus stops), these are also represented as links. Nodes simply express the connectivity relations of links in the network. Options include the detailed physical location of links and nodes and those characteristics of the links that affect flow, such as the number of lanes of highway or tracks of railroad, the grades and curves of the roadway, the type of signaling or traffic control, and the internal layout of terminals. 

Generally we shall adopt the convention of most transportation network analysis and assume that all flow properties are represented in links and that nodes create no barriers to flow. Where node properties must be modeled—for example, transfer time at a rail terminal or airport—we shall do so by a subnetwork of links in the model that represents, and has the same properties as, the terminals. Thus nodes serve only to express the topology of the network. 

Vehicles Most transportation modes involve vehicles (exceptions: pipelines, conveyors). The major options include the number of vehicles in the system and their characteristics. (Note that the choice of technologies sets a broad range to such options as networks, links, vehicles, and operating policies, but detailed decisions must still be made within the feasible range.) 

System operating policies This set of options includes the full spectrum of decisions about how the transportation system is operated. The networks, links, and vehicles establish an envelope of possibilities; within that envelope a large variety of detailed operating decisions must be made. These options include vehicle routes and schedules, types of services to be offered, including services auxiliary to transportation (passenger meals, diversion and reconsignment privileges for freight), prices (both general pricing policy and specific pricing decisions), financing, subsidies, and taxing schemes, and regulatory decisions. Some of these operating policy options can be varied almost on a day-to-day basis; others, such as pricing policy and regulatory decisions governing the entry of new carriers, may be unchanged for decades. 

Organizational policies This set of options includes a wide variety of management, organizational, and institutional decisions. Within a single transportation organization, public or private, there are many detailed decisions about functional and geographic structure. Within a region there are decisions about how the transport sector should be organized, including the numbers and types of institutions, the functions to be assigned to each, the relative domains of responsibility, and the channels of communication, coordination, and control. 

This set of transportation options fully defines the space of possible transportation plans and policies. However, these options are exercised not in a vacuum but in the context of a system of social and economic activities. 

## Activity-system options

The activity system is defined as the totality of social, economic, political, and other transactions taking place over space and time in a particular region. These transactions, both actual and potential, determine the demand for transportation; in turn, the levels and spatial patterns of those interactions are affected in part by the transportation services provided. Therefore, in modeling transportation systems, we must clearly identify those options in the activity system that will affect transportation demands. 

Travel options These are the options open to every potential user of the transportation system: whether to make a trip at all, where to make it, when, and how—by what mode and route. These options apply to the individual traveler and to the shipper of freight. The decisions actually made by the shipper or traveler will be based in part upon the perceived characteristics of the transportation system and in part upon the actual and potential patterns of transactions in the activity system. The aggregate result of all the individual decisions about travel is expressed as the demand for transportation. 

Other activity options Most of the social, economic, and political actors in the activity system have a wide range of options about how, when, and where they will conduct their activities. Over the long term these options profoundly influence the demand for transportation. For example, as major changes in a transportation system are made over time, the spatial pattern of population and economic activity will change, as actors exercise their options for changing the location or scale of their activities. Forces within the economy external to the transportation system, such as national economic policy, rapid social change, housing subsidies, or mortgage policy, may impact on the spatial pattern of activity and thus affect the demand for transportation. 

In many transportation analyses most of these activity options—for example, rate of economic growth, sectoral and regional patterns of growth, aggregate population—must be treated as exogenous, completely uncontrollable by the transportation analyst. The exercise of some of these options by various decision makers will be partially influenced by transportation; for example, transportation will affect the detailed distribution of population and employment within a region. Still other options are controllable to some extent in explicit coordination with transportation options—for example, the control of land use through zoning and land-development incentives. 

Whether fully controllable or not, however, the full set of transportation and activity system options must be considered in any analysis. 

THE CONSEQUENCES OF TRANSPORTATION: IMPACTS
When evaluating alternative transportation systems, one would like to consider all the relevant consequences. Any change in the transportation system can potentially affect a variety of groups and interests. Impacts are those aspects of the transportation and activity systems that should be considered in evaluating possible changes to the transportation system. 

The prospective impacts can be broken down as follows, in terms of the groups on which the impacts fall: 

1. User impacts: Impacts on travelers and shippers of goods. Users are differentiated by location within the region, by trip purpose, and by socioeconomic group. Examples: suburban resident commuting to central-city job; low-income non-car-owning resident of center city traveling to health facilities. 

2. Operator impacts: Impacts on operators of the transport facilities and services. Differentiated by mode, by link, and by route. Examples: air carrier, trucker, highway maintenance agency, port authority, toll-bridge operator. 

3. Physical impacts: Impacts caused by the “physical presence” of transport facilities or services affect many who are neither users nor operators. These groups can be differentiated by type of impact and by location. Examples: families, jobs, and taxable real estate displaced by new construction; neighbors affected by environmental degradation 

through noise, fumes, air pollution, or groundwater changes. 

4. Functional impacts: The impacts on the activity system as users change travel patterns in response to transport system changes. Differentiated by location within region and by type. Examples: changes in retail sales areas in suburban shopping centers and central business districts; changes in production costs; changes in land values. 

5. Governmental impacts: Differentiated by location and by level of government or agency type. Examples: municipal, state, or federal agencies; citizen groups; elected representatives. 

An essential characteristic of transportation is the differential incidence of its impacts. Some groups will gain from any transportation change; others may lose. Therefore, transportation choices are essentially sociopolitical choices: the interests of different groups must be balanced. This view has profound implications for the evaluation of alternative options. 

## 1.3 PREDICTION OF FLOWS

Any proposed change in a transportation system (or a completely new system) can be expressed in terms of the options identified in section 1.2. The problem of prediction is to anticipate the impacts that a particular proposal will have; that is, we need procedures for predicting the impacts associated with any set of options (figure 1.2). In transportation the impacts depend upon the pattern of flows resulting from the particular set of options. 

Consider the present transportation system T and activity system A. A particular proposed plan will be defined in terms of changes in the transportation options, $\Delta T$ , and in the activity-system options, $\Delta A$ . Implementation of the plan will change the transportation system from T to $T'$ and the activity system from A to $A'$ . Corresponding to these changes there will be a change in the pattern of flows: F will become $F'$ . 

The core of any transportation systems analysis is the prediction of changes in flows. There will usually be many other significant impacts as well, but predicting the change in flows is always an essential step. (Even if there is no change in flows, this judgment must be reached explicitly.) 

Specification of the transportation system T at any point in time and of the activity system A implies the pattern of flows F. The basic hypothesis underlying this statement is that there is a market for transportation which can be separated out from other markets (Beckmann, McGuire, and Winston 1956, Manheim 1966b, Wohl and Martin 1967). This market is represented by the type 1 relation introduced in section 1.2.1; the hypothesis is that the type 1 relation can be separated from the type 2 and type 3 relations. This hypothesis can be expressed symbolically as follows. First, to our three variables T, A, and F we add two more: S, the service characteristics experienced by a particular flow or set of flows (travel times, fares, comfort, and so forth), and V, the volume(s) of flow in the network. Each of these variables may be a vector or other array. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/a9a45185-cfa1-407d-8a96-209400065f95/34294309a97548a13e324cd65d2f3e08be0a3a9ea1a61fe2a08acf5aa06000ed.jpg)



Figure 1.2 The prediction problem.


We express the hypothesis as follows: 

1. Specification of the transportation system T establishes service functions, J. These service functions indicate how the level of service varies as a function of the transportation options and the volume of flows; for a particular transportation system T, the level of service S that a traveler will experience is a function of the volume V of travelers using the system: 

$$
\mathbf {S} = \mathbf {J} (\mathbf {T}, \mathbf {V}).\tag{1.1}
$$

2. Specification of the activity-system options, A, establishes demand functions, D. These demand functions give the volume of flows as a function of the activity-system options and the level of service; for a particular activity system A, the volume of travelers V that will use 

the system is a function of the level of service S experienced by those travelers: 

$$
\mathbf {V} = \mathbf {D} (\mathbf {A}, \mathbf {S}).\tag{1.2}
$$

3. The flow pattern F consists of the volume V using the system and the level of service S experienced by those travelers: 

$$
\mathbf {F} = (\mathbf {V}, \mathbf {S})\tag{1.3}
$$

For a particular transportation system T and activity system A, the flow pattern that will actually occur, $\mathbf{F}^{0} = \mathbf{F}(\mathbf{T}, \mathbf{A})$ , is the volume $V^{0}$ and the level of service $S^{0}$ determined as the equilibrium solution to the service and demand relations (1.1) and (1.2): 

$$
\left. \begin{array}{l} \mathbf {S} = \mathbf {J} (\mathbf {T}, \mathbf {V}) \\ \mathbf {V} = \mathbf {D} (\mathbf {A}, \mathbf {S}) \end{array} \right\} \longrightarrow (\mathbf {V} ^ {0}, \mathbf {S} ^ {0}).\tag{1.4}
$$

Thus the specification of T and A implies particular values of equilibrium volume $V^{0}$ and level of service $S^{0}$ (if a unique equilibrium exists—see chapters 8 and 12): 

$$
(\mathsf {T}, \mathsf {A}) \longrightarrow (\mathsf {J}, \mathsf {D}) \longrightarrow [ \mathsf {F} (\mathsf {T}, \mathsf {A}) = (\mathsf {V} ^ {0}, \mathsf {S} ^ {0}) ].\tag{1.5}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/a9a45185-cfa1-407d-8a96-209400065f95/3c15b63834056413c66295e0ac35e993e26fca78e9b2dbd128afb81ffd379e18.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/a9a45185-cfa1-407d-8a96-209400065f95/db61519ec29cb53d7df94b815b9887596b194ca8afee37e1de686ab3f538929a.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/a9a45185-cfa1-407d-8a96-209400065f95/7044aaca070555f6cb8c7e17dbfe20f2ac8e33ccb317b343138e766afde0740a.jpg)



Figure 1.3 Simple equilibrium.



The Challenge of Transportation Systems Analysis


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/a9a45185-cfa1-407d-8a96-209400065f95/6a5ba21bbcb42cf0670767cff1407f104391838e98dae177932555a350e42c04.jpg)



Figure 1.4 Comparing two systems.


The graphical interpretation of this formulation is shown in figure 1.3. In this figure V and S are assumed one-dimensional. Further, it is assumed that as the volume of flow in the system increases, the level of service decreases, as shown in part a of the figure; and as the level of service increases, the volume desiring to use the service increases, as shown in part b. $^{1}$ 

To see the implications of this formulation, suppose that we are considering two alternative transportation systems, $T^{0}$ and $T^{1}$ . $T^{0}$ is the existing transportation system, for example, a highway between two towns. We are considering replacing the highway by a new, improved facility $T^{1}$ . Figure 1.4 shows the two service functions, $J^{0}$ and $J^{1}$ , corresponding to $T^{0}$ and $T^{1}$ . Let us assume that there is one service attribute that is important: travel time over the routes, t. (Since improvement in S corresponds to reduction in t, the curves in this figure are opposite in shape to those of the previous figure.) 

The equilibrium flow over $T^{0}$ is the flow $F^{0} = (V^{0}, t^{0})$ determined by the intersection of $J^{0}$ and D, the demand curve. Now consider the improved system $T^{1}$ , represented by $J^{1}$ . If we assume that the same volume of travel $V^{0}$ will occur on the new system as on the old, we would anticipate a service level $t^{*}$ : that is, if volume remains constant, we expect a lower trip time because of the improved facility. 

However, the constant-volume assumption is erroneous, for the travel volume will increase because the increased level of service—the decreased trip time—will attract more users. The extent of this increase in volume is given by the demand function D. Thus the actual flow pattern resulting will be that given by the equilibrium of D and $J^{1}$ : $F^{1} = (V^{1}, t^{1})$ . That is, the traffic volume will increase, and the level of service will be intermediate between $t^{0}$ and $t^{*}$ : the new facility will serve more users at a level of service that is better, but not as good as it would be if no new users were attracted. 

## 1.4 APPLYING THE CONCEPTS

## 1.4.1 Simple Equilibrium: An Example

To illustrate these concepts we consider a highway connecting two towns, Suburb and City. We assume the following characteristics. 

## SERVICE LEVEL

The level of service S will be expressed by the travel time t for a trip between the two towns. 

## TRANSPORTATION SYSTEM

The road is a two-lane highway divided into two one-lane roadways, one in each direction. It is ten miles long. 

## SERVICE FUNCTION

We consider each of the roadways separately. The general form of the service function is 

$$
\mathbf {S} = \mathbf {J} (\mathsf {T}, \mathsf {V})\tag{1.6a}
$$

or, in this example, 

$$
t = m + n V,\tag{1.6b}
$$

where options T are reflected in the values of the parameters m and n: 

$$
\mathsf {T} = (m, n).\tag{1.7}
$$

For this particular highway the parameter values are 

$$
\begin{array}{l} m = 1 0 \text {minutes}, \\ n = 0. 0 1 \text {minute per vehicle / hour}. \end{array}\tag{1.8}
$$

That is, 

$$
t = 1 0 + 0. 0 1 V.\tag{1.9}
$$

The units of t and V are thus minutes and vehicles per hour, respectively. 

## ACTIVITY SYSTEM

The two towns are characterized by their populations, employment levels, and income levels. The trip-making behavior of the residents reflects these variables. 

## DEMAND FUNCTION

We consider the one-way demand for travel from City to Suburb only. The general form of the demand function is 

$$
\mathbf {V} = \mathbf {D} (\mathbf {A}, \mathbf {S})\tag{1.10a}
$$

or 

$$
V = a + b t,\tag{1.10b}
$$

where options A are reflected in the values of the parameters a and b: 

$$
\mathbf {A} = (a, b).\tag{1.11}
$$

For travel between the two towns the parameter values are 

$$
a = 5, 0 0 0 \text {   vehicles / hour },
$$

b = -100 vehicles/hour per minute. 

(1.12) 

Thus 

$$
V = 5, 0 0 0 - 1 0 0 t.\tag{1.13}
$$

## FLOW PATTERN

The flow pattern F is defined by the volume V of travelers from City to Suburb, in vehicles per hour, and the level of service they experience, expressed by the travel time t in minutes: 

$$
\textbf {F} = (V, t).\tag{1.14}
$$

## EQUILIBRIUM

The equilibrium flow pattern $(V^{0}, t^{0})$ corresponding to the options $(T, A)$ will be such that both service and demand relations are satisfied: 

$$
t ^ {0} = m + n V ^ {0} = 1 0 + 0. 0 1 V ^ {0}
$$

$$
V ^ {0} = a + b t ^ {0} = 5, 0 0 0 - 1 0 0 t ^ {0}.\tag{1.15}
$$

## 1.4.2 Exercises

## INSTRUCTIONS FOR ANSWERING QUESTIONS

Many of the questions that follow are “self-checking” in that their answers immediately follow them. First cover the page with a sheet of paper. Then slide the paper down to the solid square that announces the answer. Now, keeping the answer covered by the paper, read the question. Think through your answer and jot it down on a piece of scratch paper (especially if you are asked to sketch or calculate something). Then uncover the printed answer and compare with your solution. If correct, go on to the next question. If incorrect, go back and review the material until you understand why your answer was wrong. 

■ Question 1.1 Examine the values of the parameters a, b, m, and n as given in equations (1.8) and (1.12). Discuss briefly the physical significance of these values. What is the significance of their signs (+ or −)? of their relative magnitudes? 

■ Answer 1.1 Parameters a and b: The demand function describes the number of people or vehicles that will travel at different levels of service (considering travel time as the level of service). The parameter a can be considered as a potential demand, that is, the demand for travel if travel time between the two zones were zero. The equilibrium volume of flow will certainly be less than a. The parameter b represents the change in demand for each unit change of travel time in minutes. Note that b < 0, correctly indicating that as travel time increases, demand decreases. 

Parameters m and n: The service function describes the level of service that a particular transportation option will provide for various flow volumes. The parameter m measures the free-flow travel time, the travel time over the link for zero volume. The parameter n represents the effects of congestion on travel time. Specifically, for each vehicle on the link, travel time increases by 0.01 minute per mile. Note that n > 0 correctly indicates that as V increases, t increases. 

■ Question 1.2 Find the equilibrium flow pattern graphically. Plot the service and demand functions on the same set of axes. (Place t on the horizontal axis, V on the vertical.) Determine the equilibrium flow pattern $F^{1}$ from the intersection of the two functions. (The answer for this question follows the next question.) 

Question 1.3 Find the equilibrium flow pattern by solving the equations for $F^{1}$ algebraically. Check to see that your results match the graphical solution. (Remember that $F^{1}$ is determined by specifying both an equilibrium flow volume and a travel time.) 

■ Answers 1.2 and 1.3 The demand equation is 

$$
V = 5, 0 0 0 - 1 0 0 t,
$$

and the service equation is 

$$
t = 1 0 + 0. 0 1 V.
$$

Solving these simultaneous equations, we obtain 

V = 2,000 vehicles/hour, 

$$
t = 3 0 \mathrm{minutes}.
$$

Thus 

$$
\mathsf {F} ^ {1} = (V, t) = (2, 0 0 0, 3 0).
$$

This is shown graphically in figure 1.5. 

■ Question 1.4 The highway department is considering building an alternative link connecting zones 1 and 2. This link would be characterized by the following service function: 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/a9a45185-cfa1-407d-8a96-209400065f95/8bb07930563af2e78c31964d5342ae090cb2032d1adaf9d90339ce0f41a43bf6.jpg)



Figure 1.5 Graphical calculation of an equilibrium flow pattern.


$$
t = 1 0 + 0. 0 0 5 V.
$$

Plot this function on the same set of axes used in 1.2. Find the new equilibrium volume and travel time, graphically and algebraically. Discuss your results. 

Answer 1.4 The new equilibrium flow pattern is $\mathsf{F}^2 = (2,666,23.33)$ . Notice that the new link results in decreased travel time and increased volume. Thus the improved facility has "induced," or "generated," $2,666 - 2,000 = 666$ new users on the link. The result is shown graphically in figure 1.6. 

## 1.5 OTHER ELEMENTS OF PREDICTION

While the prediction of flows is an important part of the prediction of transportation impacts, it is not the whole of it. In section 1.2.1 we identified three major types of interrelations among the basic variables T, A, and F. The first relationship is that in which T and A determine F. As we have just seen, this type 1 relation corresponds to the hypothesis that there is a transportation market in which service and demand reach equilibrium, thus establishing the flow pattern $\mathbf{F} = (\mathbf{V}, \mathbf{S})$ . 

In addition to the type 1 relation, there are also type 2 and type 3 relations to consider. While the prediction of flow patterns is the core of an analysis, it is rarely the sole element of prediction; many other impacts must usually be predicted as well. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/a9a45185-cfa1-407d-8a96-209400065f95/0dc4290d6dc03a6ec351bdba57bac6e2a5af17ad594fb409976386f65da8b491.jpg)



Figure 1.6 Effect of a change in service function on an equilibrium flow pattern.


## 1.5.1 Activity Shifts

We now explore the type 2 relationship: the effect of the current flow pattern in causing, over time, changes in the activity system. To do this we continue the simple graphical example of section 1.3. 

Since it takes time to implement transportation system improvements while population and travel time continue to increase, the demand curve $D^{0}$ may shift upward and to the right, yielding a curve $D^{2}$ , as shown in figure 1.7. The corresponding equilibrium flow $F^{2}$ may be such that the improvement in trip time is even less. 

This shift in the demand curve is, we assume, independent of any change in the transportation system. The forces influencing this shift are external, or exogenous, events such as population growth or changes in the economy. We designate these as E, for exogenous events; the shift in the demand curve will be a function of E. 

The implementation of $T^{1}$ may cause further shifts in demand—for example, the development of residential subdivisions and shopping centers may follow the construction of a new highway, or the development of an industrial city may be a consequence of major rail or port development. Thus the demand curve shifts to $D^{3}$ . (The new equilibrium ( $V^{3}$ , $t^{3}$ ) may actually be such that $t^{3}$ is greater than $t^{0}$ : the level of service over the new system is actually worse than the level of service over the previous system at the initial period. However, it is better than the level of service $t^{2*}$ that would have resulted from the old system $T^{0}$ and the shifted demand function $D^{2}$ .) 

This effect takes place, of course, in the context of exogenous events E. We can represent this chain of effects schematically ( $t''$ being later than $t'$ ): 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/a9a45185-cfa1-407d-8a96-209400065f95/b78cac4ddb7e72f67981dcaf3e22492306ddb39a321e252aeb3da19b8cfc0666.jpg)



Figure 1.7 Activity shifts.


$$
\left(\mathsf {T} ^ {\prime}, \mathsf {A} ^ {\prime}\right) \longrightarrow \left[ \mathsf {F} ^ {\prime} = \left(\mathsf {V} ^ {\prime}, \mathsf {S} ^ {\prime}\right) \right] \longrightarrow \mathsf {A} ^ {\prime \prime}.
$$

We call this the activity-shift relation: the pattern of service at time $t'$ modifies the activity system at time $t''$ . From the point of view of a transportation analysis, the significance is that the demand curve at $t''$ is shifted from that at $t'$ . 

It is often useful to distinguish between these two relationships in the following manner. The type 1 relation involves short-run equilibrium—the pattern of flows that results from a particular activity system. The type 2 relation involves long-run equilibrium—shifts in the activity system itself in response to the flow pattern. We therefore call the type 1 relation travel-market equilibration and the type 2 relation activity-system equilibration. 

## 1.5.2 Resource Consumption

Transportation systems consume resources such as energy, labor, materials and supplies, and land. Even if no change is made to a system, resources are consumed simply to provide service. If changes are made, especially involving major acquisitions of new vehicles or new guideway facilities, then the resources consumed can be quite substantial. Thus, in addition to predicting flows, we should also predict the resources consumed in providing and operating a particular transportation system. 

## 1.5.3 The Operator Decision Loop

The resources consumed are of interest to a variety of groups, but especially to operators of transportation systems. Here we are concerned with how the operators of particular components of the transportation system decide when and how to adjust the transportation options with which they are concerned. 

The structure of this decision is represented by the type 3 relation: the way the actual flows influence decisions concerning transportation options. We do not want to assume away the logic of that decision of what options to implement and thus of what level of service to offer. Rather, we want to isolate the decision variables that are within the control of the operator and include them explicitly in our vector of options. Thus a carrier may determine fares and schedules internally under the criterion of maximizing net revenue, for example. However, a systems analyst would not want to assume that criterion, but would prefer to vary these options—schedules and fares—explicitly. That is, the analyst should deal with the full vector of options explicitly, regardless of which actors have control over particular subsets of options. Then he is in a position to try to identify those options that are within the control of the particular agency or firm for which he is doing the analysis, and to try to anticipate how other options will be manipulated by the actors who have control over them. Since the decisions of other actors may be influenced directly or indirectly, it is important that the decision-making logic of the various actors not be subsumed into the analyst's predictive models. 

Therefore, in our approach to analysis we choose to keep all of the transportation decision options external to the prediction process. That is, we “break the loop” on the type 3 relation and do not model it explicitly, as we do with the type 1 and type 2 relations. 

Of course, there will be some contexts in which it may be useful and desirable to model the operator's decision processes—for example, when an analyst working for one carrier attempts to develop a strategy in the face of competition from other carriers, or when a regulatory agency attempts to influence, through promotion or restriction, the actions of all carriers. In such cases appropriate models can be developed to predict the decisions of specific transport operators (see section 5.7, where we show how assuming an operator decision logic can lead to development of a “supply” function). 

## 1.5.4 Systems of Models

Thus, to predict all significant impacts, five major types of models are required: 

1. Service models are needed to determine, for any specified set of options, the levels of service at various flow volumes. Examples: travel time over a rail link as a function of train length, schedule, roadway conditions, and volume of passengers; volume vs. travel time curves as used in traffic assignment procedures. 

2. Resource models are needed to determine the resources consumed (land, labor, capital, and other direct costs; air, noise, and other environmental impacts; aesthetic and social impacts) in providing a particular level of service with specified options. 

3. Demand models are needed to determine the volume of travel demanded, and its composition, at various levels of service. 

4. Equilibrium models are needed to predict the volumes that will actually flow in a transportation system for a particular set of service and demand functions (short-term equilibrium in the travel market). 5. Activity-shift models are needed to predict the long-term changes in the spatial distribution and structure of the activity system as a consequence of the short-run equilibrium pattern of flows, that is, the feedback effect of transportation on land use (activity-system equilibration). 

These are the five basic components of any system of prediction models in transportation. The interrelationships among them are illustrated in figure 1.8. In addition, it would be desirable also to have models for predicting the changes in organizational and institutional behavior that result from changes in organizational policies. These models, however, are beyond the scope of this volume (see, for example, Allison 1971). 

This structuring of the transportation systems analysis problem incorporates five hypotheses. The first hypothesis is that this is a complete and useful summary of the types of options and impacts. The second hypothesis is that it is meaningful to model transportation technology from two perspectives: in terms of the service perceived by prospective users, reflected in the service functions, and in terms of the resources consumed in providing that transportation service, reflected in the resource functions. The third hypothesis is that it is useful to separate short-term and long-term equilibrium: the short-term re-

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/a9a45185-cfa1-407d-8a96-209400065f95/d5b12407ee3103eda32de7a02dfa93fa53a98de69eb1b9b3868e5947d7a590a4.jpg)



Figure 1.8 Basic prediction models.


sponses of transportation users, in a “transportation market” with the activity system fixed, as represented by the demand functions (the type 1 relation); and the long-term responses of users and others in a larger, more general market, the total economy, as represented by the activity shifts (the type 2 relation). The fourth hypothesis is that a unique equilibrium exists in each of these markets and that it can be found. The fifth hypothesis, which in a sense is the operational test of the second, third, and fourth hypotheses, is that valid predictive models can indeed be constructed. 

## 1.5.5 The Variety of Applications (Optional Reading)

This framework has been applied (implicitly if not explicitly) in a wide variety of analytical activities, including urban transportation planning, intercity passenger transport studies, and national transportation planning in developing countries. 

Urban transportation studies began in Detroit and Chicago in the mid-1950s. The prediction portion of the conventional urban transportation planning process consists of variants of the following sequence (Martin, Memmott, and Bone 1961, Hutchinson 1974): 

1. Project land use, population, and employment changes. 

2. Predict trip ends generated in each zone. 

3. Predict interzonal distribution of trip ends (using gravity or opportunity models). 

4. Predict modal split. 

5. Predict distribution of flows over the proposed network. 

These steps implicitly represent a travel-market equilibration (see chapter 11). 

There are serious internal inconsistencies in this sequence, from the point of view of an equilibrium analysis (Wohl and Martin 1967, Manheim 1970b, 1973b). For example, the estimation of trip ends assumes implicitly a general level of service in the system, whereas the interzonal distribution calculations require an explicit level of service (derived by means of a gravity model, for example). The last step of the process, traffic assignment, predicts an “actual” level of service, or set of travel times, for flows in the network. However, the initial estimates of level of service used for trip generation and distribution are rarely revised to be consistent with the travel times predicted by the traffic assignment. 

In spite of these inconsistencies and other limitations, the structure implicit in conventional urban transportation models is fundamentally that described here. The service functions are represented as volume vs. travel time functions or simply link capacities and travel times. The demand functions are represented by predicting trip ends, interzonal distribution of trips, and then modal split. The travel-market equilibrium model is the “traffic-assignment” process, with the various “capacity-restraint” formulations representing explicit attempts to find equilibrium in the network, given fixed demands. (All-or-nothing assignments are obviously very difficult to justify as a meaningful prediction of “equilibrium” flows.) The resource models are represented in a variety of ad hoc calculations involving such factors as rights-of-way and construction and operating costs. Activity-shift models are sometimes explicit, as when land-use models are used to predict the effects of differential changes in accessibilities on the location of population and economic activities. More often they are left unstated. 

While the conventional urban transportation planning models have serious limitations, a new generation of models is now being developed. These models encompass much improved demand functions and a sounder theoretical basis for explicit travel-market equilibrium analysis (see chapter 11). 

In intercity passenger transport studies, this equilibrium structure has been more explicit. For example, in the Northeast Corridor Transportation Project—the first major intercity study—the system of models used included explicit demand models for passengers and freight (see section 4.3.2); technology models to produce service and resource functions; a network simulator for travel-market equilibration; and activity-shift models for forecasting changes in inter- and intraregional location and intensities of economic activities as a function of changes in transportation and other factors (Bruck, Manheim, and Shuldiner 1967). 

The Harvard-Brookings Model System was designed for use in planning investment in transportation in developing countries (Kresge and Roberts 1971). Several explicit technology models were used for predicting service levels and resource consumption of highways, railways, and other modes and of intermodal transfer points. Demand for travel was derived from a macroeconomic model containing an inter-regional input-output model; these were also used to predict activity shifts. Network equilibrium was found with a modified traffic-assignment approach. 

These examples illustrate some of the applications of the basic concepts. They are very cursory descriptions of highly sophisticated systems of models, and they simply point out how the basic framework outlined above has been applied, implicitly or explicitly, in several major transportation analyses. In each application different practical approximations have been made. 

## 1.5.6 Two Styles of Prediction

The prediction of the future impacts of alternative transportation plans is a difficult task. For plans that involve small changes to an existing system, and impacts in the near future, information about the present system and its effects can play a strong role. In this case it is useful to predict impacts by predicting the magnitudes of the changes from present conditions, leading to a style that we shall term incremental prediction. 

In incremental prediction the analyst knows the present states of the transportation and activity systems— $T^{0}$ , $A^{0}$ —the flow patterns— $F^{0} = (V^{0}, S^{0})$ —and the resources being consumed— $R^{0}$ . For any specified change $\Delta T^{i}$ in the transportation system, the impacts to be predicted are the incremental changes in the various elements— $\Delta V^{i}$ , $\Delta S^{i}$ , $\Delta R^{i}$ , $\Delta A^{i}$ . (These symbols generally represent vectors and may represent variations over time.) 

In synthetic prediction, or simply “prediction,” the analyst predicts the new values of $V^{i}$ , $S^{i}$ , $R^{i}$ , and $A^{i}$ directly. 

The major difference is a practical one. Incremental prediction opens the way for application of powerful approximation methods. It is also good discipline for the analyst's judgments about the magnitudes of changes likely to occur from existing conditions. 

In later chapters we shall often show how short-cut, simplified analyses can be done using incremental instead of synthetic prediction. 

## 1.5.7 Conclusions: The Elements of Prediction

The same basic theory is applicable to every transportation systems problem. Prediction of the impacts of the range of alternative transport plans requires, in general, the whole system of five models for service, demand, equilibrium, resources, and activity shifts. In actually applying the theory to a particular context, however, very different practical methods may be appropriate in different problems. 

The principles presented in section 1.2 and the approach to prediction presented in this section are guidelines, not rigid prescriptions. One element of the art of doing a valid yet pragmatic and relevant analysis is to apply these concepts judiciously. The development of a long-range multimodal plan for an urban region might utilize a set of approximations very different from that of an analysis of next month's schedule changes for a single bus route or the planning of a rail system in a developing country. The practical application of these concepts in a particular context requires understanding of the theoretical basis of the field and of the practical methods available in a specific situation. 

This frames the methodological challenge of transportation systems analysis, which is to conduct an analysis in a particular situation which is valid, practical, and relevant. 

## 1.5.8 Example (continued)

We continue with the example of section 1.4. 

Question 1.5 Often, while new transportation facilities are being planned and constructed, changes occur within the activity system. In our particular case, over the ten-year period of planning and construction of the new link described in question 1.1, the following changes occur in the activity system: 

1. Population and job levels in the two zones increase. 

2. On the average, people now place a relatively higher value on time. 

Assume that the parameters of the new demand function describing the activity system at this future date are 

$a' = 7{,}500$ vehicles/hour, 

$b' = -150$ vehicles/hour per minute. 

i. Compare these values with those given earlier in this section, for the existing conditions. Are they consistent with the activity-system changes described above? Briefly discuss your reasoning. 

ii. Plot the new demand function on the same set of axes as in questions 1.2 and 1.4. Find the new equilibrium graphically or algebraically. Remember which service and demand functions we are now considering. 

iii. What would the travel time over the existing link be if the new one had not been built? 

Answer 1.5 

i. The two demand functions are 

$$
V = 5, 0 0 0 - 1 0 0 t,
$$

$$
V = 7, 5 0 0 - 1 5 0 t.
$$

The demand parameters of the second function are consistent with the described changes within the activity system. Increases in population 

The Challenge of Transportation Systems Analysis and job levels tend to increase the potential demand as expressed by parameter $a'$ . As time is valued more dearly, the unit change in demand (for each unit of travel time) will increase. Thus b, which measures the sensitivity of demand with respect to travel time, becomes more negative as people value time more dearly. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/a9a45185-cfa1-407d-8a96-209400065f95/9e7665385d69caea2e3f7cd295b3261f19021a95bdf6c39fdde621acfc548b60.jpg)



Figure 1.9 Effect of activity-system changes.


ii. Solving algebraically: 

Demand: 

$$
V = 7, 5 0 0 - 1 5 0 t,
$$

$$
t = 1 0 + 0. 0 0 5 V.
$$

Thus 

$$
\mathsf {F} _ {3} = (V, t) = (3, 4 3 0, 2 7. 1 5).
$$

Comparing this result to those of question 1.1, we see that both travel time and volume have increased. Referring to figure 1.9, we see that our equilibrium point has moved along the service curve because of the shift in demand. 

iii. From the plot or algebra, 

$$
\mathsf {F} _ {4} = (2, 4 0 0, 3 4).
$$

Question 1.6 There are many examples of facilities being outdated from their very first day of service. For example, the Long Island 

The Challenge of Transportation Systems Analysis 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/a9a45185-cfa1-407d-8a96-209400065f95/54d094d40b15763c58d7790035ab1b9fa57cec1da37821521b70ce8d00aad186.jpg)



Figure 1.10 Effect of the introduction of a new highway.


Expressway was congested soon after it was opened (Caro 1974, p. 949). In fact, it is observed that travel times can increase on supposedly new, improved facilities. Discuss this phenomenon with reference to figure 1.10. 

i. Specifically, identify the functions that represent the old facility (highway), the new, improved facility, the old activity system, and the new activity system. 

ii. Describe the relative magnitudes of the equilibrium volumes and travel times for the old and new systems. 

iii. An irate traveler was quoted as saying, "Look, since they've built the new highway my trip time is worse than ever. I haven't derived any benefit from this road." Study the figure. Do you agree that the new road has made things worse for society? Ponder seriously, but comment only briefly. 

## Answer 1.6

i. The old facility is represented by function 2, the new facility by function 1, the old activity system by function 3, and the new activity system by function 4. 

ii. Referring to the figure, it can be seen that the new equilibrium flow is $(V_{A}, t_{A})$ . Both travel time and volume are greater than the old equilibrium flow pattern $(V_{D}, t_{D})$ . 

iii. As paradoxical as it may seem, it must be concluded that users have benefited from the new system. Consider that most trips are made for useful purposes (on urban highways, for example, we find that most trips are for work, shopping, school, or recreation). If a new system induces greatly increased travel, we can only conclude that more people are traveling to work, shopping centers, schools, and social functions. From the viewpoint of users, we see that more people are making more trips and thus deriving more benefits from the new highway than from the old. The increased travel time is an unfortunate by-product of urban growth. Of course, key questions are: What costs were incurred in order to build this new facility? What would have occurred if the facility was not built? Who benefited and who was hurt by the new facility? 

It should be stressed that travel demand and changes in land use are not independent of changes in transportation systems. Often new highways spur tremendous growth in residential and industrial land use. For example, the Long Island Expressway brought about a tremendous growth in residential areas of Long Island. And Route 128 in the Boston area precipitated an industrial migration as large firms found it more profitable to locate in suburban areas (served by the new road) than in a downtown business district. Thus new highways can create jobs and spur residential land development. These benefits are often difficult to measure directly but can have great effects on society. 

## 1.6 PUTTING PREDICTION IN CONTEXT

So far, in discussing options, impacts, equilibrium analysis, and model systems, we have been relatively abstract. What implications can we draw from this discussion? What steps should we go through in order to analyze a particular transportation system problem? 

## 1.6.1 The Analysis Cycle

We start with a particular transportation system plan. This plan proposes certain transportation and activity systems described as sets of options. To assess the impacts of this plan, we must predict the flow pattern that will occur if it is implemented, that is, the short-run equilibrium of the transportation market and the long-run equilibrium effects of transportation on the location and character of social and economic activity. These predictions require a system of five models describing service, demand, equilibrium, resources, and activity shifts. 

Thus the core of the transportation systems analysis problem is prediction of the impacts of a particular plan using a system of equilibrium models. Prediction is concerned with anticipating the consequences of alternative plans: What impacts will each alternative have? On 

The Challenge of Transportation Systems Analysis whom will they fall? For a particular pattern of available transportation services, what will be the flows? How will each alternative affect the evolution of the activity system? 

But how did we get the plans in the first place? There must have been some kind of process by which a variety of possibilities were quickly examined and discarded, until some reasonably good candidates emerged. This is the search process—the generation of alternatives sufficiently well-defined to be tested in prediction. The search process may be algorithmic (a linear-programming procedure, for example) or completely intuitive (an analyst proposing a change in services or prices, or a designer sketching a network on a map) or some mixture of the two extremes. The questions one must ask in this process are: What possibilities for intervention are there? What aspects of the transportation system might be modified or improved? What alternative actions should we examine? What actions are most likely to achieve the objectives desired? 

Once one or several alternative plans have been generated through some search procedure, and the impacts have been predicted using the system of prediction models, the next task is to evaluate those impacts, compare the predicted impacts for the various alternatives, and arrive at a judgment as to which alternatives are preferred, and why. Evaluation and choice are the activities through which the predicted consequences of alternative actions are distilled and weighed, to reach a decision on a course of action. They involve such questions as the following: What impacts would be most desirable? Which of the al-

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/a9a45185-cfa1-407d-8a96-209400065f95/7a31cf6257e648152189fbe45d4292e8505de2fe0f70add678bdaa61222f8a01.jpg)


b Analysis cycle 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/a9a45185-cfa1-407d-8a96-209400065f95/6d5142a518ea68f0f82c3902ead8b8b7bf0cdcdd5540bdf5dd292dc0ba039fe8.jpg)



Figure 1.11 Prediction in the larger process.


The Challenge of Transportation Systems Analysis ternative actions would be most desirable? Whose points of view should be considered in reaching a decision? What should be the process of reaching a decision? Which alternative should be implemented? 


The Challenge of Transportation Systems Analysis


Figure 1.11 brings out the interrelations of these activities. Part b of the figure emphasizes the iterative nature of the process: after evaluation and choice, there should be the option of recycling to search again, one or more times, generating and evaluating a succession of alternatives. This iterative process may proceed until a desirable alternative is found or until the available resources (dollars, time) are exhausted. 

## 1.6.2 Analysis and Implementation

Of course, even this view of the process of analysis is limited, and we must embed it in a yet larger picture. This is shown in figure 1.12, in which several additional distinctions have been made: 

1. A setup phase precedes the technical analysis. In order to do the prediction, the system of models must be developed: data must be collected, initial goals formulated, and substantial development activity must occur in order to produce appropriate service, demand, and other models. The analysis and setup phases must be planned. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/a9a45185-cfa1-407d-8a96-209400065f95/d9b7cfc4b8bd9822fffa20973e0d6c53e221c358a1f920899d2a2d28565c0204.jpg)



Figure 1.12 The continuing analysis process—Image 1.


2. The technical-analysis phase includes not only search, prediction, and evaluation and choice, but also a goal formulation and revision task. Initial statements of objectives must be formulated in the setup phase to provide guidance for the development of models and data collection. At the start of analysis these goals are revised to provide guidance for search and a basis for evaluation and choice. However, it is to be expected that, as the transportation analysts learn about the problem by iterating through search, prediction, evaluation, and choice, goals will be revised and refined (Manheim 1970a). 

3. Transportation systems analysis is rarely conducted in a vacuum. There is usually a purpose to the analysis: to come to a conclusion as to a desirable course of action to be implemented in the real world. Therefore, we show an implementation phase following the technical analysis. 

The central idea behind this figure is that transportation systems analysis is a dynamic activity. For existing systems, analysis of alternative options is a continuing task. For systems being expanded or built new, it must be recognized that change takes time. It may take many years to implement fully a particular course of action—building a highway or an airport, restructuring the routes and services of a transit system or an airline, building a major new freeway or transit system—even after it has been adopted in principle. 

Many transportation analyses are still being set up as “one-shot” activities: do a study, recommend a course of action, and disappear. However, it is now becoming more widely recognized that a truly effective transportation systems analysis must be a continuing activity because of the long time period for implementation. As implementation of the recommended action gets under way, the actual impacts should be observed and compared with the predictions. Simultaneously, changes in technology, in demand, and in values should also be monitored. Based upon this new information, the analysis and even setup phases should be recycled, to adapt the previously recommended action to changing conditions. 

## 1.6.3 The Product of Analysis

To emphasize the continuous nature of the task, the relation of analysis and implementation might be visualized as in figure 1.13. Here we emphasize that actions are implemented periodically, leading to system changes. The system evolves over time, influenced partly by internal dynamics (the interactions of transportation and activity systems) and partly by actions taken deliberately as a result of analysis. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/a9a45185-cfa1-407d-8a96-209400065f95/557b801d554ce378c775f9bb4b568846135558c91d1acb4cc4375c80e6fce673.jpg)



The Challenge of Transportation Systems Analysis


The synthesis of the images of figures 1.12 and 1.13 can be described in terms of the product of analysis, the multiyear program plan (MYPP) shown in figure 1.14. The MYPP reflects the view that the product of analysis is a program of actions staged over an extended period, which might range up to perhaps twenty-five years. The outcome of the first period of the plan is firm and detailed: it is the set of specific implementable actions that will be taken in the next period. That is, inclusion of an action in the first period of the MYPP represents a decision to implement that action in the next period. That first period may be a year in the case of a regional or national planning agency, or a quarter (three months) in the case of an operator such as a transit agency or airline. Each succeeding period of the plan is less firm and less detailed. The actions in the first few periods (up to year three or five) of the MYPP constitute the “Short-Range Plan”; those further off (say, in years six to fifteen), the “Midrange Plan”; and later actions (say, in years sixteen to twenty-five) the “Long-Range Plan.” These time periods may be shorter or longer in different organizational contexts. For example, for an airline the short range may be three to six months, the midrange six to twenty-four months, and the long range two to five years. 

The MYPP contains all significant transportation actions proposed for the system. For a region these would cover all modes and all types of transportation and related options: changes in facilities, in vehicle fleets, in operating policies (routes, schedules, fares, classes of services, restraint and other disincentive policies), in organizations and institutions, and in transportation-related actions (staggered work hours, land-use controls, sewer and water policies). For a private carrier such as a trucker or an airline the actions would be more restricted, such as changes in vehicle fleets, routes, schedules, and services. 

The MYPP also includes a listing of studies to be undertaken. These actions are as important as implementation actions because they influence, and sometimes constrain, the implementation actions that can be seriously considered in future years—you cannot consider implementing a major new service strategy next year if you didn't do some homework on it this year. 

The MYPP logically should have different degrees of detail for different types of actions. The MYPP for a region such as a metropolitan area or state may contain component MYPPs for various subregions. Different levels of detail would be appropriate for different levels of geographic aggregation. The MYPP for a county or medium-sized city would be more detailed than that for a state. The state MYPP would summarize in a single item what might be a large number of specific actions in a county MYPP. Similarly, the MYPP for an operator's system may contain MYPPs for portions of the system. 

<table><tr><td rowspan="2">Action</td><td colspan="4">Year</td></tr><tr><td>1 Implement</td><td>2 3 4 5 Short range</td><td>6 ... 15 Midrange</td><td>15 ... 25 or 30 Long range</td></tr><tr><td>Implementation</td><td></td><td></td><td></td><td></td></tr><tr><td>Facilities: New Improvements</td><td></td><td></td><td></td><td></td></tr><tr><td>Vehicles</td><td></td><td></td><td></td><td></td></tr><tr><td>System operating policies (including pricing)</td><td></td><td></td><td></td><td></td></tr><tr><td>Organization</td><td></td><td></td><td></td><td></td></tr><tr><td>Transportation-related activity-system actions</td><td></td><td></td><td></td><td></td></tr><tr><td>Studies</td><td></td><td></td><td></td><td></td></tr><tr><td>Planning</td><td></td><td></td><td></td><td></td></tr><tr><td>Design</td><td></td><td></td><td></td><td></td></tr><tr><td>Monitoring</td><td></td><td></td><td></td><td></td></tr><tr><td>Evaluation</td><td></td><td></td><td></td><td></td></tr><tr><td>Research</td><td></td><td></td><td></td><td></td></tr><tr><td>Costs</td><td></td><td></td><td></td><td></td></tr><tr><td>Category A</td><td></td><td></td><td></td><td></td></tr><tr><td>Category Z</td><td></td><td></td><td></td><td></td></tr></table>


Figure 1.14 The transportation multiyear program plan (Manheim 1977a).


A sample MYPP for a particular region is given in figure 1.15. 

Where decisions on actions to be taken in future years have not been made yet, or are contingent on alternative outcomes of earlier actions, the MYPP can show these. For example, unresolved issues can be included or explicit contingencies shown, as in figure 1.15. 

The MYPP must be reviewed periodically and revised according to an explicit decision process in which progress in implementing actions in the first period of the preceding year's MYPP is reviewed. Obviously, not all elements of the MYPP would be subject to the same degree of scrutiny in each review cycle. For example, the long-range portion of the MYPP might be revised in a major way only once every three or five years, or when a decision is to be taken on implementing a major project in the next year. 

In the periodic decision process, some of the actions in the second year of the preceding year's MYPP may be advanced into the first year of the new MYPP, reflecting decisions to implement those actions; others may be deferred for implementation or may be discarded altogether. This reflects the fact that while the MYPP lays out planned future actions, in actuality the only firm decision is an implementable one: how to spend next year's dollars. Since actions indicated in the MYPP are never certain of implementation until they move into the first year of a current MYPP, an important issue in choosing an action for implementation in a given year is its degree of "commitment" versus "flexibility": If this action is implemented, which future options will be foreclosed, and which will remain open for future implementation? 

## 1.6.4 Implications for Analysis

Designing an analysis thus involves more than just developing a prediction model. The analyst must develop a strategy for analysis that includes plans for the full range of necessary technical activities: 

1. What data should be collected? 

2. What models should be developed? 

3. How should the tasks of search, prediction, and evaluation and choice be organized into a coherent process? 

NORTH CORRIDOR 

North Dawson Transit (Express Bus)
Transit Parking
Dawson Transit Parking
West Dawson Transit (Express Bus)
Ramp Metering Rt. 70
Riverside Transit
Riverside Transit Parking
Bell Creek Transit Parking
Bell Creek-Jackson Transit
Exclusive Bus Lanes Rt. 10
Transit Coordination
Weston Transit
Central County Transit
Dial-A-Bus Demo. Transit
Toll Bridge Metering 


CENTRAL CORRIDOR


Local Transit Study
Parking for Rapid Rail
Airport Access
Ramp Metering Rt. 15
West Bridge Transit (Express Bus)
Jackson Corridor Transit 


SOUTH CORRIDOR


Tremont Transit
Tremont Rapid Rail Parking
East Bridge Transit (Express Bus)
Tri-Cities Transit 

0 

## REGIONAL POLICY CHANGES

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/a9a45185-cfa1-407d-8a96-209400065f95/ed2064c216c69f72d88fd34a2b15a3481eb5b003de73709dd3955b726d33f3e4.jpg)



Transit Fare Coordination
Parking Surcharge
Transit Public Information Program
Car Pooling Program


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/a9a45185-cfa1-407d-8a96-209400065f95/979859fdaa1948ec56991527acaabfa36a36114cc7a3856e818e4e801e4fb528.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/a9a45185-cfa1-407d-8a96-209400065f95/c09f10827b3897f957836c90bff2eacd3e30e2d575da2cad72428b4944e1a1ca.jpg)



Figure 1.15 A sample multiyear program plan (Manheim et al. 1975b, based on Neumann 1976).


4. How should technical activities interface with the political process?
5. What should be the nature of the continuing analysis and implementation process? 

## 1.6.5 Systematic Analysis

The general structure of a systematic analysis is illustrated metaphorically in figure 1.16: the options T are varied systematically over a range, and the impacts on various interests—here, users, operators, and government—are traced out as T is varied. For example, it is often especially important to explore trade-offs among various types of options—increasing frequency of service versus reducing fares to increase ridership; changing the relative mix of resources expended on new facilities as opposed to operating expenses and improvements in existing facilities; or changing the relative mix of expenditures on various modes. 

Of course, the prediction of impacts for each T requires use of the system of prediction models. Practically, therefore, the metaphor may be difficult to apply in some situations. As we shall demonstrate in later chapters, however, a systematic analysis can be achieved in most situations. Practical strategies involve careful design of the iterations of the basic analysis cycle of search-prediction-evaluation to trace out trade-offs. 

## 1.6.6 Analysis and the Political Process

To intervene effectively in the fabric of society and bring about change through the implementation of a transportation system plan, the analyst must have a perspective on the relation between analysis and the political process. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/a9a45185-cfa1-407d-8a96-209400065f95/5cf339542893fa4e3d6fd530d18ab5ad21db5cfe8b8be726b326e0a89d4240f1.jpg)



Figure 1.16 The general structure of a systematic analysis.


The transportation systems analyst usually operates in a complex institutional environment, whether public or private. In such an environment there are usually many different groups that will have an interest in the outcome of the analyst's work, and they will all have different ideas about what it is desirable to achieve with transportation. Typically, also, there are many different institutions involved. 

To be useful, analysis must be relevant to the issues with which these institutions and interest groups are concerned (or are likely to be concerned), and must clarify the issues in ways that contribute to the constructive resolution of potential conflicts and to the making of implementable decisions by responsible decision makers. 

With this view, and with the definition of systematic analysis in the preceding section, we see that our definition of the methodological challenge of transportation systems analysis (section 1.5.7) needs to be broadened, by adding the concepts of "systematic analysis" and "clarification of issues": The methodological challenge of transportation systems analysis is to conduct a systematic analysis in a particular situation which is valid, practical, and relevant, and which assists in clarifying the issues to be debated. 

In responding to this challenge, the analyst must be concerned with many basically different kinds of activities. Our focus in this book will be primarily on prediction, with some attention to evaluation. As a result of this concentration, we shall develop a rather abstract, technical view of transportation systems analysis. This is necessary in order to foster the understanding of fundamentals that is essential to doing good analysis. But it must be kept in mind that transportation systems analysis must be rooted in the complexities of social and political reality. Ultimately we must return from the delights of abstract analytics to the realities of social and political issues and forces. 

Successful response to the challenge requires deep understanding, not only of the theory and techniques of prediction, but also of search, evaluation, choice, the structuring of a process of analysis, and, most importantly, the social, economic, and political context in which an analysis is being conducted. 

## 1.7 SUMMARY

We live in a world of rapid change—change in transportation technology, in transportation demand, and in the values, public and private, 

48 The Challenge of Transportation Systems Analysis that will influence decisions about transportation systems. The challenge of transportation systems analysis is to use the transportation system to help a society achieve its goals. Therefore, analysis must be a continuous process. Setup, technical analysis, and implementation must be continuously iterated and adjusted to changing conditions, with the adopted course of action revised appropriately. 

At the core of this process is the prediction task: based upon the current understanding of the mechanisms of interaction between transportation and activity systems, a set of models is developed and used to predict the impacts of proposed courses of action. The heart of this prediction of impacts is the prediction of flows in networks, based upon service–demand equilibrium concepts. Although simple in concept, prediction is a major technical task. 

It is this task of prediction to which we turn first in the following chapters. Though the discourse will become highly technical and somewhat abstract, it is important that the reader keep in mind the broader context in which these techniques are embedded. 

## TO READ FURTHER

For further discussion of the interrelation of transportation and activity systems, see S. B. Warner (1962) and Meyer, Kain, and Wohl (1965). The best sources of information on current transportation issues and news are newspapers, news magazines, and industry-oriented publications such as Railway Age, U.S. Transport, Mass Transit, and Aviation Week and Space Technology. 

## EXERCISES

1.1(C) Select a current transportation issue that interests you and that involves the transportation services of a particular region or operator. Identify the key elements you think should be included in an analysis of this issue, such as: 

a. major options to be analyzed 

b. major impacts to be predicted 

c. major flow types 

d. service attributes 

e. prediction procedures 

f. possible search procedures 

g. what the choice process might be like. 

1.2(P) Select a transportation study for which you have adequate documentation (a final report, environmental impact statement, or an internal staff study). 

The Challenge of Transportation Systems Analysis a. Summarize concisely the key issues that the study seems designed to address. 

b. Identify the key elements of the study: 

i. system considered (refer to the system principles in section 1.2) 

ii. options and impacts considered 

iii. flow types considered (passengers and/or commodities) 

iv. service attributes considered 

v. prediction procedures used (demand functions, activity-shift functions, service and resource functions, travel-market equilibration, operator and activity-system equilibration procedures) 

vi. search procedures and evaluation procedures 

vii. choice process 

viii. assumptions about exogenous events. 

c. Discuss the study elements: 

i. Does the system definition seem appropriate to the issues? If not, why not? 

ii. Do the options and impacts seem appropriate? If not, why not?
iii. Continue the discussion with other elements identified in part b. 

1.3(P) Choose two of the following contexts: air carrier, trucking company, shipping company, port authority, national highway agency. a. What are the major types of options that might be considered by this organization? 

b. Sketch out a hypothetical multiyear program plan for this organization. 

c. What would be the basic features of the prediction models required to predict the impacts of this MYPP? 

1.4(E) In railroad operations there is substantial debate about train length. In a particular market longer trains reduce crew costs. On the other hand, by operating more frequent, shorter trains, “railroads incur greater crew costs, but obtain better service and improved freight car utilization. Furthermore, short trains can be handled more easily at yards, at sidings, and on the line than long trains. In some instances, however, running more short trains could cause operating delays on congested portions of the system” (Martland, Assarabowski, and McCarren 1977). Consider the situation of a 200-mile segment of rail line on which the present operating policy is to run two trains per day with 90 cars each, or a total capacity of 180 cars per day: 

$$
\mathbf {T} ^ {0} = (Q ^ {0}, L ^ {0}) = (2, 9 0),
$$

where 

$$
Q = \text { frequency   (trains   per   day) },
$$

$$
L = \text { train   length   (cars   per   train) }.
$$

The cost per train in dollars is (after Martland 1977) 

$$
C _ {\mathrm{TRAIN}} (Q, L) = 2. 4 0 \frac {L}{Q} + (4 8 0 + 1. 3 3 L + 0. 0 0 4 L ^ {2})
$$

or, for a day's schedule of Q trains, 

$$
C _ {\mathrm{DAY}} (Q, L) = Q C _ {\mathrm{TRAIN}} = 2. 4 0 L + Q (4 8 0 + 1. 3 3 L + 0. 0 0 4 L ^ {2}).
$$

The total capacity available in cars per day, $V_{C}$ , is 

$$
V _ {\mathrm{c}} = Q L.
$$

Operating management believes that the following demand function applies in this corridor ( $V_{D}$ is demand volume): 

$$
V _ {\mathrm{D}} (Q, L) = 1 8 0 \left(\frac {Q}{Q _ {0}}\right) ^ {\beta};
$$

a "best estimate" of $\beta$ is 0.5. 

Management's objective is to increase net revenue, $I_{\mathrm{NR}}$ , where 

$$
I _ {\mathrm{NR}} = I _ {\mathrm{GR}} - C _ {\mathrm{DAY}}
$$

and gross revenue, $I_{GR}$ , is a function of equilibrium volume $V_{E}$ and price P: 

$$
I _ {\mathrm{GR}} = V _ {\mathrm{E}} P.
$$

At present P = $15 per carload for freight over this segment. 

a. Consider the possibility of adding 1, 2, or 3 more trains per day, maintaining the same train lengths. Predict the equilibrium flows and the corresponding costs and revenues for these strategies. Which of these strategies ( $T^{0}$ , $T^{1}$ , $T^{2}$ , $T^{3}$ ) would you recommend to management, and why? 

b. If your objective were maximum service to users, which would you recommend, and why? Compare with your answer to part a and discuss. 

c. For a given frequency, what are the advantages and disadvantages of varying train lengths? If you knew that for a frequency $Q^{i}$ the demand would be $V^{i}$ , what train length would you recommend? 

d. Consider these alternative strategies: $T^{4} = (Q^{4} = 3, L^{4} = 75)$ , 

$$
\mathbf {T} ^ {5} = (4, 7 5), \mathbf {T} ^ {6} = (5, 7 5), \mathbf {T} ^ {7} = (4, 7 0), \mathbf {T} ^ {8} = (5, 7 0), \mathbf {T} ^ {9} = (5, 6 0).
$$

Which of these would you recommend from the operator's perspective? for $Q = 4$ ? for $Q = 5$ ? Which of the ten strategies $T^0 - T^9$ would you recommend from the operator's perspective? from the user's perspective? Discuss. 

e. Using your result to part c, find the train length $L_{OPT}$ that is best from the operator's perspective for each frequency Q = 3, 4, 5, and predict the impacts of the corresponding strategies. Plot the results on axes defined by $V_{D}$ and $I_{NR}$ and discuss. Which would be best from the operator's perspective? from the user's perspective? Why? Which would you recommend, and why? 

f. How might the results change for $\beta = 0.2 ? \beta = 0.8 ?$ (Check only for $L = L_{OPT}$ for this range of frequencies.) 

g. Critique the assumptions (implicit and explicit) of this formulation of the problem: Under what conditions, and to what extent, do you think they would be reasonable? (For example, what do you think of the explicit assumption that demand is independent of the train length?) 

1.5(E) The country of Freelandia gained independence a few years ago and is mounting a major effort to promote new agricultural development in previously underdeveloped regions. A trucking operator in the town of K has previously been providing only local service. Now that a new major agricultural development program is under way, this operator is considering providing farm-to-market service to carry agricultural and other natural products from their origin in locality M to market at K. The distance is 150 miles (one way), with no intermediate major settlements. 

After discussions with the local agents of the producers at M, the trucker estimates that the demand function for shipments from M to K is 

$$
V = Z + a _ {0} Q - a _ {1} P,
$$

where V is volume in tons per week, Q is frequency of shipments (per week), P is price charged per ton, and $a_{0}$ , $a_{1}$ , and Z are parameters. Based upon an average traveling speed of 30 miles per hour, plus a loading or unloading time of 3 hours at each end, he estimates that he can manage at the most one round trip every two days, so Q = 3 per week. He also figures that his costs are related to the mileage he drives per year: his total cost per year is 

$$
C _ {\mathrm{T}} = b _ {0} + b _ {1} m _ {\mathrm{T}},
$$

where $m_{T} = 300Q$ is the total round-trip mileage driven and $b_{0}$ and $b_{1}$ are parameters. The truck carries 15 tons. He is considering offering an initial frequency of 1 or 2 trips per week at a rate of $25.00 or 

30.00 per ton. Assume $b_{0} = 270$ , $b_{1} = 0.50$ , $Z = 25$ , $a_{0} = 13$ , $a_{1} = 1$ . 

a. For these four combinations of frequency and price, what would be the tonnage carried, the gross revenues, the total cost, and the net revenue? 

b. Which of the four options would be preferred by the operator if his objective where to maximize net revenue? to minimize costs? to maximize volume carried? Which option would be preferred by users (shippers)? Can both interests get their first choice simultaneously? If not, why not? 

c. For the proposed service the predominant movement is from M to K; the amount of freight to be carried in the reverse direction is negligible. There is a possibility of picking additional cargo at D to go to M; this would incur a detour of 100 miles additional but could result in an additional load and source of revenue. Would it be profitable for this operator to make the detour? Discuss qualitatively. 

1.6(E) A railroad operator utilizes a fleet of 2,000 freight cars for service to a particular group of shippers, who produce grain. At present train schedules are poorly coordinated. Because service is unreliable, shippers take an excessive amount of time to load and unload the cars, with the result that an average car delivers n = 10 carloads per year (that is, the cycle time is $t_{c} = 365/10 = 36.5$ days). 

The cost of owning a railroad car is $2,000 per year (equivalent annual cost). At present shippers are charged $p = \$1,200$ per load, and the operating costs (excluding ownership) are $a = \$1,100$ per load. 

The service now runs at a loss. Management is considering three options: (A) increase rates; (B) improve schedule coordination and other aspects of operation so that service is more reliable, delivery times are shortened, and shippers load and unload cars more quickly; or (C) do both of the above. The marketing staff has come up with the following approximate demand function showing the effect on total carloads V of a change in rates, in cycle time, or in both: 

$$
\frac {\Delta V}{V _ {0}} = \alpha \frac {\Delta p}{p _ {0}} + \beta \frac {\Delta t _ {\mathrm{c}}}{t _ {\mathrm{c} 0}}.
$$

a. Assume $\alpha = -0.4$ , $\beta = -1.2$ , $V_0 = 2,000 \times 10 = 20,000$ . Predict the new volume $V'$ for (A) $\Delta p = +\$100$ ; (B) $\Delta t_c = -4.5$ days; and (C) both. 

b. Assuming that the fleet size stays the same, predict for each option the increase in annual revenues from shippers (Vp), the increase in 

operating costs (2,000na), and the change in net operating revenue (Vp - 2,000na). Which option would you recommend? 

c. Which option would you recommend if the cost of implementing option B turned out to be equivalent to an increase in operating costs to $a = \$1,200$ per load? 

d. Do a sensitivity analysis for the assumed demand parameters, using $\alpha = -0.8$ and -1.2; $\beta = -0.4$ and -0.8. Discuss. 

1.7(E) A marine operator presently offers service between ports $A$ and $B$ , 6,000 miles apart, utilizing a single ship. At an equivalent land speed of 20 miles per hour (ship speeds are usually expressed in nautical miles or knots), the total sailing time for a one-way voyage is 300 hours or 12.5 days. The average time spent loading or unloading cargo in either port is two days, so the average one-way trip time for the ocean voyage for a cargo is $12.5 + 0.5(2 + 2) = 14.5$ days. The round-trip time is thus 29 days. For a “working year” of 330 days (allowing time for periodic maintenance), the effective frequency is $330/29 = 11.4$ round trips per year. The ship’s capacity is 15,000 tons of cargo; the rate presently charged is $25 per ton. The average cost of a one-way trip is $225,000 per voyage, or $15 per ton of available capacity. 

The operator estimates that the demand function in this market is 

$$
V = Z _ {0} - \alpha t _ {\mathrm{iv}} - \beta / Q - \gamma c,
$$

where 

V = round-trip volume in tons per year 

$$
Z _ {0} = \text { market   size   factor }
$$

$$
t _ {\mathrm{iv}} = \text { one - way   trip   time }
$$

$$
Q = \text { frequency   in   round   trips   per   year }
$$

c = freight rate in dollars per ton 

$$
\alpha , \beta , \gamma = \text { parameters }.
$$

His estimates of the parameters are $\alpha = 19,500$ , $\beta = 3.1 \times 10^{6}$ , $\gamma = 8,000$ , and $Z_{0} = 982,680$ . The average volume per voyage is 20,000 tons. 

a. Are his estimates of the parameters consistent with this volume? What fraction of available capacity is utilized per voyage? What is his gross revenue (receipts from rates paid), total cost, and net revenue (gross revenue less total cost) per voyage? 

b. The operator is considering replacing the present ship with a newer vessel, which would have a speed of 24 miles per hour, thus cutting the one-way sailing time to 10.4 days. The cost per voyage of this newer, faster ship would be $250,000 per one-way trip. The capacity and loading/unloading times would be the same. Would this ship be more attractive to the operator: (i) if frequency and rate remained the same? (ii) if the frequency were increased to take advantage of the increased speed but the rate remained the same? (iii) if the frequency were increased and the rate increased to $30.00 per ton? Summarize and discuss your results: What consequences can a change in vehicle speed have? Discuss the significance of the parameters $\alpha$ , $\beta$ , and $\gamma$ . 

c. After doing this analysis, the operator suddenly realizes that he has ignored a fundamental principle: the time that will influence shipper's decisions (that is, the demand function) should be the total door-to-door time, not just the trip time on the ocean leg. He estimates that an average shipment spends about six days in the land portion of the trip, for a total travel time of 20.5 days. How might this affect his estimates? (Discuss qualitatively.) 

1.8(E) A railroad runs from $A$ to $B$ , a distance of 500 miles, through mountainous terrain. The present one-way travel time (including time at intermediate yards) is 20 hours, and the rail freight rate is $20 per ton. There is a truck service which competes with the railroad, running over roughly parallel roads for approximately the same distance, at an average speed of 30 miles per hour and at a rate of $30 per ton. A new highway is planned to replace the existing road; while there is some auto traffic, it is expected that most of the traffic will be trucks. The service function of the new facility is $t_{\mathrm{T}} = t_{0} + bV_{\mathrm{T}}$ , where $V_{\mathrm{T}}$ is the total volume in trucks per hour (the anticipated auto usage is negligible), $t_{0} = 10$ hours, $b = 0.08$ hour per truck per hour. The railroad's estimate of the demand function is 

$$
\frac {V _ {\mathrm{T}}}{V _ {\mathrm{R}}} = a _ {0} \left(\frac {t _ {\mathrm{T}}}{t _ {\mathrm{R}}}\right) ^ {a _ {1}} \left(\frac {\boldsymbol {c} _ {\mathrm{T}}}{\boldsymbol {c} _ {\mathrm{R}}}\right) ^ {a _ {2}},
$$

where $t_{T}$ and $t_{R}$ are the trip times by truck and rail, respectively, $c_{T}$ and $c_{R}$ are the rates, $V_{T}$ and $V_{R}$ are the volumes, and $a_{0}$ , $a_{1}$ , and $a_{2}$ are parameters. The total volume is likely to remain constant at $V_{TOT} = V_{T} + V_{R} = 200$ truckloads per hour. The rail system is utilized at only a fraction of capacity, so its service function is flat—travel time is constant independent of volume. 

a. If $a_{0} = 1$ , $a_{1} = -1$ , and $a_{2} = -2$ , find the present volumes (mode split) of truck and rail. 

b. Make an approximate estimate of the equilibrium flows if the new highway were built. (Hint: Try a range of truck volumes in a trial-and-error approach.) 

c. What would the equilibrium flow be if the railroad dropped its rates to $15 per ton? if truckers were taxed $5 per ton to help pay for the new highway? if both changes occurred? Discuss. 

d. Discuss the advantages and disadvantages of the new highway from the perspectives of each of the major affected interests. 

e. A regulatory commission is examining the question of rates. The railroad is arguing for a truck rate of $35 per truckload, while the truckers are arguing for a rate of $30. What would be the corresponding equilibrium volumes? Why is each interest advocating the particular rates indicated? 

1.9(E) An urban expressway presently carries a peak traffic volume of 2,200 vehicles per hour over three lanes in the peak direction. A simple, approximate service function for this facility is 

$$
t = t _ {0} + b \frac {q}{k q _ {\mathrm{c}}},
$$

where k is the number of lanes, $q_{c} = 1{,}200$ vehicles per hour per lane, q is the total one-way flow volume in vehicles per hour ( $q \leq 0.95kq_{c}$ ), b = 3, and $t_{0} = 2$ minutes per mile (see section 7.6). One bus is considered equivalent to about 1.6 automobiles, and the flow stream in the peak hour includes about 60 buses. The demand function for bus transit usage in the corridor is 

$$
V _ {\mathrm{B}} = V _ {0} - a t _ {\mathrm{B}},
$$

where $t_{B}$ is bus travel time in minutes, $V_{0} = 4{,}200$ people per hour, and a = 75. 

a. What is the present travel time for buses and automobiles over the eight-mile expressway? Show that the ridership on the 60 buses is $V_{B} = 1{,}982$ persons per hour. 

b. It is proposed that one auto lane be replaced by a lane for exclusive use of buses, with semipermanent barriers such as rubber cones between the bus and auto lanes. If the number of buses in the peak hour remained the same, what would their travel time be? (Assume no en route stops and no congestion for buses at exit ramps.) What would be the equilibrium volume of passengers using buses? If the maximum capacity of the buses were 50 passengers, would they be crowded? 

c. How would the automobile travel times change if one lane were set aside for the exclusive use of buses? 

d. What assumption is made in this model about the influence of automobile travel times on bus ridership? If you relaxed this assumption, how might the results change? 

## 2.1 INTRODUCTION

The basic concern of transportation systems analysts is to be able to anticipate the consequences of any proposed change in a transportation system. In chapter 1 a basic framework for prediction was presented. This framework focused on the interrelationships between transportation and the socioeconomic activity system, and three basic types of interrelations were identified. In this chapter we shall deal with two of these interrelations: first, that between the pattern of social and economic activities and the short-run demand for transportation; and second, the influence of transportation upon the long-run distribution of social and economic activities. Thus our purpose in this chapter is to explore the behavioral aspects of transportation—the activity system and the way we represent it for the analysis of transportation systems. 

## 2.2 THE NEED TO UNDERSTAND HUMAN BEHAVIOR

## 2.2.1 The Effects of Transportation on Social and Economic Activity

Transportation has always played an important role in influencing the development of societies. In more recent history transportation has played a major role in the development of the modern industrial city. 

Cities usually develop at some natural transportation link—an intersection of trade routes, a river junction, a harbor. Then, as they grow in population, they begin to expand geographically. During their early years the major influence on development is that of the local topography. However, as cities begin to reach a scale beyond that of reasonable walking distance, the available transportation technologies play a role in shaping their forms. For example, in the development of American cities during the middle of the nineteenth century, horse-drawn streetcars provided radial spokes along which the development of suburbs took place (S. B. Warner 1962). These spokes radiated outward from the central business district and served to move commuters into and out of the center of the city. As horsedrawn streetcars were replaced by electric-powered “trolley” streetcars, this pattern of development along the radial spokes of the transportation arteries continued. These arteries were replaced and extended by suburban railroads, which stimulated the development of even more extensive commuter suburbs. 

With the coming of the automobile, the areas between the radial spokes began to be filled in. Even so, until the end of World War II the level of reliance on public transport was such that cities remained relatively compact. 

In America, with the ending of World War II, a combination of public policies and private aspirations resulted in forces that significantly changed the character of most cities. Growth in personal income led to a rapid increase in the number of private automobiles and the fulfillment for many of the dream of a single-family house on a small lot in the suburbs. The explosion of American population into suburbia was accelerated and aided by this growth in auto ownership, by federal housing policies that made mortgage money more easily available, and by the development of extensive systems of express highways. These express, limited-access highways allowed rapid movement for large numbers of automobiles and trucks, radially from the central cities to the suburbs and circumferentially among suburbs. This system of highways accelerated the dispersal of population, businesses, and industry. As suburban shopping centers mushroomed to bring goods and services to the growing suburban populations, the role of central business districts began to change. Industrial parks in the suburbs brought jobs to where people lived. 

Of course, as use of the automobile became easier and as population dispersed, there was a corollary effect on public transit. Transit ridership had been declining since the early 1920s as incomes had risen and the number of private automobiles had increased. With the rapid postwar development of highways and acceleration of dispersion, the decline of public transit became calamitous. As transit ridership dropped and labor costs increased, fares were increased and service cut back in order to stabilize deficits. These changes resulted in further declines in use and made automobiles relatively more attractive. 

This short sketch of American urban patterns illustrates the extensive interrelationship between transportation and social and economic activity (Meyer, Kain, and Wohl 1965). Similar patterns have begun to emerge in Western Europe. 

As another example, consider the growth of air travel since 1945. 

The convenience of present-day intercity air travel within North America and within Western Europe has had important effects on the behavior patterns of businessmen on these two continents. One can make a round trip between Boston and Washington or between London and Paris in a single day, and many businessmen and government officials may visit two to four cities each week. 

Similarly, air transportation also provides great opportunities for social and recreational travel. Even people with moderate incomes can afford to take vacations, at any season of the year, for a few days or up to a month, almost anywhere in the world. In Boston, weekends in Miami are advertised widely; in Paris, weekends in New York or Tangiers or even Jerusalem. 

Similar interrelationships between transportation and social and economic activities can be discerned in other contexts. For example, in a country undergoing rapid development, a proposal for major improvements in the national highway network raises fundamental questions. What impact will such a highway network have on the development pattern? Will it aid the economic development and social viability of small towns and cities in the hinterland? Or will the highway systems and bus services make the one or two major metropolitan areas of the country more attractive and more accessible, so that people migrate in large numbers to the metropolis? Alternatively, what should be the relative roles of rail, truck, and water for freight transport? The provision of transportation in a developing country can have a significant impact on the social and economic development patterns, and transportation planning in this context must therefore quite explicitly be a part of overall national development planning. 

## 2.2.2 What We Are Trying to Predict

As analysts, our goal is to predict the effects of a change in the transportation system on the broader fabric of society. As discussed above, such changes in the transportation system of a region can have significant effects on the patterns of social and economic activity. In the short run a change in the transportation system will be reflected in changes in travel patterns; over a longer period of time the location and even the nature of social and economic activity may change significantly. 

To predict how the individuals and firms in a region might respond to these changes and to understand why present conditions have come about—why travel and locational patterns have taken the forms they now have—we must understand human behavior. At present our understanding of human behavior in response to transportation system changes is far from perfect, but substantial progress is being made. This information can be summarized in a demand function, which is a representation of human behavior that can be used to predict how an individual or firm, or groups of individuals or firms, will respond to changing conditions. 

## 2.2.3 The Dimensions of Human Behavior

## LEVELS OF CHOICE

In most countries an individual's activity pattern can be defined by the choices he or she makes about such things as employment, including type of work, income, and location; residence, including location, type of home, type of neighborhood, and such related factors as schools, access to shopping, interactions with neighbors, and rents or mortgage rates; “consumption” patterns; shopping and other personal business activities, including goods and services purchased, shopping areas frequented, prices paid, as well as related activities such as “browsing” or banking; and social and recreational activities, such as visiting friends and relatives and excursions on weekends and holidays. 

Each individual has a conception of the activity pattern that would constitute a full and satisfying life. This is the “basic” demand that motivates individual and household decisions: the desire to undertake particular activity patterns. 

There are several “levels” of choice that an individual must make (figure 2.1). At the highest, most basic level is the choice of a desired pattern of activity that reflects one’s life-style aspirations. Then, in order to undertake a particular activity pattern, the individual must be at particular locations at particular times; this leads to basic locational choices, including the choice of a residential location and of a place of 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/a9a45185-cfa1-407d-8a96-209400065f95/d96703933a64dd3ebbd685bbd80a9fa378823e21da39c73acaea06fb8e84a843.jpg)



Figure 2.1 Levels of choice for an individual.


The Demand for Transportation 

work. Such locational choices form a second level of decisions. Next, in order to undertake the desired activities at the chosen locations, a third level of choices is required: choices about where, when, and how to travel. 

## DERIVED DEMAND

The travel choices are the ones that lead directly to a “demand” or “desire” for travel. It is clear, then, that the demand for travel is a derived demand, in this sense: travel is desirable not in itself but as a means of being at certain locations at certain times, and this goal is itself derived from the desire to undertake certain patterns of activities. Thus, to understand the demand for travel we need, ideally, to understand the basic human desires for various activity patterns; from this we could derive the demand for locations of activities, especially for locations of residence and workplace, and from this locational demand we could derive the demand for travel. 

A similar hierarchy of choices exists in the freight sector. The primary choices made by commercial enterprises include the products to produce, the general markets to pursue, and the magnitude of economic activity (sales, employment, investment) to engage in. In order to achieve a desired pattern of economic activity, the firm must make locational decisions for its production facilities and select specific markets (that is, geographic regions) to be served and sources of raw materials. From these choices are then derived the commodity transportation choices: which commodities to ship, from where, to where, by what means (see figure 2.2). 

Clearly, in the cases of both personal travel and freight movements, the choices at each level interact in significant ways. For example, the 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/a9a45185-cfa1-407d-8a96-209400065f95/95d61958cf8ee9d832429d3d9b20899d9b80cd0bc928d77d9e437a50ceba25b2.jpg)



Figure 2.2 Levels of choice for a firm.


The Demand for Transportation 

choice whether or not to produce a particular commodity at X for sale in market Y is determined in part by the available transportation choices. 

## A WORKING HYPOTHESIS

At the present time we know most about the demand for transportation and least about the desire for certain activity patterns. Therefore, in order to cut through the complexity of the interactions between the transportation and the socioeconomic activity systems, we make the following hypothesis: It is feasible to separate the long-run shifts in the location and scale of socioeconomic activity from the short-run behavior of the market for transportation. Under this hypothesis, in considering the demand for transportation, we may assume that the patterns of social and economic activity are fixed. Then we can treat the related problem of the long-run shift in socioeconomic activity separately from that of the demand for travel; this we have called the activity shift. The separation of demand and activity-shift models—the type 1 and type 2 relationships in the analytical framework introduced in chapter 1—reflects this hypothesis. 

Thus, recalling our earlier definition of a demand function as a representation of human behavior, we find it convenient to separate the "total" demand function into two parts. The transportation demand function is a representation of human behavior which can be used to predict how individuals or firms, or groups of individuals or firms, will change transportation choices in response to changes in future conditions. The activity-shift function is a representation of human behavior which can be used to predict how individuals or firms, or groups of individuals or firms, will change activity and location choices in response to changes in future conditions. 

In a sense, the basic difference is in the time scale over which decisions take place. Transportation decisions can be made and changed very quickly. Changes in the location and scale of socioeconomic activity take much longer to occur. Therefore, another way of interpreting the hypothesis is that it is useful to distinguish between short-run and long-run decisions. 

This hypothesis is one that has often been made in practice, and it is useful for teaching purposes. However, ongoing research suggests that it may be too simple. We shall discuss this further in chapter 11, but for the rest of this chapter we shall assume its validity. For simplicity, whenever we say “demand” we shall mean “demand for transportation” unless explicitly stated otherwise. 

## 2.3 BEHAVIOR AT THE INDIVIDUAL LEVEL

The problem of predicting the demand for transportation can be approached at two levels: that of the individual or that of groups of individuals. By an individual we mean any group that behaves as a single unit in making transportation decisions. Such a unit can be: for goods movements, a firm, a part of a firm, such as the shipping or traffic department, or an individual such as a traffic manager or shipping clerk; for personal travel, a household, consisting of several interacting persons, or a single person. The essential point is that when a unit consists of more than one person, they interact in reaching a decision. For example, in a household where several drivers (parents and teenage children, say) share one automobile, the decisions about use of the automobile in the evening and on weekends may involve a collective decision among competing demands. 

For simplicity, we shall use the term consumer to denote a single decision-making unit, whether that unit consists of one or several persons. 

## 2.3.1 A Model of Consumer Behavior

Once we recognize that we are dealing with human behavior, we see that we face a tremendous challenge: People are complex; their preferences and decision-making behaviors are very different and are continually changing. In order to predict future travel, we must understand human behavior in a way that can produce operational results. Thus any model for explaining consumer behavior must indicate (1) what alternative choices consumers perceive; (2) what consequences of these alternatives they consider important; and (3) how they make their choices from among the perceived alternatives. 

## ALTERNATIVE CHOICES

The basic decisions with which the consumer must deal from the point of view of transportation are whether to make a trip, where to make the trip, at what time to make the trip, and which mode and route to take. These decisions are obviously highly interrelated. The extent of this interrelationship depends on, among other things, the purpose of the trip. For example, in an urban area trips between home and work have the “whether” and “where” fixed; the individual generally has a fixed residence and a fixed workplace and is committed to making the home-to-work trip regularly. The time, mode, and route taken are usually determined together and once a pattern is established, the typical consumer rarely changes these decisions. On the other hand, consider another example: where to go on a summer weekend. For this kind of recreational trip, all the options are open and are probably determined simultaneously. 

## ATTRIBUTES

What factors does the consumer take into account when choosing among these alternatives? In introducing the basic framework of analysis in chapter 1, we defined the concept of service level, S: the service variables are those attributes of the transportation system that influence the consumer's decisions as to whether, where, when, and how to make a trip. In general, each consumer considers a number of service variables. Therefore, the consequences are expressed as a vector, $\mathbf{S} = (S_{1}, S_{2}, \ldots, S_{j}, \ldots, S_{n})$ . An illustrative list of service variables is given in table 2.1. As this list shows, consumers may consider many attributes of transportation service. In general, different consumers will consider different service attributes to be important, reflecting differences in their socioeconomic characteristics and preferences. Since it is usually not possible to include explicitly all possible service variables when forecasting travel demand, an important practical problem is to identify those service variables that have the greatest influence on consumer choices. Another important and related practical problem is that some service variables cannot readily be quantified (“comfort,” “safety,” “perceived security”). 

Furthermore, even such seemingly simple attributes as “travel time” turn out to be complex in their influence on traveler behavior. In table 2.2 we show some of this complexity by breaking down travel time into some of its major components. These components are perceived differently in different situations; for example, in some travel forecasts “excess time” or “out-of-vehicle time” is defined as “all time components other than in-vehicle travel time.” 

In addition, "time" is not always synonymous with "distance" from the viewpoint of consumer behavior. For example, numerous surveys have shown that walking distance is a very important determinant of bus ridership—very few people will walk more than a quarter mile to use a bus. Thus walking distance should usually be one of the service parameters used to predict ridership on a bus system. 

On the other hand, for a door-to-door system such as the demand-responsive bus—"dial-a-ride"—there is no walking required, so walking distance is obviously not a factor. However, the reliability of total trip time for dial-a-ride may be lower than for most transportation systems, since it is a demand-responsive service, so this service variable should be included in any dial-a-ride analysis. Thus service attributes will have different degrees of importance in influencing consumer behavior for different transportation systems. Therefore the service variables to be included in any analysis will depend to some extent on the systems being analyzed. 


Table 2.1 Illustrative service attributes


<table><tr><td>Timea</td></tr><tr><td>total trip time</td></tr><tr><td>reliability (variance in trip time)</td></tr><tr><td>time spent at transfer points</td></tr><tr><td>frequency of service</td></tr><tr><td>schedule times</td></tr><tr><td>Cost to user</td></tr><tr><td>direct transportation charges such as fares, tolls, fuel, and parking</td></tr><tr><td>other direct operating costs such as loading and documentation</td></tr><tr><td>indirect costs such as the cost of acquiring, maintaining, and insuring an auto-mobile or, for freight, warehousing, interest, and insurance</td></tr><tr><td>Safety</td></tr><tr><td>probability of fatality or of destruction of cargo</td></tr><tr><td>probability of accident of any sort</td></tr><tr><td>probability distribution of accident types (shock vibration, water damage, and so on)</td></tr><tr><td>perceived security</td></tr><tr><td>Comfort and convenience for user</td></tr><tr><td>walking distance</td></tr><tr><td>number of vehicle changes required</td></tr><tr><td>physical comfort (temperature, humidity, cleanliness, ride quality, exposure to weather)</td></tr><tr><td>psychological comfort (status, privacy)</td></tr><tr><td>other amenities (baggage handling, ticketing, beverage and food service)</td></tr><tr><td>enjoyment of trip</td></tr><tr><td>aesthetic experiences</td></tr><tr><td>Shipper services</td></tr><tr><td>division and reconsignment privileges</td></tr><tr><td>insurance</td></tr></table>


$^{a}$ Time is often divided into the components shown in table 2.2. 



Table 2.2 Major components of travel time


<table><tr><td></td><td>Out-of-vehicle time</td><td>In-vehicle time</td></tr><tr><td>Access time</td><td>Walk timeWait time</td><td>Time in feeder vehicle (for example, in automobile or bus en route to mainline transit)</td></tr><tr><td>Line-haul time</td><td>Transfer time</td><td>Time in line-haul vehicle (mainline transit time or automobile driving time)</td></tr></table>

In general, travel time, wait time, and fare have been the primary service variables used to predict traveler behavior in urban transportation, especially for conventional transit services. The relationships might simply be described as follows: as the transit travel time, wait time, and fare decrease, the level of usage of transit will increase—more consumers will find the transit mode more attractive. 

## DECISION PROCESS

The third major feature of a model of consumer behavior must be a description of how the consumer operates on the two preceding sets of information—the perceived alternatives and the attributes of those alternatives—to reach a decision. A part of this description must include some representation of the consumer's preferences or goals as well as some characterization of the consumer in ways that allow us to distinguish among the behavior patterns of different groups of consumers. Various formulations can be proposed for this decision process. We shall next examine two particular formulations. 

## 2.3.2 Consumer Behavior Model I

In this first model it is assumed that the consumer: formulates his preferences explicitly, identifies explicitly all the alternatives open to him, identifies the consequences of each alternative, and evaluates the alternatives and chooses among them using a well-defined decision rule. 

## REPRESENTING PREFERENCES

A key feature of this model is the approach taken to representing the preferences of the consumer (see, for example, Baumol 1965, Henderson and Quandt 1958). 

The preferences of consumers vary not only in which service attributes they consider important, but also in the relative values they place on various attributes. To represent this variation the model uses the concept of an indifference curve, which is a curve indicating all combinations of choices among which the consumer is indifferent. Figure 2.3 shows a set of indifference curves involving two service attributes, travel time t and out-of-pocket cost c. This set of curves represents the preferences of a particular consumer: the consumer is essentially indifferent to all combinations of time and cost on a single curve but has definite preferences among curves. For example, he is indifferent between the combination of time and cost represented by point A on curve I and that combination represented by point B. On the other hand, both of these points are preferred to point C on curve II, because point C has both a higher travel time and a higher cost than either A or B. 

Furthermore, A and B are both preferred to D. Although D has lower cost than B, its time is sufficiently greater than $B'$ s so that it is still less desirable. In addition, the consumer is indifferent between C and D, so since B is preferred to C, B must also be preferred to D. 

The set of indifference curves can be expressed in functional form as 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/a9a45185-cfa1-407d-8a96-209400065f95/e855761db4a4be79c3b5acab6a1706139887580bdf8a5bbc2a419c2b7080aa24.jpg)



Figure 2.3 Indifference curves.


The Demand for Transportation 

$$
U = f (\mathbf {S}, \theta),\tag{2.1}
$$

where S is the vector of service attributes and $\theta$ is a vector of parameters. Two specific forms of interest are the product form, 

$$
U = \alpha t ^ {\beta} c ^ {\gamma},\tag{2.2}
$$

and the linear form, 

$$
U = \alpha t + \beta c.\tag{2.3}
$$

In these cases $\mathbf{S} = (t, c)$ and $\theta = (\alpha, \beta)$ or $(\alpha, \beta, \gamma)$ . Each of these equations defines a family of curves; each curve shows, for a specific value of U, those combinations of t and c that are equally preferred by the consumer. The product form (2.2) would generate a family of indifference curves like figure 2.3; the linear form (2.3), a family of indifference curves like figure 2.4. Different curves correspond to different values of the quantity U. 

The value of U can be interpreted as a measure of the degree to which a particular combination $(t, c)$ is desired by the consumer. When it is useful to do this, U is called a utility and the functions defining the indifference curves are called utility functions. Utility is valued positively; that is, utility is so defined that if $U_{A} > U_{D}$ , then the consumer prefers A to D. For example, in figure 2.3 $U_{I} > U_{II}$ because the consumer prefers either A or B to either C or D. 

Note that the service attributes of time and cost are negatively valued; that is, the consumer prefers /less time and/or /less cost, rather than more. So, as t and/or c increase, the corresponding values of U decrease. The parameters in $\theta$ must have corresponding signs. Sometimes the term disutility or negatively valued utility is used. In this case, instead of maximizing utility, the consumer is assumed to minimize disutility. The result is the same. To prevent confusion, we shall always use the term utility; whether the utility actually reflects a disutility will be clear in a particular context from the definitions of the service attributes used and the values of the parameters in $\theta$ . 

Utility can be measured in any convenient units: time, monetary units, or, most generally, “utiles.” The values of the parameters of these indifference curves explicitly express the preferences of the consumer. For example, one useful property of these curves is represented by the trade-off ratio, the slope of the curve. For the linear indifference curve, the trade-off ratio is $\alpha/\beta$ . This ratio expresses the “value” of time to the consumer, that is, the amount he would be willing to pay to save one unit of travel time. For every minute of time saved, the 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/a9a45185-cfa1-407d-8a96-209400065f95/9cde951e169384354784bdf6ace61c84c9130a85541ffd425ee4ef2167055c7f.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/a9a45185-cfa1-407d-8a96-209400065f95/3cfa41a86ca8a85a6ed3d9810fd59c36cc72504c5e1d835e1094e0bee9f93798.jpg)



Figure 2.4 Consumer behavior model I.


consumer would be willing to pay $\alpha/\beta$ additional dollars. 

We would expect different consumers to have utility functions with different indifference curves and trade-off ratios. For example, people with high incomes would likely place a high value on travel time and would be willing to pay a relatively high cost to save a minute of travel time; this would be reflected by a high ratio of $\alpha$ to $\beta$ and thus by the slope of their indifference curves. On the other hand, low-income consumers would probably be willing to spend substantial additional travel time to save on travel costs; this, too, would be reflected in their trade-off ratios and in the shape of their indifference curves. 

## DECISION PROCESS

The steps in the decision process in this model are as follows: 

1. The consumer explicitly formulates his preferences for all possible combinations of attributes. 

2. He identifies all the alternatives open to him. 

3. He characterizes each alternative in terms of its attributes. 

4. He uses his preference information to select an alternative. 

Assume that the consumer has expressed the preferences indicated by the set of indifference curves in figure 2.4a (the dashed lines). Each curve shows all combinations of time and cost with equal utility U, that is, all combinations that are equally desirable from the point of view of the consumer. Assume also that he has identified three alternative choices—A, B, and C—and has characterized each by two service attributes, time and cost. Thus each of the available alternatives can be represented by the time and cost that it offers, as shown in figure 2.4a. 

The decision process follows from the definition of utility and indifference curves. In line with his expressed preferences, the consumer will pick the alternative (of those available) that has the greatest utility, that is, the one that is on the indifference curve closest to the origin of the axes. In the case of the curves in part a of the figure, this is alternative B. 

Consumers with different preferences, and thus different indifference curves, will pick different alternatives. For example, in part b of the figure a consumer who places a high value on time is shown by indifference curve I; this consumer would pick alternative A. On the other hand, a consumer who places a low value on time, with indifference curve II, would pick alternative C. 

There are two alternative ways of describing this choice process: 

1. Using the consumer's expression of his preferences, construct the indifference curves. Characterize each alternative by its service attributes and determine on which indifference curve it lies. Then pick the alternative that is on the indifference curve with the highest value of utility (in figures 2.3 and 2.4, the curve to the lowest left). 

2. Characterize each alternative by its service attributes. Using the information on preferences, calculate the utility for each alternative. Then pick the most preferable alternative (that is, the one with the highest value of utility). 

Both methods produce the same results. We have used method 1 so far, but method 2 is a more flexible way of dealing with situations with many alternatives. In future applications of this model, we shall first find the utility for each alternative and then compare alternatives on the basis of their utilities. 

The Demand for Transportation 

## 2.4 APPLICATIONS OF CONSUMER BEHAVIOR MODEL I

The examples in this section illustrate the use of the foregoing model in predicting consumer responses for passenger and freight transportation. They trace through the effects of changes in the transportation in order to identify how choices may change as a result of such system changes, how consumers may differ in their behavior, and how changes in socioeconomic factors may modify consumer choice. 

## 2.4.1 A Freight Example

## THE CHOICE OF A SINGLE CONSUMER

A particular manufacturer has a choice between rail and truck for shipping his goods to market. We assume that the only service attributes that affect his choice are cost c, in-vehicle travel time t, and excess or out-of-vehicle time x, which incorporates such components as waiting times at both ends of the trip and the reliability of service. Cost includes the freight rate for either mode plus ancillary charges such as packaging for shipment and insurance. 

The present service characteristics of the two modes are shown in table 2.3. We can try to predict the choice made by this consumer by estimating the relative weights he places on cost, in-vehicle time, and excess time ( $w_{c}$ , $w_{t}$ , and $w_{x}$ , respectively). With these weights the three service variables can be collapsed into a single measure of utility: 

$$
U = w _ {t} t + w _ {x} x + w _ {c} c.\tag{2.4}
$$

Note that all the weights take negative values, since an increase in any of the attributes reduces the utility of the mode. Using our model, we then assume that the consumer will select the mode that has the highest value of this utility, that is, the least value of a negative number. We assume that the weights are - $2 per day (per ton) for travel time ( $w_t$ ) and - $4 per day (per ton) for excess time ( $w_x$ ) for this particular shipper, relative to a weight of -1 for $w_c$ . 

The utilities of the two competing modes are as follows (note that the utilities are negative because the higher the time or cost, the less attractive that choice would be, and thus the lower the utility): 


Table 2.3 Characteristics of two competing freight modes


<table><tr><td></td><td>Rail</td><td>Truck</td></tr><tr><td>Cost</td><td>$4/ton</td><td>$5/ton</td></tr><tr><td>In-vehicle time</td><td>2.5 days</td><td>2.0 days</td></tr><tr><td>Excess time</td><td>1.0 day</td><td>0.3 day</td></tr></table>

$$
U _ {\mathrm{R}} = (- 2 \times 2. 5) + (- 4 \times 1. 0) + (- 1 \times 4) = - 1 3,\tag{2.5}
$$

$$
U _ {\mathrm{T}} = (- 2 \times 2. 0) + (- 4 \times 0. 3) + (- 1 \times 5) = - 1 0. 2 0.\tag{2.6}
$$

In this case, we thus predict that the consumer will select truck as the preferred mode because it has a higher utility (a lower value of a negative number—a lower disutility). Furthermore, as long as the characteristics of the two modes and the values of the consumer do not change, the choice would always be the same for this type of shipment—from day to day and from month to month. 

## THE CHOICES OF DIFFERENT CONSUMERS

A different consumer faced with exactly the same choice would use different weights on the service attributes to evaluate the modes. Table 2.4 shows the behavior of consumers with different preferences. The resulting choice is shown for each consumer. Some choose rail and others choose truck because of the difference in preferences, reflected in the differences in weights and thus in utility functions. 

## EFFECT OF A CHANGE IN LEVEL OF SERVICE

This model is very useful for understanding the effects of a potential or actual change in the transportation system. Any such change can be expressed as a change in one or more service attributes for one or more of the alternatives. This would cause a change in the utility a particular consumer places on the affected alternatives. 

Consider shipper A in table 2.4. While under present conditions this shipper would choose truck, it is possible that changes in service could alter this. For example, if truck freight rates are increased by $4, then the utility of truck becomes — $14.20, while the utility of rail stays at 


Table 2.4 Example of mode choice based on a simple utility model


<table><tr><td rowspan="2">Shipper</td><td colspan="3">Relative weights</td><td colspan="2">Utilities</td><td rowspan="2">Choice</td></tr><tr><td><eq>w_t</eq></td><td><eq>w_x</eq></td><td><eq>w_c</eq></td><td>Rail</td><td>Truck</td></tr><tr><td>A</td><td>-2</td><td>-4</td><td>-1</td><td>-13</td><td>-10.20</td><td>Truck</td></tr><tr><td>B</td><td>-3</td><td>-8</td><td>-1</td><td>-19.50</td><td>-13.40</td><td>Truck</td></tr><tr><td>C</td><td>-2</td><td>-3</td><td>-4</td><td>-24</td><td>-24.90</td><td>Rail</td></tr><tr><td>D</td><td>-2</td><td>-3</td><td>-8</td><td>-40</td><td>-44.90</td><td>Rail</td></tr></table>

- $13. The shipper now shifts to rail. Or if special nonstop trains are introduced ("unit trains"), or other operational improvements are made, such that rail in-vehicle time drops to 1 day, then the utility of rail becomes - $10, relative to a truck utility of - $10.20. The shipper again shifts to rail. 

The effects of such variations are shown graphically in figure 2.5. Here the mode choice is shown as a function of a single service attribute, truck freight rate. For rates below $7.80, the shipper chooses truck; above $7.80, he chooses rail. 

In these examples the consumer's utility function does not change, only the value that the function takes for a particular alternative. Note also that while utility is a continuous function of freight rate, the choice is discrete: either rail or truck is chosen. 

SERVICE LEVEL NECESSARY TO CAUSE A SHIFT IN CHOICE
The utility functions can be used to find, for each shipper type, the truck freight rate that would cause that consumer to shift from truck to rail or from rail to truck. This is the point at which the utilities are just equal: 

$$
U _ {\mathrm{R}} = U _ {\mathrm{T}}\tag{2.7}
$$

or 

$$
w _ {t} (t _ {\mathrm{R}} - t _ {\mathrm{T}}) + w _ {x} (x _ {\mathrm{R}} - x _ {\mathrm{T}}) + w _ {c} (c _ {\mathrm{R}} - c _ {\mathrm{T}}) = 0.\tag{2.8}
$$

Solving for $c_{T}$ yields 

$$
c _ {\mathrm{T}} = \frac {W _ {t}}{W _ {c}} \left(t _ {\mathrm{R}} - t _ {\mathrm{T}}\right) + \frac {W _ {x}}{W _ {c}} \left(x _ {\mathrm{R}} - x _ {\mathrm{T}}\right) + c _ {\mathrm{R}}\tag{2.9}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/a9a45185-cfa1-407d-8a96-209400065f95/d719dea6ced76f5b86e130a631020d20985a1d2e69d5c34255653020cf9724d5.jpg)



Figure 2.5 Truck rate as a determinant of mode choice.


The Demand for Transportation 

or, for the given values, 

$$
c _ {\mathrm{T}} = \frac {W _ {t}}{W _ {c}} (0. 5 \text {   days }) + \frac {W _ {x}}{W _ {c}} (0. 7 \text {   days }) + 4.\tag{2.10}
$$

For shipper A, 

$$
c _ {\mathrm{T}} = 2 (0. 5) + 4 (0. 7) + 4 = 7. 8 0;
$$

for shipper B, 

$$
c _ {\mathrm{T}} = 3 (0. 5) + 8 (0. 7) + 4 = 1 1. 1 0;
$$

for shipper C, 

$$
c _ {T} = \frac {2}{4} (0. 5) + \frac {3}{4} (0. 7) + 4 = 4. 7 8;
$$

for shipper D, 

$$
c _ {T} = \frac {2}{8} (0. 5) + \frac {3}{8} (0. 7) + 4 = 4. 3 9.
$$

Thus, to get shippers C and D to shift from rail to truck would require truck rates below $4.78 and $4.39, respectively, versus the present rate of $5. On the other hand, since shippers A and B now prefer truck, the truck rates could be increased to as much as $7.80 and $11.10, respectively, before they would shift from truck to rail. 

This behavior is shown graphically in figures 2.5 and 2.6. Figure 2.5 shows the behavior of shipper A, with the choice of rail or truck displayed as a function of both the absolute value of the truck rate and the change in rate from the present level. Figure 2.6a shows the behavior of each of the four shippers, separately, for comparison. 

## TRADE-OFFS AMONG SERVICE ATTRIBUTES

Knowledge of the shippers' utility functions can also be used to explore trade-offs among the various service attributes. 

Consider shipper A again. The truck operator, because of external factors (for example, increases in driver wages or fuel prices), knows that he will soon have to increase his rate by $4 per ton, to $9. As shown earlier, this would cause shipper A to shift from truck to rail. If the truck operator wanted to prevent this shift, what in-vehicle time would he have to offer as compensation? Thus what we want to know is what in-vehicle time will give a value of truck utility equal to the rail utility; then, for lower in-vehicle times, truck will be more attractive to this shipper. Using $U_{\text{T}} = U_{\text{R}} = -\$13$ , we have, from (2.4), 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/a9a45185-cfa1-407d-8a96-209400065f95/90ff4c5b191c7a29edcb18226dcbca96b875c34bb1f24fb569bf4198e0f85934.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/a9a45185-cfa1-407d-8a96-209400065f95/eaeffe59c42d64d62711ece18b1784d59638332b73dc3af0c16565b83313e0ca.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/a9a45185-cfa1-407d-8a96-209400065f95/f45780eec40d976f75025f8b55134ddecdc92f524b0d21418bb8fe6202b0b5e9.jpg)



Figure 2.6 Relationship of individual to group choices.


$$
- 13.00 = (-2 \times t_{\mathrm{T}}) + (-4 \times 0.3) + (-1 \times c_{\mathrm{T}})\tag{2.11}
$$

or, solving for in-vehicle time, 

$$
t _ {\mathrm{T}} = 5. 9 0 - 0. 5 c _ {\mathrm{T}}.\tag{2.12}
$$

This is, of course, the equation of the indifference curve relating $t_{T}$ and $c_{T}$ for this value of utility, as represented in figure 2.4. 

For $c_{\mathrm{T}} = \$9$ , the corresponding value of $t_{\mathrm{T}}$ is 1.4: if the truck operator intends to increase his rate by \$4, he must bring his in-vehicle time down below 1.4 days if he wants to retain the patronage of shipper A. 

## AGGREGATE BEHAVIOR

So far we have looked at each of our four shippers as an individual consumer. We now examine the behavior of the group as a whole. We shall use the results shown in figure 2.6a. 

Each shipper represents 25 percent of the group of four shippers. At the present truck rate (\$5), 50 percent of the group choose truck (two shippers) and 50 percent choose rail. We call this a "50 percent rail mode split": the total market "splits" so that 50 percent choose rail. If we increase the truck rate, we change the mode split: shipper A will shift to rail at a truck rate of \$7.80, thus increasing the rail mode split to 75 percent. If we increase the truck rate further to \$11.10, shipper B will also shift to rail, resulting in a 100 percent rail mode split. Conversely, if we decrease truck rate to \$4.78, we will attract shipper C to truck, for a 25 percent rail mode split, and a decrease to \$4.39 will yield a 0 percent rail mode split (a 100 percent truck mode split). 

We can thus derive the aggregate behavior of the group from the behaviors of each of the individuals in the group. This relationship is shown in figure 2.6b. 

Usually a group will be composed of many more than four consumers. In that case the relationship between the service attribute and the fraction of the group making a particular choice will be much smoother and can be approximated by a continuous function, as shown in figure 2.6c. 

In general, of course, the modal split of a particular group can be affected by changing one or more of the service attributes. To represent this we might show on the horizontal axis the differences in utilities, leading to a function like the one shown in figure 2.6c. The intercept on the vertical axis, $a_{0}$ , represents the modal split that would result even if both modes had the same utilities (that is, zero difference in utilities). 

Then $c_{0}$ might represent the magnitude of “captive” truck users, those who do not have the option of using rail—perhaps because they or the firms to which they ship are too remote from rail service. Further, $b_{0}$ might represent those shippers who require rail for some particular reason and so will not shift to truck no matter how much the relative attractiveness changes. 

Symbolically this curve would represent the demand function 

$$
\gamma_ {\mathrm{R}} = \frac {V _ {\mathrm{R}}}{V _ {\mathrm{T}} + V _ {\mathrm{R}}} = f _ {\mathrm{D}} (U _ {\mathrm{R}} - U _ {\mathrm{T}}),\tag{2.13}
$$

where $\gamma_{R}$ is the share or fraction choosing rail, $V_{R}$ and $V_{T}$ are the volumes choosing rail and truck, respectively, and $U_{R}$ and $U_{T}$ are the utilities of rail and truck, respectively. 

## 2.4.2 An Urban Passenger Travel Example

## THE CHOICE OF A SINGLE CONSUMER

For the home-to-work trip in a particular city, a commuter has two choices, transit or automobile. Each mode is characterized by three service attributes: in-vehicle travel time t in minutes; out-of-vehicle time x (for automobile, total parking and walk time; for transit, total walk and wait time) in minutes; and out-of-pocket cost c (for automobile, operating cost based on mileage traveled plus parking charges; for transit, fares) in cents. The utility function is similar to (2.4): 

$$
U = w _ {t} t + w _ {x} x + w _ {c} c.\tag{2.14}
$$

Assume that for the commuters residing in a particular area the relative weights are 

$$
\begin{array}{r l} {w _ {t} =} & {- 1. 0,} \\ {w _ {x} =} & {- 2. 5,} \\ {w _ {c} =} & {- k / y,} \end{array}
$$

where y is annual income in dollars and k = 5,000 $-min/¢-yr, so that w $_{c}$ has units of min/¢. Thus 

$$
U = - t - 2. 5 x - (5, 0 0 0 / y) c.\tag{2.15}
$$

Since U takes on negative values, each traveler will pick the option that has the highest value of U. 

Note that the utility depends on the consumer's income. The relative values a consumer places on time and cost are given by $w_{c} / w_{c}$ . Consumers with higher incomes have smaller values of $w_{c}$ relative to $w_{t}$ 

and thus place a higher value on time. The value of the coefficient k reflects the premise that consumers value time at about 25 percent of their hourly wage rate. The relative values of $w_{x}$ and $w_{t}$ reflect the premise that out-of-vehicle time is 2.5 times as onerous as time spent traveling in a moving vehicle. 

The present characteristics of transit and automobile are shown in table 2.5. The out-of-vehicle time for transit is composed of 8 minutes of walking time and an average waiting time of 12 minutes (half the 24-minute interval between trains). 

For a consumer with an annual income of $10,000, (2.15) becomes 

$$
U = - t - 2. 5 x - 0. 5 c.\tag{2.16}
$$

The resulting utilities are -80 equivalent minutes for automobile and -90 for transit. Thus the consumer would choose the automobile. 

The transit authority is proposing a doubling of frequency along this route. Would this affect the consumer's choice? Since a doubling of frequency would yield, on average, a halving of waiting time, $x_{\mathrm{T}}$ would be reduced to 14 minutes. The effect would be an increase in utility from -90 to -75. Now transit would be more attractive than automobile, and the model predicts that the traveler would shift to transit. 

## EFFECT OF A CHANGE IN SOCIOECONOMIC CHARACTERISTICS

Any model for predicting consumer behavior should reflect the particular socioeconomic characteristics and behavior of the consumer explicitly. In the freight example we simply had different values of the parameters to represent different preferences for each shipper. In this urban example the parameters are explicitly a function of income, allowing us to see how changes in this socioeconomic characteristic would affect the consumer's choice. 

For example, consider a consumer with an annual income of $5,000. His utility function would be 

$$
U = t - 2. 5 x - c.\tag{2.17}
$$


Table 2.5 Characteristics of two competing transportation modes


<table><tr><td></td><td>Transit</td><td>Automobile</td></tr><tr><td>In-vehicle time</td><td>30 minutes</td><td>40 minutes</td></tr><tr><td>Out-of-vehicle time</td><td>20 minutes</td><td>4 minutes</td></tr><tr><td>Out-of-pocket cost</td><td>20¢</td><td>60¢</td></tr></table>

For him the automobile would have a utility of -110, so transit, having a utility of -100, would be more attractive. As his income increases, the model predicts that his tastes will change. At $10,000 his choice will be automobile over transit. 

EFFECT OF A CHANGE IN SERVICE CHARACTERISTICS
Given the utility functions, we can derive the value, for any service attribute, at which the choice of mode would change. Take, for example, transit in-vehicle time. Let $t_{E}$ be the value of transit travel time such that if $t_{T} < t_{E}$ , transit is preferred. Then for $t_{T} = t_{E}$ , 

$$
U _ {\mathrm{T}} (t _ {\mathrm{E}}) = U _ {\mathrm{A}} (t _ {\mathrm{E}})\tag{2.18}
$$

or 

$$
w _ {t} t _ {\mathrm{E}} + w _ {x} x _ {\mathrm{T}} + w _ {c} c _ {\mathrm{T}} = w _ {t} t _ {\mathrm{A}} + w _ {x} x _ {\mathrm{A}} + w _ {c} c _ {\mathrm{A}}.\tag{2.19}
$$

Thus 

$$
\begin{array}{l} t _ {\mathrm{E}} = \frac {W _ {x}}{W _ {t}} (x _ {\mathrm{A}} - x _ {\mathrm{T}}) + \frac {W _ {c}}{W _ {t}} (c _ {\mathrm{A}} - c _ {\mathrm{T}}) + t _ {\mathrm{A}} \\ = 2. 5 (4 - 2 0) + \frac {5 , 0 0 0}{y} (6 0 - 2 0) + 4 0 \\ = 2 \times 1 0 ^ {5} / y. \end{array}\tag{2.20}
$$

Thus the transit travel time at which riders would be indifferent between transit and automobile is a function of income. This demonstrates the effect of socioeconomic characteristics on the choice of mode as a function of level of service. 

## AGGREGATE BEHAVIOR

In the freight example we saw how the aggregate behavior of a group of shippers was related to the underlying individual preferences of each shipper. For this urban example consider the two groups of travelers shown in table 2.6. Group A is a relatively low-income group: its average income is $8,200, versus $11,800 for group B. Each group is divided into three subgroups. The distribution of incomes within each group is different, too; the median of group A is $7,000, lower than the mean, while the median of group B is $13,000, higher than the mean. Group C is the combination of groups A and B, with a mean income of $10,000. 

Figure 2.7 shows the aggregate behavior of the three groups, using (2.20). Because mode choice is a function of income as well as travel time, and each group has a different composition, the aggregate modal splits of groups A and B differ by as much as 30 percent over the range of transit in-vehicle times from 5 to 50 minutes. Furthermore, the behaviors of the two groups are each different from the aggregate behavior of the combined group C, as predicted on the basis of the average income for group C. 


Table 2.6 Example of aggregate mode choice


<table><tr><td rowspan="2">Subgroup</td><td rowspan="2">Size</td><td rowspan="2">Mean annual income</td><td colspan="8">Number choosing transit for <eq>t_{T} =</eq></td></tr><tr><td>50</td><td>40</td><td>30</td><td>25</td><td>20</td><td>15</td><td>10</td><td>5</td></tr><tr><td>A1</td><td>500</td><td>$4,000</td><td>250</td><td>500</td><td>500</td><td>500</td><td>500</td><td>500</td><td>500</td><td>500</td></tr><tr><td>A2</td><td>300</td><td>10,000</td><td>0</td><td>0</td><td>0</td><td>0</td><td>150</td><td>300</td><td>300</td><td>300</td></tr><tr><td>A3</td><td>200</td><td>16,000</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>200</td><td>200</td></tr><tr><td>Total A</td><td>1,000</td><td></td><td>250</td><td>500</td><td>500</td><td>500</td><td>650</td><td>800</td><td>1,000</td><td>1,000</td></tr><tr><td>Average A</td><td></td><td>8,200</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1,000</td><td>1,000</td><td>1,000</td><td>1,000</td></tr><tr><td>B1</td><td>200</td><td>4,000</td><td>100</td><td>200</td><td>200</td><td>200</td><td>200</td><td>200</td><td>200</td><td>200</td></tr><tr><td>B2</td><td>300</td><td>10,000</td><td>0</td><td>0</td><td>0</td><td>0</td><td>150</td><td>300</td><td>300</td><td>300</td></tr><tr><td>B3</td><td>500</td><td>16,000</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>500</td><td>500</td></tr><tr><td>Total B</td><td>1,000</td><td></td><td>100</td><td>200</td><td>200</td><td>200</td><td>350</td><td>500</td><td>1,000</td><td>1,000</td></tr><tr><td>Average B</td><td></td><td>11,800</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1,000</td><td>1,000</td><td>1,000</td></tr><tr><td>C1</td><td>700</td><td>4,000</td><td>350</td><td>700</td><td>700</td><td>700</td><td>700</td><td>700</td><td>700</td><td>700</td></tr><tr><td>C2</td><td>600</td><td>10,000</td><td>0</td><td>0</td><td>0</td><td>0</td><td>300</td><td>600</td><td>600</td><td>600</td></tr><tr><td>C3</td><td>700</td><td>16,000</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>700</td><td>700</td></tr><tr><td>Total C</td><td>2,000</td><td></td><td>350</td><td>700</td><td>700</td><td>700</td><td>1,000</td><td>1,300</td><td>2,000</td><td>2,000</td></tr><tr><td>Average C</td><td></td><td>10,000</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1,000</td><td>2,000</td><td>2,000</td><td>2,000</td></tr></table>


Lines labeled "total" give total of those in subgroups choosing transit. Lines labeled "average" give the number of persons choosing transit based on the average income over subgroups. Group C is the combination of groups A and B. 


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/a9a45185-cfa1-407d-8a96-209400065f95/1aeb7de7e48968f00f1ec7503cd86ee709d3671446f7de636557f25e7e38d50b.jpg)



Figure 2.7 Effect of income distribution on aggregate mode choice.


It is important to note that at any given transit time each consumer at the same income level makes the same choice. However, different consumers at different incomes may make different choices at the same service level. Therefore, the aggregate choice of any grouping of consumers depends on the composition of the group. 

Thus, as in the freight example, the behavior of a group can, in principle at least, be derived by knowing the behaviors of the individuals in the group. Different groups with different distributions of individual characteristics can be expected to have different aggregate behaviors. Even if two groups have the same average characteristics—for example, the same average income—their behaviors may differ because the distributions of characteristics within the groups are different (see section 4.7). 

## 2.5 A SECOND MODEL OF CONSUMER BEHAVIOR

## 2.5.1 Appraisal of Consumer Behavior Model I

If we know (1) the set of alternatives each consumer has available to him, (2) the attributes of each alternative, and (3) the consumer's utility function, we have shown that we can use consumer behavior model I to predict the effects of transportation system changes. Clearly this is a useful model. However, it is important to be aware of its limitations. Consider the following: 

The alternatives: Do consumers really perceive all of the available alternatives? Do they consciously and deliberately consider every one of them? Or do they scan the set of alternatives and only examine carefully a small number? How does past experience influence which alternatives a consumer will consider explicitly? 

The consequences: How do consumers perceive consequences? What consequences do they consider important? What kinds of biases are there in their perceptions of those consequences? How are these perceptions biased by individual experiences, word of mouth, or other information? 

The decision process: Does the consumer go through a careful analysis and calculation of the consequences of each alternative to reach a decision? Does he really formalize his preferences explicitly in the form of an indifference curve? Does he even behave as if he had formalized his preferences in this way? Does he choose among all alternatives in a single step or in a sequence of decisions? 

The static nature of the model: Don't consumers change their information, and their preferences, over time? Don't they "learn" from actual experiences and sometimes shift choices? 

As an example, consider the introduction of a basically new transportation technology, such as a computer-routed-and-scheduled “dial-a-ride” minibus system. How will people respond to this new technology initially? How will their responses change as they gain experience with the new system? How will they perceive the alternatives? How will their perceptions of the consequences of using this system be biased by their own experiences or the experiences of friends or acquaintances? Model I does not deal with elements of behavior such as these. 

The major limitation of the model is that it assumes that the consumer has “perfect” information: he knows all of the alternatives open to him, he knows all of their characteristics, and he knows his own preferences so that he behaves as if he had a well-defined utility function. It is also a static model, in that it does not allow for changes in information over time. What would be more desirable is a behavioral model that explicitly incorporated the biases and limited perceptions of consumers making decisions and allowed for time-varying behavior. 

## 2.5.2 Consumer Behavior Model II

One important way of partially overcoming the limitations described in the preceding section is to recognize that the consumer does not make decisions with “perfect” information. That is, there is a random or probabilistic element that enters into his decision process. This random element can be expressed a number of ways. One useful approach is to introduce a random variable $\varepsilon$ , representing the probabilistic error, as an additive term in the utility function for each mode m: 

$$
U _ {m} = \alpha + \beta t _ {m} + \gamma c _ {m} + \varepsilon .\tag{2.21}
$$

The practical result of this addition is that now we do not know precisely which alternative the individual will choose, because we do not know precisely the values of utility he will place on each choice. We must therefore talk about the probability that individual i will choose alternative m. 

Several factors may contribute to this randomness: 

1. There may be service attributes that are important to some consum-

The Demand for Transportation 

ers but have not been explicitly represented in our estimation of their utilities (for example, comfort, perception of security, or other non-quantifiable attributes). 

2. Consumers may not perceive all the alternatives open to them or may not have correct information on the attributes of the alternatives (for example, because of poor marketing, consumers are often not aware of route and schedule information that might influence their decisions). 

3. There may be essentially random elements in the consumer's behavior, in that his preferences vary from day to day or are influenced by external events (for example, the weather or the availability of the family car). 

Models of individual behavior that include an explicit random element are often termed stochastic disaggregate models in the literature. Different assumptions about the form of the utility function and/or the nature of the random elements lead to different specific forms for this consumer behavior model II. 

## 2.5.3 An Example

To illustrate, we shall extend the previous deterministic model to include an explicit random element. 

In both the freight example and the urban example the consumers involved had linear utility functions: 

$$
U _ {m} = \sum_ {i = 1} ^ {3} W _ {i} s _ {m i},\tag{2.22}
$$

where $s_{m} = (s_{m1}, s_{m2}, s_{m3})$ is the vector of service attributes, 

$\mathbf{w} = (w_{1}, w_{2}, w_{3})$ is the vector of weights in the consumer's preference function, and there are two choice alternatives ( $m = 1, 2$ ). 

We now assume that the utility is composed of two parts, a deterministic part $u_{m} = \sum w_{i}s_{mi}$ and a random part $\varepsilon$ : 

$$
U _ {m} = u _ {m} + \varepsilon = \sum_ {i = 1} ^ {3} w _ {i} s _ {m i} + \varepsilon .\tag{2.23}
$$

The probability that the consumer chooses alternative 1, denoted by $p_{1}$ , is 

$$
p _ {1} = \operatorname{prob} (U _ {1} > U _ {2}).\tag{2.24}
$$

Similarly, 

$$
p _ {2} = \operatorname{prob} (U _ {2} > U _ {1}).\tag{2.25}
$$

Under certain assumptions about the probability distribution of $\varepsilon$ —specifically that $\varepsilon$ is Weibull-distributed (Charles River Associates 1972, Ben-Akiva 1973, 1974, McFadden 1975)—the following results are obtained: 

$$
p _ {1} = \frac {e ^ {u _ {1}}}{e ^ {u _ {1}} + e ^ {u _ {2}}},\tag{2.26}
$$

$$
p _ {2} = \frac {e ^ {u _ {2}}}{e ^ {u _ {1}} + e ^ {u _ {2}}}.\tag{2.27}
$$

Equations (2.26) and (2.27) define a particular stochastic disaggregate model, the binomial logit model. This can be generalized to the case where there are M alternative choices to form the multinomial logit model (MNL): 

$$
p (m: M) = \frac {e ^ {u _ {m}}}{\sum_ {m ^ {\prime} \in M} e ^ {u _ {m ^ {\prime}}}}.\tag{2.28}
$$

For the two-choice case it is instructive to define 

$$
G (\mathbf {S}) = u _ {1} (\mathbf {S}) - u _ {2} (\mathbf {S}),\tag{2.29}
$$

so that (2.26) and (2.27) become 

$$
p _ {1} = \frac {1}{1 + e ^ {u _ {2} - u _ {1}}} = \frac {1}{1 + e ^ {- G (\mathbf {S})}},\tag{2.30}
$$

$$
p _ {2} = \frac {1}{1 + e ^ {u _ {1} - u _ {2}}} = \frac {1}{1 + e ^ {G (S)}}.\tag{2.31}
$$

These probabilities are shown as functions of $G(\mathbf{S})$ in figure 2.8. If $u_{1} = u_{2}$ , then $G(\mathbf{S}) = 0$ and the probabilities of both choices are the same, 0.5. If, on the other hand, $u_{1} = u_{2} + A'$ , then $G = u_{1} - u_{2} = A'$ and $p_{1} = p_{1}'$ while $p_{2} = 1 - p_{1}' = p_{2}'$ . (Appendix A gives values of this reciprocal exponential for use in the exercises.) 

Finally, it should be noted that alternative assumptions about the probabilistic choice structure lead to other types of stochastic disaggregate models (see McFadden 1974b, Domencich and McFadden 1975, Ben-Akiva 1977). Logit models have been especially important in the early development of practical disaggregate models. Other potentially important models are those that do not have the “independence of irrelevant alternatives” property, such as the multinomial probit (Hausman and Wise 1976, Daganzo, Bouthelier, and Sheffi 1977, Lerman and Manski 1977) and the generalized extreme value model (McFadden 1978). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/a9a45185-cfa1-407d-8a96-209400065f95/743f50ffe8e56aabf7468c95f47a80a6f63975ae7bd7e7ceb96b4513ba9e2081.jpg)



Figure 2.8 Probabilistic choice.


While in this section we have used u and U to distinguish the deterministic and total utilities, respectively, in general we shall not make this distinction. 

## 2.6 NOTE ON DIFFERENCES WITH CLASSICAL TREATMENTS OF CONSUMER THEORY (OPTIONAL READING)

The formulation of the consumer behavior model I presented in this chapter is close to but different from standard presentations of consumer theory (Henderson and Quandt 1958, Baumol 1965, de Neufville and Stafford 1971). The differences, and the reasons for them, are as follows: 

1. Choices are considered to be among discrete objects rather than among continuous, infinitely variable combinations of commodities because most transport choices are among discrete items or combinations of items: destinations, modes, routes, and auto ownership levels are naturally discrete, and even variables such as trip frequency, shipment size (for freight), and time of trip are often treated as discrete choices (off-peak versus peak hours for the time of day of the trip; carload or less-than-carload for shipment size). 

2. Choices are characterized by the values of their attributes rather than by quantities of commodities in a mix of commodities. This is a natural consequence of the first point; the only way to characterize a set of discrete objects (except by the name of each object) is by its characteristics with respect to a common set of attributes. The intellectual basis of this approach derives from Lancaster (1966) and Quandt (1970a), as articulated for transportation demand by Quandt (1970b) (although the practical applications, such as travel time ratios used for diversion curves, antedated these theoretical concepts): "The crucial modification [in this approach] is that the consumer is now regarded as deriving utility from characteristics or attributes while commodities are regarded as producing attributes in varying amounts and proportions" (p. 5). This is especially important in areas where the number of available commodities may change—for example, by the introduction of a new commodity, such as a new transportation service, to the market. 

3. Utility is maximized, constrained only by the set of available choices; no explicit budget constraint is included. Since the set of available choices is discrete, if the set is bounded (finite, or infinite and bounded), there is at least one choice that has the maximum utility of any in the set. Therefore there is no methodological reason why a budget constraint is necessary to yield a choice. Equally important, in the domain of transportation choices there is no reason to continue the emphasis on budget constraints used in standard consumer theory. First, the amount of household or firm monetary resources spent on transportation is usually only a modest portion of the available resources and is therefore almost never constrained by budget limits. Second, attributes other than monetary cost may play more important roles as constraints in many situations (a travel time budget constraint, a maximum walk distance or waiting time constraint, a “maximum probability of loss or damage” constraint). The most general approach is a general utility function that can potentially include all attributes identically. If in a specific situation the levels of one or more attributes become subject to constraints—or, equally, to “satisficing” behavior (see Simon 1960)—a specific formulation of the utility function can be established (for example, maximizing utility subject to a constraint on one or more specific attributes). 

## 2.7 SUMMARY

## 2.7.1 The Need to Understand Human Behavior

Changes in the transportation system of a region affect the patterns of social and economic activity. Over the long term changes occur in the distribution and intensity of these activities; in the short term many individuals may change decisions about modes and routes of travel and many firms may change the modes and routes they use to ship to particular markets. 

To predict how the many individuals and firms in a region will respond to changes in the transportation system, we need to understand human behavior: We need to understand present behavior, and we need a deep enough understanding of the basis of that behavior to be able to predict how individuals and firms will change their behaviors in response to a variety of factors. 

This understanding of actual and potential behavior can be represented in the form of a demand function. In transportation it is important to emphasize that the alternatives the consumer considers are, first and foremost, activities. For passenger travel these activity choices are about what to do, where and when to do it. For freight movements the choices are about what products to sell where. Included in these activity choices are corresponding choices of means of transport (both mode and route). Thus the demand for transport is derived from a demand for activities. 

As a useful working hypothesis, the total demand is separated into two parts: a transportation demand function predicts how individuals or firms, or groups of individuals or firms, will change transportation choices; an activity-shift function predicts how they will change locational choices. 

## 2.7.2 Behavior at the Individual Level

A consumer is any individual or group of individuals, such as a household or firm, that behaves as a single unit in making transportation decisions. 

A model of consumer behavior must indicate what alternative choices the consumer perceives, what consequences he considers important, and how his choice is made from among the perceived alternatives. For travel demand analysis, the choices are various combinations of transportation decisions. The attributes to be considered form the service vector S, which characterizes the various transportation choices. The decision process model then indicates how the consumer operates on these choices and their attributes to reach a decision, based upon his characteristics and preferences. 

Two models for describing the behavior of an individual consumer have been described. Consumer behavior model I assumes that the consumer formulates his preferences explicitly, identifies explicitly all the alternatives open to him and the consequences of each alternative, and evaluates and chooses among the alternatives using a well-defined decision rule based upon his expressed preferences. A key feature of this model is that the consumer expresses his preferences as a utility function defined over all combinations of attributes of the alternatives. The decision rule follows: the consumer picks the alternative that has the maximum value of this utility. 

This model is useful as a representation of the behavior of consumers of transportation. Once the utility function is known, it can be used to predict how a particular consumer will respond to changes in service attributes of the available choices or will accept trade-offs among different service attributes; how different consumers with different preferences will make different choices; how groups of consumers will behave; and how choices will change as a result of changes in socioeconomic characteristics that are then reflected in changed preferences. 

This model is limited, however, in that it assumes that the consumer has perfect information, operates in complete consistency with his well-defined utility function, and does not learn from experience. Consumer behavior model II overcomes some of the limitations of this model by introducing an explicit probabilistic element. This can represent incomplete information on alternatives or their consequences, a poorly defined preference function, or intrinsic randomness in human behavior. Particular assumptions about the mathematical forms of the utility function and of this random element lead to various forms of stochastic disaggregate models. 

Stochastic disaggregate models also assume that the consumer maximizes his utility. Since they include an explicit probabilistic element, such models predict the probability of a consumer making a specific choice. 

## TO READ FURTHER

For basic presentations of the conventional treatment of consumer theory see Henderson and Quandt (1958), Baumol (1965), or de Neufville and Stafford (1971). For a comprehensive but advanced treatment of stochastic disaggregate models see Domencich and McFadden (1975) and also the suggestions in chapters 4 and 11. We shall treat activity-system shifts only briefly in this volume (chapter 8). The reader interested in this area might begin by consulting the following: Isard 

(1960, 1975), Alonso (1965), Kresge and Roberts (1971), Edel and Rothenburg (1972), Echenique et al. (1974), James (1974), Senior (1974), and Lerman (1976). 

## EXERCISES

2.1(E) Consider the urban commuters discussed in section 2.4.2. a. Consider a commuter with an annual income of $10,000. By how much would a parking lot operator have to reduce the parking charge of 60¢ to attract this consumer back to automobile from transit after the transit frequency has been doubled? 

b. If the consumer's annual income were $20,000, by how much would transit waiting time have to be decreased to attract him from automobile to transit? 

c. Consider the initial conditions. At what income level will the consumer shift from transit to automobile? 

d. Consider the relationship behind figure 2.5: 

i. Verify the curve shown in the figure. 

ii. How would the in-vehicle time necessary to cause a shift in mode change if frequency were doubled? Develop numbers and sketch curve. 

iii. How would the in-vehicle time necessary to cause a shift in mode change if frequency were halved? 

2.2(C) In the urban passenger travel example in this chapter, the characteristics of the consumer influence the weight placed on cost. In the freight example different consumers have different weights on all service attributes. Is there any difference between these two approaches? 

2.3(P) Using the results of section 2.4.2, show graphically, as a function of income, (a) the transit travel time at which riders are indifferent between auto and transit, and (b) the transit out-of-vehicle time at which riders are indifferent between auto and transit. Compare and discuss. 

# Case Study I: Disaggregate Prediction of Behavior

## 3.1 INTRODUCTION

In this chapter we consider an example of a stochastic disaggregate demand model and explore its use for predicting responses of different consumers to various conditions. We also demonstrate how demand models can be used for prediction in a simple and direct way, with only pencil-and-paper calculations (after Jessiman and Kocur 1975, Cambridge Systematics 1976b, Kocur, Rushfeldt, and Millican 1977, Kocur et al. 1977). 

## 3.2 AN URBAN MODE-CHOICE MODEL

## 3.2.1 The Model

Consider the following urban transportation mode-choice model: 

$$
p (m: M) = \frac {e ^ {U _ {m}}}{\sum_ {m ^ {\prime} \in M} e ^ {U _ {m ^ {\prime}}}},\tag{3.1}
$$

$$
U _ {m} = \theta_ {m} + \theta_ {1} t _ {m} + \theta_ {2} \frac {x _ {m}}{d} + \theta_ {3} \frac {c _ {m}}{y},\tag{3.2}
$$

where 

$p(m: M) = \text{probability of an individual choosing mode } m$ 

$t_{m} =$ in-vehicle time (minutes, one-way) 

$x_{m} = \text{out-of-vehicle time (minutes, one-way)}$ 

d = distance (miles, one-way) 

$c_{m} =$ out-of-pocket cost (cents, one-way) 

y = annual income (dollars) 

m = automobile (A) or transit (T). 

The parameters $\theta_{1}, \theta_{2}$ , and $\theta_{3}$ are the same for both modes; $\theta_{m}$ is specific to each mode. In the case of two modes, one constant can be arbitrarily set to zero (for example, $\theta_{T}$ ), since only the difference $\theta_{T} - \theta_{A}$ influences the mode choice. 

Define $G(\mathbf{S})$ as follows: 

$$
p (m = T) = \frac {e ^ {U _ {\mathrm{T}}}}{e ^ {U _ {\mathrm{T}}} + e ^ {U _ {\mathrm{A}}}} = \frac {1}{1 + e ^ {U _ {\mathrm{A}} - U _ {\mathrm{T}}}} = \frac {1}{1 + e ^ {G (\mathrm{S})}},\tag{3.3}
$$

where 

$$
\begin{array}{r l} G (\mathbf {S}) & = U _ {\mathrm{A}} - U _ {\mathrm{T}} \\ & = (\theta_ {\mathrm{A}} - \theta_ {\mathrm{T}}) + \theta_ {1} (t _ {\mathrm{A}} - t _ {\mathrm{T}}) + \frac {\dot {\theta_ {2}}}{d} (x _ {\mathrm{A}} - x _ {\mathrm{T}}) + \frac {\theta_ {3}}{\gamma} (c _ {\mathrm{A}} - c _ {\mathrm{T}}). \end{array}\tag{3.4}
$$

Values of the parameters have been determined empirically: 

$$
\theta_ {1} = - 0. 0 3 0, \qquad \theta_ {2} = - 0. 3 4, \qquad \theta_ {3} = - 5 0.\tag{3.5}
$$

The value of the mode-specific constant $\theta_{\mathrm{A}}$ reflects the socio-economic characteristics of the worker and the household. We consider two examples: household type $A$ with $y = \$5,000$ and $\theta_{\mathrm{A}} = -0.13$ ; and household type $B$ with $y = \$10,000$ and $\theta_{\mathrm{A}} = 0.32$ . 

## 3.2.2 Basic Calculations

Now consider the following situation: 

$$
\begin{array}{r l r} {t _ {\mathrm{A}} = 1 1. 3 \min} & & {t _ {\mathrm{T}} = 1 4 \min} \\ {x _ {\mathrm{A}} = 5 \min} & & {x _ {\mathrm{T}} = 8 \min} \\ {c _ {\mathrm{A}} = 1 2 2. 5 \text {¢}} & & {c _ {\mathrm{T}} = 5 0 \text {¢}} \\ {d = 7. 2 5 \mathrm{miles}.} \end{array}\tag{3.6}
$$

Then, for household type A, 

$$
\begin{array}{r l} {U _ {\mathrm{A}}} & {= - 0. 1 3 - 0. 0 3 (1 1. 3) - 0. 3 4 (5 / 7. 2 5) - 5 0 (1 2 2. 5 / 5, 0 0 0)} \\ & {= - 0. 1 3 - 0. 3 4 - 0. 2 3 - 1. 2 3} \\ & {= - 1. 9 3,} \\ {U _ {\mathrm{T}}} & {= - 0. 0 3 (1 4) - 0. 3 4 (8 / 7. 2 5) - 5 0 (5 0 / 5, 0 0 0)} \\ & {= - 1. 3 0,} \\ {e ^ {U _ {\mathrm{A}}}} & {= 0. 1 5, \qquad e ^ {U _ {\mathrm{T}}} = 0. 2 7,} \end{array}
$$

so the probability of choosing transit is 

$$
p _ {\mathrm{T}} = \frac {e ^ {U _ {\mathrm{T}}}}{e ^ {U _ {\mathrm{T}}} + e ^ {U _ {\mathrm{A}}}} = \frac {0 . 2 7}{0 . 4 2} = 0. 6 5.\tag{3.7}
$$

An alternative way to perform these calculations is to use the difference in utilities (3.4): 

$$
G (\mathbf {S}) = U _ {\mathrm{A}} - U _ {\mathrm{T}} = - 1. 9 3 + 1. 3 0 = - 0. 6 3,\tag{3.8}
$$

$$
p _ {\mathrm{T}} = \frac {e ^ {U _ {\mathrm{T}}}}{e ^ {U _ {\mathrm{T}}} + e ^ {U _ {\mathrm{A}}}} = \frac {1}{1 + e ^ {U _ {\mathrm{A}} - U _ {\mathrm{T}}}} = \frac {1}{1 + e ^ {- 0 . 6 3}} = 0. 6 5,\tag{3.9}
$$

$$
p _ {\mathrm{A}} = \frac {e ^ {U _ {\mathrm{A}}}}{e ^ {U _ {\mathrm{A}}} + e ^ {U _ {\mathrm{T}}}} = \frac {1}{1 + e ^ {U _ {\mathrm{T}} - U _ {\mathrm{A}}}} = \frac {1}{1 + e ^ {0 . 6 3}} = 0. 3 5.\tag{3.10}
$$

Thus, for a worker in this household, transit has the highest probability, and we predict that this individual would choose transit. For a group of 100 identical individuals, we would expect that 35 percent would choose automobile and 65 percent would choose transit. 

A similar calculation for household type B shows that 

$$
\begin{array}{l} {U _ {\mathrm{A}} = - 0. 8 7, \qquad U _ {\mathrm{T}} = - 1. 0 5,} \\ {U _ {\mathrm{A}} - U _ {\mathrm{T}} = + 0. 1 8, \qquad p _ {\mathrm{T}} = 0. 4 6, \qquad p _ {\mathrm{A}} = 0. 5 4.} \end{array}\tag{3.11}
$$

Again we predict that this individual would choose transit over automobile. Correspondingly, out of 100 identical individuals, 54 percent would choose automobile and 46 percent would choose transit. This example shows that differences in socioeconomic characteristics are often reflected in different transportation demands. 

## 3.2.3 Use of Worksheets

Worksheets provide a good means of organizing the calculations involved in prediction, especially when computers are not available or when the computations are to be done on a pocket calculator or by assistants without advanced technical training. 

The logic of the worksheet shown in figure 3.1 is directly related to the preceding calculations. First, the levels of service $(t, x, c)$ , the model parameters $(\theta_{i})$ , and other data (distance, income) are provided as inputs. Then, in steps 1.1 and 1.2, the automobile and transit utilities are computed. In step 2 the mode-choice probabilities are computed using the exponential functions of utility as required for the logit model. In step 3, if the number of individuals in each group, or "market segment," is known, the expected number making each choice can be calculated. A worked example is given in the figure, repeating the earlier calculations. The market-segment sizes are arbitrarily taken as 100 individuals. 

## 3.3 THE EFFECTS OF VARIATIONS IN SERVICE LEVELS

## 3.3.1 Parametric Variations

The effects of variations in service levels can be explored with this model. As an example, consider the effects of a variation in transit fare from the present level of 50 cents to values of 0, 25, 75, 100, 125, 150, and 175 cents. The results are graphed in figure 3.2. 

Worksheet 1 

Estimation of Volumes 

$$
\text { Policy:   Base   Case }
$$

$$
\begin{array}{c} \text {Market Segment:} \underline {{\text {Household}}} \\ \text {Type A} \\ \text {Origin:} \underline {{\text {Zone I}}} \\ \text {Destination:} \underline {{\text {Zone IV}}} \\ \text {Assumptions:} \\ \text {By:} \underline {{\text {MLM}}} \\ \text {Date:} 6 / 2 1 / 7 7 \end{array}
$$

## 1. Utility for each mode

1.1 Auto 

$$
\begin{array}{l l} (t) & (\theta_ {1} = 0. 0 3 0) \\ \boxed {1 1. 3 \min} & \times \boxed {- 0. 0 3} \end{array}\tag{1.1-1}
$$

$$
= \boxed {- 0. 3 4}\tag{1.1-2}
$$

$$
+ \boxed {5} \div \boxed {7. 2 5} \times \boxed {- 0. 3 4} = \boxed {- 0. 2 3}\tag{1.1-3}
$$

$$
+ \boxed {1 2 2. 5} \div \boxed {5, 0 0 0} \times \boxed {- 5 0} = \boxed {- 1. 2 3}
$$

$$
1 - 4) + \boxed {- 0. 1 3}\tag{1.1-4}
$$

$$
= \boxed { \begin{array}{c} + \\ - 0. 1 3 \end{array} }\tag{1.1-5}
$$

$$
\text { Total   utility } (U _ {\mathrm{A}}) = \boxed {- 1. 9 3}
$$

## 1.2 Transit

$$
\begin{array}{l l} (t) & (\theta_ {1} = - 0. 0 3 0) \\ \boxed {1 4. 0} & \times \boxed {- 0. 0 3 0} \end{array}\tag{1.2-1}
$$

$$
= \boxed {- 0. 4 2}\tag{1.2-2}
$$

$$
+ \boxed {8} \div \boxed {7. 2 5} \times \boxed {- 0. 3 4} = \boxed {- 0. 3 8}\tag{1.2-3}
$$

$$
+ \boxed {5 0} \div \boxed {5, 0 0 0} \times \boxed {- 5 0} = \boxed {- 0. 5 0}\tag{1.2-4}
$$

$$
\text { Total   utility } (U _ {\mathrm{T}}) = \boxed {- 1. 3 0}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/a9a45185-cfa1-407d-8a96-209400065f95/7583a6a0fdad120adc0ac4cc09995f83fe0fa238bd8f3d68abde7a6e2cf895fb.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/a9a45185-cfa1-407d-8a96-209400065f95/89517e829850ce2aa8ead9cc0be4b1e794448ee42afd254f57414e8ccd723b4b.jpg)


## 2. Modal Probabilities

(2-1) 

(2-2) 

(2-3) 

## 3. Modal Volumes

(3-1) 

(3-2) 


Figure 3.1 Volume estimation worksheet with a sample calculation for household type A.


To perform these calculations a reduced form of the model can be derived and used as follows. From (3.3) and (3.4): 

$$
\begin{array}{l} p _ {\mathrm{T}} = \frac {1}{1 + e ^ {G (\mathbf {S})}}, \\ G (\mathbf {S}) = U _ {\mathrm{A}} - U _ {\mathrm{T}} \\ \qquad = (\theta_ {\mathrm{A}} - \theta_ {\mathrm{T}}) + \theta_ {1} (t _ {\mathrm{A}} - t _ {\mathrm{T}}) + \frac {\theta_ {2}}{d} (x _ {\mathrm{A}} - x _ {\mathrm{T}}) + \frac {\theta_ {3}}{\gamma} (c _ {\mathrm{A}} - c _ {\mathrm{T}}). \end{array}\tag{3.12}
$$

(3.13) 

Since the only component of S that will vary will be $c_{T}$ . 

$$
G (\mathbf {S}) = \alpha_ {0} + \alpha_ {1} \mathbf {c} _ {\mathrm{T}},\tag{3.14}
$$

where 

$$
\begin{array}{l} \alpha_ {0} = (\theta_ {\mathrm{A}} - \theta_ {\mathrm{T}}) + \theta_ {1} (t _ {\mathrm{A}} - t _ {\mathrm{T}}) + \frac {\theta_ {2}}{d} (x _ {\mathrm{A}} - x _ {\mathrm{T}}) + \frac {\theta_ {3} c _ {\mathrm{A}}}{y} \\ = U _ {\mathrm{A}} - \theta_ {\mathrm{T}} - \theta_ {1} t _ {\mathrm{T}} - \frac {\theta_ {2}}{d} x _ {\mathrm{T}}, \end{array}\tag{3.15}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/a9a45185-cfa1-407d-8a96-209400065f95/732a0320f63e594671f156241b9df38b8bf8263e2964fbe0d2c25c958124a26e.jpg)



Figure 3.2 Effect of fare variations on the transportation decisions of households at two income levels and facing two different sets of service characteristics.


$$
\alpha_ {1} = - \frac {\theta_ {3}}{\gamma}.\tag{3.16}
$$

By reference to figure 3.1, we see that for household type A, 

$$
\alpha_ {0} = - 1. 9 3 + 0 + 0. 4 2 + 0. 3 8 = - 1. 1 3,\tag{3.17}
$$

$$
\alpha_ {1} = \frac {5 0}{5 , 0 0 0} = 0. 0 1.\tag{3.18}
$$

Thus the methodology for this calculation is as follows: 

Step 1. For the particular household type and basic conditions, calculate $\alpha_{0}$ and $\alpha_{1}$ as given by (3.15) and (3.16). 

Step 2. For each transit fare $c_{T}$ being considered: 

2.1 Calculate $\alpha_{1}c_{\mathrm{T}}$ 

2.2 Calculate $G(\mathbf{S}) = \alpha_0 + \alpha_1\mathbf{c}_{\mathrm{T}}$ . 

2.3 Calculate $p_{T}$ by (3.12). 

Figure 3.3 shows a worksheet format for systematic execution of this calculation. Sample numerical results are given in the figure and in table 3.1. (Note that $\alpha_{0} = U_{A} - U_{T}^{*}$ .) Figure 3.2 shows the results graphically for household types A and B. 

Worksheet 2 Estimation of Volumes for Transit Fare Variations 

$$
\text { Policy: } \frac {\text { Transit   Fare }}{\text { Variations }}
$$

$$
\text { Market   Segment: } \frac {\text { Household }}{\text { Type   A }}
$$

$$
\begin{array}{c} \text {Origin:} \\ \text {Destination:} \\ \text {Assumptions:} \end{array}
$$

$$
\begin{array}{c} \text {By: MLM} \\ \text {Date: 6 / 21 / 77} \end{array}
$$

## 1. Basic constants

1.1 Auto utility 

$$
\begin{array}{l l} (t) & (\theta_ {1} = - 0. 0 3 0) \\ \boxed {1 1. 3} & \times \boxed {- 0. 0 3} \end{array}\tag{1.1-1}
$$

$$
= \sqrt {- 0 . 3 4}\tag{1.1-2}
$$

$$
+ \boxed {5} \div \boxed {7. 2 5} \times \boxed {- 0. 3 4} = \boxed {- 0. 2 3}\tag{1.1-3}
$$

$$
+ \boxed {1 2 2. 5} \div \boxed {\text {(income)}} \times \boxed {- 5 0} = \boxed {+ - 1. 2 3}\tag{1.1-4}
$$

$$
= \boxed { \begin{array}{c} + \\ - 0. 1 3 \end{array} }\tag{1.1-5}
$$

$$
\text { Total   utility } \left(U _ {\mathrm{A}}\right) = \boxed {- 1. 9 3}
$$

1.2 Transit utility components 

$$
\begin{array}{l l} (t) & (\theta_ {1} = - 0. 0 3 0) \\ \boxed {1 4. 0} & \times \boxed {- 0. 0 3 0} \end{array}\tag{1.2-1}
$$

$$
= \boxed {- 0. 4 2}\tag{1.2-2}
$$

$$
+ \boxed {8} \div \boxed {7. 2 5} \times \boxed {- 0. 3 4} = \boxed {- 0. 3 8}\tag{1.2-3}
$$

$$
\text { Partial   utility } (U _ {\mathrm{T}} ^ {*}) = \boxed {- 0. 8 0}
$$

1.3 Constant 

$$
\begin{array}{c c} (U _ {\mathrm{A}}) & (U _ {\mathrm{T}} ^ {*}) \\ \hline - 1. 9 3 & - \boxed {- 0. 8 0} \end{array}\tag{1.3-1}
$$

$$
= \boxed {- 1. 1 3}
$$

1.4 Variable term 

$$
\begin{array}{l l} \theta_ {3} = - 5 0 & (\text { income }) \\ \boxed {- 5 0} & \div \boxed {5, 0 0 0} \end{array} \times (- 1)\tag{1.4-1}
$$

$$
= \boxed { \begin{array}{c} (\alpha_ {1}) \\ + 0. 0 1 \end{array} }
$$

## 2. Parametric variations

<table><tr><td>Transitfare<eq>c_{\mathrm{T}}(\phi)</eq></td><td><eq>\alpha_{1}c_{\mathrm{T}}</eq></td><td><eq>\alpha_{0}</eq></td><td><eq>G(\mathbf{S}) =</eq><eq>\alpha_{0} + \alpha_{1}c_{\mathrm{T}}</eq></td><td><eq>e^{G(\mathbf{S})}</eq></td><td><eq>1 + e^{G(\mathbf{S})}</eq></td><td><eq>p_{\mathrm{T}} =</eq><eq>[1 + e^{G(\mathbf{S})}]^{-1}</eq></td><td><eq>p_{\mathrm{A}} =</eq><eq>1 - p_{\mathrm{T}}</eq></td></tr><tr><td>0</td><td>0</td><td>-1.13</td><td>-1.13</td><td>0.32</td><td>1.32</td><td>0.76</td><td>0.24</td></tr><tr><td>25</td><td>0.25</td><td>-1.13</td><td>-0.88</td><td>0.42</td><td>1.42</td><td>0.71</td><td>0.29</td></tr><tr><td>50</td><td>0.50</td><td>-1.13</td><td>-0.63</td><td>0.53</td><td>1.53</td><td>0.65</td><td>0.35</td></tr><tr><td>75</td><td>0.75</td><td>-1.13</td><td>-0.38</td><td>0.68</td><td>1.68</td><td>0.60</td><td>0.40</td></tr><tr><td>100</td><td>1.00</td><td>-1.13</td><td>-0.13</td><td>0.88</td><td>1.88</td><td>0.53</td><td>0.47</td></tr><tr><td>125</td><td>1.25</td><td>-1.13</td><td>+0.12</td><td>1.13</td><td>2.13</td><td>0.47</td><td>0.53</td></tr><tr><td>150</td><td>1.50</td><td>-1.13</td><td>+0.37</td><td>1.45</td><td>2.45</td><td>0.41</td><td>0.59</td></tr><tr><td>175</td><td>1.75</td><td>-1.13</td><td>+0.62</td><td>1.86</td><td>2.86</td><td>0.35</td><td>0.65</td></tr></table>


Figure 3.3 Volume estimation worksheet for transit fare variations with a sample calculation for household type A.



Table 3.1 Effect of transit fare variations by household type


<table><tr><td rowspan="2">Transitfare (ø)</td><td colspan="2">Type A(low income, walk distance)</td><td colspan="2">Type B(medium in- come, walk distance)</td><td colspan="2">Type C(low income, beyond walk distance)</td><td colspan="2">Type D(medium in- come, beyond walk distance)</td></tr><tr><td><eq>P_A</eq></td><td><eq>P_T</eq></td><td><eq>P_A</eq></td><td><eq>P_T</eq></td><td><eq>P_A</eq></td><td><eq>P_T</eq></td><td><eq>P_A</eq></td><td><eq>P_T</eq></td></tr><tr><td>0</td><td>0.24</td><td>0.76</td><td>0.48</td><td>0.52</td><td>0.31</td><td>0.69</td><td>0.58</td><td>0.42</td></tr><tr><td>25</td><td>0.29</td><td>0.71</td><td>0.51</td><td>0.49</td><td>0.37</td><td>0.63</td><td>0.61</td><td>0.39</td></tr><tr><td>50</td><td>0.35</td><td>0.65</td><td>0.54</td><td>0.46</td><td>0.43</td><td>0.57</td><td>0.64</td><td>0.36</td></tr><tr><td>75</td><td>0.40</td><td>0.60</td><td>0.57</td><td>0.43</td><td>0.49</td><td>0.51</td><td>0.67</td><td>0.33</td></tr><tr><td>100</td><td>0.47</td><td>0.53</td><td>0.60</td><td>0.40</td><td>0.55</td><td>0.45</td><td>0.69</td><td>0.31</td></tr><tr><td>125</td><td>0.53</td><td>0.47</td><td>0.63</td><td>0.37</td><td>0.62</td><td>0.38</td><td>0.72</td><td>0.28</td></tr><tr><td>150</td><td>0.59</td><td>0.41</td><td>0.66</td><td>0.34</td><td>0.67</td><td>0.33</td><td>0.75</td><td>0.25</td></tr><tr><td>175</td><td>0.65</td><td>0.35</td><td>0.69</td><td>0.31</td><td>0.72</td><td>0.28</td><td>0.77</td><td>0.23</td></tr></table>

## 3.3.2 Differences in Base Service Levels

We now consider two other household types, C and D, with the same socioeconomic characteristics as A and B, respectively. They differ from A and B in that their base levels of service are different: 

$$
\begin{array}{l l} t _ {\mathrm{A}} = 1 4. 2 \min & t _ {\mathrm{T}} = 2 1. 7 \min \\ x _ {\mathrm{A}} = 5 \min & x _ {\mathrm{T}} = 1 5. 5 \min \\ c _ {\mathrm{A}} = 1 3 1. 3 ¢ & c _ {\mathrm{T}} = 7 5 ¢ \\ d = 8. 1 3 \text {miles}. \end{array}\tag{3.19}
$$

The base mode splits are, for C, $p_{T} = 0.57$ and, for D, $p_{T} = 0.36$ . The effects of transit fare variations are shown in table 3.1 and figure 3.2. 

Note that the same model is being used to represent the behavior of individuals with different socioeconomic characteristics in the same circumstances, that is, with the same service levels (A vs. B, C vs. D); and individuals with the same socioeconomic characteristics in different situations (A and C, B and D). This is the real power of demand models: they represent behavior in a generalized way such that the different behaviors of individuals in different situations can be predicted. 

## 3.4 SERVICE LEVELS

So far we have used the demand model to predict consumer responses without going into how we actually obtain values of the service attributes. In this section we examine this question and see how differences in service levels arise and how these differences affect behavior. 

Figure 3.4 shows an urban corridor, with a rapid transit line and an expressway connecting the centers of the four zones. A network of streets covers the area. There is a rapid-transit station at the center of each zone. Table 3.2 gives the typical speeds of the various transportation facilities in the corridor. In addition, we must know the transit waiting time. Pecknold, Wilson, and Kullman (1972) reported the following empirical function for urban bus operations: 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/a9a45185-cfa1-407d-8a96-209400065f95/439fe5205eb92c93c63037aca06858eba767d99df541dd12acb7780b6ff5ac05.jpg)



Rapid transit line and parallel expressway



Figure 3.4 Characteristics of an urban corridor.



Table 3.2 Typical speeds of various transportation modes in an urban corridor


<table><tr><td>Mode</td><td><eq>Speed^a</eq></td></tr><tr><td>Walking</td><td>3 mph = 0.05 mpm (4.8 kph = 0.08 kpm)</td></tr><tr><td>Auto, local streets(peak period)</td><td>18 mph = 0.30 mpm (29.0 kph = 0.48 kpm)</td></tr><tr><td>Auto, expressway</td><td>40 mph = 0.67 mpm (64.4 kph = 1.07 kpm)</td></tr><tr><td>Bus-feeder, local <eq>streets^b</eq></td><td>8 mph = 0.13 mpm (12.9 kph = 0.21 kpm)</td></tr><tr><td>Bus-express, expressway</td><td>50 mph = 0.83 mpm (80.5 kph = 1.34 kpm)</td></tr><tr><td>Light rail transit(grade-separated)<eq>^b</eq></td><td>22 mph = 0.37 mpm (35.4 kph = 0.59 kpm)</td></tr><tr><td>Rail rapid <eq>transit^b</eq></td><td>30 mph = 0.50 mpm (48.3 kph = 0.81 kpm)</td></tr></table>


$^{a}$ mph = miles per hour; mpm = miles per minute; kph = kilometers per hour; kpm = kilometers per minute. 



$^{b}$ Average, taking stops into account. 



Note: Speeds vary greatly according to specific local conditions. 


$$
\text { waiting   time } = \left\{ \begin{array}{l l} h / 2 & \text { for } 0 \leq h \leq 1 8. 3, \\ 5. 5 + 0. 2 h & \text { for } h \geq 1 8. 3, \end{array} \right.\tag{3.20}
$$

where h is the headway (interval) between vehicles in minutes. The cutoff at h = 18.3 simply indicates the tendency of people to know scheduled arrival times on systems with long headways. 

## 3.4.1 Trip Profiles

In a trip from home to work a traveler will generally use a combination of transportation means. Figures 3.5 and 3.6 show a sampling of possible combinations. The trip profiles in which transit is used are particularly varied, and only four possible combinations of feeder and line-haul services are shown. (Note that additional complexities could exist, such as one or more transfers within the line-haul system.) 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/a9a45185-cfa1-407d-8a96-209400065f95/8aec1a8325abf1674afa00f903234cba37cd27403e54ae659dedaa9f0e896bd2.jpg)



Figure 3.5 Trip profile—auto. * = out-of-vehicle time. After Jessiman and Kocur (1975).


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/a9a45185-cfa1-407d-8a96-209400065f95/d7174ced3cd09603801c6ecf912e6e7c177bcd805b16d12f7317cdf7b9f2f6e2.jpg)



Figure 3.6 Trip profiles—transit. * = out-of-vehicle time. After Jessiman and Kocur (1975).


## 3.4.2 Worksheets

Determining the levels of service over a path for a set of trip profiles is conceptually simple but requires careful attention to detail. To assist in this process it is often helpful to use worksheets similar to those introduced earlier for calculating choice probabilities. Figure 3.7 shows such a worksheet for calculating service levels. (The speeds indicated are those of table 3.2; other assumptions may be appropriate in various contexts.) 

## 3.4.3 Examples

## CASE I: WITHIN WALK DISTANCE OF TRANSIT STATION

CASE 1: WITHIN WALK DISTANCE OF TRANSIT STATION
Two individuals live within walk distance of a transit station, in zone 1, and work in the central business district (CBD), zone 4. (Generally it is assumed that the maximum acceptable walk distance is 0.25 mile or 0.4 kilometer.) One individual is a member of a household of type A; the second, of type B. Both have essentially the same trip profiles open to them for travel between home and work: 

1. For automobile: 

- Walk to auto, garaged at home: distance essentially negligible. 

- Drive over local streets to arterial street: distance about 1/8 mile; in-vehicle time = 0.4 min. 

- Drive on expressway to CBD zone: 7 miles; in-vehicle time = 10.5 min. 

- Drive over local streets to parking location: about 1/8 mile; in-vehicle time = 0.4 min. 

- Time spent parking car: 3 min (parking charge $1.00 per day, or 50¢ each direction); out-of-vehicle time = 3 min; cost = 50¢. 

- Walk to workplace: about 0.1 mile; out-of-vehicle time = 2 min. 

- Auto operating costs: about 10¢ per vehicle-mile, for 7.25 miles; cost = 72.5¢. 

- Totals: in-vehicle time = 11.3 min; out-of-vehicle time = 5 min; cost = 122.5¢. 

- Total auto in-vehicle distance = 7.25 miles; total distance = 7.35 miles. 

## Worksheet 3

Service Levels 

Market Segment: 

Origin: 

Destination: 

By: 

Date: 

## 1. Auto

## 1.3 Expressway

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/a9a45185-cfa1-407d-8a96-209400065f95/858b628396140c821dbb8b3fcae403498c253d056b632d3c94d463e63bcf2c11.jpg)


## 1.8 Totals

## 1.9 Total auto distance

## 2. Transit

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/a9a45185-cfa1-407d-8a96-209400065f95/3538912979582611a2c3e70ef928fe6ce54930cb35bb71fc8eeaa49fe13df46e.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/a9a45185-cfa1-407d-8a96-209400065f95/67f4aeb490c97e54200985dfac89a3a733be77babcd6b1da769ca422d9b63b1d.jpg)



Figure 3.7 Service-level worksheet.


2. For transit: 

- Walk to transit station, about 1/8 mile; out-of-vehicle time = 2.5 min. 

- Wait for transit vehicle, about half the headway between vehicles, which is 6 min; out-of-vehicle time = 3 min. 

- Ride in the line-haul rapid transit vehicle to CBD zone: 7 miles; in-vehicle time = 14 min. 

- Transit fare 50¢ in one direction; cost = 50¢. 

- Walk from station to workplace, about 1/8 mile; out-of-vehicle time = 2.5 min. 

- Totals: in-vehicle time = 14 min; out-of-vehicle time = 8 min; cost = 50¢. 

- In-vehicle distance = 7 miles; total distance = 7.25 miles. 

Note that, although the two individuals have different socioeconomic characteristics, because they live and work in almost identical geographical locations they both face the same service characteristics in each of the two modes. They do have different responses to these characteristics, however. The levels of service calculated above are those that were used in section 3.2. (Note that the distance used is the total automobile in-vehicle distance.) These led to mode-choice probabilities of $p_{\mathrm{T}} = 0.65, p_{\mathrm{A}} = 0.35$ for the individual in household type A and $p_{\mathrm{T}} = 0.46, p_{\mathrm{A}} = 0.54$ for the individual in household type B. 

## CASE II: BEYOND WALK DISTANCE

Many residents of a corridor will live beyond any "reasonable" walking distance of a line-haul transit station. In this case they may have the option of walking to a "station" (such as a bus stop) from which a "feeder" transit vehicle will take them to the line-haul transit station. $^{1}$ Consider individuals in household types $C$ and $D$ with the same socio-economic characteristics as $A$ and $B$ , respectively, but residing beyond walking distance to line-haul transit. Assume that they live 1 mile from the nearest line-haul transit station but within walking distance (1/8 mile) of a feeder transit service. Again, both individuals have the same trip profiles open to them: 

1. For auto: 

- Walk to auto, garaged at home: distance negligible. 

- Drive over local streets to arterial street: distance 1 mile; in-vehicle time = 3.3 min. 

- Drive on expressway to CBD zone: 7 miles; in-vehicle time = 10.5 min. 

- Drive over local streets to parking location: about 1/8 mile; in-vehicle time = 0.4 min. 

- Time spent parking car: 3 min, out-of-vehicle time (parking charge $1.00 per day, or 50¢ each direction); out-of-vehicle time = 3 min; cost = 50¢. 

- Walk to workplace: about 0.1 mile, out-of-vehicle time = 2 min. 

- Auto operating costs: about 10¢ per vehicle-mile, for 8.13 miles = 81.3¢. 

- Totals: in-vehicle time = 14.2 min; out-of-vehicle time = 5 min; cost = 131.3¢. 

- In-vehicle distance = 8.13 miles, total distance = 8.23 miles. 

2. For transit: 

- Walk to feeder service station (bus stop), about 1/8 mile; out-of-vehicle time = 2.5 min. 

- Wait for feeder transit vehicle, about half the headway of 15 min; out-of-vehicle time = 7.5 min. 

- Feeder travel 1 mile, cost 25¢; in-vehicle time = 7.7 min, cost = 25¢. 

- Wait for line-haul transit vehicle, about half the headway of 6 min; out-of-vehicle time = 3 min. 

- Ride in line-haul rapid transit vehicle, 7 miles; in-vehicle time = 14 min. 

• Line-haul fare cost = 50¢. 

- Walk from CBD station to workplace, about 1/8 mile; out-of-vehicle time = 2.5 min. 

- Totals: in-vehicle time = 21.7 min; out-of-vehicle time = 15.5 min; cost = 75¢. 

- In-vehicle distance = 8 miles; total distance = 8.25 miles. 

These service-level assumptions result in the values used in section 3.3.2. The corresponding mode-choice probabilities are, for household type C, $(p_{\mathrm{T}} = 0.57, p_{\mathrm{A}} = 0.43)$ and, for household type D, $(p_{\mathrm{T}} = 0.36, p_{\mathrm{A}} = 0.64)$ . Table 3.1 and figure 3.2 show the responses of these households to transit fare variations. 

。 

## DISCUSSION

These two cases show that access characteristics have an important effect on choice. Figure 3.8 shows the implications diagrammatically. Part a shows a zone divided into two subzones, based upon the maximum walk distance to a line-haul station. Subzones I and II thus correspond to cases I and II, respectively. We see from the results obtained above that there can be significant variations in choices within zones. The choices made by households in a zone can vary by socioeconomic characteristics and by access characteristics (that is, the choices available). This line of reasoning can be extended to the availability of an automobile (“transit-captive”) as well as the availability of transit (“auto-captive”). 

Part b of the figure shows one extension of this line of reasoning. Subzone III consists of households beyond walking distance of line-haul or feeder services. 

## 3.5 A METHODOLOGY FOR INCREMENTAL ANALYSIS

The foregoing examples have demonstrated the basic procedure for predicting choices as a consequence of alternative service levels. For some models, once a prediction has been made for existing "base" conditions, a powerful shortcut exists for analyzing the effects of changes to those base conditions. We consider here the case of the multinomial logit model: 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/a9a45185-cfa1-407d-8a96-209400065f95/830c46351ca39dfc1e7b0b79652888a6950699b1f51107cf7e243c54eb38746d.jpg)



b


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/a9a45185-cfa1-407d-8a96-209400065f95/0bdb96c2baa9df974ce0a86219270c1c10daf8bbaae2c3a735a3198d734d903d.jpg)



Figure 3.8 Access conditions. r and $r'$ are maximum walk distances to a station and a feeder service, respectively. After Kocur et al. (1977).


$$
p (m) \equiv p (m: M) = \frac {e ^ {U _ {m}}}{\sum_ {m ^ {\prime} \in M} e ^ {U _ {m ^ {\prime}}}}.\tag{3.21}
$$

It can be shown that, given a set of changes $\Delta U_{m}$ for each mode m and base probabilities $p^{0}(m)$ , the new probability $p'(m)$ is 

$$
p ^ {\prime} (m) = \frac {e ^ {\Delta U _ {m}} p ^ {0} (m)}{\sum_ {m ^ {\prime} \in M} e ^ {\Delta U _ {m ^ {\prime}}} p ^ {0} (m ^ {\prime})}.\tag{3.22}
$$

In the case of two modes i and j, 

$$
p ^ {\prime} (i) = \frac {e ^ {\Delta U _ {i}} p ^ {0} (i)}{e ^ {\Delta U _ {j}} p ^ {0} (i) + e ^ {\Delta U _ {j}} p ^ {0} (j)} = \frac {1}{1 + [ p ^ {0} (j) / p ^ {0} (i) ] e ^ {\Delta U _ {j} - \Delta U _ {i}}}.\tag{3.23}
$$

Thus, given initial mode-choice probabilities (or shares) $p^{0}(m)$ and a specific set of changes $\Delta S_{m}$ , the new probabilities $p'(m)$ can be found from the corresponding $\Delta U_{m} = f(\Delta S_{m})$ . 

## 3.6 MODE-CHOICE MODEL II

The model introduced in section 3.2.1 is a special case of a more general model. Model II is summarized in table 3.3 and will be used in selected exercises. This model explicitly includes two socioeconomic attributes: income and the ratio of automobiles owned to the number of licensed drivers. We see that the mode-specific constant of model I arises from differences in these attributes. 

This model is a composite of several statistically estimated models and was designed primarily for teaching purposes. A number of such multinomial logit models have been estimated using Washington, D.C., data from a conventional home interview survey carried out in 1968. Many of these were estimated as part of a project studying the relationship between automobile ownership and transportation service levels (Lerman and Ben-Akiva 1975, Cambridge Systematics 1976a). Both binary and three-mode models were estimated in this study, the binary models dealing with choices between automobile and transit and the three-mode models with choices among transit, automobile driven alone, and shared-ride automobile ("carpooling," with at least one traveler in addition to the driver). The reported models were estimated with sample sizes on the order of 800–1,200 observations and met appropriate statistical tests for significance satisfactorily (see chapter 11). 

## 3.7 SUMMARY

In this chapter we have used a demand function to predict the responses of different consumers to changes in transportation service levels. The function used was disaggregate in that it predicted the behavior of individual consumers. It was also stochastic in that it predicted the probabilities of various choices. 


Table 3.3 Binary mode-choice model


Variables
Service attributes (S) (all one-way, or half the round-trip values): $t_m$ = in-vehicle time (minutes) $x_m$ = out-of-vehicle time (walking, waiting, parking) (minutes) $c_m$ = cost (out-of-pocket: fares, tolls, parking) (cents) $\theta_m$ = mode-specific characteristic $d$ = distance (miles)

Socioeconomic attributes (A): $y$ = income (household total) (dollars per year) $a_{LD}$ = autos owned divided by the number of licensed drivers (per household)

Parameters ( $\theta$ ): $\theta_i$ = general parameter value applying to $i$ th characteristic in mode $m$ 's utility $\theta_{mi}$ = mode-specific parameter value applying to $i$ th characteristic in mode $m$ 's utility $\theta_{m0}$ = mode-specific constant $m$ = mode (A = auto, T = transit)

Modal utilities
General form: $U_m$ = $\theta_m$ + $\theta_1 t_m$ + $\theta_2 \frac{x_m}{d}$ + $\theta_3 \frac{c}{y}$ $\theta_m$ = $\theta_{m0}$ + $\theta_{m4} y$ + $\theta_{m5} a_{LD}$ Coefficient values: $\theta_1$ $\theta_2$ $\theta_3$ $\theta_{m4}$ $\theta_{m5}$ $\theta_{m0}$ Automobile -0.030 -0.34 -50 8.957 × 10 $^{-5}$ 2.84 -2.00
Transit -0.030 -0.34 -50 0 0 0 

Use of the demand functions was organized around worksheets, which helped to systematize the various calculations. 

In order to use the demand function, values of service levels were required; these were developed by simple estimating procedures. Simple manual worksheets were also demonstrated for these calculations. 

The examples demonstrate that a single demand function can represent the behavior of consumers with different socioeconomic 

characteristics and/or with different transportation service levels available; consumers with different socioeconomic characteristics will display different behaviors, even at the same service levels; consumers with similar socioeconomic characteristics may behave differently when confronted with different service levels; and any grouping of consumers—such as a geographic grouping into traffic zones—may include consumers with widely varying socioeconomic characteristics and transportation service levels, and thus different choice behaviors. 

## TO READ FURTHER

Disaggregate models with simple manual worksheets have been applied to a number of practical problems. For applications to energy conservation analysis, see Cambridge Systematics (1976b) and Dunbar (1976). Of course, disaggregate models can also be used in large-scale computer models. For use in regionwide sketch planning as part of an analysis aimed at establishing transportation research and development priorities, see Kocur et al. (1977). 

## EXERCISES

3.1(E) Select two of the cases examined in section 3.3 (combinations of household type and residence location) and analyze the following (calculate typical values, plot graphs, and discuss): 

a. The effect of variations in walk distance (over a range from 0.02 to 1 mile) on the probability of choosing transit. 

b. The effect of variations in automobile parking charges (from 0 to $5 per day) on the probability of choosing automobile. 

c. The effect of changes in transit line-haul headway (from 1 to 18 minutes). 

3.2(E) Design worksheets for the parametric analysis in exercise 3.1 and demonstrate their use. 

3.3(E) Using the service-level worksheets, work through the examples in section 3.4.3 and check your understanding of the calculations and results. 

3.4(E) In this chapter trip profiles were shown for automobile and for transit. Other profiles occur in urban transportation: passenger in shared-ride automobile (carpool); automobile driven alone to transit station, then transit (park-and-ride); automobile passenger to transit (kiss-and-ride); local bus for access portion of trips, then same bus in express (nonstop) operations along arterial street, expressway, or busway to destination. 

a. Construct typical trip profiles for cases other than those presented in this chapter. 

b. Make reasonable assumptions about performance characteristics where necessary, and calculate levels of service for typical trips, using households selected from the examples in section 3.3. 

c. Make reasonable assumptions, calculate utilities of these profiles, and calculate corresponding mode-choice probabilities. 

3.5(E) Consider the following contexts, construct typical trip profiles, make reasonable assumptions about performance characteristics, and compare: 

a. Interurban passenger transport, with choices of automobile, airplane, railroad, and bus. 

b. Interurban freight transport, with choices of railroad, truck, pipeline, or inland waterway. 

c. International freight transport, with choices of ships or airplanes. 

3.6(C) The discussion in section 3.4.3 applies to many transportation contexts. Develop examples to illustrate similar influences of access characteristics for the contexts indicated in exercise 3.5. Use the trip profiles developed in your answer to that exercise. 

3.7(E) Consider the incremental logic described in section 3.5. 

a. Design worksheets for implementing this logic. 

b. Use these worksheets to explore the effects of the changes indicated in exercise 3.1. 

3.8(E) Discuss the effects of the transit fare variations shown in table 3.1 and figure 3.2. 

3.9(E) Consider the binary mode-split model shown in table 3.3. 

a. For each of the nine combinations of $a_{\text{LD}}$ and $y$ for which values of $\theta_{\text{A}}$ are shown in the table, find $p_{\text{T}}$ for the case in which automobile and transit service are identical. (Check: for $a_{\text{LD}} = 0$ and $y = \$5,000$ , $p_{\text{T}} = 0.83$ .) Discuss the implications for urban transportation policy: Is $a_{\text{LD}}$ exogenous, or can it be affected by policy? If it can be affected, then how? 

b. Consider the case $a_{LD} = 0.5$ , y = $10,000, with all service attributes except those indicated equal for automobile and transit: 

i. What is $p_{T}$ under this assumption? 

ii. What would the difference in automobile and transit in-vehicle times have to be to yield $p_{T} = 0.5 ? 0.6 ? 0.8 ?$ 

iii. What would the difference between automobile and transit out-ofvehicle times have to be to yield $p_{T} = 0.5 ? 0.6 ? 0.8 ?$ (Assume equal in-vehicle times.) 

iv. If transit fares were increased by 25 percent, what reduction in transit out-of-vehicle time would be necessary to maintain the same transit share as in part i? What reduction would be necessary to keep the same share of passengers with $a_{LD} = 1.0$ and $y = \$15,000$ ? v. At present automobile congestion is high. Highway improvements are proposed that would reduce automobile in-vehicle time by 15 minutes. How would this affect the value of $p_T$ in part i? 

vi. Assume that it is desired to keep $p_{T}$ constant. If the highway improvement is implemented, what reduction in transit fares would be necessary to maintain the present mode split? Alternatively, transit frequencies can be increased to decrease the transit out-of-vehicle time. How great would this increase in frequency have to be?

vii. Discuss the policy implications of parts iv and v. 

c. Consider some other household types (that is, other values of $a_{LD}$ and y), and explore selectively the answers to the questions in part b for these households. Discuss. 

3.10(E) In zone 2 of figure 3.4, household types P, Q, R, and S are located the same distance from the transit station as are A, B, C, and D, respectively, in zone 1; members of these households all work in zone 4. 

a. Predict the levels of service these four households face. 

b. Calculate the corresponding mode-choice probabilities. 

c. Compare your results with those for A, B, C, and D and discuss. 

d. Parametrically vary transit fares over the range indicated in figure 

3.2, plot your results on that figure, and discuss. 

e. Consider each of the changes in exercise 3.1 parts a–c. For each change, rank the eight households A, B, C, D, P, Q, R, S in order of increasing sensitivity to the change. Explain how you developed your rankings. 

# Aggregate Prediction of Behavior

## 4.1 INTRODUCTION

Chapters 2 and 3 examined demand functions that described the behavior of single consumers—individuals, households, or firms (considered as single decision-making units). This disaggregate view proved very useful in analyzing the bases of consumer choice behavior in transportation. For practical predictions of the impacts of transportation strategies, however, it is important to be able to predict the behavior of groups of consumers. 

We start by making the important distinction between disaggregate and aggregate demand functions. A disaggregate demand function predicts the behavior of a single consumer in response to changes in future conditions. An aggregate demand function predicts the behavior of a group of consumers (several individuals, households, or firms) in response to changes in future conditions. 

Historically the vast bulk of effort in transportation demand analysis has been focused on aggregate demand functions. While research on disaggregate demand functions began at least as early as 1962, only since about 1971 have disaggregate approaches begun to be put into practice (see S. L. Warner 1962, Rassam, Ellis, and Bennett 1971, Charles River Associates 1972, and the historical survey in Domencich and McFadden 1975). For this reason most of the literature simply uses the term “demand functions” to refer to aggregate functions. When a disaggregate function is used, it is labeled “disaggregate” explicitly. For convenience we shall follow this usage in this text, adding the modifier “aggregate” to “demand function” only when it is not clear from the context. 

## 4.2 MARKET SEGMENTS

The potential users of a transportation system can be classified according to many different sets of criteria. Ideally we try to include in each group consumers who are very similar in their preferences and characteristics and thus will respond similarly to changes in transportation, while at the same time we try to make the groups relatively dissimilar one from another. Thus we try to divide the total market—the total population of potential travelers or shippers—into segments each of which is relatively homogeneous but is different from other segments. Typical ways of forming such segments are as follows: 

In urban passenger transportation, consumers might be classified by: 

1. income 

2. automobile availability (cars per household) 

3. household size 

4. occupation of head of household 

5. stage in family life cycle (for example, two-person household with children living at home, two-person household without children, or elderly without children; see Aldana, de Neufville, and Stafford 1974, Cambridge Systematics 1976a) 

6. geographic location (for example, through combinations of households or firms into “traffic zones”) 

7. trip purpose. 

In planning access to airports, travelers might be grouped as: 

1. air travelers resident in the region  
a. business travelers  
b. other travelers 

2. air travelers not resident in the region
a. business travelers
b. other travelers 

3. airport employees 

4. visitors accompanying travelers 

5. visitors not accompanying travelers. 

In analyzing freight transportation, consumers might be classified by: 

1. firm size 

2. industry type 

3. commodity types being purchased and/or sold. 

A particularly important form of aggregation into market segments is by geographic location. In almost all transportation studies the region is divided into geographic zones, with all of the consumers in each zone forming the main market segments (although this is usually not stated explicitly). Then various subsidiary market segments are constructed. For example, in an urban transportation study, once the zones are established, each zone might be characterized by an average income per household and an average automobile ownership per household; alternatively, the households in the zone might be grouped by income and number of automobiles per household. 

There are obviously many different ways in which the total travel market in a particular region could be divided into market segments. Particular care must be given to constructing these segments in a way that is useful for anticipating the effects of the transportation changes being considered. 

## 4.3 EXAMPLES OF AGGREGATE DEMAND FUNCTIONS

Once we have established the basic market segments into which we shall group potential users, the next step is to develop a basis for characterizing the behavior of each group. 

Aggregate demand functions represent the behavior of a group (or "aggregate") of individuals. These functions are of the form first introduced in chapter 1: 

$$
\mathbf {V} = \mathbf {D} (\mathbf {A}, \mathbf {S}),\tag{4.1}
$$

where V is the vector of volumes or numbers of consumers making particular choices, A represents the social, economic, and other characteristics of the activity system and of the individuals in the group, and S the service attributes that characterize the transportation choices open to prospective travelers. 

Thus the aggregate demand function D gives the potential volumes and composition of flow between two (or more) points as a function of the service attributes experienced during movement between those points for a particular activity system. The activity-system variables describe the characteristics of the consumers whose behavior is represented by the demand function and of the activity system that influences their choices. 

Examples of aggregate demand functions follow. The examples were selected to illustrate the major historical streams of model development. 

## 4.3.1 Gravity Models

The gravity model is perhaps the classic transportation demand model (see the survey in Isard 1960). In its simplest form it was originally developed as a "law of social physics" analogous to Newton's law of gravitation for physical systems. We start with gravity I: 

$$
V _ {k d} = Y _ {k} Z _ {d} L _ {k d},\tag{4.2}
$$

where $Y_{k}$ is some measure of the intensity of activity at zone k, such as the population; $Z_{d}$ is some measure of the intensity of activity at zone d, such as the population or employment level; and $L_{kd}$ represents the effect of transportation service attributes on demand for travel between k and d. One common assumption is that 

$$
L _ {k d} = t _ {k d} ^ {\alpha},\tag{4.3}
$$

where $t$ is travel time and $\alpha$ is a parameter. Originally it was assumed that $\alpha \approx -2$ , thus leading to the equivalent of Newton's law of gravitational attraction. 

More generally, other service attributes may enter as well. As an example we have gravity II, described by (4.2) and the assumption that 

$$
{\cal L} _ {k d} = t _ {k d} ^ {\alpha_ {1}} c _ {k d} ^ {\alpha_ {2}},\tag{4.4}
$$

where c is out-of-pocket cost and the $\alpha$ s are parameters taking various values. 

The widest application of the gravity model in transportation has been to predict, not how many people will travel, but which destination they will choose. Assume that the region is divided into N traffic zones and that, by some separate analysis, we have estimated that $V_{k}$ trips will originate in zone k. Now the problem is to predict what fraction of these trips will go from k to another zone d. The gravity model used for this purpose is gravity III: 

$$
V _ {k d} = V _ {k} \frac {Z _ {d} L _ {k d}}{\sum_ {d ^ {\prime} \neq k} Z _ {d ^ {\prime}} L _ {k d ^ {\prime}}}.\tag{4.5}
$$

Alternatively we could write 

$$
V _ {k d} = V _ {k} \gamma_ {k d},\tag{4.6}
$$

where 

$$
\gamma_ {k d} \equiv \frac {Z _ {d} L _ {k d}}{\sum_ {d ^ {\prime} \neq k} Z _ {d ^ {\prime}} L _ {k d ^ {\prime}}}.\tag{4.7}
$$

(The index in the summation indicates that all values of $d'$ are to be included except $d' = k$ .) The term $Z_{d}L_{kd}$ is often called the “potential” (Isard 1960); (4.5) suggests that each destination d competes for the trips originating at k and that the competitive power of d is proportional to its “potential” relative to the “total potential” of all destinations. 

If we define $V_{k}$ as follows, gravity III becomes identical to gravity I: 

$$
V _ {k} ^ {\prime} = Y _ {k} \sum_ {d ^ {\prime} \neq k} Z _ {d ^ {\prime}} L _ {k d ^ {\prime}}.\tag{4.8}
$$

This suggests gravity IV: 

$$
V _ {k d} = V _ {k} \gamma_ {k d},\tag{4.9}
$$

where $\gamma_{kd}$ and $L_{kd}$ are defined by (4.7) and (4.3), respectively, and 

$$
V _ {k} = (\beta_ {k}) ^ {\theta},\tag{4.10}
$$

$$
\beta_ {k} = Y _ {k} \sum_ {d ^ {\prime} \neq k} Z _ {d ^ {\prime}} L _ {k d ^ {\prime}}.\tag{4.11}
$$

Thus 

$$
V _ {k d} = (Y _ {k}) ^ {\theta} \left(\sum_ {d ^ {\prime} \neq k} Z _ {d ^ {\prime}} L _ {k d ^ {\prime}}\right) ^ {\theta} \frac {Z _ {d} L _ {k d}}{\sum_ {d ^ {\prime} \neq k} Z _ {d ^ {\prime}} L _ {k d ^ {\prime}}}.\tag{4.12}
$$

As in gravity III, the second factor indicates that the total number of trips originating in zone k depends on the “total potential” of travel to various destinations. The last factor reflects the split or distribution of these trips among alternative destinations according to their potentials relative to the total. 

## 4.3.2 Some Intercity Passenger Demand Models

The first important demand models for intercity passenger travel were developed for the Northeast Corridor Project of the U.S. Department of Transportation. These models were used to predict the level of travel between any pair of cities together with the split among the competing modes. 

First developed in point of time was the Kraft-SARC model (Kraft 1963). Later a family of models was developed by Quandt and Baumol (1966; see also Crow, Young, and Cooley 1973), and a third type of model was developed by James McLynn (McLynn and Woronka 1969). 

For the case of three modes, and considering only time and cost as service variables, $^{1}$ these models are: 

Kraft-SARC: 

$$
V _ {k d m} = \phi_ {m 0} (P _ {k} P _ {d}) ^ {\phi_ {m 1}} (I _ {k} I _ {d}) ^ {\phi_ {m 2}} (t _ {k d 1} ^ {\theta_ {m 1 1}} c _ {k d 1} ^ {\theta_ {m 1 2}}) (t _ {k d 2} ^ {\theta_ {m 2 1}} c _ {k d 2} ^ {\theta_ {m 2 2}}) (t _ {k d 3} ^ {\theta_ {m 3 1}} c _ {k d 3} ^ {\theta_ {m 3 2}}),\tag{4.13}
$$

McLynn: 

$^{1}$ In the original formulations of the Baumol-Quandt and McLynn models a third service attribute, frequency, was included as well. In the Kraft-SARC and Baumol-Quandt forms frequency was handled the same way as the other two variables. In the McLynn model frequency was introduced as exp(frequency). The frequency terms have been left out of this discussion for purposes of clarity. For similar models for the urban context see Domencich, Kraft, and Vallette (1968). 

$$
V _ {k d m} = \phi_ {0} (P _ {k} P _ {d}) ^ {\phi_ {1}} (I _ {k} I _ {d}) ^ {\phi_ {2}} \frac {t _ {k d m} ^ {\theta_ {m 1}} c _ {k d m} ^ {\theta_ {m 2}}}{\sum_ {q} t _ {k d q} ^ {\theta_ {q 1}} c _ {k d q} ^ {\theta_ {q 2}}} \sum_ {q} (t _ {k d q} ^ {\theta_ {q 1}} c _ {k d q} ^ {\theta_ {q 2}}) ^ {\delta_ {1}},\tag{4.14}
$$

Baumol-Quandt: 

$$
V _ {k d m} = \phi_ {0} (P _ {k} P _ {d}) ^ {\phi_ {1}} (I _ {k} I _ {d}) ^ {\phi_ {2}} (t _ {k d m} ^ {\theta_ {1}} c _ {k d m} ^ {\theta_ {2}}) (t _ {k d b} ^ {\theta_ {3}} c _ {k d b} ^ {\theta_ {4}}),\tag{4.15}
$$

where 

$V_{kdm} = \text{volume between } k \text{ and } d \text{ by mode } m,$ 

$P_{k} =$ population in zone $k$ , 

$I_{k} =$ median income in zone $k$ , 

$t_{kdm}, c_{kdm} = travel time and fare between k and d by mode m,$ 

$t_{kdb} =$ travel time by fastest mode, 

$c_{kdb} = \text{fare by cheapest mode (not necessarily same as fastest mode!)},$ $\phi, \theta, \delta = \text{parameters of the model.}$ 

Subscripts indicate whether the parameters are mode-dependent $(\theta_{mj})$ or mode-independent $(\theta_{1})$ . 

Note that these models assume implicitly in each mode that there is only one path connecting each origin-destination pair of zones. This is often not a bad assumption in the case of intercity passenger travel. 

These three models are very similar and yet very different. The reader should compare them carefully after reading the discussions in the following sections. 

## 4.3.3 The Urban Transportation Model System

In urban transportation planning the prediction of travel flows is typically done in four steps. This breaks the demand model down into four submodels, but it also involves some significant assumptions and approximations in the way the submodels are used to compute equilibrium. The submodels are: 

1. Trip generation: The total trips made by a particular market segment are estimated for each zone of the region being studied. 

2. Distribution: The total trips originating at each zone are distributed among possible destinations. 

3. Modal split: The volume of trips going from a particular zone to a particular destination are split among the possible modes. 

4. Network assignment: The trips for each origin-destination-mode combination are assigned to paths in the network. 

This approach has been widely used in many urban transportation studies since the late 1950s. Because of the importance of understanding this model system, together with its limitations, a detailed discussion is presented in chapter 11. 

4.3.4 Stochastic Aggregate Demand Functions (Optional Reading)
We began our discussion of demand at the level of individual behavior with consumer behavior model I. This is a disaggregate model, in that it deals with a single consumer as an entity. It is also deterministic, in that the consumer is assumed to make his choice with perfect information and perfect rationality. After discussing the limitations of this assumption, we introduced the concept of stochastic disaggregate models with consumer behavior model II. In these models the consumer is still treated at the individual level, but a random element is assumed in his behavior to reflect less-than-perfect information. Stochastic disaggregate models yield probabilities of making particular choices rather than a prediction of a specific choice. 

In this chapter we have introduced the concept of aggregate demand functions, which represent the behavior of a number of consumers grouped into a single market segment. As we shall see in the next section, such aggregate demand functions can be derived from explicit disaggregate models of individual consumer behavior. 

All aggregate models developed to date have been deterministic, in that they predict that a specific number of individuals will make a particular choice. Such models are based, explicitly or implicitly, on consumer behavior model I (Blackburn 1970, Golob and Beckmann 1971). One would expect that, as in the disaggregate case, stochastic aggregate demand models would have been developed which would explicitly account for the variability in human behavior. These models would predict a probability distribution over the number of individuals making a particular response to a set of changes in future conditions. Such models have not, in fact, been developed yet, to our knowledge. $^{2}$ 

Note that we are defining the stochastic nature of a model as describing the form used for prediction. Explicit statistical estimation of the parameters of any demand model involves an underlying probabilistic formulation; for example, linear regression assumes an additive, normally distributed error term. However, even when statistical methods are used to estimate the parameters of demand models such as those described in the preceding section, the model is described and used in prediction as a deterministic model. 

## 4.4 ALTERNATIVE APPROACHES TO THE PREDICTION OF AGGREGATE BEHAVIOR: INTRODUCTION

In practice, one is interested in predicting the responses of groups of individuals to changes in transportation service. The prediction methods used depend in part on the type of demand function with which one begins. 

In the preceding chapters and sections we have discussed a two-way classification of demand functions: disaggregate versus aggregate and deterministic versus stochastic. These categories define four major groups of functions. 

The present state of development of the four potential groups of demand functions can be summarized as follows: 

Group I: disaggregate, deterministic demand functions—development primarily theoretical, used especially for expository purposes. 

Group II: disaggregate, stochastic demand functions—extensive development in recent years for both research and practical applications. 

Group III: aggregate, deterministic demand functions—the major area of development historically for travel demand analysis. 

Group IV: aggregate, stochastic demand functions—no theoretical or practical developments. 

At present, the major directions of development and practical use of travel demand models involve models in groups II and III. 

If aggregate demand functions have been developed for each market segment, these functions can be used directly to predict the behaviors of the corresponding segments. If disaggregate demand functions have been developed for various segments, prediction is more complex, but there are a number of practical approaches available (see section 4.7). Before turning to a discussion of specific prediction methods, however, we shall first examine some important properties of demand functions. 

## 4.5 PROPERTIES OF DEMAND FUNCTIONS

In developing demand functions and using them for prediction of consumer behavior, the analyst must make many judgments, often involving simplifying assumptions and approximations. To make these thoughtfully the analyst must understand the implications of a particular demand function as a representation of consumer behavior. 

121 Aggregate Prediction of Behavior 

When we define a demand function, what we are trying to do is to characterize the activity system A—that is, the set of consumers, their characteristics, and the potential activities in which they might engage—and the transportation system T—that is, the levels of service S of the alternative travel choices available—so that we can predict the volumes V that will demand particular transport services. The activity system may be characterized in terms of population, employment, income, family size, cars per household, or any of a wide variety of other variables. The transportation service attributes might include any one or several of the variables identified earlier. 

In general we can expect that since different consumers will have different behavior patterns, the demand functions will be different for different social and economic groups, for different trip purposes, and for different time periods. For example, the demand function for home-to-work trips by high-income workers during weekday peak hours might be different from the demand function for shopping and recreational trips by low-income workers on weekends. These differences in behavior of various market segments will be reflected in the values of the parameters of the demand functions, as well as in the forms of the functions. 

In the following subsections we shall examine a number of properties of demand functions. Then in section 4.6 we shall explore how knowledge of some of the properties of demand functions can be used for approximate predictions—for example, how incremental analysis can be done with limited information and explicit judgments. 

## 4.5.1 Variables Included

Two basic sets of variables—activity-system variables and service attributes—enter into a demand function. Various choices can be made about what activity-system and service variables are explicitly included in the demand function. The service attributes of the transportation system include travel time (separated into in-vehicle and excess or out-of-vehicle time), time reliability, service schedule, out-of-pocket cost, perceived security, tolls, freight rates, and so on, as described in section 2.3.1. The activity system may be described in terms of such variables as population, employment, income, household size, stage in family life cycle, industrial sector, or commodity code. Some of the activity-system variables will describe the characteristics of the consumers included in the market segment, such as income or cars per household (or type of industries for freight demand models). Other activity-system variables will describe characteristics of the choices 

open to the consumers, such as the attractiveness of alternative destinations for shopping trips as measured by retail sales volume or square feet of retail floor space. 

## 4.5.2 Algebraic Forms of Demand Functions

There are many different forms of demand functions possible. It is useful to distinguish several basic algebraic forms (X represents a single service attribute or activity-system variable): 

Linear: for example, $V = \alpha + \beta X$ , 

Product: for example, $V = \alpha X^{\beta}$ , 

Exponential: for example, $V = \alpha e^{\beta X}$ , 

Logistic: for example, $V = \alpha/(1 + e^{\beta X})$ . 

These forms are often used because they are simple to handle algebraically, and they are particularly suitable for calibration by standard statistical techniques. For example, for aggregate functions, linear regression techniques can be used to estimate the coefficients of the linear form of the demand model directly, from observations of the form $(X, V)$ . To estimate the coefficients of the product and exponential forms, logarithms are taken to transform the equation into a linear form, and then regression techniques are used on this transformed equation. (For disaggregate models alternative techniques are available, such as maximum-likelihood methods for the “logit” form analogous to the logistic.) 

Obviously, far more complex forms can be used, and many more activity-system or service variables could be included. 

The choice of an algebraic form for a demand function is not simply a question of convenience in calibration. Each functional form represents a somewhat different assumption about the way in which consumers will respond to changes in the choices available. These behavioral differences are seen most clearly by examining the derivatives of the demand function and a related concept, the elasticity. 

## 4.5.3 Behavioral Representations: Directions, Magnitudes, Derivatives, and Elasticities

The behavioral issue is best illustrated by an example. Consider a situation in which firms in one region ship freight to different markets. In market A the freight rate is $5 per ton; in market B, $500 per ton. A rate increase of $5 per ton is imposed. Thus the rate in market A goes from $5 to $10 per ton, a 100 percent increase. The rate in market B goes from $500 to $505 per ton, a 1 percent increase. 

What kind of behavior would we expect from these changes? There are two aspects to this question: the direction of the change in behavior, and the magnitude. First, if we increase the freight rate, would we expect the volume to increase or to decrease? In most situations we would expect any decrease in service quality, such as an increase in travel time or in cost or an increase in probability of loss or damage to the cargo, to result in a decrease in volume. Second, if we increase the rate by 5 percent, would we expect the relative magnitude of the change in volume to be about the same (5 percent) or greater (perhaps 50 percent) or smaller (perhaps 1 percent)? To answer this question we must examine the specific applicable demand model; we shall see that the algebraic form of the demand function and the numerical values of its parameters imply particular patterns of behavior. Several properties of a demand function will be examined to explore the behavior implied by the function. 

## DERIVATIVES

Consider a demand function $V = D(X)$ . The change in volume V, for a change in variable X from $X'$ to $X''$ , equal to $\Delta X$ , is given by 

$$
\varDelta V = V ^ {\prime \prime} - V ^ {\prime} = D (X ^ {\prime \prime}) - D (X ^ {\prime}).\tag{4.16}
$$

The magnitude of the change in V relative to the change in X is 

$$
\frac {\Delta V}{\Delta X} = \frac {D (X ^ {\prime} + \Delta X) - D (X ^ {\prime})}{(X ^ {\prime} + \Delta X) - X ^ {\prime}}.\tag{4.17}
$$

In the limit (as $\Delta X$ goes to zero), this is the partial derivative, $\partial V/\partial X$ . 

Thus, to determine the behavioral pattern represented by a particular demand function, we compute its derivative. The sign of the derivative tells us whether the direction of the response to changed conditions will be the same as or opposite to the direction of change: if the derivative of the demand function with respect to freight rate is negative, then an increase in rate will cause a decrease in volume. The magnitude of the derivative allows us to estimate the magnitude of the response, since 

$$
\varDelta V \approx \frac {\partial V}{\partial X} \varDelta X.\tag{4.18}
$$

The derivatives of several basic demand functions are given in table 4.1. In some cases, such as the linear form, the derivative is closely related to, or equal to, a particular coefficient, and then it is sufficient to look at the magnitude and sign of that coefficient. 


Table 4.1 Derivatives and elasticities of some common functions


<table><tr><td></td><td>Functional form (V)</td><td>Derivative<eq>(\partial V/\partial X)</eq></td><td>Elasticity<eq>(X/V)(\partial V/\partial X)</eq></td></tr><tr><td>Linear</td><td><eq>\alpha + \beta X</eq></td><td><eq>\beta</eq></td><td><eq>\frac{\beta X}{V} = \frac{1}{1 + (\alpha/\beta X)}</eq></td></tr><tr><td>Product</td><td><eq>\alpha X^{\beta}</eq></td><td><eq>\alpha \beta X^{\beta-1}</eq></td><td><eq>\beta</eq></td></tr><tr><td>Exponential</td><td><eq>\alpha e^{\beta X}</eq></td><td><eq>\beta V = \alpha \beta e^{\beta X}</eq></td><td><eq>\beta X</eq></td></tr><tr><td>Logistic</td><td><eq>\frac{\alpha}{1 + \gamma e^{\beta X}}</eq></td><td><eq>-\beta V\left(1 - \frac{V}{\alpha}\right) =</eq><eq>-\frac{\alpha \beta \gamma e^{\beta X}}{(1 + \gamma e^{\beta X})^{2}}</eq></td><td><eq>-\beta X\left(1 - \frac{V}{\alpha}\right) =</eq><eq>-\frac{\beta \gamma X e^{\beta X}}{1 + \gamma e^{\beta X}}</eq></td></tr><tr><td>Logistic-product</td><td><eq>\frac{\alpha}{1 + \gamma X^{\beta}}</eq></td><td><eq>-\frac{\beta V}{X}\left(1 - \frac{V}{\alpha}\right) =</eq><eq>-\frac{\alpha \beta \gamma X^{\beta-1}}{(1 + \gamma X^{\beta})^{2}}</eq></td><td><eq>-\beta\left(1 - \frac{V}{\alpha}\right) =</eq><eq>-\frac{\beta \gamma X^{\beta}}{1 + \gamma X^{\beta}}</eq></td></tr><tr><td rowspan="2">Share</td><td rowspan="2"><eq>\gamma_{i} = \frac{V_{i}}{\sum_{j} V_{j}} = \frac{X_{i}}{\sum_{j} X_{j}}</eq></td><td><eq>\frac{\partial \gamma_{i}}{\partial X_{i}} = \frac{\sum_{j} X_{j} - X_{i}}{(\sum_{j} X_{j})^{2}}</eq></td><td><eq>E_{X_{i}}(\gamma_{i}) = 1 - \gamma_{i}</eq></td></tr><tr><td><eq>\frac{\partial \gamma_{i}}{\partial X_{j}} = \frac{-X_{i}}{(\sum_{j} X_{j})^{2}}</eq></td><td><eq>E_{X_{j}}(\gamma_{i}) = -\gamma_{j}</eq></td></tr></table>

## ELASTICITIES

One problem with the derivative is that its value depends on the units in which V and X are measured. It would be more desirable to have a dimensionless measure of change. Thus we define the elasticity of V with respect to X, $E_{X}(V)$ , as the percentage change in V for a 1 percent change in X. The elasticity of volume with respect to a variable X is then 

$$
E _ {X} (V) = \frac {X}{V} \frac {\partial V}{\partial X},\tag{4.19}
$$

where X is a service or activity-system variable. Note that $E_{X}(V)$ is the limit, as $\Delta X$ tends to zero, of $(\Delta V/V)/(\Delta X/X)$ , from which comes the interpretation “percentage change in V for a 1 percent change in X.” 

The elasticities of several basic demand function forms are shown in table 4.1. 

## Implications of elasticities

We now consider the demand function forms of section 4.5.2 in the context of the example with which we began this section. 

For the linear form we can see from the table that the derivative of V with respect to X is $\beta$ , a constant. If X is taken as the rate c, we would expect an increase in rate to cause a decrease in volume, so the derivative should be negative. Thus, continuing the example, a 5 rate increase ( $\Delta c = 5$ ) would cause the same loss in volume in both markets A and B. This seems highly unlikely: we would certainly expect a 1 percent change in freight rate to cause a much lower loss of volume than a 100 percent change. 

For the product form, again with $X = c$ , if the derivative is to be negative, $\beta$ must also be negative (since $\alpha$ and $X$ must be positive to yield positive volumes). Since the derivative is a function of $X$ , the magnitude of $\Delta V$ will depend on the magnitude of $X$ . Note that the elasticity of the product form is a constant, $\beta$ : thus the percentage change in volume for each 1 percent change in cost is a constant. Therefore the $5 increase from a base rate of $500 would cause a $\beta$ percent decrease in volume in market $B$ . In market $A$ , however, the same increase from a base rate of $5 would have an effect one hundred times greater: a decrease in volume by a factor $\beta$ . 

Thus the two function forms represent very different assumptions about behavioral responses. Each function is valid in some cases but not in others. In the case of the linear function, the absolute magnitude of the response is directly proportional to the change. In the case of the product form, the absolute magnitude of the response varies with the level of the initial condition because the percentage change remains constant. 

The logistic form is in a sense most general. Over the middle portion of its range the response is roughly linear; at the upper and lower ends of the range the response is more like that of the product form. 

## Elastic and inelastic behavior

The relative magnitude of the elasticity is often important. When $\left|E_{X}(V)\right| < 1$ , V is said to be inelastic with respect to X. When $\left|E_{X}(V)\right| > 1$ , V is said to be elastic with respect to X. 

To see one aspect of the significance of this distinction, consider an example. Let 

$$
V = f (p),\tag{4.20}
$$

where p represents price. Then gross revenue to the transportation operator is 

$$
R = V p.\tag{4.21}
$$

A change in price will produce a change in revenue: 

$$
\frac {\partial R}{\partial p} = V + p \frac {\partial V}{\partial p} = V [ 1 + E _ {p} (V) ].\tag{4.22}
$$

Obviously since $\partial V/\partial p$ is negative, $E_{p}(V)$ will be negative. Therefore if V is inelastic with respect to p, an increase in price will yield an increase in gross revenue; if V is elastic with respect to p, an increase in price will yield a decrease in gross revenue. 

## Arc and point elasticities

A distinction should be drawn between arc and point elasticities. 

The point elasticity is 

$$
E _ {X} (V) = \frac {X}{V} \frac {\partial V}{\partial X}.
$$

The arc elasticity is 

$$
E _ {\bar {X}} (V) = \frac {X}{V} \frac {\varDelta V}{\varDelta X}.
$$

In the limit as $\Delta X$ tends to zero, the arc and point elasticities become equal. Occasionally, however, data will only be available for specific values of X and V, so only arc elasticities can be computed. Generally arc and point elasticities are different, the exceptions being special cases such as unit elasticity in a product-form model or situations in which $D(X)$ is a straight line. This is illustrated in figure 4.1, where the point elasticity is proportional to the slope of the tangent to the curve at $X_{0}$ , C–O–C', whereas the arc elasticity over $X_{0}-X_{B}$ is proportional to the slope of the arc cutting the curve, B–O–B'. These are clearly not equal, although the difference becomes smaller as $X_{B}$ approaches $X_{0}$ . 

## Direct and cross-elasticities

Elasticities can also indicate the interrelationships of several variables. Consider, for example, a case in which the demand for travel by a mode k depends on the value of a service variable s in mode k and also on the value of s in a competing mode r: 

$$
V _ {k} = \alpha s _ {k} ^ {\beta} s _ {r} ^ {\gamma}.\tag{4.23}
$$

Here we define two elasticities: 

$$
E _ {k k} \equiv \frac {s _ {k}}{V _ {k}} \frac {\partial V _ {k}}{\partial s _ {k}} = \beta ,\tag{4.24}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/a9a45185-cfa1-407d-8a96-209400065f95/737e79d8d6de6cc5cd05bd34f275ce81450fce54f9396284ba68ae382e5b3a05.jpg)



Figure 4.1 Arc and point elasticities.


$$
E _ {k r} \equiv \frac {s _ {r}}{V _ {k}} \frac {\partial V _ {k}}{\partial s _ {r}} = \gamma .\tag{4.25}
$$

The direct elasticity $E_{kk}$ is the elasticity of the volume choosing mode k with respect to a change in the level of service of mode k. The cross-elasticity $E_{kr}$ is the elasticity of the volume choosing mode k with respect to a change in the level of service of the competing mode r. The cross-elasticity thus indicates how the volume choosing one alternative is influenced by the characteristics of another alternative. 

## Properties of elasticities

Table 4.2 lists several important properties of elasticities. Elasticities of complex functions can often be derived by sequential application of these basic formulas. For example, consider the multinomial logit (MNL) model: 

$$
\gamma_ {i} = \frac {X _ {i}}{\sum_ {j} X _ {j}},\tag{4.26}
$$

where 

$$
X _ {i} = e ^ {U _ {i}}, \quad U _ {i} = \lambda_ {i} \sum_ {k} (a _ {i k} Y _ {i k}).
$$


Table 4.2 Properties of elasticities


Definition
If y = f(x), then $E_{x}(y) \equiv \frac{x}{y} \frac{\partial y}{\partial x}.$ Property E1
If y = f(w) and w = g(x), then $E_{x}(y) = E_{w}(y)E_{x}(w).$ Property E2
If y = uw, where u = f(x) and w = g(x), then $E_{x}(y) = E_{x}(u) + E_{x}(w).$ Property E3
If y = u/(u + w), where u = f(x) and w = g(x), then $E_{u}(y) = 1 - y,$ $E_{x}(y) = (1 - y)E_{x}(u),$ $E_{w}(y) = y - 1.$ Property E4
If y = u + w, where u = f(x) and w = g(x), then $E_{x}(y) = \frac{u}{y}E_{x}(u) + \frac{w}{y}E_{x}(w).$ Then define f, g, and h as follows: $\gamma_{i} = f(X_{i}), \quad X_{i} = g(U_{i}), \quad U_{i} = h(Y_{ik}).$ Using property E1, we have $E_{Y_{ik}}(\gamma_{i}) = E_{X_{i}}(\gamma_{i})E_{U_{i}}(X_{i})E_{Y_{ik}}(U_{i}).$ Then from table 4.1 we have $E_{X_{i}}(\gamma_{i}) = 1 - \gamma_{i},$ $E_{U_{i}}(X_{i}) = U_{i},$ $E_{Y_{ik}}(U_{i}) = \frac{\lambda_{i} a_{ik} Y_{ik}}{U_{i}}.$ Thus $E_{Y_{ik}}(\gamma_{i}) = (1 - \gamma_{i})\lambda_{i}a_{ik}Y_{ik}.$ (4.27)
Similarly $E_{Y_{jk}}(\gamma_{i}) = -\gamma_{j}\lambda_{j}a_{jk}Y_{jk}.$ (4.28) 

## 4.5.4 Prediction Using Demand Elasticities

The elasticities of a demand function provide a convenient shorthand way of summarizing the behavior represented in a particular function. 

Therefore it is often useful to compare evidence about the values of particular elasticities that have been observed in various situations—for example, elasticities of time and cost obtained in different cities or different countries. Knowledge of the approximate values of key elasticities can also be useful in making quick, approximate estimates of the consumer responses to particular changes. 

In all discussions and practical applications of elasticities, however, the analyst must keep in mind that elasticity is not a constant but a variable. Indeed, as shown in table 4.1, only for product-form relationships is the elasticity constant over the range of variation of a variable. Therefore a numerical value of elasticity can only give an approximate indication of the nature of a relationship. Nevertheless it is often a useful indication. 

The following paragraphs illustrate the use of elasticities for judgments about the effects of various policies. 

## INFERENCES FROM ELASTICITIES

Once a demand model has been obtained, examination of elasticities can lead to useful insights. In an important early study a demand model for urban passenger travel was estimated econometrically as part of a policy study of the effects of possible free (no-fare) transit (Charles River Associates 1968, Domencich, Kraft, and Vallette 1968). The model was analogous in structure to the product form of the Kraft-SARC model. Service attributes and elasticities are shown in table 4.3 for automobile and transit and for work and shopping trips. (Limitations in the data and the estimation methods resulted in (1) some elasticities being constrained to zero by prior hypothesis on signs and (2) an inability to separate out some service attributes, necessitating aggregated estimates.) 

Question 4.1 What inferences can be drawn from these results? Discuss. (For example, you might compare fare sensitivities for work and shopping trips, time and fare sensitivities, and sensitivities to in-vehicle and out-of-vehicle times.) 

■ Answer 4.1 There are a number of conclusions one can draw from these results. First, examine transit trips. Note that for both the time and the cost components, demand is relatively inelastic (-0.09 to -0.71). Second, fare elasticities are greater for shopping trips than for work trips. This corresponds to what our intuition tells us: people making shopping trips should be more sensitive to fare changes than people going to work. Third, time changes (on a percentage basis) would 


Table 4.3 Some examples of elasticities of urban passenger travel demand


<table><tr><td rowspan="2"></td><td colspan="4">Travel time</td></tr><tr><td colspan="2">Direct elasticities</td><td colspan="2">Cross-elasticities</td></tr><tr><td>Auto trips</td><td>Auto IV time</td><td>Auto OV time</td><td>Transit IV time</td><td>Transit OV time</td></tr><tr><td>Work</td><td>-0.820</td><td>-1.437</td><td>0</td><td>0.373</td></tr><tr><td>Shopping</td><td>-1.020</td><td>-1.440</td><td>0.095</td><td>0</td></tr><tr><td>Transit trips</td><td>Transit IV time</td><td>Transit OV time</td><td>Auto IV time</td><td>Auto OV time</td></tr><tr><td>Work</td><td>-0.390</td><td>-0.709</td><td>0</td><td>0</td></tr><tr><td>Shopping</td><td colspan="2"><eq>-0.533^a</eq></td><td>0</td><td>0</td></tr><tr><td rowspan="2"></td><td colspan="4">Travel cost</td></tr><tr><td colspan="2">Direct elasticities</td><td colspan="2">Cross-elasticities</td></tr><tr><td>Auto trips</td><td>Auto LH cost</td><td>Auto OP cost</td><td>Transit LH cost</td><td>Transit AC cost</td></tr><tr><td>Work</td><td>-0.494</td><td>-0.071</td><td>0.138</td><td>0</td></tr><tr><td>Shopping</td><td>-0.878</td><td>-1.650</td><td>0</td><td>0</td></tr><tr><td>Transit trips</td><td>Transit LH cost</td><td>Transit AC cost</td><td>Auto LH cost</td><td>Auto OP cost</td></tr><tr><td>Work</td><td>-0.090</td><td>-0.100</td><td>0</td><td>0</td></tr><tr><td>Shopping</td><td colspan="2"><eq>-0.323^a</eq></td><td>0</td><td>0</td></tr></table>


IV=in-vehicle. OV=out-of-vehicle. LH=line-haul. OP=out-of-pocket. AC=access. $^{a}$ The available shopping transit trip sample was unsuitable for estimating elasticities for the disaggregated time components. 


appear to have two to seven times the effect a fare change would have: for shopping trips $E_{t}(V) = -0.533$ while $E_{c}(V) = -0.323$ . Finally, and perhaps most importantly, changes in out-of-vehicle time ( $t_{ov}$ , waiting and walking times at the collection and distribution ends of transit trips) appear to have a much more significant effect on demand than changes in in-vehicle time ( $t_{iv}$ ): $E_{t_{ov}} = -0.71$ versus $E_{t_{iv}} = -0.39$ . Although the cross-elasticities for all terms are extremely low or negligible, the results indicate that there is more likelihood of shifting transit demand to automobile than there is of shifting automobile users to transit (on a percentage basis). For example, a 1 percent increase in transit line-haul cost will cause a 0.138 percent increase in automobile usage by people going to work, the increase coming from shifted transit users, whereas a 1 percent increase in automobile costs causes almost no shift to transit. This result is somewhat to be expected: automobile users have sunk capital costs into their vehicles, but transit users have no sunk costs, as individuals, in the transit system. 

## PIVOT-POINT METHODS

The preceding discussion has illustrated the policy implications that can be drawn from a simple examination of elasticities. It is also possible to use numerical values of elasticities for incremental prediction by means of “pivot-point” methods. 

The basic concept of pivot-point methods derives directly from the definition of elasticity, 

$$
E _ {X} (V) = \frac {X}{V} \frac {\partial V}{\partial X} \approx \frac {X}{V} \frac {\Delta V}{\Delta X}.\tag{4.29}
$$

Given an initial condition $(X^{0}, V^{0})$ and a change $\Delta X$ , the corresponding change in V can be estimated as follows: 

$$
\varDelta V \approx V ^ {0} \frac {\varDelta X}{X ^ {0}} E _ {X} (V).\tag{4.30}
$$

For example, given an estimate of the transit fare elasticity $E_{c}(V)$ , a simple model for predicting the effect on demand of a fare change would be 

$$
\varDelta V = V \frac {\varDelta c}{c} E _ {c} (V).\tag{4.31}
$$

This is applied in the following example. 

It should be emphasized that while it is a useful, approximate method, pivot-point analysis assumes a constant elasticity. Further, since it uses the point elasticity, the error increases rapidly with the magnitude of the change. 

## Question 4.2

1. If $E_{c}(V) = -0.3$ , the existing fare is 30 cents, and the present volume is 2,000, what change in transit demand will be expected following a fare increase of 10 cents? 

2. How sensitive would this result be to alternative elasticity values of -0.2 and -0.4? 

Answer 4.2 

$$
\Delta V \approx (2, 0 0 0) \left(\frac {1 0}{3 0}\right) (- 0. 3) \approx - 2 0 0.
$$

2. For $E_{c}(V) = -0.2$ , $\Delta V \approx -133$ . 

For $E_{c}(V) = -0.4$ , $\Delta V \approx -267$ . 

## LIMITATIONS ON THE USE OF ELASTICITIES

One must be cautious about the use of elasticities. Michael Kemp has stated the difficulty nicely: 

An elasticity value is merely an abstraction of a very limited amount of information from one portion of the demand surface (two points on the surface, or at best, a uni-directional point gradient) under a particular set of conditions. What it conveys about the nature and structure of demand is minimal. More importantly, a price [or any other] elasticity measured under one particular set of circumstances need not necessarily have any relevance under a different set of circumstances. 

However, as long as one is prepared to talk in very approximate terms, one often finds sufficient pattern or “constancy” in empirically determined values of elasticity to be able at least to distinguish between high and low elasticity commodities. (Kemp 1973, pp. 27–28) 

## 4.5.5 Treatment of Market Segments

In general each market segment (group of prospective users) will have different preferences. For example, the relative weights prospective travelers place on travel time and on fare (or other out-of-pocket costs) will be different for different trip purposes, for groups with different income levels, and at different times of the day or year. Thus the demand function for work trips by high-income travelers will differ from that for shopping and recreational trips, or from that for work trips by low-income travelers. 

These differences can be expressed in the demand functions in a variety of ways. Essentially the differences are reflected in the values of activity-system variables, especially those that reflect the relative weights placed on different travel attributes, and of other variables that characterize the consumers. The major means of incorporating these activity-system variables in the demand functions are stratification, explicit inclusion, and a composite of these two methods. 

In stratification a separate demand function is established for each market segment, with different parameters for each. For example, 

$$
V _ {e m} = a _ {e} c _ {m} + b _ {e} t _ {m},\tag{4.32}
$$

where 

$V_{em}$ = volume of market segment e choosing alternative m, 

$S_{m} = (c_{m}, t_{m}) = \text{service attributes of } m,$ 

$A_{e} = (a_{e}, b_{e}) = \text{parameters reflecting those activity-system characteristics that describe the travel behavior of segment } e.$ 

Some activity-system variables, such as income, can be included in the demand function explicitly. For example, 

$$
V _ {e m} = g I _ {e} + a c _ {m} + b t _ {m},\tag{4.33}
$$

where $I_{e}$ is the median income of market segment e. Thus for work trips originating in different zones the number of trips will vary with the income of the zone, even if $(c_{m}, t_{m})$ is the same from zone to zone. 

Finally, the above two approaches can be combined. For example, 

$$
V _ {e m} = g _ {e} I _ {e} + a _ {e} c _ {m} + b _ {e} t _ {m}.\tag{4.34}
$$

## 4.5.6 Composite Variables

Many demand functions include a number of variables. To better understand the behavior represented in a particular function, it is often useful to group these according to their roles and to form composite variables. Three major groups of variables are often distinguished: 

1. transportation service attributes, which can often be incorporated into a composite service variable; 

2. consumer attributes, the activity-system variables that describe the characteristics and preferences of the customers included in a market segment; and 

3. destination attributes, the activity-system variables that describe the characteristics of alternative destinations. 

## COMPOSITE SERVICE LEVEL

Our discussion of the decision process of the individual consumer was based on the concept of indifference curves among the various transportation service attributes. Each indifference curve indicates those combinations of values of the service attributes for which the consumer has the same utility. In chapter 2 we discussed how the equation of the indifference curve could be used to derive trade-offs among attributes such as the value of time. 

There is a direct analogy to the indifference curve at the level of the aggregate demand function representing the behavior of a group of individuals. For example, consider the following demand functions for modes 1 and 2 (similar to the McLynn model, section 4.3): 

$$
V _ {1} = A \frac {t _ {1} ^ {\beta} c _ {1} ^ {\gamma}}{t _ {1} ^ {\beta} c _ {1} ^ {\gamma} + t _ {2} ^ {\beta} c _ {2} ^ {\gamma}},\tag{4.35}
$$

$$
V _ {2} = A \frac {t _ {2} ^ {\beta} c _ {2} ^ {\gamma}}{t _ {1} ^ {\beta} c _ {1} ^ {\gamma} + t _ {2} ^ {\beta} c _ {2} ^ {\gamma}}.\tag{4.36}
$$

If we define 

$$
L _ {i} \equiv t _ {i} ^ {\beta} c _ {i} ^ {\gamma},\tag{4.37}
$$

we can rewrite (4.35) and (4.36) as 

$$
V _ {1} = A \frac {L _ {1}}{L _ {1} + L _ {2}},\tag{4.38}
$$

$$
V _ {2} = A \frac {L _ {2}}{L _ {1} + L _ {2}}.\tag{4.39}
$$

The total volume $V_{T}$ is given by 

$$
V _ {\mathrm{T}} = V _ {1} + V _ {2} = A,\tag{4.40}
$$

so that 

$$
\frac {V _ {1}}{V _ {1} + V _ {2}} = \frac {L _ {1}}{L _ {1} + L _ {2}} = \frac {1}{1 + (L _ {2} / L _ {1})},\tag{4.41}
$$

$$
\frac {V _ {2}}{V _ {1} + V _ {2}} = \frac {L _ {2}}{L _ {1} + L _ {2}} = \frac {1}{1 + (L _ {1} / L _ {2})}.\tag{4.42}
$$

Thus L expresses the composite effect of all the service attributes on demand. Figure 4.2a shows the shares of model 1 and 2 directly as a function of $L_{2}/L_{1}$ . Figure 4.2b shows the various combinations of $t_{i}$ and $c_{i}$ that will yield the same value of $L_{i}$ . (Note that $L_{i}$ increases with decreasing values of $c_{i}$ and/or $t_{i}$ , since $\beta$ and $\gamma$ are usually negative.) 

Part a shows that if we want to introduce an increase in fare for mode i and still keep $V_{i}$ constant, we must keep the same level of $L_{i}$ . Part b shows that to keep $L_{i}$ constant, we must vary $t_{i}$ as we vary $c_{i}$ . 

We call this variable L, which expresses the composite effect on demand of all of the service attributes, the composite service level. Note that L is positively valued: as it increases, the volume increases, reflecting the view that “service” is positively valued. This is shown in part a of the figure, where $V_{1}$ is an increasing function of $L_{1}$ (relative to $L_{2}$ ). 

Since most service attributes are negatively valued by consumers (time, cost), L is often a negative or inverse function of these variables. Therefore, it is often convenient to use the negative of L, defined as the composite negative worth of service, W. In the technical literature such terms are used as “impedance,” “friction factor,” “generalized cost,” and “generalized price.” These all have roughly the same form as $W_{i}$ ; that is, they are composite service variables that are negatively valued by consumers. In most usages, however, these terms are defined independent of an explicit demand function. The definition used here explicitly recognizes that the composite service level is not arbitrary but is specific to a demand function. 

In particular, the definition of $L$ may be different for different market segments. For example, if the population of consumers is stratified into market segments by income and household size, then the parameters $\beta$ and $\gamma$ in (4.37) will take different values for different market segments (since, as pointed out in section 2.3.2, the ratio of $\beta$ to $\gamma$ represents the value of time relative to cost, and this will vary with income). Therefore the value of the composite service level will be different for each market segment. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/a9a45185-cfa1-407d-8a96-209400065f95/1d73236dcc9cb3ef5fcb53033054e3cd1c1383ace22ca9e20794828a353d41fe.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/a9a45185-cfa1-407d-8a96-209400065f95/cd738525128c85f2476501e5e7f6bd547e213451184fcad224cc79d572053f1d.jpg)



Figure 4.2 Composite service level. a: Shares of modes 1 and 2 as a function of $L_{2} / L_{1}$ . b: Graphs of $L_{i} =$ constant for three constants.


## COMPOSITE ACTIVITY VARIABLES

It is sometimes convenient to collect the effects of some or all the activity-system variables in a demand function into one or two composite variables. These composite activity variables summarize the effect of the activity system on travel demand in much the same way as the 

composite service level L summarizes the effects of the transportation service attributes on demand. 

Activity-system variables in an aggregate demand function tend to fall into two major groups: 

1. destination attributes, which characterize the activities at possible destinations; and 

2. consumer attributes, which characterize the specific market segment in terms of its characteristics at the zone of origin and its preferences. 

Since part of the consumer preference information is reflected in the parameters of service attributes, clearly not all activity-system characteristics can be brought into the composite activity variables. We therefore define two composite activity variables: The composite destination-specific activity variable Z replaces all the activity-system variables characterizing a particular destination. The composite origin-specific activity variable Y replaces all the activity-system variables characterizing the consumers at a particular origin. For example, consider the following demand function: 

$$
V _ {k d m} = \alpha_ {1} P _ {k} ^ {\alpha_ {2}} I _ {k} ^ {\alpha_ {3}} E _ {d} ^ {\alpha_ {4}} L _ {k d m},\tag{4.43}
$$

where P, I, and E represent population, income, and employment level, respectively, L is the composite service level, k and d are the origin and destination of transportation, m is the mode, and the $\alpha_{i}$ are parameters. For this specific demand function we can define 

$$
Y _ {k} = \alpha_ {1} P _ {k} ^ {\alpha_ {2}} I _ {k} ^ {\alpha_ {3}},\tag{4.44}
$$

$$
Z _ {d} = E _ {d} ^ {\alpha_ {4}},\tag{4.45}
$$

and the demand function can be written 

$$
V _ {k d m} = Y _ {k} Z _ {d} L _ {k d m}.\tag{4.46}
$$

It is often useful, in comparing demand functions, to construct such composite variables and write the demand functions in terms of them. This helps in isolating similarities and differences among the various models (see exercise 4.1). Composite variables are also useful for analysis of elasticities using the elasticity properties in table 4.2. 

■ Question 4.3 Consider the demand function 

$$
V _ {1 2} = P _ {1} ^ {\alpha_ {1}} P _ {2} ^ {\alpha_ {2}} t ^ {\alpha_ {3}} q ^ {\alpha_ {4}} c ^ {\alpha_ {5}},
$$

where 

$P_{1}$ = population at zone 1, 

Aggregate Prediction of Behavior 

$P_{2}$ = population at zone 2, 

t = travel time between 1 and 2 (hours). 

q = frequency of service between 1 and 2 (per day), 

c = fare between 1 and 2 (dollars), 

$$
(P _ {1} ^ {\alpha_ {1}} P _ {2} ^ {\alpha_ {2}}) = 1 0, 0 0 0,
$$

$$
\alpha_ {3} = - 2,
$$

$$
\alpha_ {4} = + 0. 8,
$$

$$
\alpha_ {5} = - 1.
$$

The present level of volume is 1,088 trips per day. A fare increase of 20 percent is being contemplated. If the transportation operator wants to keep the same travel volume, what changes in service could he consider? 

■ Answer 4.3 Examining the demand function, we observe that the composite service level is 

$$
L _ {1 2} = t ^ {\alpha_ {3}} q ^ {\alpha_ {4}} c ^ {\alpha_ {5}}.
$$

As long as $L_{12}$ remains constant, the volume $V_{12}$ will remain constant. Since $E_{c}(L) = \alpha_{5}$ , $E_{t}(L) = \alpha_{3}$ , and $E_{q}(L) = \alpha_{4}$ , if we increase c by 20 percent, this will result in an (approximate) increase in L of $0.20\alpha_{5}$ , or 20 percent. To counter this, we can make changes in frequency of service, in time, or in both. If we choose to increase q, the required percentage change is $0.20\alpha_{5}/\alpha_{4}$ , or +25 percent. This can be derived as follows: 

i. $\Delta L_{1} \approx E_{c}(L) \frac{L}{c} \Delta c = \alpha_{5} \frac{L}{c} \Delta c,$ 

ii. $\Delta L_{2} \approx E_{q}(L) \frac{L}{q} \Delta q = \alpha_{4} \frac{L}{q} \Delta q,$ 

iii. $\Delta L_{1} = \Delta L_{2},$ 

iv. $\Delta q \approx \frac{\alpha_5}{\alpha_4} \frac{q}{c} \Delta c,$ 

$$
\mathrm{v.} \frac {\Delta q}{q} \approx \frac {\alpha_ {5}}{\alpha_ {4}} \frac {\Delta c}{c}.
$$

This is an approximate relationship. For a more precise answer, it would be necessary to integrate along the demand curve or to use the demand function explicitly. 

## 4.5.7 Choice-Specific and Choice-Independent Attributes (Optional Reading)

## A DISAGGREGATE VIEW

Consider the following utility functions for two modes, rail (R) and air (A): 

Aggregate Prediction of Behavior 

$$
U _ {\mathrm{R}} = \alpha_ {\mathrm{R}} t _ {\mathrm{R}} + \beta_ {\mathrm{R}} c _ {\mathrm{R}},\tag{4.47}
$$

$$
U _ {\mathrm{A}} = \alpha_ {\mathrm{A}} t _ {\mathrm{A}} + \beta_ {\mathrm{A}} c _ {\mathrm{A}}.\tag{4.48}
$$

The attributes are time t and cost c. 

Two cases of parameter values can be identified: 

$$
\begin{array}{l l} \text { Case   I: } & \alpha_ {\mathrm{R}} = \alpha_ {\mathrm{A}} = \alpha , \qquad \beta_ {\mathrm{R}} = \beta_ {\mathrm{A}} = \beta , \\ \text { Case   II: } & \alpha_ {\mathrm{R}} \neq \alpha_ {\mathrm{A}}, \qquad \beta_ {\mathrm{R}} \neq \beta_ {\mathrm{A}}. \end{array}
$$

In the first case the two utility functions become identical and independent of the modes: 

$$
U _ {m} = \alpha t _ {m} + \beta c _ {m}.\tag{4.49}
$$

Thus the attributes t and c are not defined specific to the modes, but are common to both modes; the attributes are choice-independent. Each mode is characterized by the same attributes and the same utility function, although of course the /evel/s of the attributes and of the utilities will usually be different. 

In case II the attributes have a different effect on each mode; because $\alpha_{R} \neq \alpha_{A}$ , a minute of time by rail is, apparently, not worth the same as a minute of time by air. 

A common assumption is the hypothesis of choice-independent utilities, which states that the utility function $U_{m}$ over the attributes of a set of choices is independent of the specific choices being compared. When we apply this hypothesis, we are assuming that we can include all the aspects of each choice that may be influencing a consumer's decision in a utility function whose parameters are independent of the choices. 

This hypothesis may be invalid in a particular situation for any of several reasons: 

1. We have ignored attributes that the consumer considers important. 

2. We are not measuring the attributes in the same way he measures them. 

3. Our knowledge of the weights he places on the attributes is imperfect. 

To accurately predict the consumer's behavior in such a situation, we must incorporate in his utility function one or more elements that are specific to a particular choice and that reflect those attributes of the choice that have been omitted or measured imperfectly or for which information about weights is imperfect. These are called choice-specific attributes. 

In transportation, particularly at the present state of knowledge, the hypothesis of choice-independent utilities is often not completely realistic. For example, in passenger transportation it is difficult to represent adequately such attributes as privacy or flexibility of route and time of trip, which are important aspects of automobile travel. This hypothesis is therefore particularly critical in attempting to predict which mode the traveler will choose. Because of the significance of the mode-choice problem, a name often given to this hypothesis is the abstract-mode assumption: it deals with the question of whether we can characterize each mode by the same attributes—without, in a sense, knowing its name—or whether we must know which mode we are dealing with in order to predict the utility perceived by the consumer. 

In the general situation where we must allow for choice-dependent utilities, we might have utility functions that look like 

$$
U _ {m} = \beta_ {m} + \sum_ {i} \alpha_ {m i} X _ {m i}\tag{4.50}
$$

or 

$$
U _ {m} = \beta_ {m} \prod_ {i} X _ {m i} ^ {\alpha_ {m i}}.\tag{4.51}
$$

In these forms the unique characteristics of each alternative are expressed through several means. The weights $\beta_{m}$ are given to the modes independent of their explicit attributes. For example, in the linear form $\beta_{m}$ may give greater attractiveness to the automobile than to other modes because of its schedule and route flexibility. The weights $\alpha_{mi}$ on attributes $X_{i}$ depend on the specific alternative. For example, a minute of travel time in an automobile may be more attractive than a minute in a bus if the driver enjoys listening to his own radio or stereo tapes in the car, or it may be less attractive if he enjoys being free to read the newspaper and is annoyed by driving through traffic; and a minute of time waiting in an airport lounge may be weighted differently from a minute of time in an intercity bus terminal. 

In the demand model used in chapter 3 the hypothesis of choice-independent utilities was partially met: 

$$
U _ {\mathrm{T}} = \theta_ {\mathrm{T}} + \theta_ {1} t _ {\mathrm{T}} + \theta_ {2} \frac {x _ {\mathrm{T}}}{d} + \theta_ {3} \frac {c _ {\mathrm{T}}}{y},\tag{4.52}
$$

$$
U _ {\mathrm{A}} = \theta_ {\mathrm{A}} + \theta_ {1} t _ {\mathrm{A}} + \theta_ {2} \frac {x _ {\mathrm{A}}}{d} + \theta_ {3} \frac {c _ {\mathrm{A}}}{y}.\tag{4.53}
$$

Here the coefficients of in-vehicle and out-of-vehicle times and of cost are the same for both automobile and transit. Thus these attributes in the model are choice-independent. However, there is a need to reflect important remaining differences between automobile and transit, resulting in the choice-specific constants, $\theta_{T}$ and $\theta_{A}$ . Thus the utilities are partially choice-independent. 

In our development of models for predicting consumer behavior in transportation we shall always strive toward the objective of sufficient understanding of the consumer so that we can utilize the hypothesis of choice-independent utilities. Then we shall be able to predict the response of the consumer to any choice that may be offered him. We shall often fall short of this objective, however, and be forced to employ utility models that are at least partially choice-dependent and that include some attributes that are choice-specific. For example, the automobile as a mode and the central business district as a destination will often enter passenger demand models with choice-specific attributes. 

## AN AGGREGATE VIEW

If the hypothesis of choice-independent utilities applies at the level of the individual consumer, for all consumers in a group, then the aggregate demand function for the group as a whole will exhibit similar independence of the specific choices. 

Operationally this means that the parameters of the demand function are independent of the alternative choices. For example, consider an aggregate analog to $(4.47)$ : 

$$
V _ {\mathrm{R}} = \gamma t _ {\mathrm{R}} ^ {\alpha_ {\mathrm{R}}} c _ {\mathrm{R}} ^ {\beta_ {\mathrm{R}}}\tag{4.54}
$$

$$
V _ {\mathrm{A}} = \gamma t _ {\mathrm{A}} ^ {\alpha_ {\mathrm{A}}} c _ {\mathrm{A}} ^ {\beta_ {\mathrm{A}}}.\tag{4.55}
$$

Again, if $\alpha_{\mathrm{R}} = \alpha_{\mathrm{A}} = \alpha$ and $\beta_{\mathrm{R}} = \beta_{\mathrm{A}} = \beta$ , the general model is 

$$
V _ {m} = \gamma t _ {m} ^ {\alpha} c _ {m} ^ {\beta}\tag{4.56}
$$

and the attributes are choice-independent; we can also say that the model itself is choice-abstract. 

There are several significant advantages when the condition of choice independence applies. First, far fewer parameters must be estimated to get the demand function for a particular situation, and so available data can be used more effectively. Second, the analyst can feel more confident in using the demand model to predict consumer response to conditions basically different from those observed so far (for example, when a completely new mode of transport is to be introduced), because it is sufficient to characterize that mode only by its attributes. (If each mode needed different parameters $\alpha_{mi}$ , then the 

analyst would have to guess their values for the new mode. Is it most like existing mode 1, 2, or 3?) 

Analysts have historically striven to develop transportation demand models that are choice-abstract. Their efforts began with simple “diversion curves,” in which the volume of traffic in a corridor was assumed to divide between a freeway and parallel arterial streets according to some ratio of the travel times (Martin, Memmott, and Bone 1961, FHWA 1973b). Later the term “abstract mode” was used to designate a group of specific intercity passenger demand models that also reflected this hypothesis of choice-independent utilities (for example, the Baumol-Quandt model in section 4.3). The concepts as defined here apply to all types of travel choices, as will be discussed in chapter 11. 

## 4.6 SIMPLE PREDICTION METHODS

In general the prediction of flows requires explicit consideration of both service and demand models, as indicated in chapter 1. Often, however, it is possible to make useful predictions using only demand functions (for example, when service levels are assumed known—see chapter 8). 

When there is available both a complete aggregate demand function, including all the parameter values, and also the necessary data, then the prediction of flows is straightforward. On the other hand, the analyst is often confronted with situations in which there is limited information available and estimates are needed quickly. Particularly common are situations in which there is inadequate time or resources to calibrate a model for a particular situation. In such cases approximate prediction methods using knowledge gained elsewhere can be quite useful. There are several methods available. 

4.6.1 The Use of Limited Information: Incremental Analysis Often the only data an analyst will find available will be present volumes $V^{0}$ and service levels $S^{0}$ . No other demand-related information can be collected. How can the analyst make best use of these data? 

One approach is to adapt information developed elsewhere, such as values of demand parameters or elasticities, perhaps modified by judgment. In this section we shall show how such information can be utilized. 

There are several possible approaches for utilizing limited information in this context with an incremental-analysis approach based on the observed flows $(V^{0}, S^{0})$ : pivot-point analysis using elasticities or model structure assumptions, or “judgmental-model” analysis. 

The concept behind pivot-point analysis was described in section 4.5.4. For a single mode and a single service attribute, the change in volume $\Delta V$ is estimated as a function of the change in service level and the elasticity $E_{S}(V)$ (Pecknold, Wilson, and Kullman 1972): 

$$
\varDelta V \approx V ^ {0} \frac {\varDelta S}{S ^ {0}} E _ {S} (V).\tag{4.57}
$$

No judgment about the form of the demand function is required. (Note that this approach is equivalent to assuming a product-form model, in that elasticity is assumed constant, and also a linear-form model, in that the change in V is assumed to be proportional to the change in S. These assumptions, while acceptable for small changes, are inconsistent and not acceptable for large changes.) 

To apply the pivot-point approach with elasticities, only the numerical value of the elasticity $E_{s}(V)$ is required, as indicated by equation (4.57), provided the change $\Delta S$ is in only one attribute. If several attributes change simultaneously, a more complex approach is required. In this case it is necessary to assume a functional form of the demand function or at least of the composite service level L, so that a more precise expression can be derived for the change in volume corresponding to the multidimensional service change. 

The derivatives and elasticities of common demand function forms were given in table 4.1. The variable X used there can be a single variable or a function of several variables, such as a composite service level that is a function of several service attributes. In the latter case the total elasticity can be computed as a function of the desired variables using the various properties of elasticities given in table 4.2 (see exercise 4.1). 

Some types of demand models lend themselves to a variation of pivot-point analysis in which judgments are made about the structural form of a model and about elasticities or (equivalently) the value(s) of key parameter(s). Share-type models are particularly useful in this respect. As will be shown in section 4.6.2, $\Delta V$ for a given mode is a function of the existing shares and of a parameter that can be estimated directly or derived from an estimate of a corresponding elasticity. For example, for a multinomial logit model, the new share $\gamma_{m}^{\prime}$ is a function only of the old share $\gamma_{m}^{0}$ and the change in utility, $U_{m}^{\prime} - U_{m}^{0}$ , so the only parameters required are the coefficients of those service attributes that change (for example, the coefficient of time in the utility function if only time is changed). The value of this coefficient can be estimated on the basis of empirical evidence or from an assumed elasticity. 

Finally, in the judgmental-model approach a demand model is estimated by judgment so that it meets two conditions: it fits the observed flows $(V^{0}, S^{0})$ , and it is consistent with judgments made about elasticities or other elements (such as the flows for other certain sets of conditions). Many model forms lend themselves to this approach, as shown below in the case of share models such as the multinomial logit. Specific relationships can be derived through which information on observed flows and judgments about elasticities can be used to estimate model parameters. These are described in section 4.6.3. 

## 4.6.2 Pivot-Point Analysis with an Assumed Model Structure (Optional Reading)

To illustrate this approach we shall analyze the class of share-type models. Many demand models are (or can be) expressed as share-type models: 

$$
\frac {V _ {i}}{V} = \frac {R _ {i}}{R},\tag{4.58}
$$

where 

$$
V = \sum_ {i} V _ {i}, \quad R = \sum_ {i} R _ {i}.
$$

Here $R_{i}$ is a function of activity-system and service variables and $V_{i}$ is the volume of travelers making travel choice i. The share of a choice i is 

$$
\gamma_ {i} \equiv \frac {V _ {i}}{V}.\tag{4.59}
$$

For any change in service (or other) variables, for a single choice i, 

$$
\rho_ {i} \equiv \frac {R _ {i} ^ {\prime}}{R _ {i} ^ {0}},\tag{4.60}
$$

where the superscript zero indicates an initial value, the prime indicates the value following a change, and 

$$
R _ {j} ^ {\prime} = R _ {j} ^ {0} \quad \text { for   all } \quad j \neq i\tag{4.61}
$$

(that is, $\rho_{j} = 1$ for $j \neq i$ ). Then it can be shown that the new share of mode i is 

$$
\begin{array}{r l} \gamma_ {i} ^ {\prime} & = \frac {\rho_ {i} \gamma_ {i} ^ {0}}{\rho_ {i} \gamma_ {i} ^ {0} + (1 - \gamma_ {i} ^ {0})} \\ & = \frac {1}{1 + \frac {1}{\rho_ {i}} \left[ \frac {1 - \gamma_ {i} ^ {0}}{\gamma_ {i} ^ {0}} \right]}. \end{array}\tag{4.62}
$$

For example, for the logistic form (as in the multinomial logit model), 

$$
R _ {i} = e ^ {U _ {i}},\tag{4.63}
$$

$$
\gamma_ {i} ^ {\prime} = \frac {1}{1 + e ^ {- \Delta U _ {i}} \left[ \frac {1 - \gamma_ {i} ^ {0}}{\gamma_ {i} ^ {0}} \right]},\tag{4.64}
$$

where 

$$
\begin{array}{l} \varDelta U _ {i} = U _ {i} ^ {\prime} - U _ {i} ^ {0}, \\ \rho_ {i} = e ^ {\varDelta U _ {i}}. \end{array}
$$

Note that $(4.64)$ is an exact relationship, not an approximate one as in the pivot-point approach using elasticities (section 4.5.4). 

In the more general case where $(4.61)$ does not hold, 

$$
\begin{array}{l} \gamma_ {i} ^ {\prime} = \frac {\rho_ {i} \gamma_ {i} ^ {0}}{\sum_ {j} \rho_ {j} \gamma_ {j} ^ {0}} \\ = \frac {1}{1 + (\rho_ {i} \gamma_ {i} ^ {0}) ^ {- 1} \sum_ {j \neq i} \rho_ {j} \gamma_ {j} ^ {0}}. \end{array}\tag{4.65}
$$

The corresponding form when (4.63) applies is 

$$
\begin{array}{l} \gamma_ {i} ^ {\prime} = \frac {\gamma_ {i} ^ {0} e ^ {\Delta U _ {i}}}{\sum_ {j} \gamma_ {j} ^ {0} e ^ {\Delta U _ {j}}} \\ = \frac {1}{1 + (\gamma_ {i} ^ {0} e ^ {\Delta U _ {i}}) ^ {- 1} \sum_ {j \neq i} \gamma_ {j} ^ {0} e ^ {\Delta U _ {i}}}. \end{array}\tag{4.66}
$$

Thus for models that can be expressed in share form the changes in shares for any change in activity-system or service variables can be estimated directly from the present shares $\gamma_{i}^{0}$ and the value of $\rho$ for the specific change. An estimate of $\rho$ requires knowledge of, or assumptions about, the form and parameter values of the composite function R only insofar as they concern the variables changing. 

As an example consider 

$$
R _ {i} = e ^ {U _ {i}}, \qquad U _ {i} = \sum_ {k} a _ {k} Y _ {i k}.\tag{4.67}
$$

In the case of a single variable $Y_{ik'}$ , 

$$
\rho_ {i} = e ^ {\varDelta U _ {i}} = e ^ {a _ {k ^ {\prime}} \varDelta Y _ {i k ^ {\prime}}}.\tag{4.68}
$$

The only parameter value needed is $a_{k'}$ (along with $\Delta Y_{ik'}$ of course); this can be estimated directly or by estimating the elasticity $E_{Y_{ik'}}(\gamma_i)$ 

and deriving the corresponding value of $a_{k'}$ from that estimate, using the relationship for elasticity of a multinomial logit model (4.27): 

$$
E _ {Y _ {i k ^ {\prime}}} (\gamma_ {i}) = (1 - \gamma_ {i}) a _ {k ^ {\prime}} Y _ {i k ^ {\prime}};\tag{4.69}
$$

thus 

$$
a _ {k ^ {\prime}} = \frac {E _ {Y _ {i k ^ {\prime}}} (\gamma_ {i})}{Y _ {i k ^ {\prime}} (1 - \gamma_ {i})}.\tag{4.70}
$$

## 4.6.3 Incremental Analysis Using a Judgmentally Estimated Model (Optional Reading)

To apply the judgmental-model approach assumptions must be made about the form of the model and about numerical values of elasticities or other parameters. (Alternative sets of assumptions can and usually should be made in order to produce a sensitivity analysis.) For a specific model, and given the observed flows, certain relationships must exist among the parameters, depending on the model form. The second column of table 4.4 shows these relationships for some basic forms: given an observation $(V_0, X_0)$ and an estimate of some parameter(s) 


Table 4.4 Relations among parameters and elasticities


<table><tr><td></td><td>Demand function</td><td>Parameter relations at an observed point (V0, X0)</td><td>Relation to elasticities</td></tr><tr><td>Linear</td><td>V = α + βX</td><td>α = V0 - βX0</td><td>α = V0 (1 - E)β = <eq>\frac{V_0}{X_0}E</eq></td></tr><tr><td>Product</td><td>V = αXβ</td><td>α = V0X0-β</td><td>α = V0X0-Eβ = E</td></tr><tr><td>Exponential</td><td>V = αeβX</td><td>α = V0 e-βX0</td><td>α = V0 e-Eβ = <eq>\frac{E}{X_0}</eq></td></tr><tr><td>Logistic</td><td>V = <eq>\frac{\alpha}{1 + \gamma e^{\beta X}}</eq></td><td>α = V0(1 + γeβX0)</td><td>β = <eq>\frac{-E/X_0}{1 - (V_0/\alpha)}</eq>γ = <eq>\frac{1 - (V_0/\alpha)}{V_0/\alpha} e^{-\beta X_0}</eq></td></tr><tr><td>Logistic-product</td><td>V = <eq>\frac{\alpha}{1 + \gamma X^{\beta}}</eq></td><td>α = V0 (1 + γXβ)</td><td>β = <eq>\frac{-E}{1 - (V_0/\alpha)}</eq>γ = <eq>\frac{\log \left[ \frac{1 - (V_0/\alpha)}{V_0/\alpha} \right]}{\log X_0}</eq></td></tr></table>

( $\beta$ ; $\gamma$ where applicable), the remaining parameter $\alpha$ is a function of these data. Thus an observation and a judgment can be used to “fit” a model. 

Alternatively judgments can be made about the elasticity, $E_{X}(V)$ . As shown in the third column of the table, for the first three forms, with only two parameters $\alpha$ and $\beta$ , an estimate of E together with the observation $(V_{0}, X_{0})$ is sufficient to “fit” a model. For the others, an estimate of one additional parameter, $\alpha$ , is required. 

4.7 PREDICTION WITH DISAGGREGATE DEMAND FUNCTIONS
As indicated in the preceding section, prediction using aggregate demand functions is relatively straightforward when service levels are assumed known. One can use either the entire demand function or various simple methods. 

Prediction with disaggregate demand functions requires a little more care. The methods for predicting the behavior of a group of consumers from disaggregate functions fall into two basic categories: 1. development of an aggregate demand function from the disaggregate function; 

2. use of the disaggregate function directly. 

4.7.1 Aggregating Individual Preferences into Demand Functions In principle, an aggregate demand function for a market segment can be derived from the individual utility functions for each member of the group. 

Consider a utility function of the form 

$$
U _ {m j} = \alpha_ {j} t _ {m} + (\beta_ {j} / y _ {j}) c _ {m},\tag{4.71}
$$

where 

$t_{m}, c_{m} =$ service attributes of alternative $m$ , 

$\alpha_{j}, \beta_{j} =$ preferences of consumer $j$ , 

$y_{j}$ = yearly income of consumer j. 

Assume that the N individuals in the group can be divided into subgroups j, of size $n_{j}$ , such that all the individuals in a subgroup have the same preferences and income $(\alpha_{j}, \beta_{j}, y_{j})$ . For a given service level S, we can then determine which alternative m the individuals in a given subgroup j will pick: define $r_{mj} = 1$ if subgroup j picks alternative m, and $r_{mj} = 0$ otherwise. Summing over all the subgroups, we can get the aggregate demand for alternative m: 

$$
V _ {m} = \sum_ {j} r _ {m j} n _ {j}.\tag{4.72}
$$

This aggregate demand depends, of course, on the level of service: as S changes, so also will the $r_{mj}$ and the $V_{m}$ . If we explicitly explore a large number of such changes, we can observe how $V_{m}$ changes as S changes. (This was demonstrated in section 2.4.) 

Thus, in principle, we can develop the aggregate demand function for the group as a whole by knowing (1) the individual utility functions, (2) the distribution of individuals in the group by subgroups (that is, their characteristics and preferences), and (3) the characteristics of the choices they face. 

In practice, it is difficult to derive an aggregate demand function explicitly with either deterministic or stochastic disaggregate functions. The primary source of difficulty is the need to integrate the disaggregate function over the distribution of individual characteristics. If $p(\alpha_{j}, \beta, y_{j})$ is the distribution of individual characteristics, and if $r_{mj}$ is replaced by $D_{f}(\mathbf{S}, \alpha_{j}, \beta_{j}, y_{j})$ , where $D_{f}$ is the disaggregate demand function, then (4.72) becomes 

$$
V _ {m} (\mathbf {S}) = \sum_ {j} n _ {j} \iiint p (\alpha_ {j}, \beta_ {j}, y _ {j}) D _ {f} (\mathbf {S}, \alpha_ {j}, \beta_ {j}, y _ {j}) d (\alpha , \beta , y).\tag{4.73}
$$

This integration is impractical except under very special conditions that are of limited practical importance, such as a demand function linear in all variables or probability distributions that degenerate into single values (see Koppelman 1975, 1976b; also Koppelman and Ben-Akiva 1977, Blackburn 1970). However, it indicates the nature of the problem of using disaggregate demand functions: it is necessary to incorporate in some way the distribution of characteristics represented by $p(\alpha, \beta, y)$ . 

These relationships are illustrated in figure 4.3. Here an aggregation procedure is a procedure that uses a disaggregate demand model together with information on the distribution of activity-system and service-level characteristics to produce a prediction of aggregate behavior. 

## 4.7.2 Practical Approaches

While deriving an aggregated demand function explicitly is generally impractical, there are many practical aggregation procedures that can be used to predict aggregate behavior with a disaggregate demand function (Koppelman 1975, 1976b). In relation to figure 4.3 these aggregation procedures are essentially alternate ways of representing the distribution of independent variables and operating on them with the disaggregate demand function. In this section we discuss some currently used approaches. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/a9a45185-cfa1-407d-8a96-209400065f95/6bd6aca305bb87da7576cd543853d232d9b91d572f1228708a132c00c1b6ca7e.jpg)



Figure 4.3 Predicting aggregate behavior with a disaggregate model. Adapted from Koppelman (1975).


## THE NAIVE APPROACH

Each market segment is characterized by its average characteristics (for example, $\bar{\alpha}$ , $\bar{\beta}$ , $\bar{y}$ , and $\bar{S}$ ), and the disaggregate function $D_{f}$ is used with these average values: 

$$
V _ {m} (\mathbf {S}) = N D _ {f} (\bar {\mathbf {S}}, \bar {\alpha}, \bar {\beta}, \bar {\gamma}),\tag{4.74}
$$

where 

$\bar{\alpha} = \sum_{j}\alpha_{j}n_{j} / N,$ and so forth. 

## CLASSIFICATION

Each market segment is divided into subgroups of size $n_{j}$ ; for each subgroup j mean values of the characteristics ( $\bar{\alpha}_{j}, \bar{\beta}_{j}, \bar{y}_{j}$ , and $\bar{S}_{j}$ ) are used together with the disaggregate function to predict a response; then the response of the market segment as a whole is obtained as 

$$
V _ {m} (\mathbf {S}) = \sum_ {j} n _ {j} D _ {f} (\bar {\mathbf {S}} _ {j}, \bar {\alpha} _ {j}, \bar {\beta} _ {j}, \bar {y} _ {j}).\tag{4.75}
$$

This approach is particularly useful when the variables that have the greatest influence on an individual's choices are used as a basis of classification. For example, in an urban mode-choice model, if no automobile is available, then the choice "drive alone" is not available. Separating each market segment into those with access to an automobile and those without is thus a useful classification. Historically the latter group, called “transit-captive,” has been separated out in aggregate modeling. Similarly, whether the individual has his origin (or destination) within walking distance of a transit line-haul or feeder service determines whether transit is a realistically available choice; households can thus be classified as to whether they are “auto-captive” or not. In the first case classification is by automobile ownership level (0; 1 or more); in the second, by transit service level (whether or not the traveler lives beyond a maximum walk distance to transit; see figure 3.8). Income is often also an important variable in classification. 

## DISTRIBUTIONS

For each market segment the distribution of characteristics $(\alpha, \beta, y, S)$ is represented in one of several ways: by explicit probability density functions characterized by their parameters or their moments, or by an explicit frequency distribution. 

## SAMPLING

For each market segment a population of M individuals is constructed, either from the original data base used in developing the demand function or from other data sources. Then a sample of k individuals is drawn from this population. To predict an individual's behavior, that person's socioeconomic characteristics $(\alpha_{i}, \beta_{i}, y_{i})$ together with the appropriate service levels $(S_{i})$ are used in the disaggregate demand function $D_{f}$ . The predicted behaviors of the sample of k individuals are then tabulated as in (4.72), and this estimate is expanded (by the ratio M/k) to obtain the predicted behavior of the market segment as a whole. The general methodology is shown in figure 4.4. 

A particularly interesting example of the sampling approach appeared in a recent study of the energy consequences of alternative freight transportation policies (Roberts et al. 1976). 

These are only a few of the major approaches available. Various combinations of these and other approaches are also useful; for example, sampling or distributions can be combined with classification. Alternatively the sample can be synthesized from aggregate data (Watanatada 1977, Manheim, Furth, and Salomon 1977). 

## 4.7.3 Prediction with Disaggregate Models: An Example

In this section we shall expand the urban transportation example introduced in chapter 3 to demonstrate prediction with a disaggregate function. This example will also help explain why a disaggregate approach is often more effective than an aggregate one. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/a9a45185-cfa1-407d-8a96-209400065f95/8c2a2c5a58c057362000b283116509e6342d272d1bfa6882c53b8fd2f1cc0238.jpg)



Figure 4.4 Sampling approach to prediction.


## THE POPULATION

We consider the corridor shown in figure 3.4. Zones 1 and 2 are residential zones; zones 3 and 4 are locations of workplaces. Thus there are four origin-destination zone pairs: 1–3, 1–4, 2–3, and 2–4. 

The households in this corridor have different levels of income and of automobile ownership. The mode-choice model to be used was shown in table 3.3. The model includes income and number of automobiles owned explicitly as variables. Thus choice behavior, as shown by the choice probabilities, varies with socioeconomic characteristics as well as with the service attributes of the available choices. 

We shall use the method of classification and shall classify households in the corridor by level of automobile ownership and income, dividing each variable into classes. Further, based on the analyses of chapter 3, we know that it is important to distinguish the different types of trip profiles available, specifically the “access” choices. Thus we consider the following combinations: 

I. Origin-destination pairs 

- two origins: zones 1 and 2 

- two destinations: zones 3 and 4 

- total: four origin-destination zone pairs 


Table 4.5 Distribution of 1,000 households with origin in zone 1 and destination in zone 4


<table><tr><td rowspan="3">Income</td><td colspan="9">Automobiles per licensed driver (<eq>a_{LD}</eq>)</td><td rowspan="2" colspan="3">Total</td></tr><tr><td colspan="3">0</td><td colspan="3">0.5</td><td colspan="3">1.0</td></tr><tr><td>LH</td><td>F-LH</td><td>Total</td><td>LH</td><td>F-LH</td><td>Total</td><td>LH</td><td>F-LH</td><td>Total</td><td>LH</td><td>F-LH</td><td>Total</td></tr><tr><td rowspan="2">$5,000</td><td>0</td><td>0</td><td>0</td><td>150</td><td>200</td><td>350</td><td>0</td><td>0</td><td>0</td><td>150</td><td>200</td><td>350</td></tr><tr><td></td><td></td><td></td><td>15%</td><td>20%</td><td>35%</td><td></td><td></td><td></td><td>15%</td><td>20%</td><td>35%</td></tr><tr><td rowspan="2">$10,000</td><td>0</td><td>0</td><td>0</td><td>100</td><td>0</td><td>100</td><td>0</td><td>50</td><td>50</td><td>100</td><td>50</td><td>150</td></tr><tr><td></td><td></td><td></td><td>10%</td><td></td><td>10%</td><td></td><td>5%</td><td>5%</td><td>10%</td><td>5%</td><td>15%</td></tr><tr><td rowspan="2">$15,000</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>350</td><td>150</td><td>500</td><td>350</td><td>150</td><td>500</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>35%</td><td>15%</td><td>50%</td><td>35%</td><td>15%</td><td>50%</td></tr><tr><td rowspan="2">Total</td><td>0</td><td>0</td><td>0</td><td>250</td><td>200</td><td>450</td><td>350</td><td>200</td><td>550</td><td>600</td><td>400</td><td>1,000</td></tr><tr><td></td><td></td><td></td><td>25%</td><td>20%</td><td>45%</td><td>35%</td><td>20%</td><td>55%</td><td>60%</td><td>40%</td><td>100%</td></tr></table>

II. Market segments 

- three levels of income 

- three levels of automobile ownership 

- total: nine segments, defined by combinations of income and automobile ownership 

III. Level of access choices 

- two cases within each origin zone: 

Case 1: within walking distance of line-haul transit station 

Case 2: within walking distance of feeder transit station but beyond walking distance of line-haul transit 

• total: two combinations: $^{3}$ 

Combination 1: within walking distance at home and workplace zones (line-haul only, LH) 

Combination 2: within walking distance at workplace zone but not at home zone (feeder to line-haul, F–LH) 

The resulting distribution of households, by classification, for one origin-destination pair and three trip profiles is shown in table 4.5. The levels of service that confront trips from zone 1 to zone 4 are those used in chapter 3 (summarized in table 4.6); the others can be estimated in the same way as in that chapter. 


Table 4.6 Levels of service encountered by two classes of travelers


<table><tr><td></td><td><eq>t_{A}</eq> (min)</td><td><eq>x_{A}</eq> (min)</td><td><eq>c_{A}</eq> (<eq>\varnothing</eq>)</td><td><eq>t_{T}</eq> (min)</td><td><eq>x_{T}</eq> (min)</td><td><eq>c_{T}</eq> (<eq>\varnothing</eq>)</td><td><eq>d</eq> (miles)</td></tr><tr><td>LH</td><td>11.3</td><td>5</td><td>122.5</td><td>14</td><td>8</td><td>50</td><td>7.25</td></tr><tr><td>F–LH</td><td>14.2</td><td>5</td><td>131.3</td><td>21.7</td><td>15.5</td><td>75</td><td>8.13</td></tr></table>

Groups of individuals differing by origin and destination zones, and by location within those zones (as reflected in the different access conditions and available trip profiles), face different levels of service. Thus two groups with the same socioeconomic attributes may make different choices. 

## PREDICTION USING CLASSIFICATION

Table 4.7 shows the automobile and transit choice probabilities for various market segments and trip profiles with origin in zone 1 and destination in zone 4. This table, developed using the methods described in chapter 3, shows that mode-choice probabilities vary quite significantly within an origin-destination zone combination. 

Using the numbers of individuals falling into each combination of conditions from table 4.5, average (weighted) mode-choice probabilities can be derived: 

$$
\bar {p} _ {\mathrm{T}} = \sum_ {i, j, k} p _ {\mathrm{T}} (i, j, k) \frac {n _ {i j k}}{N},\tag{4.76}
$$

where i indicates income class, j automobile ownership class, k access class, $n_{ijk}$ the number of households in class $(i, j, k)$ , $p_{\mathrm{T}}(i, j, k)$ the probability of choosing transit for a household in class $(i, j, k)$ , and 

N = total number of households = $\sum_{i,j,k} n_{ijk}$ . 


Table 4.7 Mode-choice probabilities for travelers with origin in zone 1 and destination in zone 4


<table><tr><td rowspan="3">Income</td><td colspan="6">Automobiles per licensed driver (<eq>a_{LD}</eq>)</td></tr><tr><td colspan="2">0</td><td colspan="2">0.5</td><td colspan="2">1.0</td></tr><tr><td>LH</td><td>F-LH</td><td>LH</td><td>F-LH</td><td>LH</td><td>F-LH</td></tr><tr><td>$5,000</td><td>0.89</td><td>0.81</td><td>0.65</td><td>0.51</td><td>0.31</td><td>0.20</td></tr><tr><td>$10,000</td><td>0.78</td><td>0.67</td><td>0.46</td><td>0.33</td><td>0.17</td><td>0.11</td></tr><tr><td>$15,000</td><td>0.66</td><td>0.55</td><td>0.32</td><td>0.22</td><td>0.10</td><td>0.07</td></tr></table>

For origin in zone 1 and destination in zone 4, 

$$
\begin{array}{r l} & {\bar {p} _ {\mathrm{T}} = (0. 1 5) (0. 6 5) + (0. 1 0) (0. 4 6) + (0. 2 0) (0. 5 1) + (0. 3 5) (0. 1 0)} \\ & {\qquad + (0. 0 5) (0. 1 1) + (0. 1 5) (0. 0 7)} \\ & {\qquad = 0. 2 9 7.} \end{array}
$$

## PREDICTION USING THE NAIVE METHOD

The mode choices can also be predicted using the naive method. The first step is to determine the mean values of each of the independent variables. If we define 

$$
n _ {i} \equiv \sum_ {j, k} n _ {i j k},
$$

with $n_{j}$ and $n_{k}$ defined similarly, then the weighted averages of the independent variables are 

$$
\begin{array}{r l} & {\bar {y} = \sum_ {i} \frac {n _ {i}}{N} y _ {i} = \frac {1}{1 , 0 0 0} [ (3 5 0) (5, 0 0 0) + (1 5 0) (1 0, 0 0 0) + (5 0 0) (1 5, 0 0 0) ]} \\ & {\qquad = 1 0, 7 5 0,} \\ & {\bar {a} _ {\mathrm{LD}} = \sum_ {j} \frac {n _ {j}}{N} a _ {j} = \frac {1}{1 , 0 0 0} [ (0) (0) + (4 5 0) (0. 5) + (5 5 0) (1. 0) ] = 0. 7 7 5,} \end{array}
$$

and, for each dimension $s_{l}$ of S, 

$$
\bar {s} _ {l} = \sum_ {k} \frac {n _ {k}}{N} \bar {s} _ {l k},
$$

so that the average service attributes are 

$$
\begin{array}{r l} & {\bar {t} _ {\mathrm{A}} = (0. 6) (1 1. 3) + (0. 4) (1 4. 2) = 1 2. 4 6,} \\ & {\bar {x} _ {\mathrm{A}} = (0. 6) (5) + (0. 4) (5) = 5,} \\ & {\bar {c} _ {\mathrm{A}} = (0. 6) (1 2 2. 5) + (0. 4) (1 3 1. 3) = 1 2 6,} \\ & {\bar {t} _ {\mathrm{T}} = (0. 6) (1 4) + (0. 4) (2 1. 7) = 1 7. 0 8,} \\ & {\bar {x} _ {\mathrm{T}} = (0. 6) (8) + (0. 4) (1 5. 5) = 1 1. 0,} \\ & {\bar {c} _ {\mathrm{T}} = (0. 6) (5 0) + (0. 4) (7 5) = 6 0,} \\ & {\vec {d} = (0. 6) (7. 2 5) + (0. 4) (8. 1 3) = 7. 6 0.} \end{array}
$$

With these average values, the mode-choice probability can be determined as $p_{T} = 0.22$ . Comparison with the preceding result demonstrates the differences introduced by using average characteristics rather than detailed distributions. 

## DISCUSSION

Demand models have traditionally been developed at an aggregate level, with geographically defined zones used as a primary basis for aggregation. For example, trip-generation models in UTMS (see chapter 

11) were developed by regression of total trips on zone averages of income, automobile ownership, and so on. We have seen that such zonal averages can be quite misleading. In general, there is more variation in behavior within zones than between zones (Fleet and Robertson 1968, McFadden and Reid 1975). Thus if one wants to aggregate, one might prefer to aggregate across zones, keeping access conditions and/or market segment characteristics as bases for defining classes, rather than averaging out these important variables. 

Similar behavior is observed in most situations. Thus it is usually better to begin with disaggregate models and then develop bases for aggregation appropriate to the issues to be studied (Koppelman 1975, Landau 1976, Watanatada 1977). 

## 4.7.4 Approximate Methods with Disaggregate Functions

All of the methods for simple predictions with aggregate functions identified in section 4.6 can be used with disaggregate functions also. The major difference is that the disaggregate function gives a probability, which must then be multiplied by a market-segment size to give a volume. 

As an example, consider the relationship given in section 3.5 for incremental analysis with a multinomial logit model. Similarly, the elasticities of an MNL model can be computed from the relationships in table 4.1; note, however, that this is the elasticity of a probability, that is, the percent change in the probability of choosing a mode for a 1 percent change in some attribute. 

## 4.8 LOOKING AHEAD

This chapter completes a basic introduction to transportation demand. There are many important topics we have not discussed; some of these will be treated later in this volume, while others will not be discussed here at all. 

The complexity of consumer decisions in transportation will be examined in chapter 11, where we shall consider the dimensions of consumer choice and how alternative ways of structuring these dimensions lead to different types of demand models. 

Developing good demand models for a specific situation is always a difficult task. To be effective, the analyst must understand not only the aspects of consumer behavior and the transportation issues that are most important in a particular situation, but also the statistical methods available for estimating model parameters and their limitations. This subject demands a specialized course in itself; in chapter 16, 

however, we shall introduce a few basic ideas on general model development strategy. 

We have chosen to teach demand from the perspective of disaggregate models estimated by econometric methods. These models represent the third generation of transportation demand modeling. The first generation was that of the Urban Transportation Model System and related intercity models formulated on the basis of physical analogies (such as gravitation) or weak or nonexistent causal theories and estimated on aggregate data (see chapter 11). The second generation was that of models based on explicit economic reasoning and estimated on aggregate data, such as the Kraft-SARC or Baumol-Quandt models. The disaggregate models form a third generation because, while still founded on basically economic theories of behavior (the two consumer behavior models in chapter 2), the formulation and estimation of a model at the disaggregate level allows much more subtle and realistic behavior to be represented and also allows greater efficiency in the use of data (see chapter 11). A fourth, potentially more powerful direction is beginning to emerge. This direction of model development draws on methods from psychology and market research to increase our ability to model the subtleties and complexity of consumer behavior. These methods have not yet been developed to the stage of practical use in transportation systems analysis. 

## 4.9 SUMMARY

For practical purposes it is necessary to predict the behavior of groups of consumers. A disaggregate demand function predicts the behavior of individual consumers, whereas an aggregate demand function predicts the behavior of a group of consumers. Market segments are groups of consumers whose behavior is represented by a single demand function. 

Many types of aggregate demand functions have been used, including gravity models, intercity passenger demand models, and the Urban Transportation Model System. 

Like disaggregate models, aggregate models can be either deterministic or stochastic. Thus four major groups of travel demand models can be identified: disaggregate deterministic, disaggregate stochastic, aggregate deterministic, and aggregate stochastic. The major types of travel demand models presently available for practical use are disaggregate stochastic and aggregate deterministic. 

A number of important aspects of demand functions can be identified: the variables included, the algebraic form, representation of bebehavior, the treatment of market segments, the use of composite variables, and the inclusion of choice-specific characteristics. The algebraic form of a demand function, in terms of the specific variables included, implies a particular representation of the behavior of the consumers in the corresponding market segment. The behavior is expressed in the magnitudes and signs of the coefficients, the derivatives of the function, and the elasticities (direct and cross-elasticities). The elasticity of a demand function expresses the relative magnitudes and directions of changes in a dimensionless form that is often quite useful. 

When an aggregate demand function has been calibrated for a particular situation, prediction of consumer behavior is relatively straightforward (if service levels can be assumed known). On the other hand, in many situations the analyst may have to do without a calibrated model. In such cases various properties of demand functions can be utilized for simple, approximate predictions. For example, information on elasticities can be used in the pivot-point approach to obtain quick, approximate estimates when no other method is available. A particularly important composite variable is the composite service level, which helps to identify possible trade-offs between transportation service attributes. Several approaches to prediction using demand-model properties and simple judgments have been demonstrated. 

When a disaggregate demand function is available, the prediction of group behavior requires use of an aggregation procedure. Numerous practical procedures are available, including the naive procedure, classification, distributions, and sampling. As with aggregate functions. properties of disaggregate functions can be utilized for shortcut predictions. 

## TO READ FURTHER

There is an abundant literature on transportation demand. For general economic treatments of demand in terms of the economic theory of consumer behavior see Henderson and Quandt (1958), Baumol (1965), or de Neufville and Stafford (1971). For a discussion of aggregate models and their foundations and a historical review see Domencich and McFadden (1975). Ben-Akiva (1977) and Spear (1977) describe a number of urban applications of disaggregate models. For recent models—primarily mode-choice models and their applications—see Liou, Cohen, and Hartgen (1975), Dunbar (1976), and Train (1977). Further suggestions will be found in chapter 11. 

, For fourth-generation directions see Stopher and Meyburg (1976), Hauser and Koppelman (1976), Brog, Heuwinkel, and Neumann 

(1977), Brog and Schwerdtfeger (1977), Dix (1977), Fried, Havens, and Thall (1977), Hautziger and Kessel (1977), Heggie (1977), Hensher and Stopher (1978), and P. M. Jones (1978). 

For freight applications see Quandt (1970a), Hartwig and Linton (1974), Terziev (1976), Roberts (1977), and Schneider, Baker, and Waldner (1977). For air travel applications see Damay and de Terra (1974) and Kanafani and Sadoulet (1977). 

An important early application of pivot-point methods is reported in Pecknold, Wilson, and Kullman (1972) and also, in extract form, in the more readily available Cambridge Systematics (1974). For a more detailed discussion of directions of development in urban passenger models see Brand and Manheim (1973), especially the paper by Ruiter, and Cambridge Systematics (1974). 

For approaches to market segmentation see Aldana, de Neufville, and Stafford (1974) and Cambridge Systematics (1976a). 

For recent aggregate models see Crow, Young, and Cooley (1973), Lave, Mehring, and Kuzmyak (1977), and Wilken (1978). 

## EXERCISES

4.1(C) Consider each of these models discussed in this chapter: Gravity I–IV, Kraft-SARC, McLynn, and Baumol-Quandt. 

a. For each, identify the composite service level, $L_{kd}$ or $L_{kdm}$ , and the composite destination-specific and origin-specific activity variables, $Z_{d}$ and $Y_{k}$ . 

b. Derive relevant elasticities for each model using the composite variables and the properties of elasticities in table 4.2. 

c. Identify choice-specific and choice-abstract parameters in each. 

d. Discuss. Compare the models critically. 

4.2(E, P) In section 4.5.4 we examined inferences from elasticities as utilized in a study of free transit. 

a. Compare the elasticities discussed in section 4.5.4 with the elasticities of the model used in chapter 3. Discuss. 

b. Numerous demand models have been developed since that early study. Review recent technical literature and analyze the pros and cons of “free transit” in light of contemporary knowledge of traveler behavior. (You may wish to examine the original study: Charles River Associates 1968.) 

4.3(E) The classical gravity model is given at (4.2). A disaggregate model of destination choice d might have the form 

$$
p (d) = \frac {e ^ {U _ {d}}}{\sum_ {d ^ {\prime}} e ^ {U _ {d ^ {\prime}}}}, \text { where } U _ {d} = \alpha_ {0} + \alpha_ {1} t _ {d} + \alpha_ {2} c _ {d} + \alpha_ {3} \gamma_ {d}.
$$

Show that the gravity model is a special case of the disaggregate destination-choice model, in aggregated form. Discuss the limiting assumptions of this special case. 

4.4(C) In Washington, D.C., aggregate trip-generation models were estimated using regression (Washington, D.C., Council of Governments 1974). A typical equation of this form is 

$$
V _ {e} = \alpha_ {0} + \alpha_ {1} (Z _ {1} Z _ {2}) + \alpha_ {2} (Z _ {1} L),
$$

where the $\alpha_{i}$ are parameters and 

$V_{e}$ = daily home-based trips per household for purpose e, 

$Z_{1}$ = total number of persons in the household, 

$Z_{2}$ = natural logarithm of household annual income (in dollars), 

L = transit accessibility (ratio of jobs that can be reached in 45 minutes by transit to total regional employment). 

a. What signs would you expect for each parameter? Why? 

b. For home-based shopping trips, the following values were found: 

$$
\alpha_ {0} = 0. 3 5, \qquad \alpha_ {1} = 0. 0 2 9, \qquad \alpha_ {2} = - 0. 4 8.
$$

(The magnitudes and signs were similar for other trip purposes.) Discuss the results. 

4.5(E) In exercise 1.6 we used the approximate incremental demand function 

$$
\frac {\Delta V}{V} \approx \alpha \frac {\Delta p}{p} + \beta \frac {\Delta t _ {c}}{t _ {c}}.
$$

Using the properties of elasticities, derive this from the following function: 

$$
V = Y p ^ {\alpha} t _ {\mathrm{c}} ^ {\beta}.
$$

4.6(E) In developing table 4.4 the assumption was made that X is a single rather than a composite variable. Now consider the following cases: 

$$
1. X = \mu_ {1} X _ {1} + \mu_ {2} X _ {2},
$$

$$
2. X = \mu_ {0} X _ {1} ^ {\mu_ {1}} X _ {2} ^ {\mu_ {2}},
$$

$$
3. X = \mu_ {0} e ^ {\mu_ {1} X _ {1}} e ^ {\mu_ {2} X _ {2}}.
$$

a. Extend the results of table 4.4 to these cases by deriving appropriate relationships. 

b. Make appropriate numerical judgments and demonstrate the use of your derived relationships. 

4.7(E) Consider question 4.3 in section 4.5.6. 

a. What change in travel time would be required to maintain volume in the face of a 20 percent fare increase if there were no change in frequency? 

b. If the transportation facility connecting zones 1 and 2 were congested, would the analysis given in answer 4.3 be valid? Discuss. 

c. If $t^{0} = 2$ hours, $c^{0} = \$4$ , and $q^{0} = 2$ per day, compare the answers you obtain using the approximate relationship $v$ in answer 4.3 and the explicit demand function stated at the start of question 4.3. 

4.8(P) We have presented only a few specific demand models in these discussions. The following exercises are meant to broaden the reader's perspective. 

a. Select and analyze a transportation demand model reported in the literature: 

i. What options and impacts explicitly or implicitly influenced the design of this model? 

ii. What are the major service variables? activity-system variables? other variables? 

iii. How were the values of model parameters determined (data sources, statistical networks)? 

iv. Discuss the behavior represented by the reported model (the magnitudes and signs of coefficients, important elasticities, etc.). 

v. Take some typical values of the variables in the model (reported or hypothesized variables), and use the model to predict changes in demand for several possible transportation policies (and changes in exogenous variables). Do the results seem reasonable? 

vi. To what extent does the model seem "reasonable," "valid," "relevant," and "useful"? 

vii. Any other comments? 

b. Select a problem area in transportation systems analysis, do a literature search to identify several possibly useful demand models, and compare them critically using the preceding questions as a guide. Examples of such problem areas are changes in passenger fares on North Atlantic air routes; introduction of a panatransit service in a particular area; or restructuring of rail system operations in a particular region. Include in your analysis discussions of the major options and impacts that should be analyzed in this problem and the service attributes and activity-system variables that should be included. 

4.9(P) The following article by Ian McIntyre, an employee of an international chemical company, appeared in The Sunday Times of London (October 26, 1975). The author describes a number of features of the commuting lifestyle, some attractive to him and some unattractive. 

a. Discuss the implications for demand modeling: 

i. What features must demand models have to adequately reflect the types of behavior illustrated by this article? 

ii. Critically appraise selected demand models with which you are familiar. How well or poorly do they reflect this type of behavior? iii. Suggest a research program to develop demand models to adequately reflect this behavior. 

b. Discuss the policy issues raised by the article. Assume you are responsible for developing a comprehensive transportation strategy for a major metropolitan region. What issues does this article suggest to you should be explored? What technical analyses would you do to clarify these issues? 

## Why I Commute: High-Speed Therapy

No one believes me when I say I actually enjoy commuting. But I do. It has always seemed to me a logical way of life. 

All married people who have a working life away from their families find they lead two quite separate lives. They have their business life, frequently with its own language and life-style, and circle of friends. You even buy clothes for this half of your life which seldom get worn in the other, domestic sector: your private life. 

Commuting, particularly over long distances, provides a valuable buffer period—a kind of therapeutic vacuum—between the two existences. 

I can leave the office seething with discontent over some minor skirmish in the eternal warfare of office politics. An hour later it has all been purged from my mind by the homeward journey. I step out on to the platform in the Surrey countryside a new man, with the office sealed away, as it should be, in the appropriate corner of my mind. 

It works the other way, too. I can leave home in the morning worried about some childish ailment which kept us awake most of the night, or the arrival of an unusually large bill; but when I get to Waterloo [a London rail station] these problems, too, have worked their way out of my system and I'm ready to tackle anything the world throws at me. 

Of course, there are snags. It's infuriating when things go wrong on Southern Region, which is stretched to such limits in the rush hour that one defective signal seems able to cripple the whole system. But most trains are on time, and the annual labour dispute can easily be seen writhing its way over the horizon, and convenient holidays arranged. You soon learn how to cope with train bores: the men who insist on talking for the whole journey to anyone who will listen. And how to 

avoid the early cigar smoker, who likes to blow the minds of his fellow travellers by lighting his first Havana at the uncivilised hour of 7:45 A.M. People of like interests seem to congregate by instinct in their own sections of the train. 

But what do you do with all that spare time, people are apt to say. One bonus is reading. How many breadwinners, with family, dog, house, garden, and perhaps charity or recreational commitments, can actually find time to read these days? I have a whole two hours a day when I can read books or office papers without that guilty feeling that I should be doing something else. 

And yet—I must be realistic—commuting has a bad name. I blame part of this on the shorter Oxford dictionary. Explaining how the word “commuter” came into existence, it quotes an aphorism of 1663: “Perhaps the shame and misery of this life may commute for hell.” Then, illogically, “hence commuter, one who commutes.” 

There's nothing hellish about my kind of commuting. The long distance men (I live 40 miles from London) always get a seat, and a cheaper rate per mile. We can have all the advantages of living in the country while working in the world's greatest city. 

I've travelled some 154,000 miles to and from work in the past eight years, with another third of a million miles to go before retirement. You can almost say I'm looking forward to every furlong of the journey. 

# 5

# Transportation System Performance

## 5.1 INTRODUCTION

Transportation involves the movement of people or goods from one location to another. This requires the expenditure of energy by man, animal, or machine. There are many different means of transportation, using a variety of energy sources and possessing widely differing characteristics. In many cases, especially in industrialized countries, transportation is achieved by quite complex processes in which men and machines interact, within institutions that are often large and complex, to deliver transportation services to consumers. 

The challenge facing the transportation systems analyst is to intervene effectively in these large, complex systems. To accomplish this the analyst must be able to predict the consequences of alternative actions, and this in turn requires that he be able to abstract from those systems a simplified representation—a “model”—that he can manipulate to analyze the options open to him. The model should be sufficiently close to the real system that it can reasonably be used to draw inferences about that system, should help to illuminate the issues that the analyst thinks should be clarified, and yet should be feasible within the resources available—both the resources required for model development and the resources required for model use. In this process the analyst must understand the system to be modeled, have an explicit model development strategy, and have a deliberate strategy for using the model to clarify the issues. 

It is impossible in a single volume, much less a few chapters, to discuss all aspects of all the types of transportation systems that an analyst must understand. In keeping with the introductory nature of this volume, our objectives are limited to identification of some of the key features of transportation systems that are relevant to any analysis, a description of a general approach to analyzing the performance of transportation systems that will provide the analyst with a basic framework useful in many situations, and illustration of this approach with simple examples. The various chapters dealing with transportation system performance try to achieve these limited objectives. 

In this chapter we shall first look briefly at transportation systems from several different perspectives in order to identify the major system aspects that should be represented in performance models. Then we define the concept of a transportation performance function and explore how such a function can be used in a systematic analysis. To illustrate this approach we shall develop a simple example of such a function and demonstrate its use through an air transportation example; this enables us to identify a number of issues in the use of performance functions. Finally, we shall discuss some specific principles on which the analyst can draw in developing and using performance functions in specific contexts. These will become the focus of later chapters in this group. 

## 5.2 WHAT IS A TRANSPORTATION SYSTEM?

## 5.2.1 Alternative Perspectives

There are many different perspectives from which a transportation system can be viewed. In this section we shall explore a few in order to demonstrate the complexity of real systems. 

## COMPONENTS OF A SYSTEM

A transportation system has many components. Some are physical, others institutional. Table 5.1 displays the major components of most transportation systems, together with some of the major subsystems of these components. This list is not intended to be definitive. Our intent is simply to illustrate the variety of components and functions that interact to influence system performance. 

## SPATIAL AND TEMPORAL STRUCTURE

A transportation system's components are spread over space and interact over time. The spatial structure of a system, reflected in its network characteristics, is important, as is its temporal structure (how the system's characteristics vary over time). 

Consider the example shown in figure 5.1. This system consists of 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/a9a45185-cfa1-407d-8a96-209400065f95/1a8ffea9de89b26dbb613fd87600b03edf3ef8c6af820319992d2ab04d9749a8.jpg)



Figure 5.1 A transportation system.


Transportation System Performance 


Table 5.1 Components of transportation systems


<table><tr><td>Major components</td><td>Subsystems</td><td>Examples</td></tr><tr><td rowspan="7">Load-carrying system (vehicle, conveyor belt, pipeline)</td><td>Load-containing system</td><td>Passenger and cargo compartments (truck, rail, air)</td></tr><tr><td>Support system (transmits load from vehicle to guideway or other supporting medium)</td><td>Chassis and suspension system including wheels (truck, rail); airframe, wings, and landing gear (air); ship hull (marine)</td></tr><tr><td>Power and propulsion system</td><td>Fuel tanks, engines, transmission, drive wheels (truck, rail); fuel tanks, engines, propellors (air, marine)</td></tr><tr><td>Guidance and control system</td><td>Driver, steering system, wheel interactions with roadway (truck, rail); pilot, navigation, communication and control equipment (air, marine)</td></tr><tr><td>Crew support</td><td>Driver's compartment (truck); cockpit and related areas (air); crew quarters (marine)</td></tr><tr><td>Load support services</td><td>Galleys, food and other services (air, rail); hold-cleaning mechanisms (marine, rail)</td></tr><tr><td>Loading/unloading systems</td><td>Lifts, doors (truck); doors, ramps (air); hoists, hatches (marine)</td></tr><tr><td rowspan="3">Guideway</td><td>Support system (transmits load to supporting medium)</td><td>Pavement and subgrade (truck); track and subgrade (rail); air medium (air); water medium (marine)</td></tr><tr><td>Power and propulsion system</td><td>Railside or overhead power distribution system (rail); fuel storage and distribution systems (truck, air, marine)</td></tr><tr><td>Guidance and control system</td><td>Traffic signals, control devices, regulations (truck); navigation control system, enroute air traffic control, airport approach and ground control (air); navigation aids, piloting systems, harbor procedures (marine); signal and communication systems for headway and speed control, dispatching system for movement control (rail)</td></tr><tr><td rowspan="5">Transfer facilities (intra- and intermodal)</td><td>Guidance and control system</td><td>Dispatching and train make-up (rail)</td></tr><tr><td>Loading/unloading system</td><td>Passenger boarding gates and ramps (air); cargo belts, cranes, other loading equipment (marine, rail, air); internal materials-handling equipment such as conveyors or forklifts</td></tr><tr><td>Vehicle service systems</td><td>Fueling, cleaning, maintenance checks</td></tr><tr><td>Storage systems</td><td>Cargo storage, short-term and longer-term</td></tr><tr><td>Load support systems</td><td>Documentation; passenger waiting areas and services</td></tr><tr><td rowspan="3">Maintenance system</td><td>Vehicle maintenance system</td><td>Facilities, personnel, equipment, spare parts, policies, procedures</td></tr><tr><td>Guideway maintenance system</td><td>Facilities, personnel, equipment, spare parts, policies, procedures</td></tr><tr><td>Transfer facility maintenance system</td><td>Facilities, personnel, equipment, spare parts, policies, procedures</td></tr><tr><td rowspan="8">Management system</td><td>Load support services</td><td>Fare collection, load processing, documentation, reservations, tracing</td></tr><tr><td>Operating systems</td><td>Scheduling, dispatching, resource assignment, emergency procedures</td></tr><tr><td>Marketing system</td><td>Load procurement, sales force, advertising, follow-through, incentives</td></tr><tr><td>Communications and control system</td><td>System status monitoring, channels for issuing changes to current operations</td></tr><tr><td>Personnel system</td><td>Recruiting, training, management, career ladders, incentives</td></tr><tr><td>Financial system</td><td>Cash management, billing, internal accounting and analysis</td></tr><tr><td>Planning and analysis system</td><td>Corporate planning, short-range planning</td></tr><tr><td>Organizational structure</td><td>Internal organization structure for accountability and control</td></tr></table>

five subsystems or links: movement over significant distances occurs by way of a collection link, a line-haul link, and a distribution link; much shorter movements occur within the two transfer links. This figure might represent the movement of cargo from a producer by truck (or rail or inland waterway) to an ocean port or airport, transfer to airplane or ship for a long-distance move to another ocean port or airport, and then movement to a final destination by truck or rail or water. Alternatively the figure could represent an urban passenger trip, by walk or feeder bus to a transfer station, by rail transit or express bus to another transfer station, and then by walk or local bus to a final destination. 

For simplicity we shall view each of these subsystems as a single link; in actuality each may represent networks of facilities and services. 

## LINK TYPES

There are many kinds of links and various ways of classifying them. One useful classification is by function: movement links involve movements over distances that are significant (in the particular context) in both line-haul and collection/distribution roles; transfer links involve movement over relatively short distances from one movement link to another. 

It is also sometimes useful to distinguish links according to the means of transport used: vehicle links are subsystems that involve movement in vehicles over facilities (in the case of ships or planes the "facilities" are defined by controlled shipping lanes or airways or uncontrolled sea or airspace); nonvehicle links are subsystems other than walk links in which no vehicle is involved (pipelines for solids and fluids, conveyor belts); walk links are subsystems in which people move on their own legs. 

A movement link can be a vehicle, nonvehicle, or walk link. A transfer link is often assumed to be a walk or other nonvehicle link, but this is not necessarily true. For example, passenger movement through an airport may involve vehicles such as shuttle buses or elevators or non-vehicle links such as conveyors. Also, freight moving through a marine port will often be moved around within the port by trucks, forklift devices, mechanical conveyors, or other devices, so that, while it is a transfer link, a port is not necessarily a nonvehicle link or a link in which no movement takes place. 

Clearly these definitions are relative. For one analysis it may be useful to visualize an airport or a marine port as a single transfer, nonvehicle link (for example, in a national or regional analysis). On the other hand, for detailed analysis of changes in physical features or specific operating procedures, a port could be visualized as an elaborate and detailed network of links composed of both movement and transfer links at a much smaller scale (figure 5.2). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/a9a45185-cfa1-407d-8a96-209400065f95/90979174ab085280f882754593c94d06fcd013bfa61467dc58af48918887ac8a.jpg)



Figure 5.2 Alternative views of a transfer facility. a: A single link. b: A subsystem (from Frankel and Tang 1977).


In analyzing and modeling a particular system, the characteristics of each type of link must be considered explicitly. In some cases different types of models may be appropriate for different types of links. From a general perspective, however, all types of links are functionally the same. Therefore, for our analyses of system performance in this volume, we shall deal primarily with a single type of link, a vehicle movement link, as a basis for developing fundamental concepts of transportation systems performance. 

## NETWORKS OF FACILITIES

The idea of links leads naturally to a visualization of a transportation system as a network of facilities, such as might be abstracted from a map (figure 5.3a). 


a


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/a9a45185-cfa1-407d-8a96-209400065f95/8704ffc3e88c82a378aed948ce8b75f5cef0d687e5ac68623b6769d9da53d417.jpg)


$= \text{Facilities for movement links}$ 

• = Facilities for transfer links 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/a9a45185-cfa1-407d-8a96-209400065f95/788bf732d58373f06f09cd955f48ff0bba80fc85d2adb7158db2a66413100098.jpg)



Figure 5.3 a: A network of facilities. b: Merging of two streams of vehicles within facility channels. c: Interactions of vehicles at a transfer facility.


## VEHICLE TRAJECTORIES

Clearly, as suggested by table 5.1, facilities are only parts of a system; the vehicles are also important. The path of a vehicle through a system may be quite complex and, as figure 5.4 indicates, not at all a simple mirror of the network of facilities. 

## INTERACTIONS OF VEHICLES AND FACILITIES

The vehicles and facilities interact in various ways. Over a movement link, such as a highway or stretch of rail line, vehicles interact in a flow stream and are affected by the characteristics of the facilities over which they move. Over a network of movement links, such as a highway or rail network, the interactions of the vehicle flows are influenced by the properties of a number of links, as when congestion occurs at intersections in a road network (figure 5.3b). At a transfer link the interactions are more complex, in that the performance of the transfer link depends not only on its own facility characteristics, but also on the vehicle and facility characteristics of the movement links leading to and from the transfer link (figure 5.3c). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/a9a45185-cfa1-407d-8a96-209400065f95/06c5dab4fbb6dd7d208910a602309941fe8568a88bcc2a3128dbf75dccd4ee03.jpg)



Figure 5.4 Vehicle trajectories: An aircraft routing pattern. From Borman (1977).


## A USER PERSPECTIVE

Each major interest has a different perspective on transportation. From the point of view of the user, the service level over the total trip from origin to destination is important: the total trip time, the total waiting time, the total cost, the total probability of loss or damage, the maximum waiting time, the maximum walking distance, and so on. This total service level is composed of the service levels over each of the subsystems or links used in the total trip. In this respect, therefore, the performance of the system as a whole is a function of the performance of each element in the system. 

## AN OPERATOR PERSPECTIVE

In general, each subsystem of a transportation system is controlled by a different organization (and sometimes by several different organizations). Thus there are usually several operators in a system. Each operator has available a particular set of resources in its subsystem (vehicles, facilities, labor personnel) and exercises directly options that control these resources. 

In general, each operator is interested only in the performance of his own subsystem. Resource consumption is an important consideration, particularly insofar as it is reflected in direct monetary costs. Service is considered primarily in terms of its effects on the revenues derived from users whose decisions are influenced by that service. Thus the operator is usually primarily concerned with net monetary revenues and those detailed operational aspects that influence resource consumption, and thus costs, and only secondarily with service levels. (As a further refinement, one often distinguishes the interests of various elements of an operator, such as management and operating labor.) 

Building and operating a system require an input of resources. The major areas of resource consumption in transportation are illustrated in table 5.2. 

Resource consumption can be categorized in many ways. Resources are consumed in building a system, in maintaining it in operating condition, and in operating it to provide useful services. Some resources are literally consumed, as in the taking of land from other uses or the consumption of fuel or labor. Other forms of consumption are, strictly speaking, degradations of existing quality (for example, air pollution or noise involve the “consumption” of resources in the sense that existing levels of air purity and quiet are degraded). 


Table 5.2 Typical resources consumed in building and operating a transportation system


<table><tr><td>Labor</td><td>Vehicle operationsFixed facilities operations (guideways, transfer facilities)Vehicle maintenanceFixed facilities maintenanceManagement systemVehicle fabricationFixed facilities fabrication</td></tr><tr><td>Materials</td><td>Vehicle fabrication (metals, rubber, plastics, etc.)Fixed facilities construction (cement, steel, etc.)Consumables in system operations other than energy (food paper, replacement parts, etc.)</td></tr><tr><td>Land</td><td>Fixed facilities for the system (guideways, transfer facilities, management facilities)Fixed facilities for the fabrication of materials</td></tr><tr><td>Energy</td><td>Power for system operationsPower for vehicle fabricationPower for facilities fabrication</td></tr><tr><td>Environmental degradation</td><td>Air qualityNoise levelWater qualityOdors</td></tr><tr><td>Ecological effects</td><td>Effects on animal lifeEffects on plant life</td></tr><tr><td>Social effects</td><td>System as a physical barrierEffects of displacement of homes and businessesEffects on community cohesionEffects on social stability</td></tr><tr><td>Aesthetic effects</td><td>View of the system from the outsideView of the system to usersView of the environment from the system</td></tr></table>

## PERSPECTIVE OF OTHER INTERESTS

While resource consumption is especially important to the operator, not all of its effects or costs are incident on the operator exclusively. Groups that are neither users nor operators may receive environmental, social, and economic impacts as a consequence of the resources consumed by a particular system or subsystem. These groups were identified in chapter 1 as those receiving physical or functional impacts plus agencies of government. 

## 5.2.2 Implications for Analysis

The preceding discussion demonstrates the complexity of real transportation systems. Clearly the transportation system of a region can be visualized and analyzed in many different ways. The point of view one takes depends on one's objectives. Our objective as analysts is to understand the behavior of a transportation system in ways that allow us to predict the effects of proposed changes in that system. To do this we must focus on those aspects of transportation that are of greatest concern to all those on whom the impacts of transportation fall. 

From the perspective of users, we have seen that service is most important: It is the level of service offered by a system that most influences how users will respond to changes in that system. From the perspective of users, operators, and other interest groups, the resources consumed are also important. This is the perspective from which we shall try to understand system performance. When we discuss links, vehicles, facilities, or networks, we shall do so primarily with the aim of understanding how the characteristics of these elements influence the levels of service offered and resources consumed by a system. 

5.3 REPRESENTING TRANSPORTATION SYSTEM PERFORMANCE
We can now define what we want in a representation of transportation system performance. What do we want to predict? As we consider changes $\Delta T$ in the transportation system T, we want to know what impacts they will have. To determine the impacts on users we need to know how service levels will change as we vary T; then using appropriate demand functions we can predict how users will respond. To determine the impacts on operators and others we need to know how the resources consumed in providing the transportation service will change. Then we can identify the actors on whom those impacts are incident: some of the costs of the resources consumed (monetary and nonmonetary) will be borne by operators, some will be borne by physically impacted groups (for example, homeowners on the approach paths to an airport), and some will be borne indirectly by society as a whole through taxes and other fiscal means and through effects on social and economic activity patterns. 

Each possible change in T will have a different set of effects, in terms of both service levels and resources consumed. In addition, the magnitudes of these effects may depend not only on T but also on the actual volumes of users (shippers or travelers) of the services. 

We can summarize this symbolically as follows. The magnitudes of the various resources consumed by a system (R) will depend on the specific decisions taken about the design and operation of the system, represented by the vector of transportation options (T), the specific 

geographic and economic environment in which the system exists (E), and the volume of users of the system (V). 

The primary purpose of a transportation system is to provide services to users. The level of service (S) offered by a particular system will depend on T and also on E; moreover, in most cases the service level will also vary with V even if T is held constant (due, for example, to congestion effects). 

Thus from an analyst's perspective we want to characterize transportation systems in terms of R and S, with both of these variables as functions of T, E, and V. 

For our discussions here and in the related chapters on system performance, we shall ignore the diversity of operators and of interests with different points of view. We shall concentrate primarily on the viewpoints of users and operators and shall, furthermore, assume a single operator. The style of analysis thus developed will be extended to a broader context when we take up topics such as evaluation and choice. 

## 5.3.1 The Performance Function

Thus a transportation system can be viewed as a process in which resources are consumed to produce transportation services in a particular environment. We characterize transportation by a performance function of the form $\phi_{\mathrm{E}}(\mathbf{R}, \mathbf{S}, \mathbf{T}, \mathbf{V})$ . This function describes a surface in $(\mathbf{R}, \mathbf{S}, \mathbf{V})$ space for a given T, as illustrated in figure 5.5b. This representation indicates that if we specify T and E, then R and S both vary as a function of V. 

Although R and S are both outputs of the system, we distinguish S as that set of characteristics of the system which, when perceived by users, influences their demand for transportation. Further, R can in some cases be thought of as a set of inputs to the process of producing transportation (although, strictly speaking, some resources consumed, such as noise, are physically outputs). To emphasize this it is often convenient to view $\phi$ as composed of a service function $\phi_{S}$ and a resource function $\phi_{R}$ in a particular environment E: 

$$
\mathbf {S} = \phi_ {\mathrm{S}} (\mathbf {V}; \mathbf {T}, \mathbf {E}), \qquad \mathbf {R} = \phi_ {\mathrm{R}} (\mathbf {V}; \mathbf {T}, \mathbf {E})
$$

(see figure 5.5a). We designated these as J and H, respectively, in chapter 1; we shall use the $\phi$ notation when we want to emphasize, as here, that J and H are two facets of the same underlying process. 

The interrelationship of R and S is a fundamental aspect of transportation system performance. As figure 5.5b emphasizes, specification of T establishes a specific relationship between R, S, and V; as T or V varies, in general both R and S vary. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/a9a45185-cfa1-407d-8a96-209400065f95/ddbfe53cdb35d66b1b24bb19a8d230943ba932d83858add860b9a7aff8bf080e.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/a9a45185-cfa1-407d-8a96-209400065f95/8c82a06833e432af219a5561fe13849de875b90c1353d2ddb65de39cd4df55d3.jpg)



Figure 5.5 a: Service and resource aspects of the performance function. b: A performance function surface in (R, S, V) space (after Morlok 1968).


The actual shapes of these relationships will depend significantly on the environment E in which a particular system is being operated, as well as on the characteristics of the system itself. The environment includes the physical environment (distance, geography, climate, and so forth), the economic environment (prices and availabilities of various resources such as labor, rights-of-way, and fuel), and the institutional environment (legal and administrative requirements, the structures of institutions external to the transport operators, the internal organizational structure and relationships of the operators, and related factors). 

## 5.3.2 Using a Performance Function for Analysis

We shall now outline the use of a performance function for analysis. The first step in the process is to interface the performance function with a demand model in order to predict travel-market equilibration. The second step is to use the performance function with the full set of prediction models for a systematic analysis of the options. For simplicity, we suppress the variable E. 

## EQUILIBRIUM ANALYSIS

The key features of an equilibrium analysis are that (1) the actual volume using a system is in general different from the maximum volume the system could handle or any prespecified design volume, and (2) the actual volume depends on the level of service offered, where that dependency is given by an explicit demand function. We use the following definitions (for a single-component volume): 

$V_{E}$ = equilibrium volume (the actual volume that would use the system under the specified conditions), 

$V_{\mathrm{C}} =$ the maximum or capacity volume, 

$V_{D} = \text{demand volume (volume desiring to use the system at a particular service level S).}$ 

(The units of volume are usually passengers or tons per hour or month or year.) The demand volume will usually be different from the available volume. It is given by an explicit demand function: 

$$
V _ {\mathrm{D}} = f _ {\mathrm{D}} (\mathbf {S}).\tag{5.1}
$$

As shown in chapter 1, at equilibrium the volume and service levels must by definition be such that both demand and service conditions are met: 

$$
V _ {\mathrm{E}} = f _ {\mathrm{D}} (\mathbf {S} _ {\mathrm{E}}),\tag{5.2}
$$

$$
\mathbf {S} _ {\mathrm{E}} = \phi_ {\mathbf {S}} (V _ {\mathrm{E}}, \mathbf {T}).\tag{5.3}
$$

Note that the equilibrium volume cannot exceed capacity, so $(5.2)$ must be modified as follows: 

$$
V _ {\mathrm{E}} = \min [ V _ {\mathrm{C}}, V _ {\mathrm{D}} (\mathbf {S} _ {\mathrm{E}}) ].\tag{5.4}
$$

If capacity is not constraining, then $V_{E} = V_{D}$ at the equilibrium service level $S_{E}$ . 

The relationship between $V_{E}$ and $V_{C}$ is important. To reflect the differences between the equilibrium volume and capacity, a load factor $\lambda$ is defined by 

$$
\lambda \equiv \frac {V _ {\mathrm{E}}}{V _ {\mathrm{C}}}.\tag{5.5}
$$

In some modes of transport, where no standees are allowed in the vehicle for safety reasons (airplanes, for example), the load factor for passengers, $\lambda^{P}$ , is always less than or equal to one. In other modes (bus or rail transit) $\lambda^{P}$ is sometimes allowed to be greater than one; this is called “crush loading” for obvious reasons. 

Corresponding to the equilibrium volume in the system is a certain level of resource consumption: 

$$
\mathbf {R} = \phi_ {\mathbf {R}} (V _ {\mathrm{E}}, \mathbf {T}).\tag{5.6}
$$

## SYSTEMATIC ANALYSIS

In section 1.6 we presented the image of systematically exploring variations in T and tracing out the differential impacts on various interests. To implement this image we shall want to structure a performance function in ways that allow efficient systematic analysis. Specifically, as we vary T, S will also vary, bringing about changes in V; impacts on users can be represented by V or S. At the same time users generate revenues to the operator, and monetary and other costs are incurred, resulting in a net revenue to the operator, $I_{NR}$ . 

Considering simply these two interests, we would like to use our performance function $\phi$ in a style of analysis illustrated schematically in figure 5.6. Here we systematically explore a range of options T, tracing out variations in S and R as T varies (parts 1 and 2 of the figure). As S varies, the demand and thus the equilibrium volume $V_{E}$ also vary (part 3). The impacts on users, $I_{U}$ , thus are also functions of T (part 4). Similarly the economic and other impacts on the operator, $I_{O}$ , are also 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/a9a45185-cfa1-407d-8a96-209400065f95/bd72d32d7fc83982a5d23fabe15c2afecdcef8a4e56e976c0051ac5ee3c55f44.jpg)



Figure 5.6 Using a performance function for systematic analysis.


varying (part 5). These impacts can be summarized in trade-off curves as in part 6 of the figure. If $I_{U}$ and $I_{O}$ both measure desirable impacts (such as an increase in net revenues or a reduction in travel times), curve A illustrates a situation in which users and operators are in conflict (each increase in desirable impacts on users is achievable only by a decrease in desirable impacts on the operator, and vice versa), while curve B illustrates a situation where both users and operator can be made better off simultaneously. To illustrate the generalization of this analysis to multiple interests part 6 shows two different levels of impact of an environmental contaminant as curves A and C. 

## 5.4 A SIMPLE PERFORMANCE MODEL

In this section we shall develop a very simple performance model and demonstrate how it can be used for a systematic analysis. 

## 5.4.1 Defining the Model

## BASIC RELATIONSHIPS

We assume a single route running between two points, such that the one-way distance is d and the round-trip distance (A to B and back to A) is D = 2d. We assume also that vehicles travel back and forth over this link at an average speed v and cycle continuously at uniform constant headway. Each one-way trip of one vehicle results in the delivery of a payload of w tons (or passengers). 

The productivity of a single vehicle can be determined as follows. Each vehicle makes one round trip in a time D/v. Alternatively, in one hour a vehicle makes n round trips, where 