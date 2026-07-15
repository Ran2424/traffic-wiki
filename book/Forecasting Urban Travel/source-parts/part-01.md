Forecasting Urban Travel 

For Nani Boyce and Stephanie Williams and in memory of Gale Strauss 

# Forecasting Urban Travel

Past, Present and Future 

David Boyce 

University of Illinois at Chicago and Northwestern University, USA 

Huw Williams 

Cardiff University, UK 

## © David Boyce and Huw Williams 2015

All rights reserved. No part of this publication may be reproduced, stored in a retrieval system or transmitted in any form or by any means, electronic, mechanical or photocopying, recording, or otherwise without the prior permission of the publisher. 

Published by Edward Elgar Publishing Limited The Lypiatts 15 Lansdown Road Cheltenham Glos GL50 2JA UK 

Edward Elgar Publishing, Inc. William Pratt House 9 Dewey Court Northampton Massachusetts 01060 USA 

A catalogue record for this book is available from the British Library 

Library of Congress Control Number: 2014950742 

This book is available electronically in the Social and Political Science subject collection DQI 10.4337/9781784713591 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/38754b84-3c6e-4874-b89a-d84630ad82f8/b8d4ac06ce02d58da933bc1081c8ea290d7072c30a575ce9044c07d6379668cd.jpg)


ISBN 978 1 84844 960 2 (cased) ISBN 978 1 78471 359 1 (eBook) 

Typeset by Servis Filmsetting Ltd, Stockport, Cheshire Printed and bound in Great Britain by T.J. International Ltd, Padstow 

## Contents

About the authors vi
Preface vii
1 Introduction 1
2 Emergence of the traditional approach 18
3 Early developments in the UK 71
4 Travel forecasting based on discrete choice models, I 128
5 Travel forecasting based on discrete choice models, II 182
6 Activity-based travel analysis and forecasting 246
7 Transportation network equilibrium 288
8 Tradition and innovation in US practice 358
9 Tradition and innovation in UK practice 401
10 Computing environment and travel forecasting software 447
11 Achievements, current challenges and future prospects 479
12 Conclusion 516
References 530
Names index 617
Subject index 636 

## About the authors

David Boyce majored in civil engineering at Northwestern University, and then earned a Ph.D. in regional science at the University of Pennsylvania. He also received the Master of City Planning degree from Penn. From 1966 to 1977 at Penn, he taught courses in regional science and transportation planning, and conducted research on urban transportation and land use planning programs. He then moved to the University of Illinois, at the Urbana-Champaign campus from 1977 to 1988, and at the Chicago campus from 1988 to 2003. His teaching and research concerned the integration and solution of urban models of travel demand and network equilibrium as well as activity location, among many topics. He served the Regional Science Association International in several roles since 1968. He was Co-Editor of Environment and Planning A and Associate Editor of Transportation Science, as well as a member of several journal editorial boards in regional science and transportation. He is now Professor Emeritus of Transportation and Regional Science at the University of Illinois at Chicago and Adjunct Professor of Civil and Environmental Engineering at Northwestern University. 

Huw Williams graduated in physics and received his Doctorate in theoretical physics from Oxford University. He also obtained a Masters degree in operational research from Lancaster University and a Diploma in economics from the Open University. Between 1972 and 1986 he held various research positions at the Institute for Transport Studies and the School of Geography at Leeds University where his main interests were in modelling transportation and urban systems. In 1986 he moved to the School of City and Regional Planning at Cardiff University where he taught and researched in transportation and spatial systems analysis until 2008. He has published widely on the theory and application of transportation models, public transport systems, transportation investment appraisal and spatial models of various sectors. He has served as Short Notes Editor for Transportation Research, and was a member of the editorial advisory boards of Transportation Research Part B, Civil Engineering Systems and International Planning Studies. He is now Emeritus Professor of Transport and Spatial Analysis at Cardiff University. 

## Preface

We can trace the origins of this book to the start of a personal friendship and professional collaboration of over 40 years when we first exchanged views at the Institute for Transport Studies, University of Leeds, in 1973 about the similarities and differences between US and UK transportation studies. At that time one of us (DB) was on leave from the University of Pennsylvania, the other (HW) was at the very start of his academic career in transportation. Much more recently we started to write about the developments in these countries (Boyce and Williams, 2005). What began as a comparative interest gradually broadened into a study of the evolution of ideas in the field of urban travel forecasting. The advent of retirement has allowed us to rethink and develop this project, which has proved stimulating, frustrating and almost overwhelmingly challenging. 

From very modest beginnings in Detroit and Chicago in the 1950s, interest in travel behaviour and forecasting has expanded into a worldwide activity of deep relevance to students and academics in a variety of disciplines, and to transportation planning professionals in all cities of the world. Some choose to study travel behaviour through sheer interest, while others have a more direct and urgent involvement in employing forecasting models to confront and anticipate the challenges of what is collectively understood as the urban transportation problem. The theories and models adopted to understand and forecast travel behaviour and the transportation planning framework within which they are set continue to have a profound influence on the way our cities function and how they develop. 

This field is one of the finest examples of multi-disciplinary research and practice, where over the years ideas and methods derived from the natural and engineering sciences have both vied with and combined with those from a range of social sciences to guide the practice of planners and the decisions of public officials. Throughout the past six decades, the contributions from a wide range of disciplines can be clearly identified. The application of urban travel forecasting is computationally and data intensive, much of the relevant literature is technical, and a good deal is expressed mathematically, often conveying the impression of solidity, reliability and logical rigour. But there are many views on the adequacy of the techniques, methods and theories which support travel forecasting, and this has always been the case. We shall encounter a wide variety of viewpoints in the course of this book. 

While many texts, reports and review papers cover different periods in the development of the subject, with different degrees of detail, we know of no unified account of the evolution of the field that is both sufficiently detailed and widely accessible. To write a history of these times is a daunting challenge, which we have attempted with very limited recourse to mathematics, but also without oversimplifying the essential ideas at the heart of the subject. We hope this book will interest academics, transportation planning professionals and concerned citizens, of whom many take an interest in planning decisions heavily reliant on travel forecasts. Above all we hope that it will serve the needs of students at the undergraduate, master’s and doctoral levels in transportation engineering, operations research, economics, regional science, geography, environmental studies and transportation planning, as a prelude to more detailed study. We emphasise that this is not a text on ‘how to do’ travel forecasting, but we see it complementing standard texts as part of a course of study. Nor will any new travel forecasts be found here, although we report on many that have been made in the past. We hope to convey our fascination for the application of technical procedures within the social sphere, the ideas that underpin them, and why we believe it all ultimately matters greatly to the quality of life in cities throughout the world. 

The field is fortunate to have benefited from the efforts of several remarkable people. We salute their contributions in grappling with undoubtedly one of society’s most challenging and urgent problems – that of urban transportation. We have written to several of them, some of whom are long retired, to get a sense of the context and spirit of the times in which they worked, the way they viewed relevant problems and the innovations they proposed. Sometimes their views have been expressive and presented with such clarity that we have, with their permission, used their words directly. This exchange of views has been crucial in helping us to understand the origins and background of ideas and innovations, particularly where these might have differed from more standard historical accounts. 

We have benefited greatly from the comments on these developments, and our account of them, from numerous individuals, in particular Staffan Algers, Richard Allsop, Kay Axhausen, John Bates, Martin Beckmann, Alan Black, Peter Bonsall, John Bowman, Michael Bruton, Walter Buhr, Richard Carr, Michael Clarke, Robert Cochrane, Denvil Coombe, Roger Creighton, Peter Davidson, Robert Dial, Birgit Dugge, Ronald Eash, Marcial Echenique, Paul Emmerson, Sven Erlander, Suzanne Evans, 

James Fennessy, Michael Florian, Tony Fowkes, Marc Gaudry, David Hensher, Irving Hoch, Alan Horowitz, Sergio Jara-Diaz, Peter Jones, Niels Jorgensen, Frank Koppelman, Shin Lee, David Levinson, P.O. Lindberg, Jordan Louviere, Lars-Gören Mattsson, Anthony May, Chris McDonald, John McDonald, Daniel McFadden, Bartlett McGuire, Eric Miller, Anna Nagurney, Hugh Neffendorf, Yu (Marco) Nie, Klaus Nökel, Dimitris Papaglou, Michael Patriksson, Neil Paulley, Andrew Plummer, David Quarmby, John Rose, Werner Rothengatter, Roberto Sarmiento, Joseph Schofer, Simon Shepherd, David Simmonds, Howard Slavin, Kenneth Small, Frank Southworth, Frank Spielberg, Peter Stopher, Art Trager, Dirck Van Vliet, Tom Van Vuren, Michael Wegener, Edward Weiner, Kermit Wies, Ian Williams, Luis Willumsen, Sir Alan Wilson and John Wootton, and many others whose names have slipped from our memories. 

Hillel Bar-Gera, Chandra Bhat, Elisabetta Cherchi, Andrew Daly, Frederick Ducca, Peter Mackie, Juan de Dios Ortúzar, Martin Richards, Martyn Senior and Maya Tatineni provided detailed comments on several chapters, for which we are especially grateful. We thank them all most warmly. They do not necessarily agree with all opinions expressed here. As ever, we remain responsible for any mistakes or omissions. 

We thank the University of Illinois at Chicago for the use of the plagiarism-checking software system iThenticate, which we applied to confirm that all sources were properly cited. Our editors at Edward Elgar have been most supportive and have greatly facilitated the completion of our book. We wish to thank our colleagues and friends, too numerous to mention, and especially our wives, to whom this work is dedicated, as well as our extended families, for their interest and constant encouragement in completing this endeavour. 

We would finally like to acknowledge the intellectual contributions of Professors Martin Beckmann and Sir Alan Wilson to this field and thank them warmly for their personal encouragement. 

David Boyce 

Evanston, Illinois, USA 

Huw Williams 

Cardiff, UK 

June 2014 

## 1. Introduction

## 1.1 BACKGROUND AND PURPOSE

Over 60 years ago, urban transportation was first subjected to systematic investigation, perhaps appropriately, in Detroit. The Detroit area study became the forerunner of transportation planning studies conducted in most large cities and countless other urban areas throughout the world. At the heart of this process were forecasts of personal travel and goods movement for evaluating alternative plans and policies. Significant planning decisions concerning transportation infrastructure investment and travel demand management policies, as well as major land use changes, have relied on the methods, techniques and ideas that emerged in this field over these six decades. 

The aim of this book is to describe the major developments in urban travel forecasting models and methods of analysis that were first established in the US and Canada in the 1950s and 1960s, transferred to the UK and other countries, and then extensively advanced and refined through research and practice. We trace the major technical and theoretical developments, with periodic hints of revolution, and their selective absorption into planning practice. We consider the ‘drivers of innovation’ over the years, in particular: (a) the increasing range of transportation policies considered; (b) the widening evaluation frameworks; (c) the means of analysing data; (d) burgeoning computing power; and (e) the role of simple intellectual curiosity. 

From travel forecasting’s roots in operations research, transportation engineering and urban planning, we explore the widening perspectives of various academic traditions. In particular, contributions from economics, psychology, geography and regional science have provided insights and improved representations of the travel and location behaviour of individuals, households and firms as a basis for urban travel forecasts. We also discuss the different policies and projects that attempted to influence that behaviour and how their impacts were analysed. 

As participants in our field of study, we are all extremely fortunate. Each of us comes to the subject of urban travel with different views and expectations. Each of us is a participant in the systems we study, often with strong views about the travel behaviour of ourselves and others, how the transportation system should perform, or how its shortcomings should be addressed. How we construct a framework to identify and address urban transportation problems matters greatly to the lives of citizens, whether they reside in the urban areas of the highly industrialised world or the rapidly developing cities of Asia, Latin America and Africa. 

From meagre beginnings, research and applications in this field expanded to such an extent that vast published and unpublished materials have accumulated over the past 60 years. The synthesis and presentation of this material presented a daunting challenge for selection and emphasis. We approached the task of describing and interpreting the historical record by identifying what we saw as important ‘themes’ in the development of urban travel forecasting models and methods of analysis. As will become apparent, we adopted a sympathetic view of innovations and considered them against the background of approaches existing at the time. We resisted the temptation to compare the past unfavourably with the present. Indeed, there is little reason to believe that current approaches will seem particularly enlightened or sophisticated when assessed a few decades from now. 

## 1.2 NATURE OF MODELS AND FORECASTS

Before introducing the themes and the questions they raise, a few words on the nature of travel forecasting models may be helpful. The questions faced by the pioneers of the field can be summarised as follows: 

1. What will be the pattern of flows in the transportation networks in 20 or 30 years under changes in population, car ownership and decentralisation of land uses? 

2. What will happen in the future if specific changes are made to the transportation networks? 

Faced with scant historical data on the use of urban transportation systems, as well as rapidly rising levels of car ownership, early urban transportation studies performed ‘base-year’ surveys of (a) personal travel by individuals and households, and (b) goods movement by firms and other organisations. Using these ‘cross-sectional’ data, analysts fitted empirical relationships between the demand for travel and what were identified as its determining factors in the survey year.<sup>1</sup> 

Their objective was to apply these relationships in forecasting future travel or assessing changes in travel resulting from proposed policies or projects. In this approach forecasting travel involves: (a) attempting to understand the nature, extent and cause of variations in travel behaviour among different population groups, including variations over geographic space, as a basis for assessing changes under policies and projects; and (b) making statements about the future, conditional on assumptions about improvements in transportation facilities and services. 

Travel demand is expressed in terms of demographic, social, economic and activity location (land use) variables, together with monetary costs (fares, parking charges, fuel purchases, etc.) and level-of-service variables (e.g., travel time along a road or a public transport line, waiting and transfer times), collectively referred to as the ‘generalised costs of travel’. We often refer to these quantities simply as ‘costs’, with the understanding that they embody several components, each with different units: time, money and so on. 

Generally, the amount of travel is observed to decrease in response to increasing generalised costs. In turn, travel costs usually increase with the amount of travel, and are also dependent on the capacities and regulations governing movements in networks. Travel and its costs, and the functions relating them, therefore, are simplified representations of reality, embodying our understanding of these relationships. 

We emphasise, in agreement with leading scholars, that travel forecasting is not directly concerned with determining transportation supply, such as the configuration and capacities of a road system, the network of bus services or pricing arrangements for a toll road, with its connotations of an agent actively managing the capacity of services and network regulations.<sup>2</sup> Therefore we avoid reference to what is sometimes referred to as a ‘supply function’ in discussing the mutual interdependencies between travel demand and the various costs and levels-of-service on the transportation networks. Travel forecasting is often used indirectly in conjunction with an evaluation framework as a basis for the design of transportation systems and the supply of services that they provide; we shall refer to this design process only occasionally. 

Let us summarise these two sets of relations as follows: 

1. A demand function: travel demand depends on a set of external factors and generalised costs. The external, sometimes called exogenous’, factors, such as demographic and land use characteristics, are outside the immediate influence of planners, but may change over time. 

2. A cost function: generalised costs on network links depend on link flows for given capacities and regulations. 

These deceptively simple relations, expressed in mathematical form, conceal a great deal of complexity in the representation of the real world and are subject to a number of important extensions. One of the most interesting and complex is that the land use system itself is dependent on the transportation system and will in general be influenced by changes in the costs of travel. To incorporate this mutual interdependency between the land use and transportation systems leads us into the development of what are called integrated land use – transportation models. We shall have much to say about these at various stages of our story. 

The numerical solution of these interdependent travel demand and cost functions under specified conditions and assumptions to prepare a forecast typically requires the determination of the values of millions of variables, usually by some iterative procedure. This solution determines the equilibrium flows and costs over (a) the transportation networks and (b) the associated personal travel or goods movement between different locations by various modes. This problem has proven to be as fascinating as it is challenging, and is of the utmost practical importance. 

Forecasting has the popular connotation of projection over time, much as a weather forecast indicates the likelihood of rainfall at some future time. Although forecasting travel at some future point(s) in time, perhaps a few years or even decades ahead, is certainly part of our story, this book is also centrally concerned with forecasting the impact of plans and policies. The possibility of such forecasts rests on the expression of policies and projects in terms of changes in the variables (e.g., the times and costs of travel) that influence behaviour. Models have evolved considerably to embrace the following planning contexts expressed at various levels of spatial detail: 

1. alternative arrangements of activity locations (land use); 

2. investments in new roads and capacity expansion of existing roads; 

3. investments in public transport systems, as well as changes to levels-of-service and fares; 

4. traffic management, such as one-way street systems and allocation of lanes to particular users; 

5. demand management, such as parking restrictions and road user charges; 

6. applications of computer and information systems to operate and control transportation systems more intelligently. 

In this book we are largely concerned with forecasting the response to plans and policies belonging to categories 1–5 at future points in time. We do not focus on operational issues, such as setting or adaptive control of signals. 

From a technical point of view, forecasting and/or the analysis of policies require: 

1. a ‘base-year analysis’ establishing analytical relationships between the travel demand and cost functions, and their respective sets of variables, from data obtained for that year and possibly for earlier years; 

2. a ‘reference state’ analysis to determine the future levels of certain variables, such as land use, population, car ownership and employment; 

3. impact analyses of policies or plans through their representation as measurable changes in prices and levels-of-service; 

4. evaluation of changes from the reference state arising from the policies or plans. 

## 1.3 THEMES IN MODEL DEVELOPMENT AND APPLICATION

From our present vantage point, we looked back and identified certain themes that proved relevant to developing models, to understanding the differences among them and in charting their progression to the present states of theory and practice. The themes with which we are concerned relate to: (a) the changing contexts of models development; (b) the ways in which demand and cost functions were specified, their parameters estimated, the mathematical relations solved, and travel forecasts obtained; and (c) our views on the validity of the whole enterprise. Many of the following themes are strongly intertwined and presented as such in the different eras considered. We describe them here for emphasis and clarity. 

The first theme is the role of institutions in developing, sponsoring or promoting models. While academics and practitioners, separately or in combination, were often the ‘drivers of innovation’, a variety of institutions had a major impact on the funding, development, promotion or ratification of models. We refer to institutions in the broadest sense, ranging from national and local governments and, more particularly, public agencies charged with responsibilities for transportation systems, to research institutions, expert committees and funding agencies, whose pronouncements were particularly influential in the promotion of key ideas and sometimes set the agenda for model improvements. Legislatures sometimes also made pronouncements on appropriate model forms or modelling practices. We describe ways that institutions influenced or attempted to standardise the process of modelling, promote innovations, and disseminate material relating to models. 

The second theme is planning contexts of the development and application of models. For 60 years forecasting models served an important role in transportation planning for the purpose of evaluation and informing choices among alternative plans and policies. This book does not concern the urban transportation planning process or how it changed over the years. It is sometimes necessary, however, to identify the role of models and technical methods within this process and how the objectives and evaluation framework were influential in determining the nature of models, the information that was sought and the precision of solutions required. 

At the outset of the urban transportation planning field in the 1950s. travel and traffic forecasts were often provided in the context of a formal transportation study with a well-defined scope and duration. The terms of reference for such studies changed greatly over the years, with major implications for the development and application of models. Three aspects are particularly important: (a) the particular purposes or role for which model(s) were assembled; (b) the range of policies, projects or plans to which models were applied; and (c) the information required by evaluation frameworks for identifying problems and assessing the relative merits of alternative policies or plans for ameliorating these problems. We describe many innovations over the years to improve the design of forecasting models themselves and make them, in the modern jargon, ‘fit for purpose’. 

The third theme is the role and relevance of theory. The behaviour of land use – transportation systems is the outcome of many decisions by governments and by millions of behavioural units – individuals, households and firms – constituting the urban or regional systems of interest. Information about the behaviour of distinct groups of individuals or firms, perhaps identified by a zoning system and/or socio-economic characteristics, under conditions of change is necessary for the forecasting and evaluation processes. 

The models we portray which seek to describe, explain and forecast system behaviour are simplified theoretical statements, invariably expressed mathematically, governing the relationship among many key variables of interest. What concerns us as we move through six decades of model applications is the successive conceptual frameworks and specific theoretical constructs for organising our assumptions about the current and future behaviour of personal travel and goods movement. Whether old theories or assumptions are discarded, or continue to stand alongside the new, is a matter of considerable interest in judging the theoretical maturity of the field and the requirements of practice. 

Much has been written about the nature of mathematical models in the social sciences, and in economics in particular; and the similarities and differences between model developments in the natural sciences are often noted. We do not pursue these general issues here, but note a few key features that will accompany our discussion. At the heart of model development is the process of simplification. As Paul Samuelson [1915–2009] reminded us long ago:<sup>3</sup> 

Even if we had more and better data, it would still be necessary – as in every science – to simplify, to abstract from the infinite mass of detail. . . . All analysis involves abstraction. It is always necessary to idealise, to omit detail, to set up simple hypotheses and patterns by which the facts can be related, to set up the right questions before going out to look at the world as it is. Every theory whether in the physical or biological or social sciences, distorts reality in that it over-simplifies. But if it is a good theory, what is omitted is outweighed by the beam of illumination and understanding that is thrown over the diverse empirical data. . . . But recall again this important point. . . . how we perceive the observed facts depends on the theoretical spectacles we wear (Samuelson, 1970, 8–9, italics from the original text). 

We encountered several conceptual frameworks which differ in the nature of the explanations they offer about travel behaviour, some having different implications for forecasting, evaluation of projects and formulation of policies. Some theories of urban travel will, in Richard Lipsey’s words, ‘allow us to comprehend reality in new and different ways’ (Lipsey, 1989).<sup>4</sup> 

The fourth theme is data requirements. Urban travel forecasting models are traditionally extremely heavy users of data relating to land use and transportation networks and services, the travel of persons and the movement of goods. Early transportation studies were characterised by very large household surveys. Over time important innovations occurred in the way that data were acquired, and used in establishing and testing hypotheses and in forecasting travel behaviour. As our story unfolds, we depict issues bearing on the relationship between models and data. 

The fifth theme is solution of models. The outputs of forecasting models may be conditioned by the evaluation framework adopted in a transportation study. Typically these outputs include travel demands, vehicle flows on network links, and user costs associated with a given equilibrium state. The differences in these quantities between the equilibrium states associated with a specific plan or project are usually required. The necessity to determine such differences, which are often small, imposes a level of precision on the solution of equilibrium states associated with the forecasting model. Whatever are the merits or demerits of a particular model, some requirements on its solution are usually implied to secure sufficiently precise information. At various points in the historical development of the field, theoreticians and practitioners confronted important technical questions about the efficiency, precision and computational burden involved in solving equilibrium models. Specifically, three questions are relevant: (a) Do solutions actually exist for the demand and cost functions specified? (b) What are the mathematical means for determining these solutions? (c) Are the solutions determined to the precision required for the comparisons sought? 

The sixth theme is validation and performance of models. How theoreticians and practitioners have developed criteria for accepting particular models for their intended purposes will emerge as an important theme of our discussion. In turn these criteria will be influential in determining the accuracy of forecasts. Forecasting travel one, five, ten or 20 years into the future poses special problems and may involve a multitude of potential errors. These may arise from a number of sources, such as: (a) our understanding of the demand and cost relationships; (b) the forecasting assumptions for variables such as land use and population, which represent the future state of the city or region; (c) errors in data; and (d) human error. In our discussions of developments and innovation, we shall be concerned with the framework for assessing the validity of models and how models performed in relation to outcomes. 

The seventh theme is practical compromises in model development. Some models and methods that we describe are much more complex than others, in both the representation of behaviour and the resulting system of equations. Throughout the last 60 years, more sophisticated models were generally presumed to be more accurate, and therefore preferred over more simplified ones. Yet, with some exceptions which we describe, complex models are apparently not widely sought after or used by planners. We can anticipate some of the reasons, so we wish to alert readers new to the field that to judge a model or method solely on the basis of its technical or behavioural sophistication would be to miss an important point. Planners often find themselves in that awkward position of having to make and justify their decisions on the basis of limited data, uncertain knowledge and limited resources, particularly money, manpower and time (Shepherd et al, 2006a). Only if this point is appreciated can we hope to understand the gap that has emerged between the cutting edge of theory and the world of planning practice. 

As already noted, an essential feature of travel modelling for the purpose of forecasting is simplification. In the complex systems of equations that represent the behaviour of personal and goods vehicle flows in the land use and transportation systems, what simplifications are justified? What are the implications of alternative assumptions for forecasts and policy decisions which rest on them? These are questions that lie at the heart of applications of travel forecasting models. 

## 1.4 SCOPE OF OUR WORK

The contexts of urban travel forecasting are now very wide-ranging, and include: (a) projects undertaken for private companies, as well as those proposed and financed by public agencies; (b) various spatial environments from massive, densely populated urban areas or conurbations with rich travel options to relatively small towns in extensive rural hinterlands; (c) strategic considerations as well as specific scheme-based impact studies; (d) the initial sifting of alternative plans through to testing final detailed designs; (e) area-wide, corridor-based and specific local applications; (f) the investigation of the long-range impact of large, expensive projects as well as the short- and medium-term appraisal of much more modest schemes; (g) those projects for which the knowledge base of traveller behaviour is reasonably secure or, at least, largely uncontested, and those for which there may be very little available evidence. In this book we exploit the common features of many travel forecasting models used with the cross-sectional approach, rather than consider each of these cases individually. We did, however, set some limits on the scope of our discussion based on model types, policies and spatial contexts: 

1. Application to world cities. Although the approaches that we describe had their genesis in the cities of North America and Western Europe, they were over the years applied with relatively minor modifications to the large majority of major cities and urban areas in the world. In some contexts, particularly on the periphery of some cities in the developing world, data collection and model building are highly problematic. Discussion of these cases is outside the scope of this book. 

2. Operational applications. We generally exclude operational issues, such as those relating to traffic control systems, although on occasion we do refer to some models used for such purposes. 

3. Policy and project evaluation and design. We are almost exclusively concerned with what are sometimes referred to as ‘positive’ issues – investigations of ‘how the world works’ and how people do behave under given conditions, rather than ‘normative’ issues of how people should behave and the means by which they may be induced so to do. We consider the policies and plans to be given rather than address either how they are formed or normative issues relating to the formulation of ‘optimal’ plans for the supply of transportation facilities and services. As noted in section 1.2, when used in conjunction with an evaluation framework, these forecasting models are widely used in the design of policies and projects. 

## 1.5 LIMITATIONS OF OUR APPROACH

This book is about the evolution, influence and application of ideas in urban travel forecasting over 60 years. Although we fervently hope that it will add to an understanding of the subject, we do not view our work to be a definitive history of the subject. Any history is conditioned by the personal experience, knowledge, interpretation and social context of its authors, and we are even more aware of this fact now than we were at the outset. Just as we did not always accept certain early accounts in their entirety, others may judge ours as incomplete or subject to qualification. It will be for them to fill in the gaps, amend a viewpoint here and there and perhaps correct some bias. We are aware that our account, particularly its breadth and the depth in particular areas, has been influenced by several factors, which imposed limitations on our approach. We mention the following: 

1. In assessing and synthesising material from thousands of articles published in our field, and the large number of transportation studies conducted over this period, we attempted to identify the main forms of model development, bring out the key ideas, and give credit to their originators. In synthesising this vast range of material, the possibility of omissions or inaccuracies is always present. Our own research experience has been confined to only a part of what is now an extremely broad and deep subject covering several academic traditions including mathematics, engineering, operations research, psychology, economics, geography, regional science and urban planning. We do not claim to have delved into all sub-specialities let alone possess expert knowledge in each. Others from different backgrounds or research experience would without doubt identify different themes for their discussion and emphasis. To partly compensate for this situation, we have sought the views of many experts, and in several places we point the reader to specialist texts and manuals where more details can be found. In an extensive and rapidly developing field we hope to have achieved sufficient perspective to identify the main issues, themes and developments; however, omissions are inevitable and we invite comments where these are considered significant. 

2. In most cases, identification of innovations and their originators presents few problems. In the case of the significance of innovations, we sometimes resorted to existing papers, texts or reviews, sought the insight of experts, and drew on our own experience. Where attribution of ideas was in doubt, we returned to the historical record, reread relevant articles, consulted colleagues and relevant experts in the field, and then came to a personal view. In some cases we were informed through correspondence that standard accounts are inaccurate, and we revised or revisited these. It is unlikely that we found them all. 

3. While it is relatively straightforward to consult the international literature and conference reports to assess the contributions of academics and consultants, access to transportation study reports, particularly those subject to commercial confidentiality, is more problematic. New models with catchy acronyms emerge regularly, although few are highly innovative. While we are confident that our views are broadly representative of practice, we were unable to scrutinise the full range of applications. Important innovations arising in practical studies quickly tend to find their way into the international literature and, in turn, are disseminated back into future practice. In various discussions and correspondence, we were directed to unpublished work that is often of great interest and significance. Sometimes that work was published in less visible journals and perhaps covered later in more popular or widely disseminated accounts, and the original work is forgotten, as was pointed out to us on a number of occasions. We imply no malpractice here. Sometimes it just happens. 

4. Even in a largely technical subject, the history as seen through North American eyes is rather different from that seen through European eyes; we tried to blend our two perspectives. Furthermore, we are well aware that reporting of innovations in this field is overwhelmingly in the English language, and through historical circumstances and by sheer weight of research capacity over the years this in turn is US dominated. Even less likely would be a knowledge of the French, German, Russian, Spanish, Japanese or Chinese experience both then and today. We were not able to do justice to many articles published in other languages or papers that were not presented at international conferences or published in the international literature. We had some help with important work published in other languages, especially German, French and Spanish, but this dilemma remains a major challenge for our field at a time when the research output of Asian countries is expanding rapidly. 

5. Finally, since our intention is to present ideas to a wide audience, recording developments in one of the most highly analytical fields of public policy analysis poses particular challenges in how to deal with its formal language – mathematics. Often both the language and the techniques (such as calculus and statistical analysis) are central to the expression and solution of theoretical and technical problems. As both authors have mathematical backgrounds, we know well how their use in a highly technical field has been vital to establishing logically coherent arguments and contributing to knowledge – even if it sometimes failed to achieve the level of knowledge creation and precision sometimes claimed. But the benefits of formal developments are often exaggerated when it comes to the discussion of principles and ideas, particularly when issues in the real world are ‘staring us in the face’. 

We therefore adopted a dual approach: the main text is free of mathematical analysis. However, where we felt that it would contribute significantly to the discussion, we added mathematical endnotes. References to specialised discussion are also included. Others will judge whether this approach has been successful. Even with the substitution of words for symbols, many parts of the discussion may prove difficult to newcomers. As noted in the Preface, we feel that it will be appropriate to read this book in conjunction with a technical textbook on travel forecasting and a formal course in order to augment the discussion and fill in the gaps. 

## 1.6 NAVIGATING THE TERMINOLOGY AND ACRONYMS

Experienced readers of American and British transportation literature are well aware of differences in terminology between these two major branches of the English language. A few words of explanation may be helpful. We adopted British spelling throughout, except in quotations, where the original spelling is retained. The noun ‘transportation’ is mainly used in American English, whereas ‘transport’ is the preferred noun in British English. We agreed to use ‘transportation’ in this book, except in proper titles and quotations. In British English, ‘public transport’ is the noun used to refer to public transportation systems and services. In American English, ‘transit’, ‘mass transit’ and ‘public transit’ are all used. We decided to use ‘public transport’ to refer to these systems in all countries. 

In the UK and some other places, the term ‘transport model’ is a convenient shorthand used to refer to travel forecasting methodology. We do not use this term here, except occasionally in the UK context, in order to avoid possible confusion for readers unacquainted with it. 

In an effort to be concise and improve the flow of the text, we introduced a number of commonly used acronyms. Although they are defined when introduced, an overview and some explanation may be warranted. 

Throughout the book, we abbreviate the United States of America (US) and the United Kingdom (UK). Names of governmental agencies at the national level are always preceded by these initials. The US Department of Transportation (US DoT) was created in 1967. Prior to that event, the  federal highway agency, the Bureau of Public Roads (BPR), resided in the US Department of Commerce (US DoC). At some point shortly after the establishment of US DoT, BPR was transferred and renamed the Federal Highway Administration (FHWA), the acronym ‘FHA’ having already been used to designate the Federal Housing Agency. In 1964 responsibility for public transport was assigned to the newly created US Department of Housing and Urban Development (US HUD). Subsequently, this responsibility was transferred to US DoT, where the agency responsible for public transport was named the Urban Mass Transportation Administration (UMTA). Finally, in 1970 the US Environmental Protection Agency (US EPA) was established. In a few cases ‘DoT’ is also used to designate a state department of transportation. 

The UK Ministry of Transport (UK MoT) was established in 1919, and continued in some form until 1970.<sup>5</sup> At that time transportation matters were transferred to the newly formed UK Department of the Environment (UK DoE). From 1976 to 1995, the UK Department of Transport (UK DoT) by and large had responsibility for transport problems. Following several name changes during 1997–2001, the UK Department for Transport (UK DfT) was created. 

Cross-references are inserted at many places to connect one topic to a related discussion in another section. Often these cross-references state only the word ‘section’ followed by the section number. Transition and connecting phrases are omitted in the interest of brevity. 

Finally, for historical interest, we give the birth and death dates of deceased contributors to our field and related fields. Living contributors are not so designated. In the Notes, we also cite Wikipedia web pages of many individuals for whom such pages have been posted. We have inevitably missed some, and others may be added in the future, so we ask readers to refer to Wikipedia for more information about contributors to our field. 

## 1.7 CONTENTS OF THE BOOK

Writing about our field would be considerably easier had it developed from a single point in a generally agreed direction to an identifiable, unambiguous and unchallenged ‘state of the art’ where the world of practice harmonises neatly with that of theory. But that was not to be. The field developed in a rather complex way with theoretical advances intertwined with practical developments, the latter first moving ahead of, but later lagging behind, the former. The ‘mainstream’ of practice has also revealed significant variations over time, among various countries and in different planning contexts. This situation has prompted many questions about the distinct alternatives available for travel forecasting at any particular time and their relative merits for different applications. 

We consider this rather irregular and sometimes disjointed evolution of theory and practice by developing a broadly chronological account of overlapping periods, where significant ‘break-points’ were suggested by either innovation in methods or policy development. Some have suggested that these correspond to changing paradigms, when one set of ideas and world view for interpreting issues is, by power of explanation or force of relevance to planning problems addressed, traded for another. (We shall later argue that this represents an oversimplified view of the realities of planning practice over the years.) We sometimes follow particular ideas up to the present day. We also backtrack to pick up various themes and, on occasion, to address what we consider to be missed opportunities where alternatives to the ‘mainstream’ appeared and only much later were seen to be of considerable value to forecasting practice. 

In Chapter 2 we chart the rise of the field and the establishment of what became variously described as the traditional, conventional, classical, four-step or sequential approach to travel forecasting. This account is confined to developments in the US, and Canada, where the challenge of the motor age was first confronted with a ‘systems approach’. This review takes us up to the early 1970s when political and economic imperatives (e.g., the grass-roots freeway revolts in the US and the first oil crisis) led to more emphasis on transportation system management and public transport. 

During this period the ‘systems approach’ to transportation planning was exported to other countries, such as the UK, which also took up the challenge in the early 1960s of planning for mass motorisation. Chapter 3 addresses the transfer and application of the techniques and the innovations in travel forecasting that occurred up until the early 1970s, in part owing to their adaptation to local requirements. Departing from a largely common approach being applied in the US, we describe significant innovations in forecasting models, which led to major changes in the way that forecasts were prepared. 

We then turn to a discussion of what some called the ‘disaggregate behavioural’ revolution, which emerged in the early 1970s. We describe a theoretical approach, with its roots in the statistical study of modal choice a decade earlier, based on the rational choices of individuals over discrete sets of alternatives, such as the choice between several transportation modes. Within this framework we show how the motivation and actions of decision makers (individuals and households) in a wide range of urban travel situations was described, explained and forecast, based on assumptions of economic rationality. This micro-behavioural approach, founded on what became known as the random utility maximising theory of discrete choice, provided an appealing and enduring approach to travel forecasting. Gradually it established itself as a practical alternative, and a complement to the traditional forecasting approach in urban transportation. It also enabled a theoretical reinterpretation and reformulation of the traditional four-step procedure. 

In view of the extent and importance of this micro-behavioural approach, we present it in two chapters. Chapter 4 concerns those theoretical and practical innovations that occurred in a short but formative period in the early 1970s. These were largely associated with the theory and application of a particular model form, the multinomial logit model, but also included important early research on the relationship between the basic structure of models and hypotheses about travel-related decisions. Chapter 5 introduces a large number of innovations in model specification, parameter estimation and applications. In particular, Chapter 5 describes how theoretical arguments led to the development of new models and methods for analysis and forecasting of travel behaviour, which allowed a number of problems with conventional models to be addressed. 

The micro-behavioural approach was greatly enriched in the late 1970s and 1980s by examining the wider context of individual and household decision making and impact of transportation policy at the micro-level. This development began an era of ‘behavioural realism’ in which many assumptions of the past were scrutinised and refined. By representing the demand for travel as derived from the need to conduct activities separated in space and time, activity-travel models offered an innovative approach. With their inherent emphases on constraints and interdependencies among trips and household members, they were initially presented as a distinct alternative and a possible rival to both the traditional and the micro-economic approach. Now they may be seen as part of a grand behavioural synthesis, their practical contribution being expressed first through the development of ‘tour-based’ forecasting models in the early 1980s and, subsequently, to ‘schedule-based’ analysis of travel behaviour in time and space. This framework and the models that evolved from it are the subject of Chapter 6. 

In Chapter 7 we reflect on what we see as a missed opportunity. In the mid-1950s, concurrent with the origins of the traditional approach, an intellectually demanding book appeared (Beckmann et al, 1956) that proposed a conceptual framework, which might have been used to interpret and address some of the technical and theoretical problems confronting travel forecasting. We examine the contrasts between the traditional approach to specifying and solving the sequential procedure and what later became known as the combined model approach. We offer some views of why the latter was not recognised for 20 years and discuss its significance. 

In Chapters 8 and 9, we consider the world of practice in more detail. Taking the US and UK as important examples, we examine developments of the traditional trip-based travel forecasting models as well as more advanced approaches. In addition, we record the innovations and practical application of models which incorporate the interdependency between the land use and transportation systems and goods movement. While drawing on the legacy of earlier times, we focus on the last two decades. In the early 1990s in the US, new legislation had profound implications for the specification and solution of travel forecasting models, as well as launching a major attempt to reform the way that travel forecasts were made. Important innovations also occurred in the UK in this period; however, here the emphasis was on the adaptation of traditional methods to address a broader range of policies. 

From its beginnings in the early 1950s, urban transportation planning generally, and travel forecasting in particular, was closely associated with the development and use of digital computers. In Chapter 10 we take a step back and trace the history of these ambitious efforts from the early mainframe applications on through to the current use of personal computers, and associated developments in travel forecasting software. In particular, we note how changes in computing power had profound implications for the specification and solution of these models. We also trace the evolution of the principal software systems for urban travel forecasting. 

In Chapters 11 and 12 we draw our story to a conclusion. In the former we consider the achievements and current challenges and offer some views on the future prospects for the field. Drawing on our themes we summarise the major developments in the theory, methods and practice of urban travel forecasting over a period of 60 years and reflect on the innovations that occurred to provide more satisfactory ways of undertaking existing tasks, to answer critical concerns and to address new requirements. We consider the longevity of the traditional approach, the hitherto limited application of alternatives, and the multiple ‘states of the art’ which characterise contemporary practice. We consider some views on current challenges faced and, without being prescriptive, discuss some questions and issues which might guide the future development of the field. In Chapter 12 we return to the context of urban travel forecasting and ask how innovative ideas emerged. Finally, we offer comments for those approaching urban travel forecasting as a field of study for the first time. 

We are about to take the reader back to a time quite different from the modern age, not only in the nature and scale of the problems faced and the approaches to their resolution but also in the technology of analysis and what is sometimes referred to as the ‘culture of research’ in our field. In 1950 many countries were still recovering from the Second World War. The transistor had only recently been invented (1947), while the advent of the laser was a decade in the future (1958). Computers were extremely primitive by modern standards and practically unavailable for civilian use. The inventions of the now ubiquitous internet and World Wide Web<sup>6</sup> were decades away. The problems of dealing with large amounts of data from surveys of urban transportation were enormous. Indeed, many of the mathematical, statistical and data analysis tools that are now taken for granted were then being invented. 

In those early days there was no ‘culture of research’ in our field. Transportation was not an academic discipline. There were no research institutes devoted to its development, few conferences devoted to the subject, minimal published material, no dedicated journals to serve the advances in the subject, and no automated way to conduct searches of what little literature was available. The modern age is as different and in some aspects unimaginable to those of 1950 as the world will be in perhaps 30 years for the citizen of today. 

We are now ready to tell our story. 

## NOTES



1. For a definition of cross-sectional data, see en.wikipedia.org/wiki/Cross-sectional_data (accessed 9 May 2014). 





2. Beckmann et al (1956, xiii–xiv, 59); Manheim (1979, 29–30); Florian and Gaudry (1980, 1–5): Sheffi (1985, 6–8). 





3. en.wikipedia.org/wiki/Paul_Samuelson (accessed 25 December 2013). 





4. en.wikipedia.org/wiki/Richard_Lipsey (accessed 25 December 2013). 





5. en.wikipedia.org/wiki/Ministry_of_Transport_United_Kingdom (accessed 25 December 2013). 





6. en.wikipedia.org/wiki/World_Wide_Web (accessed 10 January 2014). 



## 2. Emergence of the traditional approach

## 2.1 INTRODUCTION

To understand the emergence of urban transportation planning in the US, try to imagine the situation in large urban areas such as Chicago in the early 1950s, a prosperous period following the Second World War. Their populations had increased substantially through in-migration from rural areas, especially from the south, as well as from abroad. Moreover, within metropolitan areas, out-migration to the suburbs was increasing. 

In response to increased use of cars, and trucks for deliveries and goods movement, expressway plans proposed for the Chicago area in the 1930s were being implemented. For example, a six-lane, 13-mile expressway connecting north-west Chicago to its northern suburbs opened to traffic in 1951. Four radial expressways centred on Chicago’s central area were planned, but construction funding was not available. A circumferential tollway with radial extensions into the outer suburbs was being planned. In contrast, following the peak ridership achieved in 1946, bus, streetcar and subway-elevated ridership had steadily declined.<sup>1</sup> Similar conditions were found in Detroit, Los Angeles and Philadelphia. 

Profound changes were occurring in the planning of urban transportation systems in the US in response to these socio-economic trends and advances in urban freeway design. This chapter explores these developments from the viewpoint of the pioneering transportation studies in the Detroit, Chicago and Philadelphia areas, and the efforts of the federal (national) highway and transit agencies. These efforts were remarkable for their originality and ambitious objectives. Some succeeded in creating and applying novel travel forecasting methods; others had grand visions, but failed to achieve them. Coincident with and essential to these efforts were new computational capabilities, the first mainframe computers, unprecedented in memory and speed. Although tiny from today’s perspective, these facilities, and the programs created for their use, enabled a huge advance in implementing new methods. 

Following a short background statement (section 2.2), the innovations and contributions of the Detroit and Chicago area transportation studies are examined (sections 2.3, 2.4). Next, the activities of the Bureau of Public Roads of the US Department of Commerce (section 2.5) and the US Department of Housing and Urban Development (section 2.6) are described. Finally, efforts to extend the early urban transportation planning studies to the consideration of land use are chronicled (section 2.7). These sections consider the development of travel forecasting from the early 1950s to the late 1960s. Terminology of this period is used, for example ‘trip table’ rather than ‘trip matrix’. A brief conclusion completes the chapter (section 2.8). 

## 2.2 IMPETUS FOR URBAN TRANSPORTATION STUDIES

Urban and rural highway studies followed innovations in car technology early in the twentieth century. Likewise, studies of privately owned and operated urban and inter-urban electric railways provided the basis for their regulation. Reviews of these early studies lie outside the scope of this book. Two developments, however, are noteworthy. 

The first was the early planning for an interregional highway system, later known as the National System of Interstate and Defense Highways. These efforts began in the late 1930s and resumed near the end of the Second World War, with the passage of the Federal-Aid Highway Act of 1944, designating the system, and the Federal-Aid Highway Act of 1956, funding its construction with user taxes (Weiner, 1997, Chapter 3). 

The second was the initiation of urban origin–destination studies, also known as home interview traffic studies. Such studies continued sporadically through to the 1930s (Heightchew, 1979).<sup>2</sup> Following the resumption of origin–destination studies after the Second World War, more ambitious programmes were organised, first in Detroit and then in Chicago, known as ‘urban transportation studies’. 

## 2.3 DETROIT METROPOLITAN AREA TRAFFIC STUDY

## 2.3.1 Overview and Objectives

In 1953 highway agencies in the Detroit, Michigan area embarked upon an origin–destination study and the preparation of a long-range plan for highways. J. Douglas Carroll, Jr. [1917–1986] was appointed study director. Following graduation from Dartmouth College, and service in the US 

Navy during the Second World War, Carroll earned the third Ph.D. in city and regional planning awarded by Harvard University in 1950. From 1948 to 1953, he was resident director of the University of Michigan Social Science Research Project in Flint, Michigan. Based on his analyses of urban travel and traffic, Carroll explored hypotheses related to the separation of residences and workplaces, and urban spatial patterns (Carroll, 1949, 1952). 

In contrast to earlier origin–destination studies, the Detroit Metropolitan Area Traffic Study (DMATS) embarked on the preparation of a longrange plan for urban highways based on surveys, analyses and forecasts of future traffic. Its purpose was ‘to insure effective functioning of the movement’ of persons and vehicles ‘by thoroughly understanding the nature of the movement and then by devising the most effective highway plan to serve it’ (DMATS, 1955, 13). The principles of the study stated that ‘a valid road network plan must’: 

1. Derive from a thorough knowledge of travel that is taking place today, its component parts, and the factors that contribute to it, limit it, and modify it. 

2. Conform to and encourage the land development planned for the area. 

3. Serve the future traffic demand. 

4. While being consistent with the above principles and realistic in terms of travel trends, be economically feasible (DMATS, 1955, 13). 

DMATS issued two reports (DMATS, 1955, 1956) describing its multistep travel forecasting procedures. One difference between later studies and DMATS was its focus on expressway network planning to the near exclusion of public transport. 

## 2.3.2 Forecasting Traffic Patterns and Testing the Plan

DMATS proceeded with data collection as follows. First, a home interview study was conducted in 1953 for the study area, including interviews at external stations for sampling travel in and out of the area. The home interview study obtained data on dwelling types, the number, age and occupation of residents aged five or over, and the number of cars owned. For each resident, a trip record over a 24-hour period was obtained: for each trip, the time and place of origin; the time and place of destination; the mode of travel; and the purpose. For stable residential areas, 4 per cent of households were interviewed; for outlying suburbs undergoing active growth, the interview rate was increased to 10 per cent (DMATS, 1955, 19, 21). Over 39 000 home interviews were completed, as well as interviews of 7200 trucks and taxis. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/38754b84-3c6e-4874-b89a-d84630ad82f8/02bf8ace4594ac7bb5867ee6f1c91a83b1f4d706bc043e4fc160a5465f79e0f7.jpg)


Second, trip rates were determined for five land use types by distance from the centre and density. Third, travel volumes between pairs of traffic zones in relation to travel distance were compiled. The findings showed that ‘the travel volumes between any pair of zones would be proportional to the product of the number of trips terminating at each zone and inversely proportional to the “friction of travel” between those zones’ (DMATS, 1956, 29). Fourth, maps of vehicular traffic desire lines were prepared showing the density of travel, as shown in Figure 2.1. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/38754b84-3c6e-4874-b89a-d84630ad82f8/1b32bb97fb24e83288086c7bfd35bdb91f98b53ebd31f3ea13791cf83cce6349.jpg)



Figure 2.1 Desire line density chart of internal vehicle trips in the Detroit area


The analyses performed were described in detail in the two-volume report. Although the actual procedure followed is not entirely evident, the following points seem clear: 

1. All analyses and forecasts were prepared for a typical 24-hour weekday; peak period traffic was hardly mentioned. 

2. Although public transport usage was inventoried, and was significant (15 per cent of all person trips), no forecasts were prepared of its use. 

3. Trips were classified by nine purposes defined by activity and land use at the destination. 

4. Trip rates (person trips per land area, or per floor area in the case of the central area) were then computed in terms of arrivals at destinations by purpose. 

5. Departure rates from residential land uses were determined in relation to the means of four variables computed for 16 relatively homogeneous residential areas by relative income level, number of cars owned, distance from city centre and residential density. 

6. A ‘predictive formula’ describing the relationship between zonal trip interchanges and the number of departing and arriving trips, and a function of the separation of the zones, was fitted (DMATS, 1955, 92–93). However, this relationship was not used in the travel forecasting procedure; instead, a growth factor procedure was applied to the survey trip table, which was an extension of the method of Fratar (1954).<sup>3</sup> 

7. Much emphasis was placed on desire line density analysis. A technique of McLachlan (1949) accumulated the density of trips whose airline route traversed areas of one-quarter square mile. Extensive maps showing contours of these densities were prepared to visually inspect the travel patterns. 

The findings of these studies were applied in preparing the 1980 expressway plan. Forecasts of population and employment for 1980 were made for the study area. Land use inventories and existing land use plans for the City of Detroit and the Detroit suburban area were used to devise a forecast by traffic zone of the extent of development in 1980. This forecast in terms of land area, or in the case of the central area by floor area, was the basis for preparing a forecast of future daily person trips. 

Based on the analysis of survey traffic volumes, a modified growth factor method was devised, which included factors at both the origin and the destination of the trip (DMATS, 1956, 28–30). Suburban zones largely vacant in 1953 had their zero interchanges increased to provide the basis for a realistic 1980 forecast. External local travel and through travel were forecast separately. The forecast was validated by a thorough comparison with the 1953 survey. 

Prior to DMATS, origin–destination studies generally concluded with the preparation of maps of desire lines of future travel patterns. Forecasts of the diversion of arterial traffic to a proposed expressway began to be performed in the late 1940s in the design of the first urban expressways, such as in California, Texas and Detroit. M. Earl Campbell [1902–1979] stated: 

The estimated allocation of traffic to a proposed highway facility is commonly termed ‘traffic assignment.’ The estimated allocation may indicate annual average daily traffic volumes, periodic directional movements, and composition by types. . . . The assignment of traffic to a proposed facility involves an estimation of volumes of the following components . . . : (1) traffic diverted from alternate routes; (2) traffic created by the new facility . . . ; (3) traffic resulting from intensified land use . . . ; (4) traffic increase due to growth in . . . use of vehicles (Campbell, 1952, iii). 

The methods of traffic assignment described by Campbell were limited to assessing the impact of a new facility on an arterial corridor, and relied on relationships between the proportion of traffic diverted to the facility and the ratio of travel times, or distances, over expressway and arterial routes. DMATS advanced these methods by considering both savings in travel time and additional travel distance required to utilise a new expressway. Such methods were applied on an area-wide basis, evidently for the first time. The discussion of the traffic assignment procedure suggests the authors understood the complexity of their task. They knew the difference between ‘the theoretical total demand for expressway service’ and ‘the actual flows of traffic that would obtain if the expressway network were in place’ (DMATS, 1956, 86). They also considered that travel speeds on expressways would fall as volumes increased towards capacity, and that: 

With each additional increment of traffic, congestion naturally worsens. Under actual conditions, as congestion developed on one route drivers would tend to seek alternate travel paths [routes]. Thus, actual flows probably represent a condition where the capacities and comparative ‘friction’ of all possible routes of travel must be considered. This involves the knowledge of the number and capacity of all surface routes as well as of express routes (DMATS, 1956, 86).<sup>4</sup> 

DMATS succeeded in making traffic assignments of the 1953 origin– destination traffic volumes to the existing road network and of the 1980 forecasted volumes to an expressway plan consisting of 46 miles of existing and committed expressways and 164 miles of proposed expressways. The assignments did not include volumes on arterial routes; rather the proportion of each zone-to-zone volume assigned to expressways was tabulated by expressway route. The plan was then revised twice, and a final expressway plan devised. The ratio of the benefit of the improvement to its cost was computed for each section of the expressway network. 

Finally, DMATS appears to be the first study to combine an ‘origin– destination study’ with an ‘areawide traffic assignment’, resulting in a forecast of an origin–destination traffic pattern for a metropolitan area on a network of proposed expressways. Because of the joining of these two methods, the new concept of an ‘urban transportation study’ was born. Weiner (1997, 29) stated: ‘DMATS put together all the elements of an urban transportation study for the first time. 

## 2.3.3 Computational Aspects

DMATS was remarkable in many methodological respects, including its application of computational methods of the early 1950s. In 1949, the IBM 407 accounting machine was the last and best of the electromechanical accounting machines. The IBM 407 read a deck of 80-column punch cards on an integrated card reader, accumulated totals, subtotals, or other simple statistics in counters made of gears, and printed the results on an integrated 132-column line printer.<sup>5</sup> Speed of operation was 100 to 150 cards per minute. As with all IBM punch-card equipment, except the key punch and sorter, a control panel was wired to specify: what card columns to read, what to do with them, and how to format the report. Although the IBM 407 was really just a big adding machine, creative use could be made of the control program. The machines were large and heavy, as shown in Figure 2.2(a).<sup>6</sup> 

Factoring of the 1953 zonal interchange volumes was performed iteratively for the 254 zones plus ten external stations along the study area boundary. Of the 70 000 possible interchanges, 34 574 movements were represented in the 1953 survey data, plus added interchanges for six suburban zones with insufficient trips recorded in the survey. These movements were multiplied by origin zone factors and destination zone factors. 

The process adiusted all travel volumes from the inventoried system and thereby created a new system of movements more consistent with the predicted trip totals at each terminal zone or station group. The new traffic pattern thus obtained did not, however, meet the condition of having the predicted number of trips terminating at each zone or station group. . . . Therefore, the process was repeated using the newly predicted traffic pattern as the new point of departure. This complete repetition . . . is known as an ‘iteration.’ In actual practice, five complete calculations or iterations were made before the trip totals at each terminal point . . . closely approximated the totals predicted at each of these zones or station groups (DMATS, 1956, 31). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/38754b84-3c6e-4874-b89a-d84630ad82f8/fd78b66855374b7bc488d13ff4a2acbe8e19909cb51fc56e4a0719cd7774699a.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/38754b84-3c6e-4874-b89a-d84630ad82f8/d7340ee40196ed9cb7a6dcfcb534163c80f2acaff9a990b1457cfa54370fc30d.jpg)



Source: da Cruz, Columbia University Computing History, www.columbia.edu/cu computinghistory/.



Figure 2.2 (a) IBM 407 accounting machine (b) IBM 704 computer


Such a procedure was later called ‘balancing the trip table’. Balancing a trip table of nearly 35 000 interchanges in five iterations on a tabulator surely required considerable ingenuity. 

Likewise, a detailed procedure employing punch cards and accounting machines was developed for the preparation of desire line density charts (DMATS, 1955, 105–107) and the traffic assignment procedure (DMATS, 1956, 129–131). The assignment procedure consisted of three steps: 

1. measuring the distance of the shortest route of travel via city streets for a pair of zones; 

2. measuring the distance for a route using expressways for the same zone pair, including separate measurements of distances from the zone centres to the expressway ramps and the distance along the expressways, so that separate speed ratios could be applied to each; 

3. calculating speed and distance ratios, and determining the efficient allocation of zonal interchanges to expressways. 

Measurements were performed manually, but punch cards were used to record intermediate steps to automate the procedure partially. 

## 2.3.4 Lessons from the Detroit Area Study

The final report of DMATS provided extensive details on procedures and empirical analyses, but no overall description of the travel forecasting procedure. Fortunately, Douglas Carroll provided these insights in what may be the first diagram of the sequential travel forecasting procedure, shown as Figure 2.3. The diagram articulates the innovations and advances of DMATS summarised below: 

1. Travel forecasting is based on an ‘inventory of daily movements of persons and vehicles’, a ‘record of land activities by location’ and ‘a detailed inventory of transport networks’. 

2. ‘The relationships of these surveys are examined and quantified. People in a particular land use setting . . . have particular travel needs. Travelers must move through the utility network. People with requirements represent positive potentials; land use sites to which people may go represent negative potentials; and people and vehicles moving through the network to equalize these potentials react to the network resistances and create flows. 

3. ‘The economic activity of the community is examined and population change potentials are equated with expected future economic growth.’ A forecast of population, economic activity and land use is prepared. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/38754b84-3c6e-4874-b89a-d84630ad82f8/558230e815d4a4f3a4b7058631afd26799eedf77271058195ae95ac757dc5586.jpg)



Source: Carroll and Bevis (1957, 187).



Figure 2.3 Urban travel forecasting procedure


‘These gross estimates of future size are then translated into specific land uses which are distributed throughout the area. 

4. ‘Based on future land use and population distribution, new travel estimates are inferred. 

5. ‘These estimated travelers are forced to flow through a newly designed transport network. Gradually a plan suited to the future growth is tested and refined. 

6. ‘These results are then related back to the initial assumption of growth. Land uses, and population distributions are reviewed in the light of an anticipated new transportation network. If changes result, the process is repeated. This process is logical but difficult when it is realized that balance and equilibrium are required at successive points and for the entire model. Any change in any part of the metropolitan area will disturb this equilibrium with consequent reaction toward a new equilibrium’ (Carroll and Bevis, 1957, 185–186, excerpts are in quotes). 

Figure 2.3 ‘shows that travel is inferred from land use, and trips are forced to flow through a proposed network. The return arrows or loops show that the results at successive steps feed back information that will modify and repeat until a satisfactory solution is achieved. At present, feed back is not automatic. . . . It is, however, certain that in the future estimating and plan testing will become increasingly automatic’ (Carroll and Bevis, 1957, 186–187). 

Figure 2.3 and the above statement describe clearly the vision of Douglas Carroll and colleagues for urban travel forecasting. They understood that travel was related to urban activities and their locations, called land use. They understood that interzonal interactions must be consistent with travel times and distances. Moreover, they understood that interzonal travel must be routed over road networks, which had capacity limitations that affected travel times and costs. They used the terms ‘balance and equilibrium’ to describe interactions of land use and transportation networks in reality, and adjustments of each system to the other. They described the process of feedback of information as achieving a ‘satisfactory solution’. Carroll (1955) had earlier described a model of spatial interaction, which he tested with data on toll telephone calls. 

Douglas Carroll did not consider the contribution of public transport in the Detroit study, perhaps because of institutional constraints. Also absent were a concern and means of relating travel forecasts to the timing of travel during the day; instead, 24-hour forecasts were prepared. Trip frequencies by origin and destination and by purpose, however, were explored in detail. Finally, the handling of large masses of data with punch-card technology, and manipulating it to achieve credible results, is truly remarkable. 

Within a month of the presentation of the above paper, Douglas Carroll and Roger Creighton (1957) presented a somewhat more refined version of their thinking for the Chicago study. Among these statements, one finds the following quoted points concerning the estimation of zonal interchanges: 

1. Zonal interchanges may be a function of opportunities for interchange between two zones; 

2. Zonal interchange may be a function of competing opportunities; 

3. Zonal interchange may be an inverse function of some combination of distance, speed, cost and/or convenience that, for lack of a better term, may be called ‘travel resistance;’ 

4. Zonal interchange may be a function of demand, as expressed by the willingness or need to travel (Carroll and Creighton, 1957, 4). 

## They elaborated on these ideas as follows:

Travel resistance between zones, which must be known or estimated in order to predict zonal interchange, is a function of mode of travel, whether automobile, bus, train, or rapid transit. . . . Since travel resistances differ by mode, then zonal interchanges will also be a function of the modes which are available to serve any pair or group of zones. . . . the most logical place to study modal distribution is at the point where traffic is assigned, because it is there that flows on routes must immediately affect each other and it is there that the individual considers the use of competing modes to take him from origin to destination Knowledge gained in the assignment problem must then be fed back into the zonal interchange problem to make any necessary changes in assumed modal travel resistances. 

Feedbacks during the estimating process are essential for reasonable solutions. One of the most important is the effect which traffic flow has on zonal interchange. If the method of estimating zonal interchange predicts so many trips between two zones that the speed of travel is reduced, then the amount of travel between the two will decline and other zones, now relatively more advantageously located with respect to one another, may increase travel linkages until a status of equilibrium is achieved consistent with the new routes and the travel demands (Carroll and Creighton, 1957, 5). 

Flowcharts accompanying the text illustrated the authors’ concept of feedback. This brief paper shows that the leadership of the Chicago study had a clear vision of their task.<sup>7</sup> 

Before turning to the Chicago study itself, we draw attention to Carroll’s use of the term ‘travel resistance’, and related terms from that period. Brian Martin, Frederick Memmott and A. J. Bone, in their extensive review of travel forecasting methods, also used the term travel resistance’. Perhaps they were influenced by Carroll and Creighton (1957), which is Reference No. 40 in Martin et al (1961, B-2). 

Other papers of that period, however, used a different term, ‘travel impedance’. The earliest known use of ‘impedance’ is in a glossary by Lee Mertz: 

impedance may be some average value for travel time. It may be distance if minimum distance routes are desired or it may be a combination of the two. It is generally agreed, however, that travel time alone will not give balanced assignments inasmuch as there are many other factors besides travel time that influence the motorist in route selection. Travel time is probably the strongest single factor, however, and thus furnishes a good point of beginning for defining link impedances (Mertz, 1961, 96). 

In a slightly earlier paper with a similar glossary, Mertz (1960b, 29) had included only travel time and distance. Walter W. Mosher, Jr., at the Institute of Transportation and Traffic Engineering at the University of California at Los Angeles, published a scholarly paper on a capacity restraint assignment algorithm. In a detailed glossary, he wrote: 

Link Impedance – A value assigned to each link of the network. This impedance may be some average value of travel time, it may be distance if minimum distance routes are desired, it may be cost for use of the link, or it may be any other parameter or combination of parameters so desired (Mosher, 1963, 70). 

‘Impedance’ was used without definition in an early Bureau of Public Roads report on the trip distribution problem. In defining travel time factors, the authors stated: ‘These factors are a measure of the impedance to interzonal travel due to the spatial separation between zones’ (US DoC, 1963a, III-4). In its report on trip distribution programs, Peat, Marwick, Livingston & Co. (1967, 30) stated: ‘the contents of the skim trees supplied by the user could reflect some other measures of impedance than time alone’. This report was issued as US DoT (1969a), with the same quote appearing on page 30. 

In the same year, Alan Wilson (1967, 254) wrote in his classic paper on spatial interaction models (section 3.5.1): ‘impedance between i and j, which may be measured as actual distance, as travel time, as cost, or more effectively as some weighted combination of such factors sometimes referred to as a generalized cost’. The indices i and j refer to origin and destination zones. In later publications, ‘impedance’ fell out of use in favour of ‘generalised cost’. 

## 2.4 CHICAGO AREA TRANSPORTATION STUDY

## 2.4.1 Overview and Objectives

Douglas Carroll agreed to accept the challenge of leading an even more ambitious study of the Chicago area in 1955. He recruited Roger Creighton, also a city planning graduate of Harvard University’s School of Design, to be assistant director for research and planning. Moving with Carroll to Chicago were Wilson Campbell [1925–2007], a transportation engineer, and John Hamburg [1928–2000], an urban sociologist.<sup>8</sup>An early description indicated the study was to last three years, with a budget of $2.35 million. The home interview survey, truck–taxi survey and other inventories of land use and transportation facilities were initiated in 1956. Nearly 50 000 home interviews, 7000 truck interviews and 73 000 roadside vehicle interviews were completed. 

Although DMATS established the general concept and approach to urban transportation studies, the Chicago Area Transportation Study (CATS) devised and tested several innovative travel forecasting models. Some were successful and set the research agenda for several years. Others were less useful, and are long since forgotten. As with DMATS, data processing was a key component, as travel forecasting moved from electromechanical accounting machines to the first generation of mainframe computers. 

The purpose and objectives of the study were stated as: 

The task of the study is to analyze the present travel behavior, to forecast what the future requirements of the metropolitan region will be and, on the basis of this information, to devise a long range plan for needed highways and for mass transportation facilities. . . . In summary, the Study has two goals – first, to prepare a transportation plan and second, to provide the basic understanding and facts needed for continuing review and appraisal of the plan by responsible public officials. The plan to be purposeful and to represent the needs of the people, must have an objective. Stated formally, this is to maximize the ease of travel within the urban region, subject to the constraints of limited income, related effects on land use and development patterns, and a most probable estimate of future size and character of the region (CATS, 1959, 1–2). 

The study was extensively documented and widely disseminated as an example of how to perform an urban transportation study. Its threevolume report, Survey Findings, Data Projections and Transportation Plan, became an ad hoc textbook (CATS, 1959, 1960, 1962). For those requiring more details, an extensive set of working papers and manuals was produced, together with a serial publication, C.A.T.S. Research News. Within a decade of the completion of the study, Roger Creighton (1970) described the philosophy, concepts and techniques employed in the Chicago area study in Urban Transportation Planning. 

The study design strongly reflects the methods of DMATS with regard to developing relationships between land use and travel activities (trip generation), prediction of future interchanges of travel between zones (trip distribution), and choice of routes in a congested road network (traffic assignment). Although public transport systems were mentioned, the study description focused on planning for roads. A brief description of the electrical accounting machines and a ‘medium-speed, magnetic-tape, electronic computer’ conveyed the strong orientation of the study towards data processing and computation. A plan to build a cathode ray tube device, later dubbed the Cartographatron, for displaying desire lines of travel and related data was also described. 

Not found in this early description are several technical innovations of the study listed below. In addition, the study innovated with regard to regional economic and demographic forecasts (Hoch, 1959). The threevolume study report is relatively non-technical. In presenting the key technical innovations, such as the opportunities model and traffic assignment, the exposition was more detailed and analytical. CATS followed the basic DMATS outline, but embarked upon several major innovations. Regarding travel forecasts, these innovations included: 

1. forecasts of land use and the associated trip origins, destinations and car ownership patterns in the absence of a land use plan; all forecasts were prepared for a typical 24-hour weekday in 1980; 

2. allocation of trip origins to modes and destinations to modes; 

3. formulation and application of the intervening opportunities model for car trip distribution; 

4. formulation of a tree-by-tree assignment method for car traffic assignment; 

5. integration of the trip distribution and traffic assignment models into a single solution procedure. 

## 2.4.2 Land Use, Trip Generation and Mode Split

Unlike DMATS, there was no land use plan for the Chicago area to serve as the basis for forecasting future travel. Therefore, the study made a detailed forecast of future land use for 1980 as a basis for forecasting person trip origins and destinations. An inventory of developed land was compiled for 1956. Land requirements for total development by land use type in 1980 were determined from a regional forecast, and allocated to undeveloped land with decreasing densities from the region’s centre. Land unsuitable for urban development, as well as open space, was removed beforehand. The land use allocation procedure was detailed and empirical, and controlled by development density and concepts of competition for the use of land. Six types of developed land were allocated to 582 analysis zones defined on a square mile grid and covering 1237 square miles. 

Based on the forecast of 1980 land uses, and trip rates by land use type derived for 1956, a preliminary forecast of 1980 weekday person trips was prepared. Next, an independent forecast of weekday person trips per household was derived from forecasts of zonal residential density (ratio of dwelling units to residential land use) and zonal car ownership per dwelling unit, averages that vary substantially by zonal location. The latter forecast based on households, being substantially higher than the land use-based forecast, was adopted as the controlling forecast of daily trips internal to the study area. These trips were then allocated to the six land use types and distributed to zones. In summary, total weekday travel in the region was based on car ownership and residential density at the zonal level, and distributed to zones based on the land use forecast. External trips to and from the study area were forecast, amounting to nearly onequarter of internal trips. Truck trips were forecast by land use type. 

Having established the number of trips originating and terminating in each zone by land use type at the origin and destination, a portion of al trips was allocated to two types of public transport: trips beginning or ending in the central area, and local trips. For public transport trips to/ from the central area, the opposite trip ends were allocated to outlying areas according to the distance relationship observed in 1956 travel and the land use forecast. The number of public transport trips arriving at the central area per day in 1980 was assumed to equal the number estimated for 1956. 

Local public transport trips were determined as a proportion of total person trips at the origin and destination based on the observed use of public transport in 1956. In the case of trips from or to home, car ownership rates were considered in this allocation. For the Chicago study area, the number of local public transport trips was forecast to be 2 per cent higher in 1980 than in 1956, which was considered to be optimistic in view of substantial decreases in bus travel since 1945. The modal split allocation method devised by CATS sparked considerable discussion. The method was criticised for insufficiently accounting for the time and monetary cost of travel by public transport as compared with car (Stopher and Meyburg, 1975, 188; section 2.5.4). 

## 2.4.3 Trip Distribution

CATS departed substantially from DMATS with regard to forecasting interzonal travel. DMATS had both applied the growth factor method and experimented with the gravity model. The new approach adopted by CATS was one of several important contributions of Morton Schneider [1928–1993], who had studied physics at the University of Chicago (Black, 1990, 35). Papers by Schneider (1959, 1960) provide insights into his enigmatic personality; he was clearly talented and able to exploit the early mainframe computers. 

Morton Schneider’s contribution to trip distribution was the ‘intervening opportunities model’ (CATS, 1960, 81–86, 111).<sup>9</sup> The attraction of Schneider’s model was its simplicity and elegance. The model rested on two basic assumptions: trips prefer to remain as short as possible; a destination opportunity has a fixed probability of being accepted, if considered. The first assumption was the basis for ordering the destination opportunities for a given origin from nearest to farthest based on travel time or generalised cost. Since the probability of acceptance of each opportunity is small, the originating trips are distributed over the entire range of destinations, the extent of their dispersion being determined by a fixed probability. One should realise there was great scepticism at that time concerning the gravity model, which was regarded as an empirical regularity without theoretical basis, an attitude that changed substantially over the next ten years (section 3.5). 

Schneider (1960, 136) discussed two shortcomings of his model: first, since trips are distributed independently by origin, the total number of trips arriving at destinations from all origins does not sum to the total destinations; second, there is a ‘distinct difficulty in obtaining parameters for future or unknown situations’. The first shortcoming was also attributed to early gravity models (section 2.5.3). As became clearer by the late 1960s, trip tables can be ‘balanced’ to sum to specified numbers of destinations as well as origins (Wilson, 1967; section 3.5). That this aspect was not understood in the late 1950s may be partly attributed to computers being too small to perform such balancing calculations readily. Schneider’s point about estimating parameter values for the future, of course, is a shortcoming of all such models. 

The intervening opportunities model was applied separately to car and public transport trip origins and destinations, as allocated by the modal split procedure. For these applications, trips were divided into three classes: short residential, long residential and non-residential (Pyers, 1966, 74; Ruiter, 1967, 3). Trips in the two residential classes began at home and ended at work or other non-residential destinations. Short residential trips were effectively trips that ended within the zone of origin. Non-residential trips began at work and other activities, and ended at home, with distinctions made for central area versus non-central area locations of both origins and destinations. How trips were allocated into short and long residential was not described. The probability of an opportunity being accepted was different for each class, and effectively calibrated with an assumed trip length frequency distribution. 

The study carefully analysed the empirical frequency distribution of car driver trip lengths as a basis for calibrating the model. Hence, the model was seen as a means for distributing trips with respect to an exogenously determined forecast of vehicle-miles of travel (VMT), as contrasted with forecasting total VMT. Travel time was the basis for ordering destination opportunities, although travel distance, time and costs were also considered (CATS, 1960, 83). No terminology such as travel resistance, impedance or generalised cost was used. 

The intervening opportunities model garnered considerable support during the 1960s. Its theoretical basis was attractive to academics, and its operational features were considered positively by practitioners; Martin et al (1961, 150) offered a contemporary account of its advantages over the gravity model: its basic assumption is closer to the basic reasons for interzonal travel; the model is, computationally convenient, independent of zonal or regional boundaries, and requires no special adjustments to fit the model to data. Comparisons showed better accuracy and reliability than for the gravity model. Its disadvantages were described as: loss of simplicity and ease of application by inexperienced personnel, cost of obtaining necessary input data and difficulty of determining parameter values. 

Kevin Heanue and Clyde Pyers (1966, 36) concluded on the basis of calibration studies that the opportunities model and gravity model had ‘about equal reliability and utility in simulating the 1948 and 1955 trip distribution for Washington, DC’. The model was incorporated into the computer package of the Bureau of Public Roads (BPR) (section 2.5.3). Except for its use by CATS to 2000, however, the intervening opportunities model generally fell into disuse after the 1960s. 

## 2.4.4 Traffic Assignment

The coincidence of three essential factors brought about the major advance of CATS over DMATS with regard to traffic assignment: (a) solution of the shortest route problem (Moore, 1957); (b) availability of first generation mainframe computers; (c) the insights and computing skills of Morton Schneider. Edward Moore [1925–2003] was a mathematician working at Bell Laboratories in the 1950s.<sup>10</sup> He devised a label-correcting algorithm, in which ‘labels’ are initially assigned to each node, and then corrected such that each label gives the shortest distance from the origin to the node when the tree is complete. Whiting and Hillier (1960) proposed a label-setting algorithm; these labels denote the shortest distance from the origin, but are determined in order from the origin.<sup>11</sup> The novel procedure implemented for road and transit assignment was described in CATS (1960, 104–110). 

Douglas Carroll and his team, like their counterparts at BPR, approached traffic assignment as a somewhat mechanical procedure for placing origin– destination flows on to links of a road network. Evidently, they were unaware of the concept of user equilibrium described by Wardrop (1952), and they were not aware that Beckmann et al (1956) had formulated an aggregate demand model and user-equilibrium flows in a road network (section 7.3.2).<sup>12</sup> Abraham Charnes, however, had independently formulated a fixed demand user-equilibrium model, and worked with CATS on solving a test problem (Charnes and Cooper, 1961).<sup>13</sup>However, like others of that period, he was unsuccessful in devising a practical solution algorithm (see section 7.3.4 for biographical details about Charnes). 

Creighton (1970, 248–254) described these developments as ‘the story of a breakthrough’; additional details were given by Carroll (1959). As Carroll recognised that a capability to finding shortest routes through a network was crucial to moving traffic assignment from a cumbersome hand accounting procedure to a computer-based method, a contract was given to Armour Research Foundation, an independent research institute in Chicago. The researchers identified the shortest route algorithm of Moore (1957), and began applying it to a small test problem. Based on Armour’s investigation, Schneider wrote a computer program capable of solving such problems for CATS’s 582-zone, 2500-link road network. 

Later, Schneider and Carroll recognised that link capacities needed to be taken into account in the calculation of shortest routes, leading to the creation of the so-called capacity restraint method to modify the results to take account of congestion. Solving the shortest route problem was only the first of three tools needed to find the route and link flows such that, for each origin–destination (O-D) pair, the flows were on routes of equal and minimal travel costs, as Wardrop (1952) had stated in his first criterion. Also required was a way to load the O-D flows on to the network, which Schneider devised, and a way to average successive assignments in order to move towards the desired equilibrium. 

From the description of the traffic assignment procedure in CATS (1960, 104–110), one may grasp how the trip distribution and assignment problem was solved in an integrated manner: 

1. for each origin zone, find shortest route travel times from each origin zone to all destination zones, assuming zero-volume link travel times; 

2. use these shortest route travel times to order the destination opportunities from nearest to farthest; 

3. apply the intervening opportunities model to compute the origin– destination flows from that origin to each destination; 

4. load these flows on to the links of the subnetwork constituting each shortest route. 

Following the completion of this procedure for all origin zones, and storing the origin–destination trip table determined by this process, perform a second capacity restraint assignment as follows: 

1. choose an origin zone at random; 

2. update link travel times based on route and link flows assigned so far; 

3. solve the shortest route problem for that origin; 

4. allocate the flow for each O-D pair previously found to the shortest routes emanating from that origin, and return to step 1; continue until all origin zones are processed. 

The travel time function for performing step 2, updating the link travel time, was not given in the CATS final report. The procedure was to multiply the zero-volume link travel time by a factor of 2 raised to the power of the volume-to-capacity ratio.<sup>14</sup> The source of this function is unknown, but presumably it was specified by Schneider. The function differs substantially from the BPR function (section 2.5.5). For example, if volume equals capacity, the zero-volume time is doubled, whereas for the BPR function it is increased by 15 per cent. 

This assignment procedure was later dubbed ‘tree-by-tree incremental assignment’, since each shortest route tree was loaded on to the network after the link times were updated. The procedure was solved twice for each origin zone, once to compute the trip table, and a second time to perform the congested assignment. In contrast, in iterative assignment and another form of incremental assignment, the set of shortest route trees was solved several times (sections 2.5.5, 2.5.6). Hence, the tree-by-tree assignment procedure was considered to provide a reasonable approximation to the solution of the congested assignment problem. Only one route was used for each origin–destination zone pair in this solution, in contrast to the general situation of possibly many used routes at equilibrium. Since heavily loaded links were avoided, the flows were spread over alternative links, perhaps in a rough approximation of a user-equilibrium solution. Just how rough was not determined, since it was unknown at that time how to assess the quality of an assignment in terms of user equilibrium (section 7.4.2.4). 

The travel forecasting procedure devised by CATS considered the 24- hour weekday as a single period. That is, travel for all purposes during the 24 hours was assigned to the road network. The daily road capacities during those 24 hours were based on the percentage of daily volume occurring in the highest one-hour period, which was 11 per cent. To account for the fact that 60 per cent of the flow occurred in the peak direction, the percentage was adjusted to 13.2 per cent. Hence, daily capacity was set equal to hourly capacity divided by 0.132 (Haikalis and Joseph, 1961, 45). 

In reality, of course, traffic is not distributed uniformly over the 24-hour day. Therefore, a procedure was developed for reducing the estimated total travel delay according to the empirically observed relationship between the hourly rank of the traffic flow and the proportion of daily traffic during that hour. To our knowledge, this procedure is unique, and was not applied in subsequent studies. Using a rank–size relationship, ‘the integration of each hour’s expected delay over that hour’s fraction of the daily flow provided a weighted average daily delay’ (Haikalis and Joseph, 1961, 48). 

At the time of its implementation in the late 1950s, the combined trip distribution and traffic assignment procedure implemented by Schneider was a very substantial advance. An O-D trip table could be computed and assigned to represent a congested network with the computation of shortest route trees equal in number to twice the number of zones. As compared with the highly cumbersome procedure used by DMATS just a few years earlier, now several alternative roadway plans could be evaluated. 

## 2.4.5 Computational Aspects

The Chicago study coincided with the availability of first generation mainframe computers, in particular the IBM 704. The IBM 704 computer was the first mass-produced computer with core memory and floating point arithmetic, shown in Figure 2.2(b).<sup>15</sup> The IBM 704 installation available to CATS was in Cincinnati, Ohio. To solve the intervening opportunities and traffic assignment models, Morton Schneider travelled to Cincinnati and worked through the weekend, debugging and running his programs. When the program finally worked after months of effort, he related that one unused word of memory remained.16 

According to Carroll (1959), an assignment to the arterial and expressway network required about 11 hours, 4 hours for the zero-flow assignment and 7 hours for the capacity restraint assignment (CATS, 1960, 108). The inputs consisted of 5225 data cards representing the existing network and 630 cards representing zonal trip origins and destinations. Computation of one copy, consisting of the shortest routes from one origin, calculation and assignment of trips, and loading of trips on to links, required about one minute and computing costs of $10. Carroll estimated that to perform these calculations by hand would require five person-weeks and cost $450. 

A second technological innovation of CATS was the invention and application of the Cartographatron. Its development also marked the end of the transition from origin–destination surveys portrayed as desire lines to forecasting of travel on road and transit networks. DMATS began that transition with the use of electromechanical accounting machines to assign origin–destination flows to a road network. CATS completed the transition with the heuristic solution of the trip distribution and assignment problem. The development of the Cartographatron was a parallel effort. 

Douglas Carroll was a visionary planner; ‘he firmly believed in the rational planning process and thought that planning should be made as scientific as possible’ (Black, 1990, 28). Carroll understood the potential of the human eye and brain to process and analyse information. Perhaps based on the new technology of that day, black-and-white television, he imagined that data representing trips could be displayed on a cathode ray tube and captured on film for analysis and representation of observed and desired travel patterns. Such a display was the essence of the Cartographatron, which displayed trips recorded on magnetic tape as streaks of light on a tube to be captured on film. Photographs produced by the device graced the covers of the three volumes of the CATS reports; the device was described in Carroll and Jones (1960). Figure 2.4 shows an example of a map produced with the Cartographatron. 

According to Carroll, the Cartographatron performed its intended tasks well and inexpensively. The results extensively illustrated the CATS reports, perhaps adding to their credibility. In the end, these photos lacked the specificity of the computed vehicle-hours and vehicle-miles of travel for road network alternative plans based on the newly developed traffic assignment method. Roger Creighton later remarked: ‘the Cartographatron was a brilliant success. No longer were we slaves to the notion that all travel goes to the central business district. . . . Travel turned out to be much more evenly spread, more scattered in direction. . . . the complexity was enormous; our ignorance had been very great’ (Creighton, 1970, 36). 

Perhaps the views of these pioneers should be accepted at face value. However, CATS was the only transportation study to use the device.<sup>17</sup> Maybe once these lessons were learned they did not need to be repeated elsewhere. Moreover, the Cartographatron was not used to analyse the forecasts of travel for 1980, but was restricted only to the analysis of the 1956 origin–destination survey. The device was remarkable in its time, but its usefulness was limited, as abilities to analyse and forecast the effects of travel on road network congestion rapidly improved. One may also wonder whether Carroll had higher aspirations for this machine. Irving Hoch recalled that the original hope for the Cartographatron was to develop recommendations for locations of expressways, including estimates of roadway usage.<sup>18</sup> 

## 2.4.6 Lessons from the Chicago Area Study

For summarising the advances contributed by CATS, a contemporary review such as was provided by Carroll and Bevis (1957) is unavailable. Creighton (1970) gave a general policy assessment of strengths 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/38754b84-3c6e-4874-b89a-d84630ad82f8/d4a367242983268e9ead67417f1a1c3efecc335b8bd936ea46757dffce0e3ff7.jpg)



Source: CATS (1959, 46).


Figure 2.4 Desire lines of internal person trips in the Chicago area and weaknesses, but no detailed technical critique. Martin et al (1961) recorded the state of practice, but did not offer a critical assessment. The advances of CATS may be summarised as follows: 

1. A land use forecast was prepared based on detailed inventories and past trends. 

2. Detailed trip rates by land use and zonal location were prepared and used to make forecasts of total travel based on residential density and car ownership. 

3. Procedures for allocating portions of trip origins and destinations to transit were devised, taking into account the important role of the central area in determining mode choice. 

4. A new method for distributing three classes of trips from origins to destinations by mode was formulated from simple propositions, implemented and tested. 

5. A new traffic assignment method based on shortest routes was devised and implemented successfully. 

6. The trip distribution and assignment methods were implemented on a mainframe computer, and combined to solve these two steps logically into a single procedure. 

The shortcomings of CATS from the perspective of the early 1960s included the following: 

1. CATS was criticised by planners for not being based on a land use  plan; however, an effort based on land use – transportation alternatives followed in the mid-1960s (Boyce et al, 1970) (section 2.7.3). 

2. Despite its success in improving the theoretical basis for modelling origin–destination travel, the study did not contribute to an understanding of the theory of traffic assignment; the mathematical formulation of the traffic assignment method, which is related to the method utilised by CATS, was evidently not appreciated (Beckmann et al, 1956; Charnes and Cooper, 1961; see also section 7.3). 

3. CATS, as well as others, continued to approach the travel forecasting problem in terms of the 24-hour weekday, rather than the congested peak period; to the authors’ knowledge, the implications of this approach in terms of forecast error were never fully explored. 

Alan Black (1990) described the conceptual approach from a planning theory perspective, and added insightful details about the attitudes and working conditions of the staff. Many technical papers were published during the study period. John McDonald (1988) provided a useful retrospective of the 1980 forecasts. 

The contribution of the completed study to urban travel forecasting practice, and theory, was immense and unprecedented. A prototype procedure with extensive documentation was now available for others to follow. The use of first generation mainframe computers was successfully demonstrated. Drawing on the experience of the Detroit and Chicago area studies, as well as the efforts of the Bureau of Public Roads, the urban transportation planning process could be transferred to large urban areas throughout the country, as mandated by the 1962 Federal-Aid Highway Act (Weiner, 1997, 37–38). 

Before turning to other developments of travel forecasting methods, we briefly consider the fate of the 1980 Chicago area plan. The Chicago study devised an expressway spacing formula and an economic evaluation method to guide the design of the road network.<sup>19</sup> The spacing formula provided a systematic framework for generating alternative plans of increasing density of facilities, to which the travel forecasting models could be applied to gauge their performance in terms of vehicle-miles and vehicle-hours of travel as well as system travel time, operating costs and accident costs. CATS prepared, tested, evaluated and presented six expressway plans. The evaluation of the roadway plan concluded that an extensive system of expressways was efficient and desirable (Haikalis and Joseph, 1961). Perhaps discouraged by the complexity of the method, later transportation studies did not explore this approach further (Creighton, 1970, 283, footnote 3).<sup>20</sup> 

In the final analysis, the plan did not win the support of local and state elected officials. A discussion between Douglas Carroll and Richard J. Daley [1902–1976], the powerful mayor of the City of Chicago from 1955 until his death, was reported in the Chicago Sun-Times, following the release of Volume 3 (CATS, 1962). In proposing the 1980 plan, Carroll stated to the press: 

We have too much traffic to handle on the streets. . . . Our proposal is . . . a carefully designed and spaced system of freeways which leave the surface and go underneath or above the ground. With this kind of system we can function very effectively, leaving little islands of local residential areas and drawing the bulk traffic off to these heavy-duty systems that will carry it below or aboveground. And thus we will provide a workable network of roads and streets. 

## According to Sun-Times reporter Donald Schwartz:

one of Carroll’s main premises is that the city will thin out, being reduced in time to an area of density resembling a suburb. Carroll contends that this is because of personal choice – a desire to live in areas of reduced density. Others say that all-out catering to the auto, through expressway building, would force the change. But wherever the truth lies, Carroll foresees a steady dispersal of the city (Schwartz, 1962, 1). 

Only one expressway (I-355) recommended by the 1980 plan was constructed within the CATS study area in addition to those facilities whose locations were specified in the existing and committed system of 1955.<sup>21</sup> Although Mayor Daley supported the construction of the Crosstown Expressway, even that basic link in the committed system of expressways did not come to fruition. In 1962 when the plan was released, the northwest and west sides of Chicago had been a construction zone for the past six years. Residents were distraught with the dirt, noise and disruption of expressway construction. 

With the benefit of 20–20 hindsight, one wonders what Carroll and his staff were thinking in proposing a grid of expressways with a threemile spacing, enclosing ‘islands of local residential areas’ in the City of Chicago. But then an urban expressway system of the scale being proposed had never been experienced by anyone up to that time. 

## 2.5 BUREAU OF PUBLIC ROADS

## 2.5.1 Overview

Development of travel forecasting methods and associated computer programs was initiated by the Bureau of Public Roads, a long-standing unit of the US Department of Commerce (US DoC), based on the experience with the Detroit and Chicago area studies, and other pioneering efforts in Puerto Rico and Washington, DC.<sup>22</sup> BPR initiated the development of computer programs for factoring survey-based trip tables and solving gravity-type trip distribution models and traffic assignment models, when electronic computers became available for civilian use (Brokke, 1969, 32). 

Glenn Brokke [1912–1992] and W. Lee Mertz [1920–1993]<sup>23</sup> initiated tests of the Fratar and Detroit area methods for factoring a survey trip table for a future forecast year with an IBM 705 computer (Brokke and Mertz, 1958). Somewhat later, programs for calibrating and testing a gravity model were written for the IBM 704 and later modified for the IBM 7090/94 (US DoC, 1963a, ii). Programming for a ‘battery’ of assignment programs for the IBM 704 was initiated in 1958 under contract with the General Electric Computer Department, Phoenix, Arizona (Mertz, 1960b, 1961). ‘This project produced a battery of high-speed computer programs that would assign nondirectional interzonal traffic movements’, including options of using diversion curves or all-or-nothing assignment based on the shortest route algorithm of Moore (1957) (US DoC, 1964, I-3). These programs were extended to permit directional assignments as well as turn penalties and prohibitions. Following the transition to second generation machines, BPR incorporated its major programs into a library of programs. 

These two manuals (US DoC, 1963a, 1964) sought to provide computer programs needed ‘to complete the analytical phase of a comprehensive transportation planning study’ (US DoC, 1963a, ii).<sup>24</sup> No overall statement of objectives for the BPR travel forecasting procedure, however, was described in these manuals. In the following sections, the models and methods that make up the four-step or sequential travel forecasting procedure are reviewed. The dates of the reports and manuals indicate the order of their development, which differ from their description here. 

Section 2.5.8 reviews early studies of urban goods movement undertaken by three transportation studies; subsequent studies are considered in section 8.6. 

## 2.5.2 Trip Generation

In early transportation studies in the US, procedures were devised to forecast the number of trips leaving or entering a zone according to the following definitions: 

1. the number of trips ‘produced’ by a zone, or ‘trip productions’, was defined as the trips originating at and returning to the zone; 

2. the number of trips ‘attracted’ by a zone, or ‘trip attractions’, was defined as the trips arriving at and departing from a zone. 

Both productions and attractions were related by statistical methods to total values or averages of selected zonal characteristics. For trip productions, these variables were typically the number of persons or households, number of cars owned by households and number of employed residents; zonal averages were also used, such as the number of workers per household, mean household income or number of cars per household. Trip attractions were related to floor area, land area or employment in various activity classes (retail, manufacturing, etc.) at the non-home end of the trips (US DoC, 1963a, III-2) (section 8.4.2).<sup>25</sup> In subsequent studies, trips were categorised as home-based and non-home-based. Home-based trips were further divided into classes by purpose: work, shop, school and other. Documentation of these procedures was found only in early transportation study reports, as there was no BPR manual on trip generation before 1967. 

By the early 1960s, academic research and some transportation studies found substantial variations in the rate of trip making among individual households, which were not captured by these zone-based methods. Using data from two home interview studies, Paul Shuldiner identified the most significant variables associated with trip making of individual households as household size, income, and car ownership (Oi and Shuldiner, 1962; Shuldiner, 1962). His research also explored which statistical methods were appropriate for the analysis of such data, concluding that crossclassification methods based on household types were superior to linear regression, which requires assumptions of linearity and continuity of variables, as well as normality of errors, for hypothesis testing. The use of dummy variables to represent classification variables, however, provides another way to combine elements of the regression and cross-classification approaches. 

Forecasting the explanatory variables on which to base travel rates of households posed new challenges, since each variable would need to be forecast for the target year of the study. Forecasting household size and car ownership was a significant challenge. Progress in implementing the household-based category analysis, drawing on the research of Shuldiner, was also being made in the UK (Wootton and Pick, 1967) (section 3.3.1). 

Guidelines for Trip Generation Analysis (US DoT, 1967) and Fleet and Robertson (1968) built upon and incorporated the experience from urban transportation studies. Trip Generation Analysis (US DoT, 1975) provided more specific guidance. Concerning the definition of trip categories and trip generation modelling procedures in the early transportation studies, Stopher and Meyburg noted: 

production and attraction and origin and destination are not synonymous. Briefly, it can be summarized as follows: For a home-based trip, the zone of production is the home end of the trip; while the zone of attraction is the nonhome end of the trip. Thus, a trip from home to work and a trip from work to home will both have a production end which is home and an attraction end which is work. For non-home-based trips, the production end is the origin and the attraction end is the destination (Stopher and Meyburg, 1975, 64). 

## 2.5.3 Trip Distribution

Following the tradition of the earliest urban transportation studies, a future trip table for a study area was estimated by adjusting the sampled table from the survey year to conform to future origin and destination totals. An early approach to this adjustment was proposed by Fratar (1954). Subsequently, additional adjustments were proposed using the newly available electronic computers. Computer programs prepared by the Bureau of Public Roads for adjustment of survey trip tables were not included in BPR’s first trip distribution manual (US DoC, 1963a), but were later included in Peat, Marwick, Livingston & Co. (1967, 3–14) and US DoT (1969a, 3–14). Concurrently with Fratar’s proposal, Alan Voorhees (1955) and Douglas Carroll (1949, 1952, 1955) were exploring the application of the gravity model in forecasting interzonal urban travel. These early studies led to applications by Voorhees (1958), Voorhees and Morris (1959) and Hansen (1962). 

US DoC (1963a, sections I, II) reviews the theory and history of the gravity model, plus a brief description of the intervening opportunities model (Schneider, 1959), as well as the competing opportunities model (Tomazinis, 1962), and proceeds to a description of the model implemented in BPR computer programs. The implementation was highly empirical, incorporating ‘travel time factors’, based on the shortest route travel time, and specific zone-to-zone adjustment factors, known as ‘K-factors’. The BPR gravity model stated that the number of two-way trips produced in an origin zone and attracted to a destination zone,  also known as the number of trip interchanges, is directly proportional to: 

1. the number of trips produced by the origin zone, or two-way trip productions; 

2. the number of trips attracted to the destination zone; 

3. ‘an empirically derived travel-time factor, which expresses the average areawide effect of spatial separation on trip interchange between zones which are a given travel time apart’, also known as ‘friction factors’; 

4. ‘a specific zone-to-zone adjustment factor to allow for the incorporation of the effect on travel patterns of defined social or economic linkages not otherwise accounted for in the gravity model formulation’, also known as K-factors; 

5. a denominator term equal to the sum over all destination zones of the product of the number of trip attractions, the travel time factor and the adjustment factor.<sup>26</sup> 

The denominator term ensured that the sum of the trips from an origin zone to all destination zones equals the origin zone productions. The converse that the sum of the trips to a destination zone over all origins equalled the destination zone attractions was not satisfied by the function. This lack of agreement between the trip sums to a destination zone and the zonal trip attractions was addressed later in the report (US DoC, 1963a, IV-37–39), as noted next. 

An automated adjustment procedure was described as follows: ‘the program adjusts each zonal attraction factor by the ratio of the trip attraction factor to the gravity model results’, that is, the sum of the trip interchanges over all origin zones. Three iterations of this adjustment procedure were recommended. No interpretation of the adjusted trip attraction factors was offered, but the description of this procedure as part of the calibration, or fitting of the function to data, suggests that these adjusted attraction factors were considered to have been ‘calibrated’. These adjustments are equivalent to the imposition of a destination constraint such that the sum of trips to a destination zone from all origins equals the destination zone attractions (section 3.5.1). Unlike the case of the doubly-constrained procedure, the effect of adjusting the attractions in order to invoke the attraction constraints is implicit. 

The calibration of the travel time or friction factors was based upon the frequency distribution of trip lengths. A separate empirical, decreasing function of interzonal travel times was determined for each trip purpose by adjusting an initial guess by the ratio of the observed proportion of trips of a given length to the proportion computed from the model. After a trial function was calculated, the attraction factors were updated before the predicted trip length frequency distribution was compared with the observed distribution. Finally, zone-to-zone adjustment factors (K-factors) were specified by trip purpose and mode to account for poorly fitting results. The report describes in detail how such factors should be specified. 

Although Carroll and Voorhees investigated the empirical values of the negative power of travel time, in the calibration section of the report only empirical factors were presented. Generally, the report is clearly and precisely presented, especially computational details related to computer programs for the IBM 7090. Statistical tests were reported for a small urban area, Sioux Falls, South Dakota. A procedure for converting twoway trips to one-way trips for use in traffic assignment was described (US DoC, 1963a, VI-1–5). A final section described assumptions necessary to use the model and associated programs for forecasting. The authors of the report noted: ‘travel-time factors, as developed from present data, are used for the future time period. Very limited evidence leads to the conclusion that this is a reasonable assumption to make. However, much research work is required on this point before the assumption can be accepted without reservation’ (US DoC, 1963a, VI-4). 

## 2.5.4 Modal Split

The report Modal Split documented the procedures used in nine urban transportation studies between 1955 and 1966 for estimating the proportion of future urban travel by public transport (US DoC, 1966). Early transportation studies, such as Chicago and Pittsburgh, implemented ‘trip-end’ modal split procedures (section 2.4.2). Car ownership, residential density and distance from the central area were the principal explanatory variables. Later, transportation studies for Erie, Puget Sound and Southeastern Wisconsin introduced level-of-service variables at each origin zone to represent the effect of differences in accessibility by car and public transport to other destinations. Diversion curves related the mode share from an origin zone to the ratio of accessibility by car to accessibility by public transport (Hutchinson, 1974, Chapter 3; Stopher and Meyburg, 1975, sections 3.7, 9.5). 

Alternatives to the trip-end modal split procedure were proposed in the early 1960s for two reasons. First, the trip-end procedures proved to be insensitive to changes in public transport service, which was attributed to the ‘gross accessibility measures used’ (Stopher and Meyburg, 1975, 188). Second, federal funding for public transport improvements at that time required an appraisal of changes in transit levels-of-service between specific locations. Hence, alternative methods for modal split analysis were designed to improve the responsiveness of the models to proposed improvements in public transport systems. 

By having the modal split step follow the distribution stage, known as trip-interchange modal split models, modal choice could be directly related to the modal travel times and costs for each pair of zones. In contrast to trip-end models, which tended to emphasise the identification of captive users of public transport, the trip-interchange structure emphasised choices facing travellers between pairs of zones. 

Hill and von Cube (1963) prepared modal split studies for Washington, Toronto and Philadelphia, which ‘represents the first major attempt to hypothesize the decision process that may underlie modal split and to incorporate this process into a predictive model’ (Stopher and Meyburg, 1975, 189). Their procedure expressed the modal split between car and public transport for zonal interchange in terms of: 

1. relative overall travel time of the modes expressed as a ratio; 

2. relative overall travel cost of the modes expressed as a ratio with four levels; 

3. relative out-of-vehicle time of the modes expressed as a ratio with four levels; 

4. income of the worker with five levels; 

5. trip purpose – work or non-work. 

Based on these variables, 80 diversion curves were specified for work trips. Data were analysed both separately and in combination for samples from Washington, Toronto and Philadelphia to assess transferability and extend the variable ranges. 

While a rigorous behavioural basis for the location of modal split in the travel forecasting procedure, either before or after trip distribution, was not established during this period, the justification for different structures seemed to reflect travel decisions. The language of choice and the conditionality of decisions slipped into the discussion. Those researching the individual models, and particularly modal split, were often conscious of the broader context of their investigations and the behavioural ambiguities of the structure. In a paper summarising the findings of DoC (1966), Edward Weiner wrote: ‘the most actively debated issue in modal split is whether an urban area should use a trip-end or trip-interchange model’ (Weiner, 1969, 25). 

## 2.5.5 Traffic Assignment

Well before BPR released its manual, transportation planners had agreed that link capacities needed to be considered in the assignment of traffic to a road network. The earlier reliance on unconstrained assignments, called ‘all-or-nothing assignment’, was not practical. The Traffic Assignment Manual documented ‘in detail the complete process of traffic assignment, as it was then defined’ (US DoC, 1964, i). As with the gravity model manual, the presentation is detailed and precise, including useful historical background: ‘Traffic assignment may be defined as the process of allocating a given set of trip interchanges to a specific transportation system’ (US DoC, 1964, I-1). In the manual one finds little discussion of ‘route choice’; rather, assignment was viewed as a mechanical procedure for placing trips on to the network. Chapter V – Theory, however, did state: ‘it is assumed that the vehicle operator desires to use the “easiest” route between his origin and destination’ (US DoC, 1964, V-1). 

A method of assignment that considers link capacity was described in the 1964 manual as ‘iterative capacity restraint’. This method consisted of performing a sequence of all-or-nothing assignments in which the link travel speeds were updated after each all-or-nothing assignment of the trip table. Iterative capacity restraint assignment was described in more detail in Chapter V. What has became known as the BPR volume-delay or link performance function was stated there, relating ‘travel time at the assigned 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/38754b84-3c6e-4874-b89a-d84630ad82f8/47448c5b57a608f5c119bc6189e71e628dd2a1142053cfea0babc78061f3d714.jpg)



Note: Speed 5 link length/T (miles/hour).



Source: US DoC (1964, V-20).


Figure 2.5 Relative link speed versus ratio of assigned link volume to practical capacity 

volume’ to a ‘base travel time’ defined to be the travel time at practical capacity times the factor 0.87, which is the reciprocal of 1.15. Therefore, if the assigned volume equalled the link’s practical capacity, the travel time function equalled the base travel time. The basis for the parameter value was not described. Hence, as it was originally defined, the BPR function was related to the travel time at practical capacity, and not to zero-volume, or free-flow, travel time. Practical capacity was defined as the maximum flow that can be achieved at a specified level-of-service.<sup>27</sup> As shown in Figure 2.5, the BPR function is expressed as the ratio of the speed at the assigned volume to the speed at practical capacity; its property that travel time increases without limit as volume increases was not stated. 

Following the completion of an all-or-nothing assignment of the entire trip table, the link ‘parameters’ were adjusted, and a second all-or-nothing assignment was performed. The parameter adjustment was to the link speed, not to the link travel time. Moreover, to ‘moderate the full effect of the change’ a speed for the next iteration was obtained by averaging the new speed and the former speed, thereby eliminating ‘large oscillations of loads on links from one iteration to the next. . . . This process may be continued for as many iterations as desired. However, experience showed that after four iterations the accuracy of the assignments does not improve appreciably’ (US DoC, 1964, V-21). The term ‘link loads’ was sometimes used to refer to link volumes. A subsequent manual reported that ‘reasonable assignments are obtained by using the average of four loadings’ (US DoT, 1973a, 36). 

One forgotten aspect of these early trip distribution and traffic assignment methods is that most calculations were performed in integer arithmetic. Trips, link volumes, capacities and speeds were all integers. If averaging was performed, the result was rounded or truncated to an integer, further restricting the ability of the procedure to converge to a stable solution. 

## 2.5.6 Alternative Traffic Assignment Methods

The iterative capacity restraint method of traffic assignment implemented by BPR was one way of solving this problem during the 1960s. Robert Smock (1962, 1963) proposed a different way of averaging link volumes from a sequence of all-or-nothing assignments for the continuing Detroit area study. Following an initial all-or-nothing assignment to shortest routes based on free-flow link travel times, and a second assignment to shortest routes based on the travel times corresponding to the link volumes from the first assignment, he averaged the link volumes from these two assignments with equal weights (0.5/0.5). After the travel times were updated for the averaged volumes, a third all-or-nothing assignment was performed. This third assignment was averaged together with the previously averaged results. Precisely how the volumes were averaged is unclear (Smock, 1963, 15).<sup>28</sup> If each all-or-nothing assignment had equal weight in the final averaged result, then Smock’s procedure would correspond to the method of successive averages (MSA). Michael Patriksson (1994, 23) stated that Smock may have been unknowingly responsible ‘for what is probably the first adaptation of a convergent traffic assignment algorithm'. Smock used the term convergence' to describe the behaviour of his method, as is now common (see sections 7.4.2.4 and 7.4.3.2).29 

Traffic Research Corporation implemented a method incorporating the trip distribution and assignment models in a complex cyclic process (Irwin and von Cube, 1962). The assignment method consisted of all-or-nothing assignments of an updated trip table to shortest routes. No averaging of link volumes is apparent from their paper. 

For CATS, Morton Schneider had implemented and applied a type of incremental assignment, later termed quantal loading (Patriksson, 1994, 21) (section 2.4.4). Brian Martin proposed another ‘incremental assignment’ method (Martin and Manheim, 1965). Martin may have been the first to use that term; however, his method bore only a general resemblance to later usage. 

A different incremental assignment procedure was implemented in the assignment programs offered by the Control Data Corporation (CDC) (1965) in its Transportation Planning System for the Control Data 3600 Computer or TRANPLAN (section 10.3.2). In this method, the trip table was divided into several increments, possibly but not necessarily of the same proportion of the entire table. The first increment was assigned to shortest routes defined on free-flow travel times. The assigned volumes on each link were then scaled up to represent the full volume, as if the entire trip table had been assigned. New shortest routes were computed for these volumes, and the second increment assigned to them. Next, the link volumes from the two increments were combined according to the proportion of each increment, and again the volumes were scaled up to represent the entire trip table, the link times were updated, and new shortest routes were re-computed. This procedure was repeated until all increments were assigned and averaged together. Although this procedure was described in US DoT (1973a, 38) and in CDC (1965, 147), these descriptions differed from the typical descriptions of ‘incremental loading’ (Van Vliet, 1976, 146; Ortúzar and Willumsen, 2011, 369) in which a sequence of increments of the trip table were assigned with the link volumes, travel times and shortest routes being updated after each increment. 

CDC’s averaging of volumes according to their proportions, and the scaling of those volumes to the full trip table, may correspond to the method of successive averages described above, and therefore may also be a convergent assignment method. The originator of this scaling procedure is unknown. Presumably, the rescaling of the link volumes was intuitively more plausible than using the partially assigned volumes directly in the volume-delay function. No tests of this variant of incremental assignment have been found, and seem unlikely to have been performed, since no meaningful measures for assessing the quality of an assignment were known at that time (section 7.4.2.4). 

As noted in section 2.5.5, traffic assignment computations were performed in integer arithmetic. Therefore, in devising the increments, the values of each increment had to be determined so that the sum over all increments would equal the integer values in the original trip table. In assigning a large trip table even in the 1960s, a typical origin–destination flow was a single digit number, and possibly one vehicle per day. In this case, the cells with values equal to one were typically assigned in the middle increment.<sup>30</sup> 

Drawing upon his experience with the development of computer programs for transit network problems in the late 1960s, as described in sections 2.6 and 10.3, Robert Dial (1971) proposed a method for more widely distributing origin–destination flows over multiple routes using an exponential function of fixed route travel times.<sup>31</sup> Dial was initially motivated by a desire to provide a better method than all-or-nothing assignment to fixed travel time routes, and not by the shortcomings of the capacity restraint assignment method. His STOCH method was sometimes used by practitioners, however, as an alternative to the iterative capacity restraint method. Later, STOCH was understood to be a stochastic network loading method, given fixed link costs, in the same sense that all-or-nothing assignment is a deterministic loading method of a trip table to shortest fixed cost routes (Patriksson, 1994, 148). Dial’s method depended upon a definition of ‘efficient’ routes. One example of an efficient route is a route that does not backtrack: ‘As it progresses from node to node it always gets further from the origin and closer to the destination’ (Dial, 1971, 89). 

## 2.5.7 Application and Experience

BPR offered no advice concerning the solution of the sequence of models described in the four manuals issued between 1963 and 1967. In Urban Transportation Planning, General Information (US DoT, 1972a, I-5), these models were described together for the first time, and their relationship was depicted diagrammatically in Figure I-2, reproduced as Figure 2.6. Modal split was not shown in this figure. Solving the trip distribution and traffic assignment steps with feedback was not addressed in the report. ‘Feedback’ is denoted in the figure, but in the context of land use – transportation network interaction, and not travel forecasting. 

As the agency charged with oversight of road planning, design standards and road financing, BPR was at the forefront of the development of urban travel forecasting methods, and the use of mainframe computers. The staff charged with these responsibilities acquired their skills on the job to prepare for this rapidly developing field. Highway engineers and mathematics majors were thrust into model development and the programming of the latest mainframe computers. They eagerly applied research findings, such as Moore’s algorithm for finding shortest routes through a network, although they were unschooled in the optimisation methods that advanced rapidly from the late 1940s (section 7.2.2). They did their best to apply common sense and experience gained on the job. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/38754b84-3c6e-4874-b89a-d84630ad82f8/61b7ac9575cc56d249556d59107f636629bb911a7ed00929512029738e433e43.jpg)



Source: Redrawn from US DoT (1972a, I-5).


Figure 2.6 Elements of the urban travel forecasting process 

The principal accomplishments of this era pertaining to travel forecasting may be summarised as follows: 

1. Using data from the Washington, DC area home interview surveys, trip distribution models for 1948 and 1955 were implemented on an IBM mainframe. 

2. Road traffic assignment methods were implemented on a mainframe based on the shortest route method. Procedures for solving a capacity restraint method were experimental. Empirical travel time-volume functions, later known as volume-delay functions, were devised based on little data, but continue in use to this day. 

3. Over a period of years, computer programs, later called ‘packages’ or ‘batteries’, for solving trip distribution and traffic assignment models were developed, documented and distributed to urban transportation studies and computer service bureaus. These programs became the mainstay of urban travel forecasting methods during the 1960s. 

4. Procedures for trip generation and modal split were also reviewed and documented in support of urban transportation studies. 

## 2.5.8 Urban Goods Movement

BPR reports of this period did not consider truck traffic. Early urban transportation studies did survey truck use, and analysis was performed with these data. These early studies are briefly described here. For developments from 1970 onwards, see section 8.6. 

The Detroit and Chicago studies each inventoried truck movements. Assignment of future truck traffic was not described in the final report of the Detroit study. The Chicago study explored the relation of truck originations and terminations to land use. Origin–destination flows of trucks were forecast and assigned in the 1980 plan evaluations (CATS, 1960, 48). 

Magne Helvig (1964), a graduate student at the University of Chicago, performed a study of Chicago’s external truck movements with data from the Chicago Area Transportation Study. Helvig investigated the relationship between the number of trucks entering the Chicago study area in relation to the size of the shipment origin (population, employment) and distance. He estimated the parameter value of a simple gravity model defined on a power function of distance at three geographic scales: states; counties in the four states surrounding the Chicago study area; and municipalities in the larger Chicago region. This study is probably the first detailed application of the gravity model to interregional truck flows in a metropolitan area. Helvig’s study followed the completion of the 1980 transportation plan for the Chicago area.<sup>32</sup> 

Donald Hill (1965b) proposed a ‘truck interactance’ model based on the gravity hypothesis for implementation in the Toronto, Canada region. Hill hypothesised that interzonal truck flows were proportional to the number of truck trips originating and terminating at zones and to the negative exponential function of the interzonal travel time or distance, giving no reason for using the negative exponential function and no references except Helvig (1964). Although the use of the negative exponential function in such a model was not typical, Hill offered no explanation for its choice.<sup>33</sup> Hill estimated his model with Toronto data, and determined parameter values of the exponential function for three classes of trucks. His study is probably the first implementation of a spatial interaction model of truck flows. 

The first transportation study to undertake a comprehensive inventory of freight movements was the Tri-State Transportation Commission for the New York region (Wood, 1967; Wood and Leighton, 1969). Extensive inventories were performed for trucking, but no forecasts were prepared by 1970. 

## 2.6 URBAN MASS TRANSIT PLANNING PROJECT

The urban transportation studies initiated in the 1950s were strongly orientated towards planning for road systems. The Detroit area travel forecasts ignored public transport altogether. Travel forecasting for public transport was later added to the original study design at CATS. The impetus for urban transportation planning, after all, was the planning of urban sections of the National System of Interstate and Defense Highways. Even so, the Federal-Aid Highway Act of 1962 required that the planning process be comprehensive. BPR defined and interpreted section 134 of the 1962 Act as follows: 

The comprehensive character of the planning process requires that the economic, population, and land use elements be included; that estimates be made of the future demands for all modes of transportation both public and private for persons and goods: that terminal and transfer facilities and traffic control systems be included in the inventories and analyses; and, that the entire area within which the forces of development are interrelated and which is expected to be urbanised within the forecast period be included (US DoC, 1963b). 

Responsibility for planning of urban public transit systems was assigned to the US Department of Housing and Urban Development (US HUD) by the Urban Mass Transportation Act of 1964, as amended in 1966 (Weiner, 1997, Chapters 4, 5). The 1966 amendments provided for a technical studies programme, including federal assistance for planning, engineering and designing of urban public transit projects. 

Charles Graves, a HUD land use planner from the Puget Sound Regional Transportation Study, Seattle, proposed the development of a program battery for public transport systems planning comparable to BPR’s highway program battery. Since HUD had no technical staff to develop such a capability, a contract for the Urban Mass Transit Planning Project was awarded to Alan M. Voorhees and Associates for development of computer programs for modal split, transit assignment and related functions. 

Walter Hansen headed the HUD project; Richard Bunyan and Robert Dial<sup>34</sup> were the initial programming staff. Bunyan prepared a process diagram, mimicking BPR’s highway package, which consisted of seven modules (Dial and Bunyan, 1968): ‘network description; transit path builder; O-D travel times; modal split model calibration; modal split model application; load trip table; and report generator’. Several of these programs, especially the transit path builder and the modal split model, were highly innovative for that time (US HUD, 1966, 1967, 1968). Independently, John Wootton was developing similar methods for analysing public transport networks in the UK; see sections 3.6.1 and 10.3.1.<sup>35</sup> 

The HUD transit battery provided computer programs for modal split forecasting and transit network planning that were compatible with the  BPR highway program battery. These in turn became the basis for the Urban Transportation Planning System (UTPS) developed during the 1970s (section 10.3.3). 

The US Department of Transportation (US DoT) was established in 1966. In 1968, an agreement between US DoT and US HUD established the Urban Mass Transportation Administration (UMTA) and transferred responsibility for many public transport programmes to US DoT. After that time, further responsibility for development of travel forecasting computer programs became the joint responsibility of the Urban Mass Transportation Administration and the Federal Highway Administration. 

## 2.7 LAND USE – TRANSPORTATION STUDIES

## 2.7.1 Overview

The successes of the Detroit and Chicago area studies, as well as BPR and US HUD, in creating models and computer programs for travel forecasting stimulated other large metropolitan areas to initiate studies. Moreover, some metropolitan areas were forming regional planning commissions or councils with broader scopes than transportation planning, including land use, sewer and water utilities, open space, housing and employment. 

Urban planners argued that transportation planning should not be undertaken in isolation, without coordinated planning for urban activities (land use) to be served by the new highway and public transport systems. As financial support for land use planning activities became available from federal, state and local governments, several land use – transportation studies were proposed. 

One of the first, and most ambitious, was for the south-east Pennsylvania  – south-west New Jersey region centred on Philadelphia. The proposal was written by Robert Mitchell [1906–1993], formerly director of city planning of the City of Philadelphia, and the first chair of the Department of City and Regional Planning at the University of Pennsylvania. Mitchell had co-authored an early study of land use and traffic with Chester Rapkin [1918–2001] (Mitchell and Rapkin, 1954). The Penn Jersev Transportation Study (PJTS) resulting from Mitchell's proposal is examined in section 2.7.2. 

Influenced by the PJTS proposal, other large metropolitan areas proposed metropolitan land use and transportation planning programmes, based on the belief that: 

1. land use arrangements different from recent development trends could be more efficiently served by balanced transportation systems that included new public transport services as well as new freeway systems; 

2. transportation systems were an important lever for obtaining a more desirable physical pattern of metropolitan development through the relationship of the type and density of urban activities to the level of transportation facilities and services available. 

BPR contracted for a review of these new studies by two junior faculty at the University of Pennsylvania, David Boyce and Norman Day [1933–2002]. Their 1969 report Metropolitan Plan Evaluation Methodology, later published as Metropolitan Plan Making (Boyce et al, 1970), provided detailed descriptions of these studies for seven urban regions.<sup>36</sup> 

A young urban economist at the Pittsburgh Regional Study, Ira Lowry, formulated a prototype model of urban activity location, which influenced research on land use models in the US and the UK. Other researchers built upon Lowry’s ‘Model of Metropolis’, spawning new research on urban land use models (section 2.7.4). Douglass Lee’s (1973) ‘Requiem for Large-Scale Models’ quelled interest in land use models for several years (sections 2.7.5, 8.5). 

## 2.7.2 Penn Jersey Transportation Study

The Detroit and Chicago area studies were respectively based on a land use plan and a forecast of land use activities for the target year. The  Penn  Jersey Transportation Study proceeded differently, in a way  considered revolutionary at the time. As stated in the study’s Prospectus: 

It is intended not only that the recommended transportation system should provide convenience and economy of travel, but also that its influence on the development of the area should tend toward facilitating a desired pattern of regional development. Stress is to be laid on the design and analysis of alternative patterns both of possible transportation systems and of the future regional development likely to be associated with each system. The workable alternatives are to be evaluated so that a reasonable choice can be made from among them (PJTS, 1959, 2). 

The proposed approach, first described by Robert Mitchell, is paraphrased as follows: 

1. ‘A dynamic metropolitan growth model needs to be constructed, expressing the relationships among the components and influences of the future area distribution of population, jobs, and land uses’, based in part upon ‘the amount, nature and location of transportation facilities and services. . . . Using the metropolitan growth model, a first projection is made of the distribution of population and jobs by major classes of industry based on the assumption of the past rate of improvement in transportation services. 

2. ‘With the first land use projection as a basis’, alternative transportation schemes for highways and transit should be prepared, ‘giving varying weight to highways and transit’. 

3. The distribution of population and jobs should be forecast for each transportation alternative, holding constant other factors. In this manner, ‘several sets of internally consistent land use and transportation alternatives for comparison’ should be prepared. 

4. A travel forecasting ‘model should be applied to the various  transportation plans to determine their feasibility with respect to the capacities of critical transportation facilities. It may be found, for  example, that the “maximum highway – minimum transit” plan would not be sufficient to carry expected volumes of traffic. . . . Readjustment of the plan and reassignment of traffic . . . should be repeated until a balance is attained’ (Mitchell, 1959, 19–20). 

The PJTS Prospectus, paraphrased below, described the application of Mitchell’s approach: 

1. A traffic model based upon land use variables, and consisting of trip generation, trip distribution and assignment, is first described, based upon the current state of practice. 

2. A regional growth model ‘identifying and analysing those factors and relationships in the physical, social and economic structure of the region which determine the growth and change in regional land development’ is then described. ‘Sets of mathematical relationships . . . which reflect in simplified form the relationships between land development and the key factors determining growth and change’ will be developed. ‘The influence of transportation on non-transportation factors in establishing land development patterns will be particularly important. 

3. The regional growth model will be applied ‘to produce a range of alternative patterns of future regional transportation and land development. . . . Each alternative must be realizable in a practical sense, but different from the others in some important aspect. . . . Alternative transportation systems, emphasizing different modes of travel, locational patterns or construction priorities, will be taken as the starting point for investigating possible patterns of regional growth. 

4. ‘Each regional alternative pattern, and its related transportation system’, will be evaluated with regard to a range of effects. ‘One of the alternative generalized transportation systems, possibly with modifications, will be selected as the basis for proceeding’ to elaborate ‘a single transportation plan and program’ for the region (PJTS, 1959, 12–16). 

The Prospectus and budget for a three-year study were adopted in December 1959, and the submission of the final report was scheduled for September 1962. The cost of the study was $2.9 million, of which $1.8 million was budgeted for data collection, coding and processing. PJTS evolved into the Delaware Valley Regional Planning Commission (DVRPC) in 1964. The principal developments related to land development models were the following. 

The first description of the regional growth model (RGM) was issued in April 1961. Vladimir Almendinger, a PJTS staff member and an innovative systems analyst, gave a broad outline of the model. Britton Harris [1915–2005], on leave from the University of Pennsylvania, was cited as the ‘intellectual progenitor and moving spirit of the model’. The RGM was described as an attempt: 

to simulate the aggregate locational and trip-making behavior over time of a population of decision-making units within an intra-regional setting made up of: (1) a spatial distribution of land use and activities, (2) a transportation system, and (3) a market for land and space. The heart of the model is the allocation procedure . . . [for] the distribution of residential activity in a metropolitan region (Almendinger, 1961, 8). 

Almendinger described a detailed stochastic simulation method for residential locators, location-serving industries and ‘footloose’ industries, and their land requirements, which he proposed to apply to a region sub-divided into 162 districts. His brief description ends with a flowchart depicting how the method would be solved. 

During the summer of 1960 at the University of Pennsylvania, John Herbert, a Ph.D. student in city planning, and Benjamin Stevens [1929–1997], an assistant professor of regional science, formulated a residential location model as a linear programming problem (section 7.2.2). By formulating the model with this method, they were not seeking to optimise the location of households. Rather, they sought to emulate a spatial market clearing process for the housing sector using the concept of households offering competing bids for residential locations (Herbert and Stevens, 1960).<sup>37</sup> 

The proposal of Herbert and Stevens led Britton Harris to embark upon a search for fast methods for solving large-scale linear programming problems, which occupied him during his ensuing academic career at the University of Pennsylvania. Harris also sought to conceptualise and design models for location of retail trade and services. Generally, Harris was not inclined to publish his research. However, in 1961 he did offer a relatively detailed description of the proposed regional growth model. In the following, Harris used the term ‘iteration’ to refer to a five-year time period, sometimes described as a recursion by others: 

operations: the supply of land, and the take-up of land and housing by industry and commerce, by home-renters, and by home-buyers. These four markets will interact within and between iterations by way of the rents generated in the linear-programming models. The effects of these interactions will be changes in the state: locating the locators, and assigning to land various fixed improvements, alterations, or redevelopments. 

A transportation system is an integral part of the model. It establishes accessibility measures that in part determine the behavior of locators. One output of the model is a set of transportation flows, expenditures, and facility loadings. 

Inputs to the model include increments of population and economic activity for the period of the iteration, and changes in policy variables or technological relations. The most important of the last group is changes in the transportation systems, which will presumably have marked effects on the behavior of locators and thus on future patterns of development and on the use of the transport system itself (Harris, 1961, 715–716). 

In ‘Linear Programming and the Projection of Land Uses’, Harris (1963) expounded on extensions of the Herbert–Stevens model, and offered an illustrative example. However, he did not describe further implementation progress. Shortly thereafter, work on the RGM ended. By the end of 1964, an activities allocation model (AAM) had replaced the RGM. The AAM consisted of seven major submodels: residential location; manufacturing location; non-manufacturing location; and four space consumption models, one for each of these sectors plus one for street area. David Seidman explained: 

Our thinking then turned to an alternative type of model which did not attempt to explain locational or land use behavior in economic terms at the household or firm level, but simply described this behavior in an aggregated manner sufficiently accurately that we could use these descriptions to project the locational tendencies of activities in the future. These descriptions are still mathematical models, but they have a form similar to that of a multiple regression; that is, they define the location of an activity as a function of a number of variables which specify the characteristics of each subarea (Seidman, 1964, 2). 

Development of the AAM continued to the mid-1960s. An initial set of assumptions concerning transportation policies consisted of six alternative sets of transportation plan inputs. In the testing of the 1985 plan, six combinations of policies were used: two alternative levels of freeway plans in combination with two alternative levels of public transport plans, together with varying assumptions concerning fares and parking fees. In the results, the largest variation in land use output was about 5 per cent, which was produced by a 30 per cent variation in accessibility among the plan alternatives; only a 10 per cent difference in accessibility was found between the two extreme highway and public transport alternatives (DVRPC, 1967, 26–30; Boyce et al, 1970, 69, 420–424). 

DVRPC’s 1985 Regional Transportation Plan candidly summarised the conclusions of ten years of effort: 

Earlier efforts to determine the relationship of regional transportation systems and alternative land use plans provided DVRPC with some important insights. Essentially, there is no defined single optimal regional plan. It has been observed that most land use activities locate in space to satisfy human needs rather than conforming to specified spatial patterns. Past experiments in simulating the interaction between land use and transportation with varying transportation systems, varying transportation capital investments and varying transportation policies have been rather ineffective in appreciably altering land use patterns. In contrast, it is known that when different combinations of highway and transit test plans are input to the traffic simulation models, significant changes or variations in travel by mode may be indicated (DVRPC, 1969, 43). 

Seidman (1969) completed a detailed report documenting his efforts to implement a forecasting model suitable for bringing the original land use and transportation alternatives concept of the Penn Jersey Transportation Study to a successful conclusion. Further efforts to develop land use and transportation alternatives for the Delaware Valley Region ended. 

## 2.7.3 Consideration of Land Use – Transportation Alternatives

The attempt to implement an innovative land use and transportation planning programme for the Philadelphia region represented a break from the approach of Douglas Carroll and his associates in Detroit, Chicago and Pittsburgh. During the early 1960s, metropolitan planning agencies were formed in several major US metropolitan areas. Criticism of the emphasis on road networks in the Detroit and Chicago transportation studies stimulated the exploration of a range of modal combinations, as well as land use arrangements for a future target year. The examination of alternative comprehensive land use and transportation alternatives had become a common approach to analysing and evaluating urban transportation problems for large metropolitan areas by the mid-1960s. Whether or not mathematical land use models were applied, several transportation planning studies, sometimes in conjunction with the regional land use planning agency, began to explore the interdependencies between the transportation and land use systems. An extensive review of land use models by Irwin (1965) offered an indication of the extent and variety of models implemented. 

One attempt to relate the effect of the transportation system to urban development was made by the Traffic Research Corporation with its EMPIRIC model developed for the Boston Regional Planning Project in eastern Massachusetts (Boyce et al, 1970, 197–221). Changes in population and employment were allocated to zones by a set of simultaneous regression equations using accessibilities by car and public transport to various land uses. Other independent variables included existing activity distributions and quality of water and sewer services (Hill, 1965a; Hill et al, 1965). The population differences among the four alternatives forecast for 1990 were compared with the change in population from 1963 to 1990 (Boyce et al, 1970, 69–72). Outside the area developed by 1963, the relative differences among the alternatives were extremely small. Hence, like the Penn Jersey case, the Boston model was unable to forecast differences in land use patterns, given different transportation system assumptions. 

During the same period, the Regional Planning Council serving the Baltimore, Maryland area pursued a land use planning activity based on a retail market potential model (Boyce et al, 1970, 147–195). Unlike other programmes described here, this effort was not part of an urban transportation study. The programme did successfully employ a market potential model to explore alternative patterns of future retail growth in the Baltimore area (Hansen, 1959; Lakshmanan and Hansen, 1965). The land use alternatives elaborated with the use of this model were substantially different, but still relatively similar as compared with the forecast change in population over the 20-year planning period (Boyce et al, 1970, 72–73). 

Other US metropolitan areas (Chicago, Minneapolis – St Paul, Minnesota and Milwaukee, Wisconsin) constructed land use and transportation alternatives using conventional (non-model) allocation techniques. These programmes succeeded in elaborating and evaluating plans that led to the selection or recommendation of a preferred land use and transportation plan (Boyce et al, 1970, 74–78). The methods employed were based on arrangements of land use exhibiting a singular organising principle for the physical structure of the region called ‘plan-form’ concepts. These arrangements related to the design of alternative plans, as well as the expected density of development, current or expected zoning regulations, holding capacity of vacant or agricultural land, and expected timing of its development. The methods applied were often labourintensive and time consuming, but the results were generally considered meaningful and worthwhile. 

The broad conclusions of Boyce et al provided a sombre termination to this period of excitement and anticipation of a new era of metropolitan planning: 

1. Many of the methods for preparing alternatives that had been envisaged for these programs were substantially more difficult to implement than expected. This conclusion applies both to the computer models of urban development, and to the refinement of plan-form concepts for preparing alternatives. 

2. The land use and transportation alternatives prepared were much less different than expected, given the variation in the number and range of policies and the assumptions examined. This conclusion applies both to differences in land use patterns forecast for alternative transportation policies, and to differences in transportation systems requirements forecast for different land use patterns. . . . 

3. The subsequent evaluation of alternative plans was much less successful than expected in terms of providing an adequate basis for decisions. This was partly attributable to the difficulties and delays in preparing alternatives, and the consequent shortage of time for evaluation, and partly a result of the reluctance to attach significance to the minor variations that emerged (Boyce et al, 1970, 4, 7). 

At a more general level, the premise that a land use pattern and associated transportation systems could be found that were in some sense optimal for a region’s future development was not supported by the experiences of these programmes. 

## 2.7.4 Lowry’s ‘Model of Metropolis’

Of the urban land use models developed during the 1960s, one became the best known by far, a prototype model offered by Ira (Jack) Lowry (1964). Lowry completed a Ph.D. in economics at the University of California, Berkeley in 1959. He then joined the Economic Study of the Pittsburgh Region, a three-year effort of the Pittsburgh Regional Planning Association. His research was undertaken as part of a regional economic study, and not as a component of a land use – transportation study. In 1963, Lowry joined the RAND Corporation, where he completed his report on the model’s development in 1964. Subsequently, he contributed to the discussion of land use models (Lowry, 1965, 1968). 

The Lowry model was formulated on a two-sector representation of employment, basic and retail: basic employment was exogenously allocated to zones; retail employment included not only retail trade and services, but also local government and schools. The location of residential population was based on the location of total employment according to a gravity or spatial interaction model. A second gravity model located retail activity according to the distribution of population and total employment. Through a set of economic multipliers, and with due regard for physical constraints on development, the interdependencies among exogenous regional employment and regional population totals, and their spatial distribution to discrete zones, were solved through an iterative scheme, leading to what was characterised as an ‘instant metropolis’. 

The simplicity of the mechanisms at the heart of the model and the relative ease of its implementation led to additional research and some applications, especially in the San Francisco Bay Area. Refinements included a time-oriented metropolitan model and a projective land use model (Goldner, 1971; Goldner et al, 1972). Putman (1975) reviewed this research, as well as describing his own model implementation efforts that evolved from it. 

Generalisations of the Lowry model took many forms, including: 

1. an increased disaggregation (stratification) of the population sector; 

2. explicit consideration of the supply side and decisions affecting the allocation of stock; 

3. relaxation of the comparative static status of the model to take account of incremental (quasi-dynamic) change over time; 

4. more sophisticated representation of spatial interaction behaviour. 

Further academic research on allocation and locator decisions in competitive housing and land markets drew on the bid-rent concepts of Herbert and Stevens (1960). Examples include Ingram et al (1972), Anas (1973) and Wilson (1974, Chapter 10). 

## 2.7.5 Lee’s ‘Requiem for Large-Scale Models’

In 1973 Douglass Lee was an assistant professor in the Department of City and Regional Planning at the University of California, Berkeley. Following completion of his Ph.D. thesis on land use models at Cornell University in 1968, Lee continued his interest in urban land use models, as well as engaging in empirically oriented research on the impact of largescale rail transit investment. His article ‘Requiem for Large-Scale Models’ (D. B. Lee, Jr., 1973), in the Journal of the American Institute of Planners, was an attack on land use models and their developers, initiated in the past 15 years. 

By the time the article appeared, nearly all urban model implementation efforts in the US had ceased. In this sense, Lee’s use of the term ‘requiem’ was appropriate. Nevertheless, his article caused an uproar among the proponents of urban activity models. The article was seen as a polemic, an aggressive attack on or refutation of the opinions or principles of another. 

Lee summarised his conclusions in three points: 

1. In general, none of the goals held out for large-scale models have been achieved, and there is little reason to expect anything different in the future. 

2. For each objective offered as a reason for building a model, there is either a better way of achieving the objective (more information at less cost) or a better objective (a more socially useful question to ask). 

3. Methods for long-range planning – whether they are called comprehensive planning, large-scale systems simulation or something else – need to change drastically if planners expect to have any influence on the long run (Lee, 1973, 163). 

From the perspective of this book, some of Lee’s concerns are no longer relevant, in view of the enormous increases in computing, data handling and geographic data analysis capabilities now available to urban modellers. Nevertheless, his views remain worthy of consideration. A retrospective on Lee’s Requiem was published in 1994; the introduction by Richard Klosterman (1994) and the papers by Michael Batty (1994), Britton Harris (1994), Douglass Lee (1994) and Michael Wegener (1994) are relevant to Lee’s original article. 

## 2.8 CONCLUSION

Urban transportation planning, and specifically urban travel forecasting, was definitely ‘where the action was’ for young transportation engineers and planners entering the field in the 1960s. The problems were challenging, from both a research and a policy perspective. Opportunities for innovation were ample, and agency directors were receptive. By applying the new computer technology of the day, as well as recent mathematical advances, new findings could be anticipated. 

Considering the time schedules for these studies, staff members were clearly under great pressure to produce results. Shortcuts were necessary. Judgements had to be made based on incomplete analyses. Some efforts were probably doomed to fail from the outset. Even so, much knowledge and experience was gained from this period, laying a foundation for future activities by both practitioners and academic researchers. US practice matured during the 1970s, as the new computer programs emerging from US DoT became available (section 10.3). Academic research offered new developments during the 1970s, after rediscovering a fundamental contribution of the mid-1950s, recognised by neither practitioners nor researchers for nearly 15 years (section 7.3). 

## NOTES

1. Daily surface weekday ridership was 45 rides per 100 persons in the City of Chicago, onehalf of the post-war peak ridership (Chicago Area Transportation Study, 1960, 124). 

2. The first procedural manual for conducting such studies was issued in 1944, revised as US DoC (1954), and updated and reissued as US DoT (1973b). 

3. Fratar’s growth factor method adjusts an observed trip table constructed from a home interview survey to a forecast trip table corresponding to independent forecasts of origin and destination (row and column) totals. In contrast, in a gravity model forecast, the number of trips from origin to destination is proportional to the row and column totals, and inversely proportional to a function of travel time. Section 2.5.3 offers more details about the gravity model. See also Brokke and Mertz (1958, 78) and Mertz (1960a, 24–25). 

4. This discussion reflects a level of understanding similar to that found in Wardrop’s more succinct description ‘that traffic will settle down into an equilibrium situation in which no driver can reduce his journey time by choosing a new route’ (Wardrop, 1952, 345). At this same time, fundamental research on this problem was under way at the Cowles Commission for Research in Economics located at the University of Chicago, which led to the publication of Beckmann et al (1956), as described in section 7.3. 

5. The standard punch card, invented by Herman Hollerith [1860–1929], was first used for vital statistics tabulation by the New York City Board of Health and by several states. After this trial use, punch cards were adopted for use in the 1890 census. After Hollerith had perfected his first series of electromechanical punch-card machines, including a punch, a tabulating machine to accumulate statistics from the information punched on cards, and a sorting machine, he founded the Tabulating Machine Corporation. As with more recent high-tech start-ups', the company had a somewhat rocky start until an experienced manager, Thomas Watson, took over. One of Watson’s moves was to rename the company International Business Machines (IBM). en.wikipedia.org/wiki Herman_Hollerith (accessed 18 February 2014). 

6. www.columbia.edu/cu/computinghistory/ (accessed 26 January 2013). 

7. W.L. Mertz (1961, 100) described the use of feedback between trip distribution by gravity model and assignment by the Traffic Research Corporation; for an anecdotal description of his experience, see www.fhwa.dot.gov/infrastructure/memories.cfm (accessed 17 February 2014). Martin Wohl [1930–2009] published an insightful paper on the principles of the travel forecasting procedure with feedback, and its relationship to travel demand, link capacity and travel time on a link (Wohl, 1963). 

8. Guide to the John R. Hamburg Transportation Papers, 1956–1992, sca.gmu.edu/ finding_aids/hamburg.html (accessed 17 February 2014). 

9. According to Bruce Hutchinson (1974), Schneider’s intervening opportunities model was a modification of the hypothesis of Samuel Stouffer [1900–1960] (1940), although Schneider apparently never so stated. 

10. en.wikipedia.org/wiki/Edward_F._Moore (accessed 28 March 2014). 

11. The study of the properties of shortest route algorithms is a subfield in network optimisation. Gallo and Pallottino (1984) made a detailed study of these algorithms. 

12. Roger Creighton, personal communication with David Bovce in 2005 

13. Robert Dial, personal communication with David Boyce. 

14. The CATS congested travel time function is stated in Muranyi (1963, 20): 

$$
t _ {l} (V _ {l}) = t _ {l} ^ {o} \cdot 2 ^ {(V _ {l} / C _ {l})}
$$

where t (V ) 5 congested travel time on link l at volume $V _ { l }$ 

t<sup>o</sup> 5 travel time on link l at zero volume 

V 5 volume on link l 

C 5 design capacity of link l 

15. From 1955 to 1960, 140 units of the IBM 704 were sold. The IBM 700 series were binary computers, as opposed to decimal, vacuum-tube logic computers with 32 000 words of 36-bit length. The IBM 709 succeeded the 704, adding overlapped input/output, indirect addressing, and decimal instructions. The IBM 7090 was a 709 with transistor, rather than vacuum-tube, logic. The 7040 and 7094 were scaled-down and scaled-up variations of the 7090. www.columbia.edu/cu/computinghistory/701.html (accessed 25 March 2014). The 36-bit 700 and 7000 series were IBM’s scientific computers from 1952 until the introduction of the 32-bit System 360 in 1964. en.wikipedia.org/wiki/IBM_704 (accessed 18 February 2014). 

16. Recollection of David Boyce of a discussion with Morton Schneider about 1962. 

17. The CATS staff performed a transportation study for the Pittsburgh area using the same methods as developed in Chicago. The Cartographatron was also used to prepare images for the Pittsburgh region. 

18. Comments bv Irving Hoch to David Bovce, 2006 

19. Creighton et al (1959, 1960) described the derivation of the expressway spacing formula. CATS (1962, 39–42) described the application of the method; also see Appendix to CATS (1962, 121–123). Boyce (2007a) reviewed the expressway spacing formula and economic analyses of the expressway plans. 

20. A hypothetical study by Levinson and Roberts (1965) compared grid and radial freeways systems, and showed small advantages for grid layouts. Peter Steenbrink (1974a, 1974b) applied a heuristic network design procedure to the Netherlands. 

21. Additional details were treated by Scheff (1977). Garrison and Levinson (2006, Chapter 14) discussed the problems faced in locating urban segments of the Interstate System. 

22. The detailed history of the Bureau of Public Roads and the Federal Highway Administration are found at www.fhwa.dot.gov/highwayhistory/history_fhwa.cfm (accessed 19 February 2014). 

23. Lee Mertz wrote a memoir about his early experiences with travel forecasting models and learning to write computer programs for the new IBM mainframe computers; www.fhwa.dot.gov/infrastructure/memories.cfm. A biography of W.L. Mertz is at www.fhwa.dot.gov/infrastructure/mertz.cfm. Guide to the William L. Mertz transportation collection, 1955–1990, sca.gmu.edu/finding_aids/mertz.html (accessed 17 February 2014). 

24. Several additional manuals were issued during the $1 9 7 0 \mathrm { s } ;$ of these, the most useful from a historical viewpoint is Urban Transportation Planning, General Information (US DoT. 1972a) 

25. The concepts of trip production and attraction originated with BPR’s early efforts to implement the gravity model as a trip distribution model, and related to two-way travel between an origin and a destination. 

26. The gravity model described in US DoC (1963a) may be stated in slightly simplified form as follows: 

$$
T _ {i j} = \frac {P _ {i} \cdot A _ {j} \cdot F _ {i j} \cdot K _ {i j}}{\sum_ {k = 1} ^ {n} A _ {k} \cdot F _ {i k} \cdot K _ {i k}}
$$

where T 5 trip interchange between zone i and zone j 

$$
\dot {P} _ {i} = \text { trip   production   of   zone } i
$$

$$
A _ {j} = \text { trip   attraction   of   zone } j
$$

$$
F _ {i j} = \text { travel   time   factor   for   zone   pair } i j
$$

$$
\dot {K _ {i j}} = \text { zone - to - zone   adjustment   factor   for   zone   pair } i j
$$

$$
\dot {n} = \text { number   of   zones }
$$

The denominator term ensures that $\begin{array} { r } { \sum _ { j = 1 } ^ { n } T _ { i j } = P _ { i } } \end{array}$ for each origin zone. The adjustment procedure for the values of $A _ { j }$ ensures approximately that $\begin{array} { r } { \sum _ { i = 1 } ^ { \widetilde { n } } T _ { i j } = A _ { j } } \end{array}$ for each destination zone. If these two equations are considered to be constraints on the matrix $( T _ { i j } )$ then it may be said to be ‘doubly-constrained’. Section 3.5 provides further details. 

27. The originally stated form of the BPR volume-delay function is as follows: 

$$
T = T _ {0} \left[ 1 + 0. 1 5 \left(\frac {V}{C}\right) ^ {4} \right]
$$

where $T =$ travel time at which the assigned volume can travel on the link 

$T _ { 0 }$ 5 base travel time at zero volume 5 travel time at practical capacity × 0.87 

V 5 assigned volume 

C 5 practical capacity 

Practical capacity was defined in the 1950 Highway Capacity Manual as ‘the maximum number of vehicles that can pass a given point on a roadway or in a designated lane during one hour without the traffic density being so great as to cause unreasonable delay, hazard, or restriction to the drivers’ freedom to maneuver under the prevailing roadway and traffic conditions’ (US DoC, 1950, 7). Furthermore, the Manual stated: ‘The maximum practical capacity of multilane freeways in urban areas, when access and egress facilities are not a factor, is 1,500 passenger cars per lane per hour in the direction of the heavier flow. At this volume . . . the average speed of all vehicles will be 30 to 35 miles per hour’ (US DoC, 1950, 47). In highway capacity manuals subsequently issued by the Transportation Research Board, the concept of practical capacity was replaced by the ‘level-of-service’, which in turn is related to the maximum flow and density. 

28. Smock wrote: ‘For the third pass the same procedure is followed, and such passes can be repeated, dividing interzonal volumes over more and more paths, until capacityadjusted speeds, on the average, come to approximate typical speeds. 

29. Smock devised his volume-delay function based on ‘mathematical logic and trial-anderror experimentation': 

$$
T _ {i} = T _ {0} \exp \left(\frac {V _ {i}}{C} - 1\right)
$$

where $T _ { i }$ 5 travel time on a link at i iteration n 

$T _ { 0 }$ 5 ‘original (typical) travel time on the link’, by which he clearly meant the time when volume equals capacity 

$V _ { i }$ 5 averaged assigned volumes from all preceding iterations 

$\dot { C }$ 5 link capacity 

exp(x) 5 the exponential function, 2.71828, raised to the power x 

Smock's function evaluated at zero link flow vields a value of $0 . 3 7 \mathrm { T } _ { 0 } ,$ which is substantially less than the value of $0 . 8 7 \mathrm { T } _ { 0 }$ vielded by the BPR function 

30. Comments by James Fennessy to David Boyce in 2013; Fennessy was an early user of CDC TRANPLAN, and a developer of subsequent versions of this software (section 10.5.1.1). 

31. For biographical details of Robert Dial, see sections 10.3.1 and 10.3.3. 

32. The expanding literature on gravity, potential and spatial interaction models was synthesised by Walter Isard (1960), Methods of Regional Analysis, in Chapter 11 with 51 references. Although much of Isard’s treatment concerned interregional flows of population as well as freight, the concepts are general. Helvig cited several of Isard’s papers and books, but he did not include a reference to Isard's Methods. 

33. Wilson (1967) is generally credited with the introduction of the negative exponentia function into trip distribution models of person travel. 

34. Based on an interview with Robert Dial in November 2003, and extensive notes he provided in August 2007, and subsequently. 

35. Interviews of John Wootton by Huw Williams. 

36. The publication of Metropolitan Plan Making resulted from the dedicated efforts of Chris McDonald 

37. William Wheaton (1974) revisited the Herbert-Stevens model, discussed some of its shortcomings, and proposed an alternative formulation and solution method. 

## 3. Early developments in the UK

## 3.1 INTRODUCTION

In the late 1950s, after a post-war economic boom, London and other Western European cities were starting to encounter the growing impact of the motor age that many US and Canadian cities experienced over a decade earlier. The problems were manifest in a variety of ways, as described by Gerard Drake, director of the first London Traffic Study: 

acute and growing traffic congestion; central area parking shortages; increased incidence of road traffic accidents; decreasing patronage of bus and tram services; financial difficulties for the railways, even though suburban commuter services are overcrowded; the need for restrictions on the individual’s use of his private vehicle to improve traffic flow and promote safety in the interest of the general public; and last, but certainly not least, mounting pressures for greatly increased capital expenditures for the construction of new highways and the modernization of existing main roads (Drake, 1963, 81). 

In response to these growing concerns, the UK minister of transport, Ernest Marples [1907–1978], who had already endorsed an inter-urban motorway programme, introduced three activities concurrently: (a) he formed the London Traffic Management Unit; (b) he initiated major studies of traffic in London and Glasgow; and (c) he asked a senior civil servant, Colin Buchanan [1907–2001],<sup>1</sup> to look into problems arising from the car (Wootton, 2004). 

Fifty years later, it is hard to imagine the apprehension and sense of urgency at the start of the 1960s with which British planners approached these problems and the prospect of mass motorisation. Rereading the report Traffic in Towns (Buchanan, 1963), one perhaps gets a flavour of those times and also the dilemmas faced presently by many cities of the developing world that are experiencing rapid rises in personal income and car ownership. The team of traffic engineers and town planners assembled by Buchanan was charged with investigating the long-term consequences for mobility and the urban environment of car ownership and use suggested by trends evident at that time. 

In their report to the minister, the Steering Group addressed the challenge and potential consequence of ‘the impending motor age’ in words of Churchillian gravity: 

It is impossible to spend any time on the study of the future of traffic in towns . . . without being at once appalled by the magnitude of the emergency that is coming upon us and inspired by the challenge that it presents. There is another source of fascination. We are nourishing at immense cost a monster of great potential destructiveness. And yet we love him dearly. Regarded in its collective aspect as ‘the traffic problem’ the motor car is clearly a menace which can spoil our civilisation. But translated into terms of the particular vehicle that stands in our garage (or more often nowadays, is parked outside our door, or someone else’s door), we regard it as one of our most treasured possessions or dearest ambitions, an immense convenience, an expander of the dimensions of life, an instrument of emancipation, a symbol of the modern age (Report of the Steering Group to the UK Minister of Transport, preface to Buchanan, 1963, para 55). 

For inspiration Britain had already started to look westwards and was quick to embrace the new systems approach to transportation planning and the methods of travel forecasting under development. Visitors to the US who were charged with witnessing these new developments embodied in the transportation studies were clearly impressed by what they saw and returned to convert the doubters: 

As far as motor traffic is concerned, predictions about the increase in vehicle ownership and the effect on traffic flows have not been conspicuously accurate in the past, and this has created doubts in many people’s minds whether it is really possible to predict changes in the pattern and scale of movement in a complex urban community. Such doubts are fermented by the general lack of understanding about how and why movement is generated and what dictates the choice of method. If movements were completely random and irregular no amount of study would be of any use, but research in the United States in the last decade shows beyond doubt that urban movement is remarkably orderly, that motivation is basically rational and predictable, and that definable relationships exist between any given pattern of land uses and the character and amount of traffic that is generated (Buchanan and Crow, 1963, 37). 

These authors saw the scientific study of movement and its relationship to urban development as not only desirable but inevitably leading to the ‘deployment of transportation studies on the American pattern but refined and adapted to the smaller and more intimate scale of our own conditions’ (Buchanan and Crow, 1963, 37). 

Soon after the Buchanan Report was published, the inauguration of further transportation studies took place. These were to become major instruments of the UK Ministry of Transport (and after 1970 the Department of the Environment) in policy development and local decisions on capital investment and the balance between public transport and the car. This chapter charts the transfer, adaptation and the main theoretical and practical innovations in urban travel forecasting in UK transportation studies up until the early 1970s. 

In section 3.2 we record the establishment of such transportation studies in the UK and the means by which, primarily through US consultants, the torch was passed, resulting in strong similarities in the approach to urban transportation analysis in the US and the UK. We note, as part of this legacy, the main variants of the conventional zone-based multi-stage<sup>2</sup> travel forecasting models applied in the early to mid-1960s. 

In section 3.3, we describe a successful attempt to account for greater variability in travel behaviour ‘within zones’, rather than solely ‘between zones’, by adopting household classes as the units for analysis at the generation stage. The resulting household-based category analysis approach introduced by Wootton and Pick (1967) had major implications for both trip generation models and car ownership forecasting in UK studies. 

Initially, as if on a parallel track, the multivariate statistical models based on modal choice observations of individual travellers, stemming from Stanley Warner’s [1928–1992] pioneering research (Warner, 1962), appeared to offer an alternative to the mainstream in both the US and the UK. The derivation of information on the way people were considered to trade off travel time and money costs in their modal choices was however to be of great significance for the analysis and forecasting of travel, and the evaluation of transportation schemes. In the mid- to late 1960s we witness the emergence of the variously termed ‘disutility’ or ‘generalised cost’ concept derived from the studies of modal choice, and its adoption in conventional forecasting practice. In section 3.4 we describe these developments and the absorption of generalised costs into UK travel forecasting models in the late 1960s. 

One of the most trenchant criticisms of models and methods of the early 1960s was the absence of a unifying theoretical approach to guide the formation of travel relationships and establish their validity in the forecasting process. This omission was most evident in the wide use of empirically derived functions: ‘friction factors’, ‘diversion curves’ and ‘look-up’ tables in the distribution, modal split and assignment models. In section 3.5, we describe the gradual emergence of analytic forms for the relationship between travel demand and its determinants, and particularly the wide use of the multinomial logit (MNL) share model. We discuss the introduction of a new approach by Alan Wilson, the ‘entropy maximising method’, to the interpretation of statistical variability or dispersion in travel patterns, and the theoretical and practical synthesis it provided, particularly in forecasting the modal split and the distribution of trips. Because Wilson offered an important new perspective on many of the problems confronting transportation analysts and urban and regional researchers, we discuss his contributions in some detail. 

As in the US, the 1960s was a period of considerable refinement in the analysis, assignment and forecasting of flows in both highway and public transport networks. Two aspects received particular attention in the former: 

1. the use of capacity restraint methods for achieving consistency between route selection and level-of-service provided by the highway system; 

2. the incorporation of what were variously described as probabilistic or stochastic models of route selection. 

In addition, a more realistic representation of the behaviour of passengers in public transport networks was partly a consequence of a greater emphasis on this mode in the formation of UK transportation plans. These advances are addressed in section 3.6. 

In section 3.7 we discuss three aspects of UK practice in the late 1960s and early 1970s and note some important differences in the structure and form of the models adopted. Firstly, we describe the travel forecasting model applied in the SELNEC (South East Lancashire North East Cheshire) Transportation Study, which anticipated important subsequent developments, and must be regarded as one of the most technically advanced models anywhere at that time. Secondly, we discuss the variation in the overall specification of models together with their justification, particularly in relation to the position of modal split in the overall structure, and the means by which the multiple stages were joined together. Finally, we comment on the notion of validity accompanying the construction and testing of the travel forecasting models in this period and the results of a major study on their predictive accuracy. 

In section 3.8, we examine the expanding scope of economic evaluation, and the relationship between the models developed for travel forecasting, and the performance measures adopted for project evaluation. In particular, some intriguing theoretical developments in the construction of economic measures of user benefit accompanying project appraisal are noted, which were later to be of great significance. 

In section 3.9, the final section, we comment on the problems solved, outstanding challenges and changing attitudes towards traditional travel forecasting procedures. Throughout, we note some of the similarities and differences between the practices adopted in the US and the UK. 

## 3.2 METHODS INHERITED FROM THE US AND EARLIER STUDIES

## 3.2.1 Establishment of Land Use – Transportation Studies in the UK

Prior to the adoption of a comprehensive US-style systems approach in the UK, there was already a suggestion of what was to come. In the late 1950s, the UK Ministry of Transport started to encourage local authorities in the conurbations to co-operate in the production of long-term highway plans for their areas and, for this purpose, to adopt the US practices of surveying traffic patterns, particularly origin–destination movements, and analysing them with computers (Starkie, 1973; Bruton, 1975). There is some debate as to the first ‘comprehensive analysis of the movement of people and goods in a single large urban area’, although ‘Leicester and the County of London vie for the claim to have been first to place stress on the quantified approach’ (Starkie, 1973, 328). The first major conurbation traffic studies, however, were undertaken in London and Glasgow. Begun in 1961–62, the London Traffic Survey was primarily concerned with establishing land use and traffic data for a base year of 1961 and forecasting traffic on highway networks for 1971 and 1981 (Freeman, Fox, Wilbur Smith and Associates, 1966).<sup>3</sup> 

At the turn of the decade when these studies were in their early stages, there was a growing appreciation of the relationship between urban development and transportation planning that was emerging from early studies in the US (Starkie, 1973). This led, as noted in section 3.1, to the appointment of Colin Buchanan to lead a team to investigate the long-term consequences for the urban environment of traffic growth and potential road construction. The Buchanan Report, Traffic in Towns (Buchanan, 1963), was destined to have a major guiding influence on urban transportation planning in the UK. Following publication of the report, a joint circular was produced by the UK ministers of transport and housing and local government in January 1964, endorsing the report’s findings and emphasising the need for local authorities to undertake land use – transportation studies ‘to achieve a co-ordinated approach to land-use and transport planning’ (Bruton, 1975, 20). 

The first study was the West Midlands Transportation Study, begun in 1964; those in the other conurbations and larger urban areas soon followed: Greater Glasgow (1964), Teesside (1965), Belfast (1965), SELNEC (1965), Merseyside (1966), West Yorkshire (1967) and Tyneside (1967) (see Spence, 1968 and Starkie, 1973, 332 for the timing, duration and organisation of the first generation of UK transportation studies in the conurbations and larger free-standing towns). The UK Ministry of Transport was active in encouraging these studies, making a contribution to their technical direction and sharing the costs with the local authorities involved. 

These ‘comprehensive’ studies were meant to contribute to decisions on the future highway and public transport networks in a study area. As in the US, central to their execution were: 

1. surveys of the use of land and the movement of people and goods in an area; 

2. projections of car ownership, population, employment and other land uses; 

3. on the basis of computer models, the derivation of travel and traffic forecasts for networks envisaged for some future year(s). 

## 3.2.2 Transfer of Expertise and Technology in the Early 1960s

The earliest conurbation studies in the UK, such as those in London and Glasgow, were carried out by consortia involving teams of British and American consultants. ‘The formation of these teams ensured that the experience gained in the urban land use – transportation studies carried out in America in the 1950s was transferred to British practice’ (Wootton, 2004, 274). As described in an early textbook, ‘This knowledge of the traffic forecasting model was an essential first step in developing fresh methods designed more specifically to answer the particular problem of obtaining the best return from the limited funds available for investment in urban and rural transport infrastructure’ (Lane et al, 1971, 205). 

John Wootton (M.Eng., University of California Berkeley, 1963) was one of a handful of British transportation engineers who undertook graduate work in the US and returned to the UK to distinguished careers in transportation consultancy, senior transportation planning and management, and academia (others were Brian Martin, M.S., MIT and Tony Ridley, Ph.D., University of California Berkeley). Wootton joined Wilbur Smith and Associates in London in 1962 to work on the London Traffic Survey. As one of the few people with analytic experience at that time, he recalled being drawn inexorably to traffic modelling.<sup>4</sup> Echoing the earlier comments of Chapter 2, Wootton recalled how the analysis of transportation survey data and computers grew up together: 

in 1962, when the analysis of the London and Glasgow Survey data began, computers were so new that there were only two computers in Britain (IBM 7090’s) powerful and large enough for completing the task. . . . Happy hours were spent during the middle of many nights watching magnetic tapes turn and lights flash until the results produced by the computer programmes were printed (Wootton, 2004, 276). 

These initial studies were limited in scope and drew on the earlier experience in Detroit and Chicago for their methodology (Lane et al, 1971; Starkie, 1973; Bruton, 1975). Even so, they provided formidable challenges for the collection and analysis of data. The surveys were processed and analysed with specially written computer programs, while those for implementing the traffic models were acquired from the US. In the case of Freeman, Fox and Wilbur Smith, Wootton recalls: ‘Initially, we used the BPR suite of programs but Wilburs bought a CDC 3300 for which we had to write new programs.’<sup>5</sup> This development resulted in the Transport Analysis Programs (TAP), written by Wootton and his colleagues, allowing innovative methods and models developed in the UK to be incorporated in an evolutionary way in the second half of the 1960s. 

Certainly, in those early days access to computing services was influential on what could be achieved. As Martin Richards, who joined the London Traffic Management Unit direct from his civil engineering degree at University College London, later recalled: 

access to computing and the limited software available on a bureau basis influenced much of what was done. I recall, when working on the Worcester Transport Study of the mid 1960s, we would send run specifications to English Electric Computers (later to become BARIC) by British Rail’s Red Star, and collect the output many days later, also sent Red Star. What we could do was limited by their software as well as the time taken to complete a run, including checking for input/keying errors and re-runs.<sup>6</sup> 

With reference to data, he added: 

much of the modelling depended on data collected specifically for the studies, and there was a steep learning curve as skills in survey design and execution developed as well as survey processing and analysis software. Sampling, interview process, dealing with missing data, geo-coding were among the areas on which real progress was made. 

## 3.2.3 Methods for Forecasting Travel in the Early Transportation Studies

## 3.2.3.1 Available methods

In Chapter 2 we outlined in some detail the general approaches to transportation planning and travel forecasting in early US studies. These studies were reviewed for a British audience by Davinroy et al (1963), and later for the field generally by Hutchinson (1974) and Stopher and Meyburg (1975). We review briefly the situation in the early 1960s as a basis for considering future innovations. 

In the early days of the 1960s, prior to any standardisation of the methods around a broadly common multi-stage approach, there were almost as many ways of preparing forecasts as there were studies. One example is the relationship between trips generated at the zonal level and land use characteristics, where expansion factors and regression models were applied in various forms (Davinroy et al, 1963). At the distribution stage, growth factor methods devised by Fratar and Furness were applied, as well as intervening opportunity and gravity models to determine the effect of changes in travel times on the distribution patterns. At the assignment stage, the diversion curve approach was giving way to a computer-based ‘all-or-nothing’ allocation of origin–destination (O-D) flows to shortest routes. Capacity restraint methods relating travel times to congestion on individual links were at a very early stage of development. 

Methods for analysing public transport systems were rudimentary both with respect to determining modal choice and in the network representation and assignments. In the early 1960s modal split models were still in their infancy; there was a widespread view that ‘at the present time this phase is probably the most inadequate of those comprising traffic analysis’ (Davinroy et al, 1963, 371). The earliest travel forecasting models were appropriately described as three-stage models; studies giving serious consideration to forecasting modal split were based on zonal averages of socio-economic variables, such as car ownership and income, at the trip ends, which Starkie (1973) identified as one of the more unsuitable transfers of US methods to a UK setting. Because of a failure to identify level-of-service (the times and costs of travel on the modes) as a determining factor of modal choice, such models would indicate an inexorably declining share of public transport as real levels of income and car ownership rose, irrespective of policy to improve the public transport system. As David Starkie remarked: 

This was the situation in general terms when the concept of the North American urban transportation study was first introduced in this country and it was therefore out of step with British circumstances, where the overwhelming proportion of conurbation journeys was made by public transport and out of phase with the views and attitudes then germinating amongst those who determined transport policy (Starkie, 1973, 371). 

There were attempts in the early 1960s to introduce zonal accessibility variables, both in US studies (for example, in the studies for Puget Sound, Erie and south-eastern Wisconsin)<sup>7</sup> and in Britain (in the studies for Glasgow, Leicester and London). These approaches were viewed as being rather crude, however, and lacking in sensitivity to level-of-service variables to appropriately inform policy. Later in this chapter we comment further on this issue. 

In the early 1960s, modal split models of the ‘trip-interchange’ variety, which treated modal opportunities as a travel market, had only recently been formulated. The pioneering contributions of Traffic Research Corporation (TRC) on post-distribution modal split models (Hill and von Cube, 1963) were absorbed into UK practice in the Merseyside Area Land-Use/Transportation Study (MALTS) and West Yorkshire Transportation Study undertaken by the Traffic Research Corporation (1969a, 1969b), as well as adopted in the London Transportation Study (LTS III) (Tressider et al, 1968). In these studies the distribution and modal share models were expressed in terms of empirically derived functions based on modal travel times. 

Interestingly, Davinroy et al (1963) emphasised the interdependency of the models in the overall procedure, and the need for some feedback mechanism to achieve consistency in travel times throughout. They remarked: 

Today the trend is towards a systems approach. This implies a consideration of each step as part of the whole process and not as one of three separate steps. As yet the techniques which have been developed have not been able to consider the complete process. For this reason, separate methods have been described here. Yet it is important to emphasize the interdependence of each phase. This interdependence is not one way. Not only does assignment depend on generation and distribution, but there must also be a ‘feedback’ of data from the assignment phase to the earlier phases. . . . Up to the present no great progress has been made in the feedback of data. There have been some elementary attempts, but largely because of the complexities which are introduced, they have not been extensive. There has been use of iterative techniques in order to achieve convergence of the distribution and assignment phases (Davinroy et al 1963, 371). 

There is little evidence that feedback was undertaken in any systematic way in the earliest UK studies, but by the late 1960s there was both recognition of its importance and some rudimentary attempts to achieve consistent solutions. An example of the implementation of feedback is described in section 3.7. 

## 3.2.3.2 Treatment of land use

Although the studies were termed land use – transportation studies, there was little attempt in the UK to reflect the effect of transportation on land use other than in a general descriptive way (Starkie, 1973; Bruton, 1975). Moreover, compared to the US, where land use models were being used to allocate population and employment in several land use – transportation studies, Bruton commented: 

In Britain . . . with its long history of comparatively strong land-use controls, the approach to forecasting of future land-use distribution and characteristics has been somewhat different. Indeed, with notable and recent exceptions, such as the Teesside study, it could be argued that in Britain no real attempt has been made to forecast, on a systematic and comprehensive basis, estimates of the future land-use characteristics and distribution. Rather, ad hoc estimates of land-use distribution tend to be produced, based on generalized and rather crude predictions of population and employment (Bruton, 1975, 35). 

To our knowledge no UK transportation study in the 1960s utilised land use forecasts derived from urban models. However, a great deal of research, development and application to regional growth based on the Lowry model occurred in the UK in the 1960s, particularly in a structure planning context (Wilson, 1971, 1973a; Batty, 1972). In section 3.5 and more extensively in Chapter 9, we discuss the development of land use models and particularly the evolution of integrated land use – transportation models in Britain. 

Furthermore, very few transportation studies carried out systematic testing of alternative land use plans (Dalvi and Martin, 1973). Unlike several studies in the US where land use – transportation alternatives were analysed (Boyce et al, 1970), in the UK the time and resources involved in drawing up the latter almost invariably resulted in a single land use arrangement with the possibility of some minor sensitivity analysis about that plan. 

## 3.3 FROM ZONES TO HOUSEHOLDS AT THE TRIP GENERATION STAGE

## 3.3.1 Household-Based Category Analysis for Trip Generation

The early methods of trip generation based on zonal regression equations, while sometimes identifying key determining variables and giving impressive goodness-of-fit statistics, were often to be found wanting. Problems of multicollinearity and the dangers of ecological fallacy were ever present (Stopher and Meyburg, 1975; Ortúzar and Willumsen, 2011). The lack of causality and stability of parameters, when transferred to different areas and zoning systems, made them an unpromising basis for forecasting. 

The early studies of Oi and Shuldiner (1962) in the US (section 2.5.2) drew attention to the potential of trip generation approaches based on the household as the unit of analysis. By directly addressing and accounting for the variation of travel between household classes or categories rather than the zone, this new approach offered the potential for greater behavioural content and stability in forecasting. Loss of information accompanying aggregation of trips and explanatory variables to the zonal level prior to model specification was avoided. Indeed, it was later shown that zonebased models captured a relatively small proportion of the variation of travel among households in an urban area (Fleet and Robertson, 1968) These realisations led to ‘household-based category analysis’ models in the UK (Wootton and Pick, 1967) and ‘cross-classified household models’ later in the US (US DoT, 1972a, 1975). In the following we use the UK terminology as expressed in the mid-1960s by its originators John Wootton and Gerald Pick at Freeman, Fox and Wilbur Smith. 

In this disaggregated formulation the number of trips generated in a zone could be expressed in terms of the number of households in different household categories multiplied by the average trip rates for those categories. Summation over the contributions from the various categories would then generate zonal trip production totals. Under the assumption that trip rates for various household categories and other external factors would remain stable, the burden of forecasting was passed to determining the number of households in the different categories within each zone for the future year(s). 

In applying the approach, Wootton and Pick were concerned with four different questions: 

1. What combination of household characteristics should be taken to define the categories? 

2. Did these combinations allow statistically reliable trip rates to be established? 

3. How were the distributions of households over household groups to be forecast? 

4. Was the approach transferable to other study areas? 

These choices implied a trade-off between the number of categories to be included to account for significant variation between households, on the one hand, and the requirement for reliable estimates of the mean trip rates to be established, particularly in those categories with relatively few observations, on the other. This approach prompted the search for relatively homogeneous household categories with low intra- and high intercategory variations in trip rates. They first successfully addressed these issues in the London Traffic Survey and, more fully, in the West Midlands Study (Wootton and Pick, 1967). 

John Wootton recalled these early efforts: 

Attempts to predict trip ends using multiple linear regression analysis were proving to be poor and there was the added need of predicting future levels of car ownership at a zonal level. The moment of inspiration came when I linked some illustrations I had seen in a paper while at Berkeley in 1962/3 to probability theory. The paper, by Paul Shuldiner illustrated the number of journeys made by families with no car and those with a car. I suddenly realised that using probability theory it should be possible to determine the number of families with no car, one car, two cars, etc. using probability distributions and a few independent variables. One could then tabulate the home interview data in a corresponding structure and estimate the number of trips made.<sup>8</sup> 

Wootton and Pick tested various household categories in terms of combinations of income, car ownership and household structure variables and also formulated different probability distributions to estimate the numbers of households in each: 

Once we could classify the number of families by car ownership estimating the trips generated was a fairly straightforward process. Income proved to be important not only in determining the probability of owning a car but also in the level of trip making. The other important variable was the number of people in the family. We spent some time exploring different ways of representing family structures (size, age and children were important), eventually settling on a Poisson distribution to determine the number of people in a family and a binomial to determine the number of children. A strong influence on the choice of categories was the need to maintain reasonable sample sizes. Less important, but relevant, was where a family lived. It was clear that a family was more likely to own a car if they lived in a suburb than if they lived in a city centre, but we could not determine the precise factors involved. We decided to use residential density as a proxy for the location effects.<sup>9</sup> 

In the West Midlands Transportation Study, mean trip rates were established for 108 household categories, which were combinations of various levels associated with three variables: (a) car ownership (0, 1, 21); (b) household income (six levels); and (c) household structure (six levels relating to household size and number of workers) (Wootton and Pick, 1967). This categorisation provided a template for many other UK transportation studies.<sup>10</sup> To test the stability and transferability of their approach, Wootton and Pick investigated the variation in household trip rates in both London and the West Midlands and the extent to which different levels of public transport accessibility would be significant. 

Their studies on London and Birmingham, including a back-casting exercise, suggested that trip generation rates by both car and public transport were reasonably transferable over space and time. They noted: ‘it is encouraging to find families in the same category behave in a similar manner in both areas’, adding that the trip rates were relatively insensitive to accessibility indices. ‘These indices suggest that the effects of changes in levels of public transport service are less important than the household characteristics’ (Wootton and Pick, 1967, 141, 150). 

Trip attraction models could be developed on the same basis, in which land use categories were defined, based on standard industrial classes, and trip rates established for each. In the West Midlands and typical applications that followed, eight categories were applied.<sup>11</sup> In the UK, householdbased category or cross-classification analysis made a dramatic impact on the trip generation procedures applied in practice from the late 1960s onwards. At least in the larger studies, zone-based regression models for trip production quickly fell from grace, although zone-based regression analyses were often retained to forecast trip attractions. 

In the late 1960s and early 1970s various practical and theoretical developments of the category analysis technique took place (Pick and Gill, 1970). From a methodological viewpoint, the approach was quickly recognised to be a form of regression analysis incorporating dummy variables, the dependent variable being the number of trips made by a household and the independent variables recording the presence or absence of a household in the various categories (for example, Douglas and Lewis, 1970, 1971; Douglas, 1973). Analysis of variance techniques were also applied to identify the significance of individual variables and the structure of dependency between the variables over which categories were defined (Dale, 1973, 1977). 

In the West Midlands model, the number of trips generated per day in each household category was further disaggregated by purpose (work, business, education, shopping, social and non-home-based) and by mode (car drivers or motorcyclists, public transport passengers and others, mostly car passengers), and became a fairly widely used method of travel forecasting for those studies that performed modal split prior to the distribution of trips. 

## 3.3.2 Developments in Car Ownership Forecasting

Early forecasts of car ownership in the UK were made on the basis of past trends and comparisons with conditions in the US. ‘Thus in the London Transportation Study (1966) it was assumed that car-ownership in London in 1981 would be similar to levels already achieved in metropolitan Boston, Philadelphia and New York’ (Lane et al, 1971, 162).<sup>12</sup> 

Along similar lines, John Tanner’s influential studies at the UK Road Research Laboratory used a time series approach (Tanner, 1965) involving the estimation of the parameters of a logistical curve, expressing the number of vehicles per person as a function of time. This curve was assumed to reflect that the market penetration of cars would rise, slowly at first, then grow at a fairly constant rate and eventually approach a ‘saturation rate’, S. The initial model contained three parameters, a, b and S, the saturation rate.<sup>13</sup> Forecasts were particularly sensitive to the value of the saturation rate, which was estimated by Tanner on the basis of linear regressions and assumptions relating the rate of growth of car ownership to the actual levels of that variable. Data from the UK and the US were used for this purpose; for a good exposition of this approach, see Ortúzar and Willumsen (2011, section 15.3). Tanner revised his forecasts in 1965, 1974 and 1977, and included more explanatory variables: income per capita, residential density and the cost of motoring. 

By the late 1960s, there was discomfort among some car ownership forecasters with the use of trend extrapolation techniques, which were considered to contain too many assumptions and to be of limited practical use at the local level (e.g., Button et al, 1982; Whelan, 2007). As described above, in the early 1960s, in contrast to adopting the aggregate time series approach, Wootton and Pick were exploring the possibility of using crosssectional data to relate car ownership to household income as a basis for deriving forecasts of both car ownership and the generation of trips. From functions expressing the conditional probabilities of car ownership against income and knowledge of the distribution of household income across a population, the numbers of households with 0, 1 and 21 cars were established. Forecasts could then be made by estimating the number of households in each income group in future periods. 

Using data from the West Midlands, Wootton and Pick derived the set of conditional probabilities of car ownership against household income relative to the price of cars. They noted that ‘evidence has also been gained that these relationships remain remarkably stable from one area to another, even between countries’ (Wootton and Pick, 1967, 144), and assumed these forms would remain stable over time while the distribution of income would change. To test the validity of the technique, they estimated car ownership in the West Midlands over the period 1953–65 using the historical variation in car prices, and obtained ‘good agreement with actual car ownership’ (Wootton and Pick, 1967, 148). 

Over the period to the early 1970s several variants of the above approach were developed in the UK characterised by differences in the functional forms and number and type of explanatory variables. Button et al (1982) gave a full discussion and critique of the various approaches to car ownership forecasting and their application in the UK; for a more recent perspective, see Whelan (2007, section 2). 

## 3.4 DRAWING FROM MICRO-STUDIES: THE ‘GENERALISED COST’ OF TRAVEL

## 3.4.1 Introduction

The impression is often given that the approach to travel forecasting based on ‘micro’ or ‘disaggregate’ models, specified and estimated at the level of the individual, made little impact on the conventional travel forecasting methods of the 1960s. There is some truth in this assertion, but it is more relevant to the US than to the UK. Certainly, during this period, there was no systematic attempt to derive network flows or travel demand by aggregating model results obtained at the individual level. However, there are three reasons why we consider here in a preliminary manner the microlevel or disaggregate approach to modal choice, pioneered by Stanley Warner in his study of Chicago commuters (Warner, 1962): 

1. Studies at the micro-level established the concept of ‘generalised cost’, which was absorbed directly into conventional aggregate multi-stage demand models in the late 1960s in the UK. 

2. During this period, the generalised cost concept provided a bridge between the travel forecasting procedure and the economic evaluation of transportation projects, and attained a standard form. 

3. As early as the mid-1960s, the micro-approach was being referenced in powerful critiques of the conventional styles of analysis. 

We shall have much to say about this class of models in Chapter 4 and, in particular, the marriage of theoretical perspectives based on microeconomics with greater statistical sophistication of dealing with data on individuals. Here we briefly record the background to selected studies of modal choice conducted in the 1960s, and how a standard form of ‘generalised cost’, or ‘disutility’, emerged in the UK, to be widely applied in subsequent travel forecasting models. 

## 3.4.2 Disaggregate Modal Choice Models: Research of Warner and Quarmby

Early disaggregate studies of modal choice were not primarily directed at forecasting, but at understanding, and in some cases measuring the tradeoff individuals were assumed to make between travel time and money cost (interpreted as the ‘value of time’), and more generally determining the range of measurable factors influential in modal choice. In this respect the studies of Warner (1962), Moses and Williamson (1963), Lisco (1967) 

and Lave (1969) in the US, and of Beesley (1965), Quarmby (1967) and Stopher (1969) in the UK, were particularly significant. Reichman and Stopher (1971) and Stopher and Meyburg (1975) provided a detailed review of these studies. Investigations in the late 1960s and early 1970s at the Local Government Operational Research Unit (LGORU) of modelling choice between modes for the journey to work, drawing on the research of Warner, Beesley and Quarmby, are also noteworthy (Gapper and Rolfe, 1968; Rogers et al, 1970; Davies and Rogers, 1973).<sup>14</sup> For a fuller discussion of early UK work on demand analysis and the value of time, see Daly (2013). 

Rereading Stanley Warner’s Ph.D. thesis, Stochastic Choice of Mode in Urban Travel: A Study in Binary Choice, undertaken at Northwestern University (Warner, 1962), one cannot help being struck by how utterly different it was compared with practical transportation study procedures in use at that time. Here was a study of choice between competing travel options based on the trip characteristics and socio-economic attributes of the individuals concerned. Warner’s model of modal selection was specified in probabilistic terms, economic in flavour, with concern for elasticities, and with detailed regard for parameter estimation within a multivariate statistical framework. 

Warner’s main objective was to determine how modal choice was influenced by the travel times and costs of various modes, as well as demographic and socio-economic variables of the travellers, such as income, age and sex. He used data on trips to the Chicago central business district (CBD) from an outer suburban area of Chicago in multiple regression and discriminant analyses to predict the probability of an individual selecting a particular mode in binary choice contexts (car and urban rail transit; car and suburban train; and suburban train and urban rail transit) for work and non-work trips. From the parameter estimates, the significance of different factors in individual choice was determined and the associated demand elasticities derived. In the probabilistic model derived by Warner for modal choice between train and car, the logarithm of the cost ratios for the two modes, and the logarithm of the time ratios were taken as part of the discriminant function to allocate individuals to the modes. 

As Stopher and Meyburg later noted: ‘Following this work, whose significance was not recognised for some time, there appears to have been something of a hiatus in disaggregate, mode-choice work until a number of pioneering efforts were published in the period 1967 through 1969’ (Stopher and Meyburg, 1975, 300). 

Included in the reviews by Reichman and Stopher (1971) and Stopher and Meyburg (1975, Chapter 16) was research undertaken in the mid-1960s by David Quarmby, which was particularly important for the way that cost and level-of-service variables were incorporated in aggregate travel forecasting models in the UK. Moreover, it was central to the methodology applied in the UK for the economic evaluation of transportation projects (section 3.8). 

David Quarmby graduated from the University of Cambridge in 1962 with a degree in engineering and economics, an unusual combination in those days. He moved to the University of Leeds, where after a one-year post-graduate course in management he started his professional life as a lecturer in operational research and subsequently in transport economics. In contrast to that of Stanley Warner, the study undertaken by Quarmby for his Ph.D. thesis, ‘Factors Affecting Modal Choice for the Journey to Work’, and reported in Quarmby (1967), was conducted against a background of considerable practical development of aggregate ‘tripinterchange’ modal split models. By the mid-1960s, the ‘trip-end’ modal split models were gradually being replaced in the larger US transportation studies by trip-interchange models, applied after the distribution of trips in the overall four-step sequence. The innovative modal split model developed by Hill and von Cube (1963) of Traffic Research Corporation of Toronto was, according to Quarmby (1967, 277), ‘undoubtedly the best available for predicting travel within urban areas for aggregated groups of zones, and it is based on reasonable hypotheses of behaviour’. However, Quarmby was critical of the zonal basis of the TRC approach, noting that modal choice was found to be fairly sensitive to level-of-service ratios, and: 

one would expect as much variation of travel time ratios, service ratios and perhaps cost ratios among individual observations within one zone as among the mean values of these variables between different pairs of zones. This is recognised by TRC and is one of the strongest arguments against attempting to use diversion curves and zonal analysis for predicting the use of public transport for particular routes or corridors, or for investigating policy changes on a ‘micro’ basis (Quarmby, 1967, 276). 

He warned of the problems of adopting aggregate zone-based approaches, including the dangers of ecological fallacies and relationships that would lack true behavioural correlations and temporal validity. 

In the theoretical foundations of Quarmby’s study, there was a close relationship between the assumed economic motivation of individuals and the multivariate statistical analysis. Here, Quarmby drew on the discriminant analysis approach adopted by Warner (1962) and the insights obtained from a simpler graphical approach used by Beesley (1965) to determine the trade-off between time differences and cost differences. He summarised the relationship between the underpinning notion of utilities and choice and the statistical technique in the following terms: 

We have thus derived, from first principles, a discriminant analysis solution: from basic notions of disutility and choice advancing to the simple misclassification criterion used by Beesley, and subsequently to a form using total population characteristics, in a way that is both behaviourally and intuitively valid. The relative disutility function becomes what is known as the discriminator or discriminant function (Quarmby, 1967, 304). 

In deciding which independent variables to test, he drew on the results of both Warner and TRC. 

Data for Quarmby’s study of modal choice for the journey to work to the Leeds CBD were drawn from a firm-based survey, yielding 542 observations for commuters who had a choice between car and bus, and 97 between car and train. The following seven factors formed the basis for the initial data analysis: (a) relative overall travel time; (b) relative excess (walking, waiting and transfer) travel time; (c) relative cost; (d) income; (e) car demand ratio (the ratio of the number of driving licences to the number of cars in the household); (f) use of car for work; and (g) ownership of the car by the firm. Quarmby found differences in relative times and costs, as determinants of modal choice, reflected in statistical goodness-of-fit measures, to be consistently better measures than ratios or logarithms. He drew the following conclusion: 

travel time difference, excess travel time difference, cost difference, and the possibility of use of the car at work are all important in influencing modal choice; income is an insignificant factor most probably because of the very small cost differences between modes . . . as also manifested by a small difference between mean incomes for both sets of mode users. It was also found that walking and waiting times are worth between two and three times in-vehicle times; that an average value of time on both modes lies between about . . . 21 percent and 25 percent of wage rates (or, leaving out two significant factors, about one third of wage rates, corresponding closely with Beesley’s results) (Quarmby, 1967, 297). 

While the initial motivation for Quarmby’s study was the need to understand what factors affected the choices people were making, he related: ‘Discovering that I had also thereby elicited a value of time was a fascinating and unexpected by-product!’<sup>15</sup> Quarmby left the University of Leeds in October 1966 to join the Mathematical Advisory Unit (MAU) in the Economic Planning Directorate of the UK Ministry of Transport, then under Alan Wilson’s leadership. There he played a crucial role in the development of the evaluation methodology for land use and transportation schemes. 

Although mode selection in the multivariate statistical studies of Warner, Quarmby and others was sometimes cast in different functional forms and employed different techniques for parameter estimation, they 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/38754b84-3c6e-4874-b89a-d84630ad82f8/219b941875d5b54b6742b7f9dd4c2493b3ee47f667656b959c19baefde56a0bb.jpg)


$$
\mathbf {M} _ {1}
$$

$$
\mathbf {M} _ {2}
$$

Figure 3.1 Probability of mode selection as a function of relative advantage 

gave rise to rather similar ogive-shaped curves; see Figure 3.1. These curves expressed the probability of an individual selecting, or being allocated to, a given alternative (mode) in terms of the relative advantage of one mode in relation to the other. This relative advantage was often reduced to a linear function of the difference between the modal attributes or some transformation of them. We postpone to section 4.2 further discussion of the theory for generating such curves and the subtle differences between their functional forms. 

## 3.4.3 Emergence of the Concept of ‘Generalised Cost’ of Travel

In conventional travel forecasting models the term ‘impedance’ was often reserved for describing the inhibiting character of travel time and geographical separation; as discussed in section 2.3.4, this term was used in the international literature mainly in the early 1960s. Interzonal centroid-to-centroid car travel time was often taken as a single measure of impedance, especially for spatial interaction models (trip distribution). The above studies on modal choice, however, postulated the disutility of travel to be a (typically linear) function of various attributes assumed to be influential in individual mode choice. From the late 1960s in the UK, the terms ‘disutility’ and ‘generalised cost’ were increasingly treated almost interchangeably to describe this linear expression. These terms began to replace ‘impedance’ in network and spatial interaction models. 

Following Quarmby’s findings, the disutility or generalised cost of travel in money units was understood in the UK to represent a linear combination of travel attributes, as follows: 

$$
\text { generalised   cost } = \alpha_ {1} \times \text { travel   time } + \alpha_ {2} \text {   excess   time } + \text { money   cost }
$$

The parameters $\mathbf { Q } _ { 1 }$ and ${ \bf Q } _ { 2 }$ were, respectively, often referred to as the behavioural values of travel time and excess (walking, waiting and any transfer) time. These values varied by income, by trip purpose and over time, and were adapted from Quarmby’s original study. 

As a ‘rule-of-thumb’, excess times were regarded as approximately twice as onerous as in-vehicle time. This factor was usually taken to imply that people were prepared on average to pay double (or more) the amount to reduce excess times by one unit compared with a similar reduction of in-vehicle time. In this regard, the quantitative challenge of improving the relative position of public transport in relation to the car, and thus bringing about significant modal switching ‘through the carrot’ – improving times on the public transport system (average vehicle speed, frequencies and spatial coverage) or reducing fares – against the proverbial ‘stick’ of parking and other restraint policies, became much clearer. 

By substituting the interzonal (centroid-to-centroid) values of the travel attributes into the generalised cost formula, and applying the relative weights derived by Quarmby, the ‘average’ interzonal generalised costs by each mode could be obtained. In the UK, the stage was set for the introduction of generalised cost, with its flexibility in the representation of transportation policies, into the mainstream of conventional travel forecasting practice. According to David Quarmby, who actually referred to ‘disutilities’ in his 1967 study, the term ‘generalised cost’ was coined by Alan Wilson at the Mathematical Advisory Unit.<sup>16</sup> It is to a discussion of his contributions that we now turn. 

## 3.5 THE ENTROPY MAXIMISING APPROACH TO TRAVEL MODELLING

## 3.5.1 Wilson’s Early Work and Its Impact

In 1967 an extraordinary paper was published in the first volume of the new journal Transportation Research, which became one of the most cited papers in the history of urban transportation and regional science. Its author was a University of Cambridge-trained mathematician who, after a period in the theoretical physics section of the Rutherford Nuclear 

Laboratories, had converted to the social sciences by joining the Institute of Economics and Statistics at the University of Oxford in 1966. There, Alan Wilson<sup>17</sup> joined a team led by Christopher Foster,<sup>18</sup> who with Michael Beesley had recently published a seminal paper on cost–benefit analysis applied to the proposed addition of the Victoria Line to the London Underground system (Foster and Beesley, 1963). 

Foster and his colleagues were interested in the impact of such major transportation investments on land use. In that new research environment, Wilson began his research on travel behaviour and the interrelationship between transportation and land use. Reviewing US transportation and urban development models of that period, Wilson was struck by what he later described as ‘fudge factors’ introduced to make the spatial interaction models consistent with outputs from the generation stage. Being familiar with the principles of statistical physics, he immediately saw a correspondence between the partition functions of the statistical mechanics of gases and the ‘balancing factors’ used for the distribution of trips in standard models of that time.<sup>19</sup> 

Wilson’s insight was to interpret the spatial interaction pattern, hitherto viewed in terms of a gravitational analogy, as the most likely arrangement of trips between origin and destination zones that was consistent with the total trips produced by, and attracted to, each zone, and with the total generalised cost of travel of the trip distribution pattern observed in survey data. Although the initial derivation of the ‘doubly-constrained’ spatial interaction model for the journey to work drew on the analogy from statistical physics, Wilson showed how such models were compatible with different interpretations, drawing on ideas from information theory and Bayesian statistics (Wilson, 1970), and later described the procedure as ‘a statistical average of the behaviour of individuals making trips’ (Wilson, 1973a, 288). 

In Wilson’s approach, travel and location models were derived by determining the most likely pattern of trips (or trip proportions) that maximised an entropy function that expressed the number of possible ways that travel could occur, subject to a set of constraints reflecting the information independently available to the analyst.<sup>20</sup> In this constrained maximisation problem, the ‘balancing factors’ of the standard gravity trip distribution models were introduced naturally through Lagrange multipliers accompanying each constraint, ensuring that the distribution pattern was consistent with the ‘trip-end constraints’ determined from the trip generation models. These balancing factors bore a strong (reciprocal) resemblance to accessibility measures and were often interpreted as such.<sup>21</sup> The empirically derived ‘deterrence function’ of conventional distribution models emerged in this approach as a specific form, a negative exponential function of the generalised cost, with an associated parameter ${ \lambda _ { \mathrm { { D } } } } { \cdot } ^ { 2 2 }$ 

In a synthesis of existing spatial interaction models, what Wilson described as a ‘family of models’ could be generated by maximising the entropy associated with the distribution of trips, subject to various constraints to be satisfied by the trip pattern. Thus, ‘doubly-constrained’ (sometimes termed ‘production–attraction-constrained’) journey-to-work distribution models were characterised by independent estimates of the trips generated by workers and attracted to employment opportunities in the various zones obtained from the generation model.<sup>23</sup> ‘Singly-constrained’ (sometimes referred to as ‘production-constrained’ or ‘attraction-constrained’) models pertaining, for example, to shopping and residential choice contexts required the distribution pattern to be consistent with information available at only one end, either the origin or the destination, of the trip. What was both interesting and significant was the expression of such location models as multinomial logit forms, with an added zone-dependent multiplier, or balancing factor, for the journey-to-work model. Later, we will say more about these particular forms and how the demand for travel varied with the generalised cost of alternative travel options. 

Although Wilson’s 1967 paper is mainly noted for its development of a new approach to the derivation of the gravity model from entropy maximising principles, it introduced several significant contributions, which are often overlooked, as follows: 

1. reinterpretation of spatial interaction/location models within a probabilistic (entropy maximising) framework; 

2. derivation of a family of spatial interaction/location models of multinomial logit form that included all existing types; 

3. the introduction of new multi-modal, multi-person-type models of practical importance, in particular a ‘joint distribution modal split’ model, which we denote D-M, of multinomial logit form; 

4. establishment of the concept of generalised cost in zone-based spatial interaction (distribution) and modal split models; 

5. identification of ‘composite impedance’ measures for the distribution of trips in terms of the modal costs; 

6. synthesis of the gravity and intervening opportunity models; 

7. introduction of accessibility measures consistent with the models used for the distribution of trips. 

In introducing the concept of generalised cost in the multi-modal distribution model, Wilson referred to the work of Quarmby, also in the Mathematical Advisory Unit, in these terms: 

It should be remarked that the modal split formula . . . is identical in form to that derived from a statistical approach to modal split using discriminant analysis (Quarmby, 1967). There could be a complete identification if the generalised cost c could be identified with the discriminant function used by the statisticians. If such an identification can be made, then discriminant analysis would provide a method for determining the generalised costs (Wilson, 1967). 

Thus, Wilson took the disutility/generalised cost concept, which in Quarmby’s formulation was used to express hypotheses relating to individual behaviour, and embedded it directly into the forecasting procedures for groups travelling between zones. In section 3.7 we discuss its introduction into the forecasting model adopted in the SELNEC Transportation Study, where, as a first approximation, the relative weightings on the travel attributes derived from Quarmby’s micro-approach were retained in the calibration of the model. 

## 3.5.2 Wilson’s Synthesis: Multinomial Logit Share Models

Wilson (1969, 1970) provided a unified way of viewing the statistical dispersion that could be ‘observed’ in personal location and travel choices accompanying trip distribution, modal split and route split patterns between different zones. With suitable market stratification, he showed that the respective models could all be expressed as proportions or shares of a travel market associated with different locations, modes and routes, respectively, and were of multinomial logit form. These could be derived by maximising an appropriately defined entropy function, subject to any relevant constraints. This formulation resulted in the most likely probability distributions consistent with information available to the analyst. 

In this way, the distribution of trips among various locations (d) and their share among various modes (m) and among various routes (r) could be described, analysed and predicted through multinomial logit expressions,<sup>24</sup> with corresponding parameters $\lambda _ { \mathrm { { D } } } , \lambda _ { \mathrm { { M } } }$ and $\lambda _ { \mathrm { R } }$ , and a suitably constructed generalised cost as the explanatory variable mediating the effect of transportation policies.<sup>25</sup> In this framework the dispersion or spread in trip patterns was interpreted in entropy maximising terms. 

## 3.5.3 Linking the Stages Together: Towards Hierarchical Logit Models

Having derived distribution/location D, modal split M and route split R models, the latter implicit in the assignment model A, each of similar analytic form, within the entropy maximising framework, Wilson (1967, 1969, 1970) considered in detail how they could be linked together. With his eye firmly on the conventional multi-stage travel forecasting models, he explored different ways of linking distribution and modal split models, representing the demand for combinations of destinations and modes. He generated different travel forecasting models, which we refer to as a joint form D-M and a sequential form D/M. The latter, which corresponded to the conventional G/D/M/A arrangement of stages, involved the construction of interzonal costs for the distribution model D as an ‘average’ over, or composite of, interzonal modal costs. Here G refers to trip generation and A to trip assignment; see section 3.7.1. As Wilson noted: ‘The question of determining the form of composite impedance or cost, which is a question of long standing in the construction of transport-demand models, turns out to be very important in an analysis of alternative modal split models’ (Wilson, 1970, 27). 

Similarly, for models that combined modes and routes, corresponding to the sequential arrangement M/A, composite modal costs needed to be specified as an ‘average’ over the costs associated with potentially several routes or services used by travellers in the corresponding modal networks between any origin–destination pair. He argued that these ‘composite impedances’ or ‘composite costs’ that linked together the different stages in the sequential models could not be arbitrary. He proposed at each stage several candidates, the appropriate composite cost in principle being governed by the way that travellers perceived their opportunities, and in practice it would be determined through empirical investigation (Wilson, 1970, 29–33). 

Here we see a rather detailed discussion of the use of similar analytic models of a particular form, the multinomial logit model, arranged either ‘jointly’ or ‘hierarchically’ to represent the demand over combinations of destinations, modes and routes and linked together through composite costs. Specific models would be determined by the values of the parameters $\lambda _ { \mathrm { { D } } } , \lambda _ { \mathrm { { M } } }$ and $\lambda _ { \mathrm { R } }$ and the form of the composite costs selected. Furthermore, Wilson was well aware that, in special cases when the parameters $\lambda _ { \mathrm { { D } } }$ and $\lambda _ { \mathrm { { M } } }$ were equal, and the composite cost took a particular form, which later became known as a ‘logsum’, a sequential arrangement of models D/M would transform mathematically into a joint model D-M of multinomial logit form, in which different combinations of destination and mode were treated on the same footing. 

To the authors’ knowledge, Wilson’s formulation, and the application described in section 3.7, were the first time that travel forecasting was expressed in terms of a ‘hierarchy’ of multinomial logit models, linked together by composite cost functions that expressed the interdependency between the stages and transmitted the effect of policies. For reasons that emerge later, these rather theoretical ideas on alternative model structures turned out to have particular significance. We consider them further in section 3.7 and in Chapters 4 and 5. 

## 3.5.4 Parameter Interpretation, Properties, Computation and Forecasts

Within the formulation of the models from entropy maximisation principles, the parameter l had a specific, although unenlightening, interpretation relating the marginal change in the entropy function at its optimal value to the marginal change in the total cost of travel. Within the resulting multinomial model, the parameter λ also has a functional interpretation and properties that determine the dispersion or spread in the pattern of travel predicted by the model and, in the distribution model in particular, the form of the trip length distribution. It also governed the variously described ‘sensitivity’, ‘response’ or ‘elasticity’ properties of travel demand to changes in the generalised costs. In these travel forecasting models, therefore, the parameter l was the link between modelling the variability or spread in aggregate behaviour at the cross-section and determining the response to transportation policies mediated through the generalised costs. We refer to l as a cost sensitivity or response parameter in the relevant model (Wilson, 1970, Chapter 2). In any practical application, the parameter l would be determined from travel data in a way described later in this section and in section 3.7. 

In general terms it was the limiting property of entropy maximising models, corresponding to $( \lambda \to \infty )$ , that led Wilson to interpret his approach to modelling as injecting some sub-optimality’ in travel or locational behaviour about the ‘optimal’ or ‘lowest cost state’. Specifically, if this limit $( \lambda \to \infty )$ was applied to the ‘singly-constrained’ spatial interaction (location) models, all trips from a given zone were distributed (or allocated) to the nearest (least cost) destination. Similarly, in a mode (M) or route (R) selection context, when the parameters $\lambda _ { \mathrm { { M } } }$ and $\lambda _ { \mathrm { R } }$ of the corresponding MNL model increased without limit, the mode or route option(s) with the minimum generalised cost was selected by all in the relevant market segment. In the ‘doubly-constrained’ trip distribution model, used in modelling the journey to work, the trip pattern for the $\lambda _ { \mathrm { { D } } } \partial \infty$ limit tended towards (one of) the solution(s) of the ‘transportation problem of linear programming’, which was studied by Evans (1973a) in this context. Related applications of this linear programming formulation have been studied in relation to: 

1. logistics models for individual firms; 

2. modelling the spatial flow patterns of relatively homogeneous commodity groups; 

3. distribution models for personal travel forecasting; 

4. generalisations of the Herbert–Stevens model of competitive housing markets (Herbert and Stevens, 1960; Senior and Wilson, 1974). 

Entropy maximising models were thus considered by Wilson to be generalisations of these limiting forms and would therefore almost inevitably allow a better fit to relevant data sets than the corresponding limiting forms. 

In practical applications of the journey-to-work trip distribution and location models, the numerical values of the model parameters and, in particular, the parameter $\lambda _ { \mathrm { { D } } }$ were determined as part of the calibration process that involved reconciling the predicted travel pattern with its various constraints, including the requirement that the predicted mean generalised cost of travel be equated with the observed mean generalised cost in the survey data. Much research was conducted in the late 1960s and early 1970s in order to devise efficient methods for this purpose (Hyman, 1969; Evans, 1971; Batty and Mackie, 1972). 

In a forecasting context, the parameter $\lambda _ { \mathrm { { D } } }$ was implicitly assumed to remain constant over time, and the distribution pattern (or modal/route shares) would adjust to any future changes in the exogenous variables such as the land use arrangement, and the user costs arising from transportation policies or projects. Wilson viewed this assumption of constant $\lambda _ { \mathrm { { D } } }$ as but one hypothesis and explored the consequence of alternatives: for example, (a) that the total travel cost remained constant; or (b) the product of $\lambda _ { \mathrm { { D } } }$ and the total travel cost was constant in forecasting. Hyman and Wilson (1969) showed that the distribution pattern was indeed sensitive to the hypothesis selected. 

Wilson (1973b) took this analysis a stage further, arguing that, if the total travel cost could be independently estimated, a means of determining the parameter l would be directly available, making the parameter l endogenous (or internal) to the model. In generalising this argument, Wilson (1973b; 1974, 162) envisaged travel relationships being determined in a multi-level scheme based on the utility tree concept of Strotz (1957), in which an individual’s travel was described and modelled at various levels of resolution or aggregation, interpreted here as a ‘commodity hierarchy’. More specifically, the hierarchy was expressed in terms of: (a) the amount of travel consumed; (b) the distribution of travel among trip purposes; (c) the distribution of travel among destinations for each purpose; and (d) the distribution of travel among modes. Wilson saw this approach as a way of fruitfully combining economic models with entropy maximising procedures at appropriate levels of the ‘commodity’ hierarchy. As he put it: ‘what has been suggested here is that there is an aggregation level at which economic theory and utility maximising should be helpful (and best) and another, finer level at which entropy maximising remains the most useful procedure’ (Wilson, 1973a, 295). 

## 3.5.5 Wider Contributions of the Entropy Maximising Approach

In less than five years after the publication of his 1967 paper, Wilson produced innovative model applications in several study areas, including: travel forecasting, commodity flows, location and land use, problems of missing information, and general urban systems theory. These were assembled in a research monograph, Entropy in Urban and Regional Modelling (Wilson, 1970), which became a classic text in theoretical geography and regional science. Some further developments, particularly those relating to the foundations of general urban models, were included in a subsequent text (Wilson, 1974). 

The gravity analogue was traditionally used to describe the interaction of activities in space in terms of the attractive influence of ‘mass effects’ and the deterrence effects of increasing transportation distance, times or costs. The entropy maximising approach introduced a probabilistic basis for that interaction. At the heart of model development was the determination of the most likely arrangement for the relevant person trip or commodity flow matrix elements (for example, interzonal flows), which was consistent with a set of constraints appropriate to the problem at hand. These might include some or all of: 

1. logical interdependencies between matrix elements; 

2. consistency with any independent information available to the analyst; 

3. requirement that the predicted travel costs are equated with those observed; 

4. non-negativity conditions on trips or flows. 

His contributions to land use, commodity flow and general urban models would later prove to be particularly significant. What Wilson and other researchers did was to take relatively simple, but incompatible, urban development and multi-stage travel forecasting models and provide not only greater realism in their founding assumptions but also a synthesis in which the demand for travel was derived from urban and regional location decisions (Wilson, 1974, Chapter 11). In this way significant progress was made on the conceptual framework for integrating land use and transportation models. Inevitably this generality was achieved at the expense of additional complexity; the development and implementation of such models would prove to be a protracted process. In Chapters 8 and 9, we consider in much greater detail the integrated models that were taking shape at the end of this period. 

## 3.5.6 Some Reactions to the Approach

As an approach to model building, the entropy maximising method had a wide and enduring role in urban and regional research generally, and in transportation planning practice in the UK in particular (see Wilson, 2010, for recent developments, interpretations and research agenda). It was not however uncontroversial, encouraging the full range of emotions, from the great enthusiasm with which it was initially greeted to outright hostility. The name alone engendered suspicion among those who were uncomfortable with analogies drawn from the natural sciences, drawing comments along the lines of ‘people are not particles’. As Wilson observed, the approach ‘ran into trouble with the Marxists later in the 1970s’.26 

The approach was seldom accepted, and sometimes summarily dismissed, by those who saw the constructive derivation of travel demand functions from behavioural principles as necessary for a convincing forecasting approach for a social system. It was becoming clear that spatial interaction, modal split and related models could be derived from the economic principles of utility maximisation that began to provide a competing paradigm from the late 1960s (for example, Neidercorn and Bechdolt, 1969; Quandt, 1970; Golob and Beckmann, 1971; Beckmann and Golob, 1972). Wilson was equally sceptical about the strict and restrictive optimising assumptions underpinning standard utility maximising models, particularly in a locational context where dispersion, the statistical spread of trips (for example, from a given origin zone), could arise from many sources in historical, economic and social contexts. Nor, as we noted above, did he believe that the entropy maximising approach was necessarily incompatible with micro-economic foundations, which he argued could happily co-exist at different levels of resolution of a system under study. In later reflections, Wilson saw entropy maximisation as a general approach to model building with a range of interpretations, and in his view: ‘Entropy maximising methods can be used to derive robust most-probable state models of large population systems. . . . It is worth emphasising that although this idea was introduced as one borrowed from physics, it in no way relies on this analogy’ (Wilson, 2000, 63). 

We note the remark of Stopher and Meyburg (1975, 251) writing at the end of the period considered in this chapter: ‘one may perhaps question the importance of the controversy between utility-maximization and entropy maximization approaches to the gravity model. Indeed, it appears from the literature that proponents of each approach can muster as many arguments against the other approach as for their own.’ 

Jumping ahead in our story we shall see developments in, and alternative interpretations of, the entropy maximising method, as in the ‘minimum information adding’ approach of Snickars and Weibull (1977). In a further development, Erlander (1977) interpreted the entropy function directly as a measure of dispersion or spread in the travel pattern. He then noted that equivalent trip distribution models could be derived by determining the pattern of trips that minimised overall travel costs consistent with any constraints, including the requirement that the predicted and observed spread of trips, interpreted through an entropy function, be equated. Erlander’s approach exchanged the entropy objective function and cost constraint in the optimisation problem used to derive the distribution model (section 7.4.4.3). 

We shall meet these issues again and will later reflect on a wider range of theories and methods for building comparable models in land use and transportation systems. The implementation of the entropy maximising models of distribution and modal split in UK transportation studies is considered further in section 3.7. 

## 3.6 NETWORK ANALYSIS AND ASSIGNMENT

## 3.6.1 Developments in Public Transport Network Representation and Assignment

In the early 1960s, if they were constructed at all, public transport networks were conceived on the same basis as highway networks. This representation implied a level of connectivity qualitatively different from that associated with the fixed routes, interchanges and timetables that characterised real systems. By the mid-1960s major improvements had been made to the representation of public transport systems in independent initiatives in the UK and US. In the UK, the modern line-based representation of networks was pioneered by Freeman, Fox, Wilbur Smith and Associates (1967). John Wootton recalled ‘poring over maps of railway lines and bus routes plus timetables and wondering how we could realistically represent these services’.<sup>27</sup> His efforts resulted in the TRANSITNET suite of programs (Wootton, 1967; Tressider et al, 1968). 

The new approach accounted appropriately for: (a) the detailed structure of different services; (b) their boarding and alighting points; (c) the relationship between average waiting times and service headways; and (d) the interchange between different services. Within the new representation, information appropriate to route (service) choices could then be made available, with public transport travel times between origin and destination zones suitably expressed as the sum of access, wait, in-vehicle, transfer and egress times.<sup>28</sup> Interchange time penalties could be added to reflect the aversion of passengers to changing services. In turn this information could be used to determine the share of trips by each mode (Tressider et al, 1968). Similar developments occurred independently in the US under contracts with US HUD (Dial, 1967; Dial and Bunyan, 1968) (sections 2.6 and 10.3.1). 

Usually assignments were based on minimum time or generalised cost with simple distance-dependent fare functions. At the assignment stage, passengers were loaded on to a single route between an origin and destination, or split equally between routes (services) of equal time or generalised cost. Later, multi-route algorithms were used to share interzonal travel demand for public transport among groups of services (section  3.6.3). During this period there was little attempt to incorporate formally the effect of vehicle loadings on waiting, boarding and in-vehicle times, although adjustment by inspection would often accompany unrealistic service levels and load factors. 

## 3.6.2 Improved Methods for Road Capacity Restraint Assignment

In the early years of experimenting with capacity restraint methods, several alternative formulations for the time-volume or speed-flow curves were proposed that were to a greater or lesser degree informed by traffic flow theory. In the UK these were typically of a piecewise linear form for different road types with some non-linearities introduced in the flow regime above capacity. Commenting on these level-of-service functions applied in this era, Marcus Wigan (1977, 136) noted: ‘The basic choice between speed flow functions is a three stage series of straight and curved lines, and an exponential or power law function.’ The latter included the fourth power function recommended for use by the US DoT (1972a), as discussed in sections 2.5.5 and 2.5.6. In the UK, curves recommended by the UK Department of the Environment, Advice Note 1A, were commonly used (Wigan, 1977). Their basic form is shown in Figure 3.2. The free-flow speed, free-flow limit and speed at capacity were specific to the road type. 

As in the US, a great amount of experimentation was evident on capacity restraint methods in the 1960s and early 1970s (for example, Almond, 1965; Steel, 1965; Van Vliet, 1973, 1976, 1977; Wigan, 1977). In the incremental method, the number of increments was varied, as well as the proportions applied in successive allocations of the trip matrix. In the iterative method, different proportions were applied to weight successive solutions. As an early example, the traffic assignment procedure employed by the SELNEC Transportation Study (1971, 31) employed three iterations of a ‘serial loading technique’ that corresponds to the method of successive averages, in which the link volumes from each iteration received equal weight; section 7.4.3.2 provides a definition of the method. See also section 2.5.6. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/38754b84-3c6e-4874-b89a-d84630ad82f8/988eaf9e4df0f0245ebcf74945d982c46579aae9bea638ec14dae9de8144947f.jpg)



Source: UK DoE (1971) Advice note 1A.



Figure 3.2 Speed-flow curves widely applied in UK transportation studies after 1970


In view of the limited computing resources available, solutions were often limited to three or four increments or iterations. Study teams needed to strike a balance between the number of increments or iterations and the precision to which equilibrium states were considered to be determined. Until the mid-1970s, the nature of convergence and quality of the solutions, and their dependence on the way iterations or increments were applied, were not well understood. For this reason, it was always the convention to apply the same procedures to seek convergence in different networks for consistent comparisons in evaluation. It became clearer by the early 1970s that some of these heuristic methods did not converge to the equilibrium solution (Van Vliet, 1977), as examined in more detail in sections 7.2.1, 7.4.2.4 and 2.5.6. 

Many transportation study teams found that assigning the future car trip matrices to networks in the peak period, particularly in the ‘donothing’ situation, resulted in severe overload of some and often many links. This result posed a significant dilemma for both the acceptability of the assignment itself and the lack of consistency between the supposedly equilibrium link flows and the level-of-service throughout both the network and the model as a whole. Much lip service was paid in transportation studies of this period to the search for this consistency, and there is some evidence in later studies of the application of ‘feedback’ of modified travel times from the capacity restraint assignment stage to the modal and distribution stages, although this was typically done on an ad hoc basis with no formal measures of convergence offered. 

## 3.6.3 Multi-Route Selection Methods

The above assignment methods were based, for any given flow pattern, on a single numerical value for the travel time (or cost) accompanying each link in the network. Each traveller was assumed to face the same set of times (or costs) of travel along each link. In capacity restraint assignments, the existence of multiple route selection between any pair of zones was considered to be a consequence of the decline of level-of-service (increased travel times) associated with increasing congestion, and was characterised by equal route times, as required by Wardrop’s first principle (Wardrop, 1952). However, it was a matter of empirical observation that multirouteing occurred and could be extensive, even in relatively uncongested networks (Lane et al, 1971). 

As noted in Chapter 2, in the late 1960s various attempts were made to introduce the consequences of imperfect information, the effect of zone sizes and the effect of non-measured factors on route choices. Two approaches in particular, developed respectively in the UK and the US by Burrell (1969) and Dial (1971), led to practical and enduring route selection and associated trip assignment models. Their methods differed according to the procedure for generating acceptable alternative routes between each zone pair (or pairs of nodes) and the rules for allocating portions of the interzonal flow to each. Here we describe Burrell’s approach that was applied in several UK transportation studies from the late 1960s as a means of introducing probabilistic elements into the link level-ofservice and route selection. 

In order to reflect variation in behaviour over the relevant population confronted by a route choice, the assumption that link times were perceived equally by all travellers was relaxed. The detailed nature of the assignment was determined by the probability distributions selected for the journey times on the different links, as well as the number of times these were sampled for route building from each trip origin. In Burrell’s original approach, the distributions of link times took a rectangular form, in which times could take one of eight values. The standard deviation was set at typically 20 per cent of the actual link time. To economise on computing time, the times on each network link were sampled once for each trip origin and shortest route trees built accordingly. The trips from each origin were then assigned on an all-or-nothing basis. The possibility of drawing several link time samples prior to building a number of shortest route trees from each origin centroid and assigning portions of the trip matrix to the network was well recognised as the basis for a stochastic model of route choice (Lane et al, 1971), although the additional computing times did not encourage use of this approach. 

Burrell’s procedure was quite effective at spreading trips over competing routes or services in highway and public transport networks, and was applied on its own, and in conjunction with capacity restraint methods in highway networks. We examine the approaches of Burrell and Dial further in section 7.4.3.1. 

## 3.7 STATE OF PRACTICE AROUND 1970

## 3.7.1 Overview

Towards the end of the 1960s and in the early 1970s, travel forecasting models were being applied in the UK in several different contexts, including the formulation of structure plans and new town development plans, as well as conventional land use – transportation studies undertaken in the conurbations, cities and large towns. For various reasons, including academic review, general audit purposes, and learning from the experiences of the past, the methods of travel forecasting adopted during this period later came under particular scrutiny and comparative analysis (for example, UK House of Commons, 1972; Starkie, 1973; Senior and Williams, 1977; Mackinder and Evans, 1981). 

Mackinder and Evans (1981) provided a summary of the forecasting models or approaches applied in 45 UK studies completed before 1971, as shown in Table 3.1. Although the table does not indicate the progression of modelling practices over time, we can assume that, in the major studies conducted in the late 1960s, household-based category analysis was becoming the dominant method at the trip generation stage, gravity or entropy-based models were used for trip distribution, and road traffic was assigned with capacity restraint for the peak period. Modal split models were applied about equally in pre-distribution and postdistribution forms (we shall use the notation G/M/D/A and G/D/M/A to describe these respective arrangements of the generation, distribution, modal split and assignment stages within the overall model), with the gradual move to the latter form being one of the most significant modelling developments. 


Table 3.1 Summary of techniques applied in UK travel forecasting models up to 1971


<table><tr><td>Stage of model</td><td>Modelling technique</td><td>Studies using technique (%)</td></tr><tr><td rowspan="3">Trip generation model</td><td>Zonal growth factors</td><td>29</td></tr><tr><td>Zonal regression analysis</td><td>17</td></tr><tr><td>Category analysis</td><td>54</td></tr><tr><td rowspan="3">Trip distribution model</td><td>Gravity model*</td><td>63</td></tr><tr><td>Intervening opportunities</td><td>2</td></tr><tr><td>Furness iteration</td><td>35</td></tr><tr><td rowspan="3">Modal split model</td><td>Highway only</td><td>40</td></tr><tr><td>Trip-end modal split</td><td>30</td></tr><tr><td>Post-distribution modal split</td><td>30</td></tr><tr><td rowspan="3">Assignment model</td><td>All-or-nothing</td><td>59</td></tr><tr><td>Multi-routeing</td><td>8</td></tr><tr><td>Capacity restraint</td><td>33</td></tr></table>


Note: * This includes entropy maximising models. 



Source: Mackinder and Evans (1981, Figure 1). 


In this section we summarise the state of UK travel forecasting practice in this period, highlighting the innovations applied in the SELNEC study centred on the city of Manchester (Wilson et al, 1969). Some significant and more general points on the overall structure of UK models are then discussed; in particular, we refer to those attempts to apply closer relationships between the various stages in each of the G/M/D/A and G/D/M/A forms. We conclude the section with a discussion of the validation of models and their predictive accuracy derived from comparison of forecasts to actual outcomes in a design or target forecast year. Sometimes the latter is referred to as ‘out-turn’ data. 

## 3.7.2 Travel Forecasting Models Adopted in the SELNEC Transportation Study

In terms of forecasting methodology, the study was distinguished by its incorporation of most of the important advances in travel forecasting proposed and applied in the UK up to the late 1960s (Wilson et al, 1969; SELNEC Transportation Study, 1971, 1972). In outline the forecasting approach had the conventional four-stage G/D/M/A structure, inelastic at its trip ends. The computational organisation of the programs was ‘loosely based on the TAP package developed by Freeman, Fox, Wilbur Smith and Associates (1967)’, with ‘major innovations . . . introduced . . . in relation to trip distribution and modal split, and in the use of generalised cost concepts to replace travel time’ (Wilson et al, 1969, 337–338). The overall model included: 

1. household-based category analysis for the trip generation stage, in a form very similar to that introduced by Wootton and Pick (1967); 

2. the modern line-based public transport programs (TRANSITNET) introduced in the third phase of the London Transportation Study (Wootton, 1967; Tressider et al, 1968); 

3. capacity restraint road assignments; and 

4. ‘feedback’ of level-of-service variables to the distribution and modal split stages to seek consistency among demand and cost variables. 

Goods vehicle forecasting assumed its usual ‘poor-relation role’ in the overall model with the application of growth factors. 

The study had the direct involvement of the Mathematical Advisory Unit of the UK Department of the Environment, headed by Alan Wilson, which enabled his theoretical developments on the modal split and distribution stages based on generalised costs to make a rapid and smooth transition into practice. A unified approach was adopted in which generalised costs quantified the relative importance of time and money components in the distribution, modal split and assignment stages, with a distinction made between in-vehicle and out-of-vehicle (walking and waiting) time components. The study thus represented a watershed between those forecasting procedures founded on empirically derived diversion curves for modal split and deterrence functions for trip distribution, and analytic forms based on the multinomial logit model in the D and M stages ordered hierarchically. A summary of the travel forecasting procedures adopted in the SELNEC study is given in Table 3.2. 

The SELNEC Transportation Study was not only a major investigation for a large conurbation. In implementing innovative travel forecasting models in the distribution and modal split stages, it was a research application representing work in progress. Several subsequent studies in the UK applied very similar modal split (binary logit) and distribution (singly- and doubly-constrained entropy maximising) models, perhaps with differences in their market segmentation, composite cost structures and methods of parameter estimation. Some studies retained empirical deterrence functions at the distribution stage, but applications of interzonal-based binary logit share models for determining modal split between car and public transport became common. 


Table 3.2 Characteristics of the SELNEC travel forecasting models


<table><tr><td></td><td>Procedure/categories</td><td>Comments</td></tr><tr><td>Survey</td><td>Standard household survey of 3% of the population of 2.5 million by WS Atkins.</td><td>Base year – 1966. Forecast year – 1984.</td></tr><tr><td>Spatial resolution</td><td>362 zones, 6000-plus links in the highway network.</td><td></td></tr><tr><td>Journey purposes</td><td>Home-based work (HBW), school, home-based other (HBO). Non-home-based (NHB).</td><td></td></tr><tr><td>Temporal resolution</td><td>Peak, 24 hours.</td><td></td></tr><tr><td>Transportation variables</td><td>Generalised costs used in assignment, modal split and distribution models.</td><td>Costs defined differently in modal split and distribution models (see below).</td></tr><tr><td>Model structure for passenger journey forecasting</td><td>G/D/M/A.</td><td>Growth factors used for commercial vehicles and external trips.</td></tr><tr><td>Generation model</td><td>Category analysis based on six household structure classes, six income classes and three car ownership classes.</td><td>108 household categories used for trip generation; eight activity categories used for trip attractions; insensitive to transportation level-of-service variables.</td></tr><tr><td>Distribution model</td><td>Doubly-constrained entropy maximising/ multinomial logit.</td><td>Car owner, non-car owner stratification.</td></tr><tr><td>Interface between D and M composite costs</td><td>‘Logsum’ for car owners – see text.</td><td>Distribution parameter <eq>\lambda_{D}</eq> used in ‘logsum’ formula; parking charge and modal penalty removed from generalised cost.</td></tr><tr><td>Modal split model</td><td>Binary logit model based on interzonal generalised costs. Value-of-time parameters obtained from disaggregate studies of modal choice. Split between bus and rail determined at the assignment stage.</td><td>Stratified by two person types (car owners, non-car owners). Generalised cost with parking charges and modal penalty included.</td></tr><tr><td>Assignment (highway) model</td><td>Wardrop equilibrium based on minimum generalised cost routeings.</td><td>Iterative loading with averaging used in capacity restraint approach.</td></tr><tr><td>Assignment (public transport) model</td><td>Minimum cost routeing in line-based public transport system.</td><td>TRANSITNET model used for public transport.</td></tr><tr><td>‘Feedback’ sought for internal consistency of the model?</td><td>Yes, to distribution and modal split models.</td><td>No formal convergence criterion used.</td></tr></table>

Sources: Derived from Wilson et al (1969); SELNEC Transportation Study (1971, 1972). 

The entropy maximising approach did not make an impression on travel forecasting practice in the US, where other methods were available through FHWA computer programs, publications and procedures, and subsequently the Urban Transportation Planning System (UTPS). In the UK however it was increasingly adopted, and entropy maximising entered the travel forecasting lexicon, implying models interpreted in terms of most probable trip patterns at the aggregate (interzonal) level. Distribution and modal split models were analytic functions of the multinomial logit form, and transportation policies were mediated through generalised and composite costs. 

It was not for improving ‘goodness-of-fit’ that entropy maximising models began to make an inroad in the UK into the position held by the BPR gravity model and modal split diversion curves in the US. Rather, the approach was seen to have stronger conceptual foundations than the gravity analogue for trip distribution. In the modal split context, the approach was supported by the analytic forms appearing in concurrent studies at the micro-level. As we noted in section 3.4, it also harmonised with the economic evaluation of schemes based on the generalised cost concept. 

## 3.7.3 Variations in Model Structures

## 3.7.3.1 The rationale for alternative structures

We wish to make a number of comments about the overall travel forecasting model structures and describe some similarities and apparent differences between the approaches applied in the UK and the US. These issues will later emerge to be of great theoretical and practical interest. As noted in Chapter 2, by the late 1960s the position of the modal split model in the overall ordering of the stages, and the choice between the sequential fourstage orders, G/M/D/A and G/D/M/A, was a topic of considerable importance and some contention (Weiner, 1969; Starkie, 1973). As we shall see later, it remains a subject of debate to this day. 

The increasing choice of the G/D/M/A form in major studies undertaken after the mid-1960s was one of the most significant developments in model specification (Starkie, 1973). In the theoretical literature (for example, Wilson, 1967, 1969), we also saw the development of a ‘simultaneous’ structure (G/D-M/A) with the distribution and modal split models specified together. This arrangement did not appear in any major UK transportation study until the early 1970s, however, when it was adopted in Coventry and in the Greater London Transportation Study (Coventry City Council, 1973; Havers and Van Vliet, 1974; Senior and Williams, 1977). 

Since the mid-1960s, the sequential arrangement of the modelling ‘stages’ was often tacitly assumed to reflect an underlying decision process of travellers over the various ‘dimensions’ of choice (for example, Quarmby, 1967; Starkie, 1973). Thus, the commonly applied G/D/M/A structure was associated with a decision sequence in which an individual, after deciding to make a trip (reflected by a frequency choice f), was considered to select the destination d; then the mode of travel m was selected conditional on the destination; and finally the route or public transport service r was selected conditional on the selected mode. Symbolically, we represent this sequential decision process as f�d�m�r. Each successive decision was considered to be conditional on the previous decision. However, there was no clear rationale or empirical evidence for selecting one particular ordering (f�d�m�r) over another (f�m�d�r). 

In the case of the journey to work it was sometimes argued that the selection of residence and/or workplace would precede the choice of mode, justifying a G/D/M/A structure, while for discretionary travel it was sometimes suggested that the reverse might be true, supporting a G/M/D/A structure. More often than not, a common structure was adopted for all journey purposes. Towards the end of the period considered in this chapter, the ‘simultaneous’ structure G/D-M/A, although rarely found in major studies, was justified as a result of an assumed greater interdependency between the destination and mode decisions with the destination and mode ‘selected together’ (symbolically f1d3m1r). This conclusion may well have been inspired by US research conducted in the early 1970s, described in detail in section 4.4. The structures and their assumed decision sequences are shown in Figure 3.3. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/38754b84-3c6e-4874-b89a-d84630ad82f8/d95dae2868f5a6874b951b37a24434ad8979cd9caf022dae71f4fa189749d5ae.jpg)


There were also other considerations in selecting an appropriate model structure, notably: (a) practical convenience; (b) representation 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/38754b84-3c6e-4874-b89a-d84630ad82f8/fc7193c50fd234d34a94a9fb7d386b8ecb3c9fd2341920db7f866b418cb22d18.jpg)



Assumed underlying decision sequence



Note: For notation, see text.


Figure 3.3 Alternative model structures and information flows for travel forecasting and the assumed conditional dependency on the underlying trip decision process 

of captivity to a mode; and (c) the assumed responsiveness of demand to proposed public transport schemes (Hutchinson, 1974; Stopher and Meyburg, 1975). With regard to broad usage of the different model structures applied internationally in this period, Bruce Hutchinson noted: 

In transport studies performed to date in medium- and smaller-sized cities, trip end modal split models have normally been used. . . . The basic assumption of the trip-end-type models is that transport patronage is relatively insensitive to the service characteristics of the transport modes. Modal patronages are determined principally by the socioeconomic characteristics of the trip makers. Transport studies performed in larger urban areas, where the public-transport system is well developed, or where significant improvements in the public transport system are contemplated, have usually employed trip-interchange modal split models (Hutchinson, 1974, 55–56). 

To sum up, the structure of the forecasting procedure, and specifically the position of the modal split stage within it, was at various times justified in the US, Canada and the UK by: (a) practical considerations; (b) variables assumed to influence modal demand; (c) the relative sensitivity of modal split to level-of-service and socio-economic determinants; (d) the prominence of public transport schemes in current transportation systems and in policies to be tested; and (e) the assumed nature of the travel choice process. In fact, no data, surveys or analyses were offered in support of the last view. 

## 3.7.3.2 Joining the stages together

The problem of structural ambiguity and choice of model specification, which form to select from the options G/M/D/A and G/D/M/A, did not end there. For each sequential ordering, M/D and D/M, how were explicit links to be made between the modal split and distribution models to reflect the influence of level-of-service variables within the different stages? In the former this ordering established at the zonal level the differential effect on modal split of accessibilities to different destinations by the two main modes, car and public transport. In the latter they reflected at the interzonal level, as in the SELNEC study, the differential effect of modal opportunities and their levels-of-service on the distribution pattern. 

As noted, in those early studies in the US that adopted a G/M/D/A structure, if the issue was considered at all, the commonly interpreted accessibility variables derived from the denominator of the gravity trip distribution model were used for the purpose, the ratio of the accessibilities by car and public transport being a popular choice of variable (US DoC, 1966; Hutchinson, 1974; Stopher and Meyburg, 1975). A similar example could be found in some UK studies, such as in Glasgow (Scott Wilson Kirkpatrick & Partners, 1969). 

For the more popular G/D/M/A structure, a corresponding problem arose. By the mid-1960s a common method for determining the composite interzonal time for each zonal pair in the gravity model was simply to take the minimum time across modes, which was almost invariably that of the highway mode. This procedure had the advantage of not requiring detailed information about the predicted modal share and was easily generated from the network analysis routines. A review of US practice relevant to this period observed: ‘the travel impedance factors are typically based only on car travel. . . . The full range of travel time and cost factors for all relevant modes of transportation is very seldom included in the impedance factor' (Domencich and McFadden, 1975, 19). But there were clear problems with this approach, as those authors pointed out. Changes in the travel time or cost for those who selected an improved public transport mode might not be reflected in changes to the distribution pattern. 

In the UK there appears to have been considerably more experimentation with different combinations of modal level-of-service variables to insert into the distribution model. In their survey of 25 British transportation studies conducted over the period 1962–73, Senior and Williams (1977) found eight possible methods of combining modal information for distributing trips in the G/D/M/A structure. As in the US, the minimum cost or travel time or generalised cost was widely applied, but various combinations of modal travel times or generalised costs were also implemented, including: (a) weighting by modal proportions; (b) geometric weighting; and (c) the ‘logsum’ measure adopted in the SELNEC study. 

There was also the problem of representing the effect of level-of-service variables on the demand for travel at the generation stage in both the G/M and G/D structures. By far the most common approach was to assume that the demand for travel from a given zone was insensitive to transportation variables. In those few attempts to make the zonal demand for travel elastic with respect to the times and cost of travel, variously defined accessibility variables derived from the distribution model (or a proxy variable denoting distance from the city centre) were incorporated. In terms of additional explanatory power, these attempts were generally not very successful. However, we would emphasise that the dependence of trips generated by a zone on accessibility variables was almost invariably absent throughout this period, a source of considerable criticism of the standard forecasting approach. Indeed, Starkie (1973, 367) commented: It is with regard to making the sum total of travel sensitive to the conditions of travel that least progress has been made. 

With the exception of Wilson’s formulations (section 3.5.3), questions of appropriate linkages between stages of the travel forecasting model were not formulated rigorously nor were the procedures informed by theory. 

For reasons that will emerge later, however, there were many attempts to link the stages in a way that would pass level-of-service variables from one stage to the other to reflect interdependency between them. However, the way that the models were usually calibrated and applied from the ‘top down’ (e.g., in the order G→D→M→A) posed real problems for both specification and implementation. Therefore, modellers often resorted to simplified structural relationships. 

The impression from several transportation study reports of this period is that these structural issues, the ordering and interfacing of the individual steps or stages, were considered to be technical problems to be solved at the discretion of the study team. They did not appear to have been endowed with great conceptual or numerical significance. The lack of a theoretical framework also reinforced the view that the travel forecasting procedure was a set of four (or three if modal split was omitted) somewhat independent stages or ‘submodels’ strung together in a rather ad hoc way. Not only were there conceptual issues to be resolved here; these specification choices had significant practical implications for the organisation, calibration and equilibration of the overall model.<sup>29</sup> Moreover, they were the crucial means by which the effects of policies were to be transmitted throughout the solution procedure and thereby influence the broad pattern of travel. We take up these issues in Chapters 4 and 5, where their full significance is considered further. 

## 3.7.4 Validation and Predictive Performance of the Models

Except when time series data or before-and-after studies were used to assess the stability of parameters such as trip rates (Wootton and Pick, 1967; Downes and Gyenes, 1976), model validity during this period was almost exclusively assessed by the ability of models to provide close correspondence between the predicted and observed patterns of travel in the base year. This correspondence was assessed in the various stages of the model through ‘goodness-of-fit’ statistics, with additional checks made on factors such as screen-line crossings and so on that depended on the output of the forecasting model as a whole. Usually a large amount of ‘fine-tuning’, adjustment of network coding and small changes to the specifications was required before the model was deemed satisfactory. Analysts often found themselves in the predicament of adopting a relatively parsimonious specification and accepting modest ‘fit statistics’ for travel demand patterns (interzonal movements, modal proportions and network flow patterns), or including additional parameters to improve the goodness-of-fit. This approach was sometimes seen as investing in additional accuracy in the base year at the expense of incurring added problems of parameter forecasting over time; the default solution was usually to assume the constancy of such parameters. 

The calibration process for a large urban travel forecasting model of several hundred zones and several thousand network links was an extensive and computationally costly task. The succession of model calibration, adjustment of specification, network checking and adjustment and any recalibration, all in the context of developing forecasts for multiple trip purposes, multiple users competing on the networks and (possibly) multiple time periods, made the attempt to secure a well-fitting model for the base year nothing less than monumental. Few studies attempted additional iterations of the model sequence between demand and assignment in order to obtain consistency with the generalised cost of travel. An attempt to achieve greater consistency was considered a luxury to be treated in a very cursory fashion or not at all. 

The most exacting assessments of the validity of models adopted in this period were those very few ex post comparisons of model predictions with data collected for the year of forecast, sometimes referred to as ‘out-turn data’. Mackinder and Evans (1981) of the Local Government Operational Research Unit assessed the predictive accuracy of a wide range of UK land use – transportation models, following a small investigation of five transportation studies in the US (Institute of Transportation Engineers, 1980). Data were obtained from 44 UK transportation studies conducted during 1962–71 that fell into three categories: (a) urban studies; (b) conurbation studies and land use – transportation studies, including county structure plans; and (c) new town master plans. 

The UK study sought to assess the extent and implications of the various errors and uncertainties associated with forecasts, including: (a) data errors; (b) misspecification errors; (c) errors in the forecasting of exogenous variables such as land use, socio-economic and transportation system variables; and (d) human errors. Because these were related to the actual forecasting date, 15–20 years from the base year, they were particularly influenced by errors in model specification and exogenous variables such as population, employment and car ownership. The findings of Mackinder and Evans (1981) involved the forecasting performance against out-turn results for 12 demographic, socio-economic, modal demand and screen-line crossing variables. Ominously, the authors came to the following conclusions: 

Nearly all of the forecast items considered were overestimated. On average, population was overestimated by 10%, car ownership and household income by 20%, and highway and public transport trips by 30 to 35%. Traffic flows across highway screenlines were overestimated by an average of 13%. An assumption of zero change in the input parameters would not have produced markedly greater forecast errors in any of the items and in many the average errors would have been considerably less. There was no evidence that the more recent transport studies or those that used more sophisticated modelling techniques (up to 1971) performed better than the others. Although the highway trip forecasts were dominated by the errors in the planning variables, there is evidence that the models used for forecasting public transport trips contained errors of specification (Mackinder and Evans, 1981, 1). 

They also noted that errors in forecasts for public transport trips, amounting to an overestimate of 42 per cent, arose both from errors in exogenous factors and from model misspecification. They added, significantly: ‘anecdotal evidence obtained during the feasibility stages of the project and certain of the analyses described in this report lead to the conclusion that optimistic planning forecasts and insufficient checking procedures were the most important factors in reducing the overall accuracy of the forecast’ (Mackinder and Evans, 1981, 26). 

We return in section 5.2, and later in section 9.5 and Chapter 11, to various aspects of goodness-of-fit and the notions of validity adopted in many urban travel forecasting models, particularly those relating to the specification of the models and their ability to generate logically consistent forecasts accompanying policy tests. 

## 3.8 TRAVEL FORECASTS AND THE EVALUATION FRAMEWORK

## 3.8.1 The Widening Evaluation Framework

In the early 1960s the relationship between the travel forecasting procedures and the evaluation framework was rudimentary. It was dominated by operational considerations and measures of the cost and effectiveness of modifying (highway) networks to accommodate future patterns of demand. With the greater appreciation of urban transportation problems, a richer set of objectives emerged by the end of the decade and with them a growing concern for: (a) economic efficiency; (b) the distribution of benefits over space and social groups; and (c) the environmental impact of plans (Lane et al, 1971; Dalvi and Martin, 1973; Prestwood-Smith, 1977). These objectives stimulated research into the relationship between road and public transport network flows, levels-of-service, and the wider impacts of schemes; investigations of energy and environmental effects were developing rapidly.<sup>30</sup> However, in practice, the impacts of increased traffic flows and transportation infrastructure on noise, pollution, pedestrian delay, community severance effects and visual intrusion were assessed in a rather cursory way and conditioned by the quality of the information that could be provided by the forecasting procedures. 

Towards the end of the 1960s, measures of economic efficiency attained an increasingly important role in the evaluation process. In particular, the money value of travel time savings that dominated the ‘quantified’ measures of benefits derived from transportation plans and projects exerted considerable influence. We comment here on specific aspects of the relationship between travel behaviour and user benefit measures, which was destined to have important consequences for conceptualising user benefits, and on the structuring of travel demand models themselves. 

## 3.8.2 Economic Measures: Equilibrium States and User Benefit Assessment

Whether a project was worthwhile or not was almost invariably assessed through a social cost–benefit analysis (SCBA) framework that was applied with varying degrees of sophistication. For determining the economic benefits, the assumed equilibrium measures of travel demand and user (generalised) costs were ‘passed on’ from the ‘bottom’ of the multi-stage travel forecasting procedure to the evaluation stage, where the language of the transportation planner and traffic engineer changed abruptly into the language of the applied transport economist. The travel forecasts were used to assess the consequences of ‘doing something’, in the form of various transportation schemes, in relation to the do-nothing or ‘reference’ situation. The alternatives were sometimes designated the ‘with’ and ‘without’ schemes. The latter was often the consequence of literally ‘doing nothing’ or including previously committed facilities and, very occasionally, some management or restraint measure (Dalvi and Martin, 1973; Starkie, 1973). UK studies in the mid- and late 1960s into the monetary expression of travel time savings, formulated through disutilities or generalised costs and incorporated into user benefit measures, were central to this analysis (Quarmby, 1967; Harrison and Quarmby, 1969; McIntosh and Quarmby, 1972). 

During the 1960s, in urban and regional land use – transportation studies in the UK, there emerged subtle differences between methods for determining the total user benefits accruing from projects, according to what allowance was made for the response of travellers to changes in user costs. Some early studies assumed that, apart from route switching, the change in demand attributed to transportation schemes would be sufficiently small to be safely neglected, and thus evaluation was conducted under a ‘fixed demand’ or ‘fixed trip matrix’ calculation based on changes in route times and costs determined at the assignment stage (Neuberger, 1971). The number of trips between a pair of zones was multiplied by the change in user costs, incorporating the value of travel time saved among other costrelated measures, and then summed over all zone pairs. 

Later UK studies, specifically those that followed the cost–benefit evaluation method applied in phase III of the London Transportation Study (LTS III) (Tressider et al, 1968), sought to accommodate the effect on interzonal demand of user cost changes by adopting the change in consumer surplus as a measure of benefit. An ad hoc extension of the Marshallian consumer surplus measure, which became known as the Rule-of-a-Half (RoH), was proposed during LTS III (Tressider et al, 1968; Lane et al, 1971).31Its origin is attributed to Tim Powell and his colleagues at Freeman, Fox, Wilbur Smith and Associates (Wootton, 2004, 278). This approach for estimating the perceived user benefits derived from a scheme, which became standard practice, involved multiplying the change in generalised cost for each O-D pair and each mode of travel, by the average number of trips for that O-D pair by mode, made in the ‘with’ and ‘without’ schemes. These contributions were then summed over all zone pairs and modes to give a total perceived user benefit. In this analysis it was assumed that the change in user costs would be sufficiently small that any curvature of the demand function could be safely ignored and, furthermore, that income effects would be negligible (Neuberger, 1971; Williams, 1976; Jara-Diaz, 2007). This RoH measure,<sup>32</sup> a key link between the forecasting process and the economic assessment, was often applied to different trip purposes and modal splits and sometimes subject to sensitivity tests with respect to variation in the value-of-time parameters (Dalvi and Martin, 1973). To this day, it remains the most widely applied measure of user benefit accruing from transportation schemes. Jara-Diaz (2007) offered an extended discussion of the approach and its theoretical basis. 

## 3.8.3 Neuberger’s Analysis of User Benefits

Henry Neuberger [1943–1998] derived some intriguing results that would later turn out to be of considerable theoretical and practical significance for both demand analysis and the evaluation of land use – transportation plans. In Neuberger (1971) he considered three alternative approaches of increasing sophistication for calculating the user benefits arising from land use and transportation projects (see also Wilson and Kirwan, 1969). These methods entailed different assumptions and approximations for treating the forecast of traveller responses to those projects, the first two having already been noted above. They may be summarised as follows. 

Method I simply ignores the demand response, apart from route switching; the user benefit is derived from the reduction in perceived user cost for each zone pair. Method II is based on the Rule-of-a-Half as a marginal approximation to the change in the Marshallian consumer surplus measure. Method III is a generalisation of the Marshallian measure due to Hotelling (1938); it consists of the (path) integral of demand with respect to user cost between the initial and final generalised cost states.<sup>33</sup> 

Method III was of particular interest to Neuberger. It sought to accommodate the mutual changes of demand and all interzonal user costs arising from a modification to the transportation networks, and took explicit account of the curvature of the demand function between the initial and final equilibrium cost states. The technical details underpinning the approach need not concern us here other than to note that Hotelling’s generalised consumer surplus measure is defined unambiguously only if certain ‘integrability conditions’ are satisfied by the demand function (Hotelling, 1938; Neuberger, 1971). These conditions express a form of ‘cross-symmetry’ in the responses of any two different groups of travellers under a change in the generalised costs of travel of the alternative group.<sup>34</sup> 

By good fortune (was it a coincidence?), these mathematical conditions were satisfied for demand models expressed in multinomial logit form, which were increasingly applied in the UK by the late 1960s for determining both the distribution of trips and their modal split. Furthermore, for the MNL function the required consumer surplus measure could be calculated exactly. Therefore, in principle, it was not necessary to invoke a linear approximation to the demand curve underlying the RoH. From the MNL distribution model, the user benefits associated with each zone could be expressed in terms of the number of trips generated in that zone multiplied by the change in the natural logarithm of the denominator of the MNL model evaluated in the ‘after’ and ‘before’ states. What was of immediate interest about this rather esoteric procedure was that the denominator was commonly interpreted as an accessibility measure to all opportunities from that zone.<sup>35</sup> 

This result showed that the measures of economic user benefit for such models of MNL form could be derived from either: 

1. the trip pattern and generalised costs in the do-something and donothing states, approximated by the RoH, and summed over all origin–destination zone pairs in the study area (Method II); 

2. the trips generated in each zone and the change in (the logarithm of) the accessibility measure computed in the do-something and donothing states, summed over all trip origin zones in the study area (Method III). 

Neuberger extended the application of Method III to situations where both the land use and transportation costs were subject to change. The change in consumer surplus again resulted in expressions involving terms previously interpreted as accessibility measures (Neuberger, 1971, 68). 

Thus, in the context of the spatial interaction share models of MNL form, Method III could be used to generate more precise measures of user benefit, accounting for the curvature of the demand function. For typical projects, the difference between Method II and III estimates of user benefit was in the range of 2–5 per cent (Neuberger, 1971; Williams and Senior, 1977). For transportation projects that resulted in modest changes in user costs, the RoH measure turned out to be a satisfactory approximation. For larger changes in user costs, associated with such projects as estuary crossings or completely new land use and transportation opportunities, however, Method II could result in significant inaccuracies, or be invalid. In these cases, and for demand models of multinomial logit form, recourse to Method III was available. 

However, as Neuberger recognised, a far more important conceptual issue emerged: 

it shows the relation between economic evaluation on the one hand and the notions of accessibility and comfort and convenience on the other: hitherto these have usually been regarded as completely unrelated. . . . There is a close connection between economic analysis and the measurement of accessibility, and that the two do not need to be assessed separately (Neuberger, 1971, 64, 66). 

Accessibility measures and benefits could thus be closely integrated with the standard user benefit analysis. 

The full significance of these results was not apparent in the early 1970s. Moreover, it was unclear whether they could be extended to more complex travel forecasting models such as the G/D/M/A forms being used in practice. Indeed, it seemed unlikely, since the conventional demand functions did not satisfy the technical symmetry conditions noted above for the consumer surplus measure to be unique, except in very special cases. But it raised the question: how could the travel demand relations used in practical transportation studies, involving generation, distribution, modal split and assignment models, be formulated so as to allow an extension of Neuberger’s result? If this could be achieved, it would forge a closer integration between the models used to forecast the response of travellers to changes in the transportation networks and land use arrangements, on the one hand, and the economic measures of welfare change associated with that response and interpreted in terms of accessibilities, on the other. This issue will later take centre stage in our story. 

## 3.9 CONCLUSION

By the mid-1960s, the systematic study of urban transportation and methods of travel forecasting had been successfully transferred from the US and Canada and incorporated into the UK transportation planning process. Within a period of a few years, considerable experience in their application had been gained and local innovations were evident. While still recognisably the outgrowth of the earlier studies in Detroit, Chicago, Toronto and other metropolitan areas, major practical developments in the UK resulted in a proliferation of models and methods reflecting an evolution of objectives, information requirements and state of the art in travel forecasting. The resulting variation of methods is important for our story. It was not only against widely applied forms, but also against the leading edge of practice, that progress could be assessed and against which subsequent competitors would need to be compared. As becomes clearer in later chapters, such assessments were seldom performed. 

There was significant progress in addressing some of the problems of urban travel forecasting of the early 1960s; it is easy to discount this achievement in the light of what was to come. Much of that advance was common to the UK and US: 

1. improved representation of passenger behaviour in public transport systems and its application in the assignment of demand to services; 

2. modal split models that were more sensitive to travel time and cost variables; 

3. refinements in the modelling of congestion in road networks; 

4. a limited practical incorporation of ‘feedback’, to seek consistency between the demand for travel and the level-of-service variables entering different parts of the forecasting procedure. 

Other innovations appear to have been more fully developed in the UK. By the end of the 1960s, advanced urban travel forecasting models contained some or all of the following: 

1. model specifications that addressed the greater degree of the variability of travel behaviour within zones, particularly through householdbased category analysis at the generation stage; 

2. establishment of travel demand models formulated in terms of generalised costs that began to reflect behavioural discrimination and choice, and provided a succinct means of representing transportation policies; 

3. a new theory of statistical dispersion in travel patterns, the entropy maximising approach, that enabled a synthesis of the distribution and modal split stages based on share models of multinomial logit form; 

4. composite cost formulations of varying sophistication that allowed an interdependency between the different stages of the model to be established, and the effects of policies represented by changes in generalised costs, to be transmitted through the assignment, modal split and distribution stages of the travel forecasting process; 

5. a closer integration between demand analysis and the method for calculating economic user benefits founded on generalised costs and the Rule-of-a-Half consumer surplus measure. 

The leading edge of practice in the early 1970s was perhaps best described as a ‘hybrid’ approach that drew on ‘disaggregate’ concepts and methods, household-based category analysis for trip generation, and generalised costs derived from the modal choices of individual travellers, grafted on to the conventional zone-based approach. By introducing new concepts and procedures within all stages of the forecasting procedure, these efforts were seen by many as a strengthening process. 

At this point it is important to mention the collaborative and collegiate nature of several of the advances made in travel forecasting and economic evaluation in the period 1966–70, in particular the pivotal role played by the Mathematical Advisory Unit at the [UK] Ministry of Transport, headed by Alan Wilson from 1965 to 1968. As David Quarmby, who joined the MAU in 1966, noted: 

It was an incredibly fertile period; the academic publications tend to be in the name of one or two individuals, and certainly Alan Wilson’s own personal contribution was enormous, but you only have to see the huge range of really innovative output in the form of MAU notes to realise that this was a group of individuals who working with economists like Henry Neuberger elsewhere in the Economic Planning Directorate was pushing back the frontier on several fronts. I think this phenomenon and this period is quite unique in the annals of Whitehall; and it is a testament to Christopher Foster’s vision, his leadership and ability to persuade senior civil servants and Ministers that it all mattered.36 

John Wootton also attested to the collaborative nature of this key period, recalling: ‘with Alan Wilson at the Ministry of Transport we were constantly bouncing ideas and papers off one another’.<sup>37</sup> Although we have emphasized advances in the larger transportation studies, particularly those which had a research focus, it is important to note that the MAU was also influential in the work undertaken in the smaller cities and towns. <sup>38</sup> 

However, there were also many examples of transportation studies that incorporated few of the above innovations, which caught the eye of critics. Also, in relation to growing requirements overall progress was being made rather slowly and against a moving target. The transportation planning framework was evolving, and what was emerging was a lengthening list of objectives, a wider range of policies, and evaluation frameworks that required greater precision in the information sought. Furthermore, there were growing expectations for the speed and cost with which data could be gathered and travel forecasting procedures could be implemented. 

In both the US and the UK, at the start of this era there was considerable sympathy, even enthusiasm, for the application of mathematical models in travel forecasting and transportation policy analysis. By the early 1970s, in spite of the achievements made, the conventional methods were beginning to take a battering, as we noted in section 2.7. The role and purpose of the forecasts within the planning framework, the theoretical foundations of the models, the practical procedures for generating appropriate information for the evaluation of projects and policies, and the ‘policy sensitivity of the models were all subject to attack. Prior criticism was revisited and expressed more forcefully, confidently and systematically. 

The charge of ‘policy insensitivity’ was of central importance and now tended to imply one or more of the following criticisms (Charles River Associates, 1972; UK House of Commons, 1972; Ben-Akiva, 1973; Starkie, 1973; Wachs, 1973): 

1. The models failed in some or all parts of the forecasting process to reflect the full range of changes in price and level-of-service variables deemed to represent the policies. 

2. The models embodied a limited range of behavioural responses to policies. While the more advanced models, through generalised and composite costs and feedback, could reflect the effect of policies through route, mode and destination switching, progress in representing the influence of policies on timing of travel, car occupancy, trip frequency, car ownership and land use arrangements was very limited or non-existent. 

3. With their limited market segmentation, the models lacked, particularly in post-distribution modal split models, the variation of socioeconomic conditions to fully represent limited choice and captivity to either public transport or car. 

4. The models, specified and estimated at the zonal level and for long daily time periods, lacked spatial and temporal precision, particularly in their ability to address the subtleties of fare policies and parking  charges, or the consequences of new and improved public transport facilities. 

5. Only motorised modes were treated in any detail; and representation, let alone policies towards walking and cycling, were treated either crudely or not at all. 

6. Emphasis was often on peak hour problems and policy impacts on associated journey-to-work movements. Progress in modelling the effect of projects and policies on other types of journeys, such as those for business and goods movement, was considerably slower. 

7. The models were often deemed too spatially aggregated to produce useful information pertaining to groups distinguished by socioeconomic characteristics and location. 

There were also important unresolved questions relating to the specification of the travel forecasting model as a whole: 

1. What overall structure should be adopted and why? 

2. Were the relevant alternatives confined to the G/D/M/A, G/M/D/A and G/D-M/A forms? 

3. How were the underlying decision processes of travellers for different trip purposes reflected in the model forms? 

4. How should the different stages be linked together so that policies would influence the several aspects of behaviour represented by the model? 

5. To what extent did all this matter? 

These were questions that remained in the air in the late 1960s and early 1970s. 

Travel forecasting models were increasingly seen by many in the planning community as a whole, sometimes by their users, and certainly by their critics, as monolithic black boxes. Expensive in resources, the models appeared incapable of delivering in a timely manner the sort of detailed economic, social and environmental indicators increasingly required by planning agencies (Lee, 1973; Starkie, 1973; Wachs, 1973; Bruton, 1975). Frequently, too much time was devoted to developing the model and not enough time to exhaustive testing of alternative policy options. According to Bruton (1975, 21), the transportation planning process was ‘too concerned with the technical problems associated with traffic estimation and network planning, and too little concerned with the transport needs of the community at large’. 

Public opposition to road construction schemes on a grand scale was growing. Energy conservation, air quality, noise abatement, road safety and the accessibility provision of particular groups were beginning to emerge as important considerations among the criteria by which transportation schemes and policies would be judged. In the US, the UK and many other countries, the initial strong emphasis of urban transportation planning on road network development had moved on to address public transport investments and even restraint schemes. However, most transportation budgets were still dominated by highway schemes, often assembled from plans compiled years, even decades, earlier, in order to ameliorate congestion and cater for increased mobility for current and future car users. 

Then, suddenly the world changed. The first oil shock occurred in late 1973, with its profound economic consequences that gave rise to a period of austerity and of cut-backs in transportation budgets in many industrialised countries including the US and the UK. The era of ambitious large-scale capital projects gave way to one where greater emphasis was placed on public transport initiatives, transportation systems management and a range of shorter-term measures, including various parking instruments and restraint mechanisms, and car pooling incentives in the US. The conventional forecasting methods, developed in both the US and the UK, were not particularly well suited for the policies contemplated in this new era (Ben-Akiva, 1973; Brand and Manheim, 1973; Domencich and McFadden, 1975). Marvin Manheim [1937–2000] commented on the continued relevance of the traditional four-step approach, or the urban transportation model system (UTMS), as he preferred to call it: 

The UTMS was a major accomplishment for its time. The profession and the governmental transportation agencies (federal, state and local) must recognise that the UTMS is no longer satisfactory; it is neither relevant to the practical issues that must be addressed in the urban transportation studies of today . . . nor acceptable when viewed from a theoretical perspective. The UTMS should be neither completely discarded nor allowed to remain unchanged as the basic working tool of urban transportation analysis. A new generation of transportation analysis tools is required. Development of new systems should build on the several directions of current research, as well as the practical experience gained from the UTMS. The recommendation is that we begin by asking not whether but how (Manheim, 1973, 35). 

How this challenge was taken up is the subject of the next two chapters. 

## NOTES



1. en.wikipedia.org/wiki/Colin_Buchanan_(town_planner) (accessed 4 November 2013). 





2. In the early days of the 1960s the ‘multi-step’ terminology, employed in the US, was in 



common use in the UK. Increasingly, the term ‘multi-stage’ was adopted in the UK. In this chapter ‘multi-step’ and ‘multi-stage’ are used interchangeably. 

3. The first London Traffic Survey began as a roads-only study; some 30 000 households were selected for the home interviews. As John Wootton recalled (personal communication with Huw Williams, 2010), ‘It was Gerry Drake, the Director of the study, who persuaded London County Council/Greater London Council and Ministry of Transport to expand the work to include public transport and a further 10 0001 households were added. This also provided one of the incentives for the later development of the public transport assignment procedure. 

4. John Wootton, personal communication with Huw Williams, 2010. 

5. John Wootton, personal communication with Huw Williams, 2010. 

6. Martin Richards, personal communication with Huw Williams, 2013 

7. See Stopher and Meyburg (1975, Chapter 9) for an extended review. 

8. John Wootton, personal communication with Huw Williams, 2010. 

9. John Wootton, personal communication with Huw Williams, 2010. 

10. More details on the form and estimation of the distributions for determining the future distributions of households over the categories can be found in the paper by Wootton and Pick (1967, 143–148) and in the textbooks by Wilson (1974. 136–140) and Ortúzar and Willumsen (2011, section 4.3). 

11. The categories employed by Wootton and Pick were related to aggregations of standard industrial classes for seven of the categories and residential land use for the eighth. The number of trip attractions to a given zone was then written as the sum over the contributions from the different categories. This involved multiplying the intensity of activity in the different categories in each zone by the corresponding rate at which trips were attracted per unit of activity. For further details see Wootton and Pick (1967, 152) and Wilson (1974, 140). 

12. For the London Transportation Study (1966), see Freeman, Fox, Wilbur Smith and Associates (1966). 

13. Early forms of the logistical model adopted by Tanner for car ownership forecasting related the number of cars per capita CO to time t as follows: 

$$
C O _ {t} = \frac {S}{1 + \beta \exp (- \alpha S t)}
$$

in which S (the saturation level), and a and b are parameters to be determined. For a discussion of the estimation of these parameters, and subsequent modifications to the basic model form, see Tanner (1965) and Button et al (1982). 

14. The authors are grateful to Andrew Daly for discussion of the LGORU studies. 

15. David Quarmby, personal communication with Huw Williams, 2011. 

16. David Quarmby, personal communication with Huw Williams, 2008. 

17. en.wikipedia.org/wiki/Alan_Wilson_(academic) (accessed 5 June 2014). 

18. en.wikipedia.org/wiki/Christopher_Foster_(economist) (accessed 5 June 2014). 

19. Alan Wilson, personal communication with Huw Williams, 2007. 

20. The entropy of a physical system is an expression of the disorder arising from the different ways its state can occur. In this social system it relates to the number of possible wavs in which a trip pattern could arise from different arrangements of the trips. This is also related to the statistical dispersion in the trip data. 

21. In the doubly-constrained form the balancing factors accompanying the origin and destination constraints were explicit and treated on an equal footing, although one or the other set of constraints could be used to make one set of balancing factors explicit, as in the BPR manuals. 

22. In Wilson’s writing this parameter was usually given the symbol b. For reasons that will become clear we shall use the symbol $\lambda _ { \mathrm { { D } } }$ when discussing the distribution model. 

23. Wilson’s ‘doubly-constrained’ model, widely used to forecast the spatial distribution of work trip journevs, is derived by determining the non-negative trip pattern $\{ T _ { i j } \}$ which maximises the entropy function s, subject to the independent constraints reflecting information available to the analyst. These include the requirement that the trips generated by, and attracted to, any zone are equal to the values derived from the generation model, and the requirement that the predicted trip cost is equal to that observed in the data: 

$$
\max \sigma = - \sum_ {i j} T _ {i j} \ln T _ {i j}
$$

$$
\sum_ {i} T _ {i j} = O _ {i} \text {   for   all   } i
$$

$$
\sum T _ {i j} = D _ {j} \text {   for   all   } j
$$

$$
\sum_ {i} ^ {i} T _ {i j} c _ {i j} = C
$$

$$
T _ {i j} \geq 0 \text {   for   all   } i \text {   and   } j.
$$

Here $O _ { i }$ is the number of trips generated by the activity in zone i and $D _ { j }$ is the number of trips attracted to the activity in zone j. In the journey-to-work model these are related to the population and employment in the respective zones. The solution to this constrained optimisation problem is given by: 

$$
T _ {i j} = a _ {i} b _ {j} O _ {i} D _ {j} \exp (- \lambda_ {D} c _ {i j})
$$

in which the balancing factors, on substitution, are given by: 

$$
a _ {i} = \left[ \sum_ {j} b _ {j} D _ {j} \exp (- \lambda_ {D} c _ {i j}) \right] ^ {- 1}
$$

$$
b _ {j} = \left[ \sum_ {i} a _ {i} O _ {i} \exp (- \lambda_ {D} c _ {i j}) \right] ^ {- 1}
$$

The model may also be written in the form: 

$$
T _ {i j} = O _ {i} \frac {b _ {j} D _ {j} \exp (- \lambda_ {D} c _ {i j})}{\sum_ {j} b _ {j} D _ {j} \exp (- \lambda_ {D} c _ {i j})}
$$

24. Thus, the distribution or location, modal share and route split share models considered by Wilson take the following multinomial logit share forms: 

$$
p _ {i j} = \frac {A _ {j} \exp (- \lambda_ {D} c _ {i j})}{\sum_ {j \in J} A _ {j} \exp (- \lambda_ {D} c _ {i j})}; \quad p _ {m} = \frac {\exp (- \lambda_ {M} c _ {m})}{\sum_ {m \in M} \exp (- \lambda_ {M} c _ {m})}; \quad p _ {r} = \frac {\exp (- \lambda_ {R} c _ {r})}{\sum_ {r \in R} \exp (- \lambda_ {R} c _ {r})}.
$$

with $j { \in } J$ denoting an alternative $j$ in a set of destinations J available from location $i ;$ $m \in M$ a mode m in the set of modes M available, and $r \in R$ a route r in a set of routes or services available between an arbitrary origin–destination pair. $A _ { j }$ is here a measure of attraction of zone $j .$ In general, the set M is dependent on person type (such as those with a car available and those without). The parameters $\lambda _ { \mathrm { { D } } } , \lambda _ { \mathrm { { M } } }$ and $\lambda _ { \mathrm { R } }$ determine both the dispersion (spread) of the trips over the various options and the response of the respective distribution, modal and route shares to changes in the relevant costs. 

25. Although most of Wilson's model development with destination, mode and route alternatives was based on the negative exponential function, as in notes 23 and 24, he argued that the functional form describing the variation of demand with the travel attributes (e.g., under increasing spatial separation) would actually be determined by the way in which people perceived travel costs and that this might depend on the length of the trip Thus, if generalised costs, or their components, were perceived logarithmically instead of linearly, the negative exponential terms would be transformed into power functions (see, for example, Wilson, 1970, 34–35). This allowed a link to be established with the class of abstract mode models applied in the mid-1960s, as, for example, in the model of Quandt and Baumol (1966). 

26. Alan Wilson, personal communication with Huw Williams, 2007. 

27. John Wootton, personal communication with Huw Williams, 2010. 

28. This sum could be weighted to reflect the different importance of components in the generalised cost between the origin and destination. 

29. Here, equilibration is interpreted as a method for seeking consistency of level-of-service (travel times and costs) throughout the demand model. 

30. In the UK other key studies, such as the Roskill Commission into the siting of the third London airport and the Greater London Development Plan Inquiry, also were important drivers for the development in methods of environmental assessment. 

31. en.wikipedia.org/wiki/Economic_surplus (accessed 11 March 2014). 

32. If the trip and generalised cost matrix elements for the zone pair $( i , j )$ and mode m are written $T _ { i j m }$ and $c _ { i j m }$ and the superscripts 1 and 2 denote their computation in the initial (do-nothing or reference) and final (do-something) equilibrium states, the user benefit $U B ,$ , which is given by the change in consumer surplus, is approximated by the Rule-ofa-Half (RoH): 

$$
U B = \frac {1}{2} \sum_ {m} \sum_ {i j} \left(\left(T _ {i j m} ^ {(1)} + T _ {i j m} ^ {(2)}\right) \left(c _ {i j m} ^ {(1)} - c _ {i j m} ^ {(2)}\right)\right)
$$

33. If $D _ { \sharp } ( c _ { 1 } . . . c _ { \sharp } . . . c _ { N } )$ represents the demand for a travel-related option $A _ { \xi }$ out of a set of N alternatives $( A _ { 1 } . . . A _ { \xi } . . . A _ { N } )$ , the generalised costs of which are given by $( c _ { 1 } . \cdot . c _ { \xi } . . . c _ { N } )$ the change in generalised consumer surplus is given by: 

$$
\Delta C S = - \sum_ {\xi} \int_ {Q} D _ {\xi} (c _ {1} \dots c _ {\xi} \dots c _ {N}) d c _ {\xi}
$$

in which $Q$ is the path of integration between the initial and final cost states $c ^ { ( 1 ) } = ( c _ { 1 } ^ { ( 1 ) } . . . c _ { \xi } ^ { ( 1 ) } . . . c _ { N } ^ { ( 1 ) } )$ and $c ^ { ( 2 ) } = \mathsf { \breve { ( } { } } c _ { 1 } ^ { ( 2 ) } . . . . c _ { \xi } ^ { ( 2 ) } . . . c _ { N } ^ { ( 2 ) } )$ , respectively (Neuberger, 1971). It was later shown by Williams (1976) that the Rule-of-a-Half measure of user benefit: 

$$
\Delta C S \cong \frac {1}{2} \sum_ {\xi} ((D _ {\xi} ^ {(1)} + D _ {\xi} ^ {(2)}) (c _ {\xi} ^ {(1)} - c _ {\xi} ^ {(2)}))
$$

can be generated within the Method III framework by taking a linear path of integration and applying a first order approximation for the expansion of the demand function between the initial and final cost states. For a more extensive discussion of the assumptions and developments of this approach, see Jara-Diaz (2007). 

34. Broadly, this symmetry condition requires that the change in demand $D _ { \xi }$ for a particular option $A _ { \xi }$ under a marginal change in the cost $c _ { \Psi }$ of a substitute $\boldsymbol { A } _ { \boldsymbol { \Psi } }$ is equal to the change in the demand $D _ { \Psi }$ for $\boldsymbol { A } _ { \boldsymbol { \Psi } }$ under a marginal change in the cost of $c _ { \xi }$ of $A _ { \xi } .$ . More formally, the generalised surplus change is unambiguously defined only when the following symmetry or integrability conditions hold: 

$$
\frac {\partial D _ {\xi}}{\partial c _ {\psi}} = \frac {\partial D _ {\psi}}{\partial c _ {\xi}} \text {   for   all   } A _ {\xi}, A _ {\psi}.
$$

35. For a demand function of the form: 

$$
T _ {i j} = O _ {i} \frac {A _ {j} \exp (- \lambda_ {D} c _ {i j})}{\sum_ {j} A _ {j} \exp (- \lambda_ {D} c _ {i j})}
$$

in which $A _ { j }$ is here a measure of the attraction of zone $j ,$ the measure of user benefit accompanving a change in the user costs from $c ^ { ( 1 ) }$ to $c ^ { ( 2 ) }$ is given (Neuberger, 1971) by; 

$\Delta C S = \Sigma \ { _ { i } } \ O _ { i } ( B _ { i } ^ { ( 2 ) } - B _ { i } ^ { ( 1 ) } )$ in which $B _ { i } = \frac { 1 } { \lambda _ { _ D } } \ln \left( \sum _ { j } A _ { j } \exp ( - \lambda _ { _ D } c _ { i j } ) \right)$ 

or 

$$
\Delta C S = \frac {1}{\lambda_ {D}} \sum_ {i} O _ {i} \ln \left(\frac {\sum_ {j} A _ {j} \exp (- \lambda_ {D} c _ {i j} ^ {(2)})}{\sum_ {j} A _ {j} \exp (- \lambda_ {D} c _ {i j} ^ {(1)})}\right)
$$

where ln (x) again denotes the natural logarithm of $\mathbf { X } .$ 

36. David Quarmby, personal communication to Huw Williams, 2011. 

37. John Wootton, personal communication to Huw Williams, 2008. 

38. An example of this involvement was the development of the software program COMPAĆT, which the UK MoT encouraged some studies to use. Furthermore, UK MoT officials, such as Roy Spence, A.E. Fieldhouse and Gordon Wells, used their involvement in studies for the cross-fertilisation of methods and ideas and learning from successes and failures (Martin Richards, personal communication with Huw Williams, 2013). 

## 4. Travel forecasting based on discrete choice models, I

## 4.1 INTRODUCTION

The early 1970s was the beginning of a golden age for travel demand analysis and forecasting. Progress made in the following two decades still has major theoretical and practical relevance today. Innovations were achieved in all phases of model development and application: survey design and sampling methods, model specification, parameter estimation, validation, aggregation, and forecasting, policy analysis and evaluation. The framework established in this period also allowed traditional methods to be subjected to detailed scrutiny, which had quite unforeseen consequences for the validity of travel forecasting models based on the four-step approach. For the purposes of our review, we divide this material into two parts. In this chapter we consider advances in the short but formative period 1970–76, ending with several practical applications of the new forecasting methods in the US (Spear, 1977). This period is largely associated with the emergence of a behavioural approach at the individual level, based on the economic analysis of choice between travel-related alternatives, and the formulation and application of the multinomial logit (MNL) model. These investigations were mainly associated with modal choice; however, increasingly complex choices were considered. Advances following this initial period are reviewed in Chapter 5. 

At the conclusions to Chapters 2 and 3, we noted the rising criticism of traditional travel forecasting methods which was directed at their theoretical and statistical deficiencies, their limitations in the representation of behaviour and the effects of policies, and their lack of precision in generating information of relevance to the evaluation of policies and projects. By the early 1970s, in many parts of the industrialised world and in particular in the US and the UK, emphasis was changing from long-range highway dominated planning towards transportation system management (TSM) and public transport investment, requiring analyses of greater precision and more sensitive to the behaviour of individuals. The Williamsburg conference in 1972 (Brand and Manheim, 1973) gave impetus to a new approach to travel forecasting conceived in terms of individual motivation and choice, which held the promise of greater data efficiency, improved policy sensitivity, and more relevant information for economic and social evaluation (Stopher and Lisco, 1970; Charles River Associates, CRA, 1972; Ben-Akiva, 1973; McFadden, 1973). A challenge was laid down that offered a new approach for a new era. The whiff of revolution was in the air. 

As is always the case with revolutions – if this was to be one – its roots were to be found in earlier times. Our story returns to the 1960s in the US when the ‘disaggregate behavioural approach’ to the analysis of travel demand, introduced at the start of that decade, was taking shape, particularly in the context of academic research into modal choice and the value of time (Reichman and Stopher, 1971). The term was intended to signify a break with the past in two respects. Rather than specify and calibrate models for groups of passengers, such as those travelling between zones, ‘disaggregation’ implied an attempt to capture greater statistical variability in trip making and its determining factors, and avoid information loss and potential bias accompanying the grouping of data prior to model specification and parameter estimation. Probabilistic models would be specified at the micro-level and their parameters estimated from data pertaining to individuals or households. Although not emphasised in the earliest studies, it would later become more explicit how summation over the probable behaviour of individuals would provide the required aggregate travel demand information. 

The case against specifying travel demand models at the level of the zone and calibrating them with grouped zonal data had been growing steadily through the 1960s (Oi and Shuldiner, 1962; Quarmby, 1967; Wootton and Pick, 1967; Fleet and Robertson, 1968; Stopher and Lisco, 1970; de  Neufville and Stafford, 1971; Reichman and Stopher, 1971; CRA, 1972). In relation to modal split models, specified and calibrated at the zonal level, Reichman and Stopher were to remark: 

these second generation models are all aggregate models and have drawbacks in that they can neither be transferred geographically nor readily subdivided; they are extremely sensitive to zoning; and the measurements of trip distances, particularly for short trips, are inaccurate because of the aggregation under which all trips are designated as originating or terminating at a point, the centroid of a zone (Reichman and Stopher, 1971, 92–93). 

In retrospect, perhaps the term ‘disaggregate’ was an unfortunate descriptor for an approach based on data pertaining to individuals and households. ‘Micro-approach’ might have been preferable, because different components of traditional models were also applied in a stratified or disaggregated form. Several household types were identified at the trip generation stage, and trip matrices were usually stratified by car ownership classes and, occasionally, by person type (e.g., blue collar/white collar workers). However, for the purposes of trip generation, distribution, modal split and assignment in the US, traditional travel demand variables and data were aggregated to the ‘zonal’ level prior to model formulation, typically with a very coarse socio-economic segmentation. 

The term ‘behavioural’ indicated a response to the common criticism that traditional urban travel forecasting was essentially a curve-fitting exercise or based on analogues from the natural sciences, and lacking a theoretical approach underpinning the choices made by individuals and households. Only if demand forecasts were based on explicit behavioural hypotheses at the level of the fundamental decision-making unit, it was increasingly argued, could there be any hope or expectation for the transferability of models to different geographical settings and forecasting stability over time. Although economic concepts of utility underpinned some of the research applied in the 1960s, the detailed link between the statistical analysis of individual data and the derivation of probabilistic modal choice models based on behavioural hypotheses was still rather tenuous and subject to different interpretations (Domencich and McFadden, 1975). 

By the mid-1960s travel behaviour was also being investigated, and operational models of the choices associated with the generation, distribution and modal split behaviour established within an aggregate (zone-based) econometric framework. A number of travel demand models were constructed which, to some extent, anticipated the reformulation of consumer demand theory by Lancaster (1966), in which demand was expressed in terms of the characteristics of goods or services from which utility was derived. Specified in terms of the attributes of the alternatives, these models had been applied successfully but predominantly within an inter-urban travel context (Kraft, 1963; Quandt and Baumol, 1966; McLynn et al, 1967). Urban applications were confined to isolated cases (Domencich et al, 1968; Plourde, 1968), although the general approach and detailed specifications established a point of comparison with the traditional four-step procedure. But these economic foundations were typically based on the actions of ‘representative’ consumers for whom utility functions were expressed. This approach did not harmonise well with the data on individual choices, which disaggregate probabilistic models applied in the 1960s were originally designed to address (McFadden, 2000b, 2001). 

Could an alternative approach to acquiring the sort of information relevant for transportation planners be developed based on the summation (aggregation) of information derived from theoretically convincing behavioural models constructed at the micro-level? Over the next decade many people were to contribute to the development of such an approach. Outstanding among these was the US economist Daniel McFadden, and we shall have much to say about his work in this and the following chapter. 

The origins of the initial impetus for the practical application of the discrete choice approach based on the random distributions of cost or utility remain a matter of some discussion. Andrew Daly (2013) has drawn attention to the initial progress on demand analysis and value of time made in the UK (section 3.4), and particularly the influence of Michael Beesley, prior to major initiatives in the US in the 1970s, following the early research of McFadden. Almost certainly the initial analysis of a travel choice situation with random distributions of costs was that of Claude Abraham in the late 1950s (Gaudry and Quinet, 2011), with a seminal publication in 1961, as noted in section 4.2 (see also notes 1 and 12). 

If a micro-behavioural approach was to be developed, major issues needed to be confronted. Throughout the 1960s the analysis of individual travel behaviour was confined to the treatment of binary choice, and almost invariably the selection of one of two alternative modes for the journey to work.<sup>1</sup> But the aspirations accompanying the ‘disaggregate behavioural’ approach implied a new style of modelling that addressed the travel forecasting problem from first principles. What was missing was the formulation and implementation of probabilistic choice models that could be applied to an arbitrary number of alternatives (be they modes, destinations, time periods, routes, etc.) and to combinations of such choice ‘dimensions’. The aggregation process would then need to be confronted to generate the urban trip and flow patterns on networks and information required in the policy analysis and evaluation stages of the transportation planning process. Only if these challenges were met could an alternative to the traditional four-step travel forecasting procedure be established. 

This chapter gives an account of the early developments of the theory and practice of disaggregate modelling based on the analysis of discrete choices conceived within an economic framework. The first half of the 1970s is particularly noted for the application in studies of the MNL model specified at the micro-level and estimated from data derived from a sample of individuals. But far more was achieved. The groundwork laid in this period has had major implications for travel forecasting to this day. Important theoretical issues relating to the structure of models appeared right at the start. We therefore chart our way through difficult territory in which theoretical innovations interweave with important practical advances. We forgo a strictly chronological account to address the innovations involving the simple MNL model prior to examining the more complex forms relating to model structures derived from it. 

The formulation of the discrete choice approach, in which individuals were considered to select one of a set of alternatives according to the maximisation of utility, was the theoretical basis upon which behavioural travel modelling progressed into and beyond the 1970s. In section 4.2 we consider this early conceptual development and the formulation of discrete travel choice models based on random utility maximisation (RUM) with the MNL model as an important special case. 

As Spear (1977) noted, in about 1970 transportation planning practitioners in the US began to become aware of the new disaggregate behavioural techniques and their potential for use in urban travel forecasting. In section 4.3 we describe the uptake of the new approach, recording early applications of disaggregate travel forecasting models, and particularly those of travel choice forecasting based on the MNL model applied to more than two modes. 

In section 4.4 we consider the development of more complex models that combined different choice dimensions, such as frequency, destination, trip timing and mode. For an explicit theory of model structures derived within a discrete choice framework and its empirical development in an urban context we turn to the pioneering study of Charles River Associates (CRA, 1972) and the subsequent work of Ben-Akiva (1973, 1974), which were to attain particular importance and influence. Judged from later times neither study is completely unproblematic, and we later pinpoint issues of concern; but both have great merit in three respects: (a) in providing alternative behavioural hypotheses governing the structure of demand models involving complex travel choices they anticipated important future developments; (b) they greatly extended the scope of disaggregate model applications; and (c) the research agenda emerging from these studies would guide the field and eventually establish the disaggregate behavioural approach as an intellectually coherent and practically viable alternative to traditional methods. Because the contributions were of such importance, we shall describe these and related studies in detail. 

By the early 1970s the merits of a discrete choice approach based on distributed utilities or generalised costs had been independently recognised by several researchers. In section 4.5 we describe some early innovative European applications and theoretical investigations, particularly relating to model structures, which were later to have considerable significance. 

While great strides were made in the early years of the 1970s to develop individual choice models for a range of practical situations, a new set of problems was to emerge. In section 4.6 we summarise the difficulties pertaining to both disaggregate and traditional aggregate models encountered in the mid-1970s, together with some views expressed at that time on the possible way ahead. An assessment of the contribution of the discrete choice models applied at the micro-level in this period concludes the chapter. 

## 4.2 DISCRETE TRAVEL CHOICE MODELS: EARLY THEORETICAL PERSPECTIVES

## 4.2.1 Rise of the Behavioural Approach

In Chapter 3 we introduced the disaggregate studies of modal choice conducted in the 1960s, the purpose of which was to identify and quantify the influence of the factors involved in the selection of one mode over another (Stopher and Lisco, 1970; Reichman and Stopher, 1971). This approach established a functional relationship between the probability $P _ { j } ( \mathbf { x } )$ that an individual would select or be associated with one or other of two modes $A _ { i } , j = 1 , 2$ and a set of measured attributes x of the individual and the alternatives. The models embodied hypotheses suggesting how certain attributes might influence the choice probabilities and were sometimes expressed explicitly in terms of utilities or disutilities. 

Various statistical techniques were applied in the formulation and estimation of these multivariate statistical models: discriminant analysis by Warner (1962), Quarmby (1967) and McGillivray (1970); and probit analysis by Lisco (1967) and Lave (1969). Parameters of logit models were estimated by Warner (1962) and Stopher (1969). 

Reichman and Stopher summarised the probabilistic models in the following terms: 

the stochastic model of modal choice may be considered as a translation of the theoretical elements of decision-making into operational terms. . . . This probability is assigned on the basis of the consideration of user and system characteristics, and this procedure is most consistent with modern theories of human discrimination and choice (Bock and Jones, 1968; Luce, 1959). These theories state that every human decision is, in essence, probabilistic (Reichman and Stopher, 1971, 94). 

What was not always clear in these early models was the extent to which an individual was considered to be consistent in the way choices were made, and in what sense the probability of choice reflected uncertainties of the individual confronted by that choice and/or that of the modeller. After all, the latter was an unprivileged observer of the process of choice, having only limited information and measurements from a survey of the individual characteristics and a few attributes of the alternatives. The means of extending such models to the choice among multiple alternatives was also not fully apparent. 

Where attempts were made in the late 1960s to establish a specific theoretical link between individual behaviour and the probability of selecting a given alternative, particularly where the formulation of models involved more than two alternatives, it was often to mathematical psychology, and in particular the work of Duncan Luce [1925–2012], that researchers turned.<sup>2</sup> In the psychological perspective an individual, when repeatedly confronted with a set of choices under the same conditions, was considered to select an alternative with a given probability. 

We note the historical significance of the axiomatic approach to probabilistic choice models of Luce (1959). In any discussion of the foundations of choice models to more than two alternatives, the ‘independence of irrelevant alternatives’ (IIA) axiom<sup>3</sup> assumes particular importance. The axiom, which in this context may be regarded as a postulate or assumption, required the ratio of the probabilities $P _ { j } / P _ { i }$ of an individual selecting the alternatives $A _ { j }$ and $A _ { i }$ from a choice set A of N alternatives $A = \{ A _ { 1 } . . . .$ $A _ { N } \}$ to be independent of the presence or absence of any other alternative in that choice set. Luce showed as a consequence of the IIA condition that the probability of selecting an alternative $P _ { j }$ could be written in proportion to the psychologists’ concept $\mathrm { o f } ^ { \cdot }$ ‘strict utility’, a function of the attributes of the alternative and the individual (Luce, 1959; Luce and Suppes, 1965). McFadden (1968, 1973), Domencich and McFadden (1975, 69) and Stopher and Meyburg (1975, 275–278) give a full discussion of the strict utility model and the derivation of the MNL model from the IIA axiom. 

Another basis for the establishment of probabilistic choice models was one in which individuals were considered to select an option from distributions of the utilities of alternatives. This approach has a long pedigree; a time-line dating back to the work of Thurstone [1887–1955] (1927) is given by McFadden (2000b).<sup>4</sup> The contribution of Jacob Marschak [1898–1977] (1960) is of central importance.<sup>5</sup> He explored the implications of the IIA axiom and demonstrated that the resultant choice model was consistent with utility maximisation (a good discussion of this early work is provided by Kenneth Train, 2009). Marschak established what we now refer to as probabilistic choice models based on random utility maximisation: the probability $P _ { j }$ that alternative $A _ { j }$ is selected is equal to the probability that an individual draws a utility from a distribution associated with $A _ { j }$ which is greater than the utilities drawn from the distributions of all other alternatives. The relationship between the distribution of utilities and different choice probabilities is considered later in this section. 

This formulation of the choice model as a maximisation problem involving distributed utilities was to prove both attractive and powerful in both theoretical and practical studies on travel behaviour. Although the large majority of early work on RUM models in transportation was done in the context of modal choice, the earliest examples of the approach can be found in random cost models of route choice. Gaudry and Quinet (2011) have traced the approach back to work by French engineers in the late 1950s and particularly to research by Claude Abraham (see note 12). For an authoritative discussion of this and earlier unpublished French work, see Gaudry and Quinet (2011, 10). 

For his fundamental contributions to establishing the economic foundations and providing a unified approach to general discrete choice models on the basis of random utility theory it is to the work of Daniel McFadden<sup>6</sup> that we now turn. 

## 4.2.2 McFadden’s Early Research on Economic Models of Discrete Choice

In McFadden (2000a, 2000b, 2001), he reflected on his progression from an undergraduate physics major to doctoral studies in behavioural science and economics at the University of Minnesota, his early interests in discrete choice analysis, and the influence of mathematical psychologists, notably Thurstone, Marschak and Luce. McFadden recalled the way, in the mid-1960s when he first started thinking about problems of discrete choice, in which economists approached such problems by adapting the traditional methods of demand analysis, where the quantity of a product consumed is a continuous variable, through the device of a ‘representative consumer’ who exhibited ‘fractional consumption rates’. This adaptation of the standard marginal analysis approach, he noted, was not plausible in cases when the decision maker’s alternatives are qualitative or ‘lumpy’ and data on individual choices were expressed in terms of the selection of one item from a set of distinct alternatives (McFadden, 1973, 106): 

I observed that in a population with heterogeneous tastes self interest would lead some to one discrete choice and others to a different one. The attributes of the different alternatives, such as their costs, would determine a tipping point in the distribution of tastes where people would switch from one alternative to another. Thus, the same reasoning that led to the indifference curves and substitution effects found in economics text books would, in a world of discrete alternatives and distribution of tastes, lead to probabilities of choice that depend on economic variables and the attributes of each option in a predictable way (McFadden, 2002, 4). 

Although his active interest in discrete choice analysis applied to travel behaviour came through a project in 1970–71 (CRA, 1972) (section 4.4), it was work on a problem in transportation that proved to be a useful precursor to that study. McFadden recounted his formulation of an econometric version of the Luce model for the analysis of data on the highway routeing choices of the California DoT. Drawing on the work of Thurstone, Marschak and Luce, he expressed the utilities associated with different routeing options in terms of a set of measured attributes, including the cost of construction, route length and areas of parkland and open space taken. He then recalled commencing the task of developing software for the estimation of what he then called the conditional logit model: ‘I set about writing a computer program to produce maximum likelihood estimates for this model, a difficult exercise in the early days of FORTRAN when linear algebra and optimization routines had to be written from scratch. The program was finally finished in 1967’ (McFadden, 2000b, 3). 

This work was initially described in McFadden (1968) and in a fuller account several vears later. In the hands of McFadden (1973) the theoretical foundation of travel behaviour forecasting based on discrete choices was to take a different direction from that developed by the mathematical psychologists, one consistent with the tenets of consumer economics. This would preserve the notion of a rational decision maker who would make the same choice if repeatedly confronted with a set of choices under the same conditions. As he later expressed: 

the assumption that a single subject will draw independent utility functions in repeated choice settings and then proceed to maximize them is formally equivalent to a model in which the experimenter draws individuals randomly from a population with differing, but fixed, utility functions, and offers each a single choice; the latter model is consistent with the classical postulates of economic rationality (McFadden, 1976a, 365). 

In this interpretation, it is hypothesised that an individual selects the option that conveys maximum satisfaction, or utility, and the notion of probability ‘reflects the effect of individual idiosyncrasies in tastes or unobserved attributes for alternatives’ (Domencich and McFadden, 1975, 52). Here, the limits of knowledge of the modeller become central to the description and explanation of the travel behaviour of an individual who is always assumed to act rationally in the situation in which he finds him- or herself (McFadden, 1973, 1976a; Manski, 1977). 

To discuss historical developments and prepare for later innovations, we draw on the above references to sketch the formulation of choice models based on random utility maximisation. 

## 4.2.3 Probabilistic Choice Models Based on Random Utility Maximisation

As noted, the RUM approach to the development of probabilistic choice models is consistent with both psychological and economic viewpoints. ‘The fundamental difference between the psychologist’s approach and the economist’s approach is that the economist postulates individuals as being deterministic utility-maximisers, while the psychologist asserts that individuals make probabilistic choices based on utility assessment’ (Stopher and Meyburg, 1975, 278). 

In the economic approach to disaggregate modelling the imperfect knowledge of the modeller played a crucial role in explaining why utility maximising individuals with the same observable characteristics and facing the same choice situation might make different selections. The problem of generating aggregate information is then decomposed into the two distinct processes: 

1. derivation of the probabilistic choice model on the basis of utility maximising behaviour to account for variations of individual behaviour due to unobserved features and unmeasured attributes of those within each market segment (those with the same x); 

2. an aggregation process, which summed up the contributions to any required aggregate information from each travel-related choice arising from the variation between market segments (those with different measured attributes x) 

Because of the limits of knowledge of the modeller, the utility that an arbitrary individual derives from selecting an alternative is considered by the modeller to be a random variable; it has been convenient to express this utility as the sum of a representative or systematic component common to all individuals in the market segment (those with the same x), and a random term, often referred to as a residual error term. That is: 

$$
\text { Utility }, U (x) = \text { Representative   Value }, V (x) + \text { Error   Term }, E (x)
$$

The error term is usually attributed to one or more of the following: the variation in tastes over the population; the contribution of unobserved or unmeasured attributes; the use of proxy variables; and any measurement errors (McFadden, 1973; Manski, 1977; Ben-Akiva and Lerman, 1985). Both the representative utility and the residual error term will in general vary with x, the measured socio-economic attributes of the individual and attributes of the alternatives. 

Under the assumption of utility maximisation, the modeller assigns to an individual $q ,$ drawn randomly from the market segment with the same x, a probability $P _ { j q }$ of selecting any alternative $A _ { j }$ in the choice set A. $P _ { j q }$ is equal to the probability that the utility $U _ { j q }$ is greater than the utilities of all other alternatives.<sup>7</sup> An operational discrete choice model based on RUM is now formed from assumptions about: 

1. the dependence of the representative utility $V _ { j } ( \mathbf { x } , \phi )$ derived from any alternative $A _ { j }$ on the set of attribute values x; 

2. the distribution of the unobserved components of utility for the N alternatives, $F ( E ) = F ( E _ { 1 } . \cdot . . E _ { i ^ { * } } . . . E _ { N } , \boldsymbol { \Theta } )$ 

in which the sets of parameters , q characterise the representative utility and the joint distribution of errors, respectively. 

Although different approaches were adopted for expressing the variation of the representative component of utility with the set of attributes x, by far the most common approach in early studies of travel behaviour was simply to treat all relevant attributes, such as in-vehicle times, outof-vehicle times and money costs, on the same footing. The representative utility was then typically expressed in terms of a weighted sum of the attributes, in so-called compensatory utility functions, which allowed in principle the ‘good’ features of an alternative to compensate for what might be considered its ‘bad’ characteristics. The weights in this expression, sometimes referred to as the taste parameters, reflected the partial or unit contribution of each attribute to the overall utility derived from an alternative.<sup>8</sup> In addition to their simple form, these linear-in-parameters utility functions allowed contact to be made with the disaggregate modal choice models applied in the 1960s and provided a post-hoc rationalisation for their form (McFadden, 1976b; McFadden and Train, 1978).<sup>9</sup> 

These assumptions established the relationship between the probability of selecting any alternative $P _ { j } ( \mathbf { x } )$ in terms of the set of characteristics x of the individual and those of the attributes of the alternatives, together with the sets of parameters , q.<sup>10</sup> 

The selection of the joint distribution of the utilities $F ( E _ { 1 } . \cdot . E _ { j } . \cdot . E _ { N } )$ was historically governed by the need to strike a balance between the formulation of choice models which were based on reasonable behavioural hypotheses, on the one hand, and the practical computational requirements for solving the model and estimating its parameters, on the other (McFadden, 1973). Various simplifications were adopted to render workable models, and a considerable part of the history of discrete choice modelling concerns the justification for successive generalisations of this function $F ( E _ { 1 } . \cdot . E _ { j } . \cdot . E _ { N } )$ and the consequent computational challenge for estimating the parameters of the choice model. In the early 1970s assumptions were made more for mathematical convenience than for behavioural sophistication, as well as for achieving a touchstone with prior disaggregate choice models. 

## 4.2.4 Random Parameter and Invariant Random Utility Maximisation Models

A distinction that would later become important in classifying different models was based on the assumed nature of the variation (randomness) underpinning choices and how it was incorporated into the utility function (McFadden, 1973). In so-called random parameter models, the random nature of the utilities was attributed explicitly to variation in the tastes over the population, reflected in the distribution of the parameters in the representative utility function or generalised cost. This assumption allowed the trade-off between times and costs associated with the different alternatives to vary over the population. Some early studies on the value of travel time invoked this model of choice with differing degrees of formality as an explanation for modal choice decisions. 

In terms of its subsequent influence, the most important random parameter model developed in the 1960s was that by Richard Quandt. Quandt (1968) discussed the formulation and estimation of a modal choice model in which individuals selected either air or car between several Californian cities on the basis of minimising a disutility function involving the trade-off between travel time and travel cost attributes. The parameters of the utility function, of power function form, were considered to be exponentially distributed, reflecting differences in taste in the choice making population.<sup>11</sup> 

Later in this and the following chapter we have more to say about random parameter models, but now we concentrate on invariant random utility maximising (IRUM) models, which have dominated practical applications up to the present. In IRUM models the random utilities for the different alternatives are expressed in the form: 

$$
\text { Utility }, U _ {j} = \text { Representative   Utility }, V _ {j} + \text { Random   Residual }, \varepsilon_ {j}
$$

in which the utility residual or error terms $\mathfrak { E } _ { j }$ subsume all unobserved factors and errors in measurement. Further, they are assumed to be independent of the value of the representative or systematic component $V _ { j } .$ As a judicious choice for the distributions of the residuals led to wellestablished choice model formulations (CRA, 1972; McFadden, 1973), their popularity was effectively guaranteed. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/38754b84-3c6e-4874-b89a-d84630ad82f8/357abffc48890f45d4eccc34c61adeb25870cf965d51e94116065978cb9d3ca0.jpg)



Figure 4.1 Utility distributions for choice between two alternatives


Not surprisingly, in early discrete choice models based on random utility concepts, the most convenient assumptions were made for the form of the representative utilities and the distributions of the random residual error terms (CRA, 1972). As noted, the linear-in-parameters compensatory model was almost invariably taken for the former. In the case of both binary choice and subsequent extension to an arbitrary number of alternatives, the distributions for the error terms for the different alternatives were assumed to be identical and independent. In the conceptual development of choice models, this so-called IID assumption of ‘identical and independent distributions’ for the random utilities $( U _ { 1 } . . . . U _ { i } . . . U _ { N } )$ was of utmost importance; for many applications it seemed both plausible and mathematically convenient. 

In Figure 4.1 we illustrate the RUM approach to discrete choice between two alternatives $A _ { 1 } , A _ { 2 }$ . Here, each individual’s choice is assumed to be the result of a random draw from the two distributions $f ( U _ { 1 } , V _ { 1 } )$ and $f ( U _ { 2 } , V _ { 2 } )$ with respresentative utilities, $V _ { 1 }$ and $V _ { 2 }$ . Alternative $A _ { j }$ which offers the maximum utility, max $( U _ { 1 } , U _ { 2 } )$ , is selected. For independent random utility distributions there is non-zero probability of selecting the option from the distribution with the lower mean, shown in Figure 4.1 as $V _ { 2 } ,$ in the region in which the probability distributions ‘overlap’. We note here a trap awaiting early researchers, which had important implications for the formulation of complex demand models and the evaluation of transportation plans: the quantities $V _ { 1 }$ and $V _ { 2 }$ are not the mean utilities actually achieved from utility maximising individuals selecting the alternatives $A _ { 1 }$ and $A _ { 2 } ,$ respectively, because some of those individuals whose utilities contribute to the distribution $f ( U _ { j } , V _ { j } )$ 

of alternative $A _ { j } , \thinspace \thinspace \mathrm { s a y } \thinspace j = 1$ , are destined not to select it (sections 4.5 and 5.2.1.2). 

Although the selection of normal distributions for the random utility variables had an obvious conceptual appeal, its application to two or more choice alternatives carried with it an increasingly onerous numerical task as the number of attributes and alternatives increased. For this reason there were relatively few applications of the binary or multinomial probit model to the analysis of travel choices (Abraham, $1 9 6 1 ; ^ { 1 2 }$ Lisco, 1967; Lave, 1969; Golob and Beckmann, 1971; Spear, 1977). For both binary choice and particularly the generalisation of discrete choice models applied to multiple alternatives, the extreme value or Weibull distribution, similar in shape to the normal distribution but slightly skewed, was of particular interest.<sup>13</sup> 

The Weibull distribution has a number of fascinating properties. Most notably the distribution of the maximum value $( U _ { M A X } )$ of identical and independent distributed (IID) Weibull variables $( U _ { 1 } . . . . U _ { N } )$ , with corresponding $( V _ { 1 } . . . . V _ { N } )$ but common standard deviation s, is itself Weibull distributed with the same standard deviation s and a mean equal, up to a constant term, to the logarithm of the denominator of the MNL choice probabilities (Cochrane, 1975; Domencich and McFadden, 1975). The latter is often referred to as the ‘logsum’.<sup>14</sup> This invariance or stability property under maximisation led Domencich and McFadden to comment: ‘In our problem, where maximization of utility is the critical operation, this stability property of the Weibull distribution makes it a natural distribution with which to work, just as the normal distribution is natural for problems involving addition of random variables’ (Domencich and McFadden, 1975, 61). 

Adoption of IID Weibull distributions for the distribution of utilities for the N alternatives within the above RUM framework leads directly to the MNL model for the choice probabilities.<sup>15</sup> The resultant choice model had great attraction from two perspectives: ‘this model is computationally tractable and in many applications corresponds to a plausible stochastic specification. It is virtually the only multinomial choice model known to date satisfying both these criteria’ (Domencich and McFadden, 1975, 61). 

Although slightly skewed, the IID Weibull distribution results in the closed form MNL model, the numerical predictions from which are similar to those derived from IID normal distributions (the probit model). Because the probit model requires numerical methods for its solution, and for the other reasons mentioned above, the MNL model was to have a charmed future. 

Towards the end of a long and productive academic life, Waloddi Weibull [1887–1979]<sup>16</sup> learned that the probability distribution that bore his name was being used in the derivation of the MNL model and was having wide application in travel forecasting. The venerable professor chuckled and pointed out that, although related, it should be attributed to the Gumbel Type I extreme value distribution.<sup>17</sup>To this day many, including the second author, have referred to the Weibull function when discussing the derivation of the MNL model. From this point onwards, we refer more appropriately to the Gumbel Type I distribution or, for short, the Gumbel distribution.<sup>18</sup> 

After several years of study, Daniel McFadden (1973) set out the theoretical foundations of discrete choice modelling based on RUM, together with the properties, statistical estimation and early applications of the MNL model, including his collaboration with Thomas Domencich (CRA, 1972). The paper outlines: 

a general procedure for formulating econometric models of population choice behavior from distributions of individual decision rules. A concrete case with useful empirical properties, conditional logit analysis, is developed in detail. The relevance of these methods to economic analysis can be indicated by a list of the consumer choice problems to which conditional logit analysis has been applied: choice of college attended, choice of occupation, labour force participation, choice of geographical location and migration, choice of number of children, housing choice, choice of number and brand of automobiles owned, choice of shopping travel mode and destination (McFadden, 1973, 106). 

McFadden also spelt out central tasks which would occupy theoreticians to this day: (a) identifying the relationship between specific distributions of utilities and econometrically useful choice probabilities that result from utility maximisation; and (b) the identification of the classes of choice models that are consistent with random utility maximization (McFadden, 1973, 108). 

This reference, more than any other, provided a concise statement of the new behavioural approach to travel choice analysis combining a plausible theoretical framework with a rigorous statistical estimation method. It was this formidable combination that gradually established the discrete choice approach based on RUM as the dominant theoretical and practical approach to travel forecasting at the micro-level. Although a wider range of choice models was discussed in this period (sections 5.3 and 5.4), including the general multinomial normal form (McFadden, 1973) and the elimination-by-aspects model of Amos Tversky [1937–1996] (1972), the main empirical tool of the disaggregate behavioural approach was the MNL model. 

McFadden (1973) was followed by McFadden (1974, 1976a) in setting out the foundations of travel demand analysis from a disaggregate behavioural perspective, outlining theoretical and practical problems, and discussing wider economic applications and outstanding issues of that time. Amemiya (1975) offered a further discussion of the development and estimation of multivariate statistical models of qualitative choice from this era. By the mid-1970s the theoretical basis for, and applications of, econometric analysis to a range of discrete choice problems was becoming well established. 

## 4.3 APPLICATIONS OF NEW TRAVEL DEMAND FORECASTING TECHNIQUES IN THE US

Returning to the early 1970s, we now consider the early applications in the US of the MNL model to more than two alternatives. Much of the commentary in this section draws on a report by Bruce Spear (1977) for US DoT describing several early applications of the disaggregate behavioural approach. These studies were conducted by consultants with a substantial commitment to research, sometimes in conjunction with state and large metropolitan planning organisations. 

Spear organised his discussion around three general areas in which ‘individual choice models’ (his descriptor) had been applied: (a) as elements in the traditional transportation planning process; (b) in the evaluation of transportation system management policies, such as those directed at public transport fares, fuel prices and parking charges, as well as car pool preferential policies; and (c) for demand forecasting for new transportation systems and major service improvements. All applications involved modal choice either on its own or, infrequently, in combination with other individual and household decisions. We first consider the contexts and motivation for the new approach, before examining methodological aspects relating to specification and estimation of the choice models, aggregation issues, and validation and some evidence relating to the performance of such models. 

## 4.3.1 Contexts and Motivation for Adopting the New Approach

In the early 1970s there was some unease about the conceptual and theoretical deficiencies of the dominant four-step approach to travel forecasting. On the whole, however, this was confined to academic debates. The concerns of practice were largely its efficiency and the resources required for the forecasting process, and the precision and timeliness of the information generated. The resources required to collect the data, the expense of solving traditional models, and the insensitivity of the latter to transportation system management (TSM) policy variables were often cited in critiques of traditional methods. In transportation planning practice there was (probably) widespread agreement with the view that: 

while the traditional travel demand forecasting process is reasonably effective in long range planning, it is quite inefficient in evaluating short range, TSM type policies. There are several reasons for this. First, the data needed to drive the models in the traditional process are both costly and time consuming to collect. Secondly, the models themselves are expensive to run, making it impractical to evaluate more than one or two alternatives. Finally, most of the models are insensitive to changes of the magnitude associated with TSM policies. Because of these problems, some planners have turned to individual choice models for evaluating TSM policies (Spear, 1977, 67). 

In this regard Spear expressed the view: ‘Clearly, the greatest assets of individual choice models are their relatively small data requirements, their consistency with theories of individual choice behavior, and the ease with which policy variables can be included in the linear utility expression’ (Spear, 1977, 17). 

The possibility of geographical transferability of these models also offered planning agencies the opportunity for adapting existing calibrated models from other metropolitan areas with little additional data. 

## 4.3.2 Specification and Estimation of the Discrete Choice Models

## 4.3.2.1 Application of the multinomial logit model

Another spur to the implementation of the disaggregate behavioural approach related to the unsatisfactory specification of traditional demand models in which car occupancy factors were inserted between the modal split step and the assignment step. Spear suggested this practice had ‘resulted more from the inability of early mode split models to handle more than two modes at one time than from any attempt to reflect human behavior’ (Spear, 1977, 23). 

Expressing car occupancy as the outcome of a choice process, and specifically combining modal choice and car occupancy into a single choice, not only made the forecasting approach more sensitive to policies being proposed to encourage transfer from the drive-alone option, but also was considered to be more behaviourally realistic. 

Traditional binary modal choice models, which aggregated modal opportunities into two main groupings, car and public transport, were extended to the exploration of multi-modal choice as represented by the MNL model. These were formulated with linear utility functions, whose parameters were estimated by the maximum likelihood method, for which programs were becoming more widely available, later through the Urban Transportation Planning System (US DoT, 1976). 

The study undertaken for the San Diego County Planning Organization by the consultants Peat, Marwick, Mitchell & Co. (1972) was one of the first applications of individual choice models for a transportation planning agency. Three factors were influential in their decision to apply the approach: (a) the low usage of public transport trips in San Diego would have made traditional trip factoring statistically unreliable; (b) the desire to specify a combined modal split and car occupancy model; and (c) the experience gained with a very early example of a multiple choice MNL model in a study of airport access by Rassam et al (1971). In the application for San Diego, the model was applied to the journey to work with the choice of car driver, car passenger and public transport passenger, as represented by the MNL model choice set illustrated in Figure 4.2(a). 

In the first half of the 1970s individual choice models were applied in a variety of settings, including a range of TSM initiatives, applications of initial design and preliminary feasibility studies, and detailed impact and evaluative studies in access and new mode investigations. The latter included studies of: modal access to and egress from parking facilities at commuter rail stations; new commuter rail stations; a community feeder bus service; various combinations of dial-a-ride subscription bus and fixed route bus services; and the feasibility of alternative light rail and express bus systems. Examples of the mode choice sets applied in conjunction with the MNL model drawn from these studies are also shown in Figure 4.2. Various forms of market segmentation were adopted, including standard home-based work (HBW), non-home-based (NHB) and other homebased (OHB) purposes, in some cases further sub-divided or limited to a subset of journeys. 

## 4.3.2.2 Variables, parameters and model estimation

The prospect of developing statistically reliable models on the basis of a few hundred observations was a considerable attraction of the new approach, making it particularly suitable for evaluation of TSM policies. Socio-economic and mode choice data were obtained from individual trip records derived from home interview surveys, while level-of-service variables were derived from perceived, reported or measured values of the attributes for the accepted and one or more rejected alternatives (Stopher and Meyburg, 1975; Spear, 1977). A commonly applied approach was to use, particularly for non-selected alternatives, zone-to-zone travel times and costs, derived from the shortest route searches for the network model, in place of the point-to-point values associated with individual journeys (McFadden, 2000b). 


Source: Derived from Spear (1977) and review by the authors. u<sup>rce:</sup>


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/38754b84-3c6e-4874-b89a-d84630ad82f8/f47e63b0bec9db73b289c3deb6448b2b969211e66067da967d3acc68104f49f0.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/38754b84-3c6e-4874-b89a-d84630ad82f8/0616a698bbda772724cbc835d64333d89c2c32cec71c9bec8ee81950f9dc6ff6.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/38754b84-3c6e-4874-b89a-d84630ad82f8/b2fa7f60f26248e0daa6e42db040410b4bf7d9c842b87aaf100bd12b8f3dc161.jpg)



<sub>tu</sub>d<sup>ies</sup> Figure 4.2 Examples of modal choice sets applied in conjunction with the multinomial logit (MNL) model in early US


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/38754b84-3c6e-4874-b89a-d84630ad82f8/bc84f22759aec49aa7c9886a6485600557661c0868db3a0399b75c36a0b79dd1.jpg)


Spear also noted examples of the use of data derived from attitudinal surveys to ‘enhance the information derived from the choice models’ and, in particular, cited studies conducted by the New York State DoT. He added: 

Attitudinal data can also be used to create variables for such attributes as comfort, convenience, or reliability where objective data is difficult or impossible to obtain. And they can be used to define market segments based on attitudes or perceptions of transportation service. These and other potential applications of attitudinal research are just beginning to be recognised by transportation planners (Spear, 1977, 141–142). 

Early studies of modal choice investigations involving attitudinal variables may be found in the work of Hartgen and Tanner (1971), Hartgen (1974), Stopher et al (1974), Hensher et al (1975) and Spear (1976). Wider reflections on the use of attitudinal measurement and psychometric techniques in such studies are summarised in the book by Stopher and Meyburg (1975, 312). 

Models specified with linear utility functions, in which time, cost and any other factors were weighted with coefficients, were widely adopted in MNL specifications. The acceptability of the resultant parameter estimates, typically derived from a maximum likelihood criterion, was subjected to several additional statistical and ‘behavioural’ checks, using overall likelihood ratios, success tables and statistical significance, as well as the requirements that the signs of parameters be in accord with expectations and their numerical values be broadly consistent with the range of estimates achieved in similar studies elsewhere. Because these coefficients represented the relative importance of the included attributes in decisions and the response to changes in attribute values induced by policies, their values and associated demand elasticities were widely reported. They were particularly useful for the rapid analysis of system management policies and in the design of changes to transportation systems. 

## 4.3.3 Aggregation Issues

In the early days of disaggregate modelling, the main focus of development was ‘on improved understanding of travel choice behavior’, as Koppelman and Ben-Akiva (1977, 165) noted. Later work was directed towards using disaggregate models in the analysis of practical planning issues. For these, the aggregation problem needed to be confronted directly. Summing individual contributions to travel-related alternatives over distributions of socio-economic and level-of-service variables or spatial groups associated with the zonal system to generate required aggregate output information, while in principle straightforward to state, constituted a significant practical challenge. By the time Spear had completed his survey, various aggregation methods and their potential accuracy and bias in different contexts had been studied by, among others, Talvitie (1973), Domencich and McFadden (1975), McFadden and Reid (1975) and Koppelman (1975, 1976). 

The approach used most commonly in early urban applications became known as the ‘naïve method’. It involved substitution of the mean values of explanatory variables in the estimated individual choice probabilities to represent the choice probabilities for the group concerned. For non-linear models this procedure gives rise to biased estimates of group behaviour. From the early 1970s, aggregation procedures of varying sophistication were formulated to attempt to correct for such bias. For applications with zonal-level variables, Talvitie (1973) proposed a formulation to derive estimates of choice frequencies for interzonal trips based on zonal means and estimates of within-zone variances of the explanatory variables (Spear, 1977, 86). 

The most extensive numerical analysis of the aggregation process was undertaken by Frank Koppelman (1975, 1976). Koppelman graduated from MIT (BS, Civil Engineering) and Harvard (MBA), later returning to MIT for his Ph.D. (Civil Engineering), for which he undertook a comprehensive analysis of the aggregation process involving discrete choice models, including the development of taxonomy of methods. He proposed five practical approaches for integrating or summing the contributions to a final demand measure from individuals with different socio-economic and level-of-service variables and the choice sets available to them. These procedures were based on information that was either commonly available in current forecasting studies or could be developed with little additional effort. The selection of an appropriate procedure from those available was determined by several factors, including input data availability, accuracy requirements, and the outputs and required level of detail of the forecasts. Koppelman (1976) and Koppelman and Ben-Akiva (1977) reported on numerical studies of the bias that may arise under inappropriate aggregation over population segments. 

As more applications were undertaken, the two approaches that were used most often in practical studies were those based on market segmentation and sample enumeration as defined in Koppelman’s taxonomy. Market segmentation involved the division of the population into relatively homogeneous groups with respect to the socio-economic and levelof-service variables; then, the average values of the independent variables were substituted for each market segment. For the sample enumeration method, currently in widespread use, the disaggregate model was applied separately to each member of a sample of households or individuals; the sample was then expanded to be representative of the whole population. Spear (1977, 105) concluded: ‘the random sample explicit enumeration procedure seems best suited for those studies involving short range area wide policy evaluation in an area which has travel choice data from a recent population based travel survey’. 

## 4.3.4 Model Validation and Evidence

As noted in Chapter 3, there was no established tradition for assessing the validity of forecasts derived from aggregate models beyond requiring a ‘good fit’ of predictions against observed travel patterns, major flows and screen-line crossings, and obtaining ‘sensible’ signs and magnitudes for model coefficients. In the disaggregate cross-sectional approach, parameter significance and goodness-of-fit were also necessary conditions for assessing an adequate model; the latter could be applied both before and after the aggregation process. 

Increasingly, it was recognised that goodness-of-fit was an insufficient test for the validation of models for the purpose of policy testing, particularly if the applications (e.g., modifications to a transit system) exhibited significant differences from conditions in the base year. From this period the notion of validity in travel forecasting based on probabilistic choice models, founded as they were on behavioural assumptions, became closely associated with the possibility of geographical transferability of model forms and their estimated parameter values. As a hypothesis this was not uncontroversial, as there was little theoretical basis to assert that disaggregation itself was adequate to ensure geographic or temporal transferability, other than that some causes of non-transferability arising from the use of aggregate data were eliminated (Koppelman, 1975; Koppelman and Wilmot, 1982).<sup>19</sup> 

Nevertheless, models applied in one urban area, if constructed on sound behavioural principles, it was suggested, would be a good representation of travel behaviour in another, or at least would require only minor adjustment of their parameters with a small sample derived from the new study area. Different methods of transferring and updating disaggregate modal choice models were considered by Atherton and Ben-Akiva (1976). This approach to model development was in stark contrast to the practice of calibrating traditional aggregate model forms which lacked a sound behavioural basis and contained parameters reflecting the zoning systems. Sometimes transferability of probabilistic choice models with little or no parameter adjustment was asserted a priori, allowing the wholesale lifting of models from one geographical context to another, a practice represented in Spear’s review. 

The most exacting test of the validity of disaggregate behavioural models was to compare forecasts with observed outcome measurements in well-designed before-and-after studies. The most prominent and welldocumented example of such a study in the early 1970s was undertaken by Daniel McFadden and colleagues at the University of California, Berkeley. This research sought to refine urban travel demand forecasting models and to investigate potential applications of disaggregate models in demand forecasting for new modes and short-range policy analysis. The completion of the Bay Area Rapid Transit (BART) system in the San Francisco Bay Area provided ‘a natural experiment that would give this modelling framework an acid test’ (McFadden, 2002, 3). For this shortterm forecasting test an MNL model was applied with choice sets in the forms shown in Figure 4.3. In the collection of data, scrupulous concern was given to the accuracy of the level-of-service and access variables. McFadden later recalled: 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/38754b84-3c6e-4874-b89a-d84630ad82f8/dd86cc1b4ee316671b90190859284b7ade783ad78c70082173d7b42f9a1f659f.jpg)



Source: Based on McFadden (2000b).


Figure 4.3 Choice sets used in conjunction with the MNL model in the before-and-after study of the introduction of BART 

The critical experiment came when our pre-BART forecasts from 1972 data, adjusted for actual 1975 travel times and costs, were compared with the observed BART mode shares in 1975. . . . The predictions . . . are made by summing over the representative sample the estimated choice probabilities for each alternative, with the new BART modes added to the list of alternatives in the MNL formula. . . . Coefficients of alternative-specific variables and interactions for the new BART alternatives were assumed to be identical to the corresponding coefficients for the existing bus variables. . . . The model forecast a total BART share of 6.4 per cent in 1975, closer to the actual share of 6.2 per cent that might reasonably have been expected given the sizes of standard errors. The model under-predicted the Auto Alone mode, and substantially over-predicted transit share, 21.3% versus 18.4% (McFadden, 2000b, 8). 

The Berkeley team’s forecasts for BART were considerably better than achieved by the official forecast in 1973, which foresaw that BART would carry about 15 per cent of all work trips (McFadden, 2002, 5). McFadden recognised that good fortune was on their side: ‘We were lucky to be so accurate, given the standard errors of our forecasts, but even discounting luck, our study provided strong evidence that disaggregate RUM-based models could out-perform conventional methods. Our procedures were also more sensitive to the operational policy decisions facing transportation planners’ (McFadden, 2001, 355). The validation test and detailed analysis of the discrepancies in this application of the MNL model were recorded by Train (1978). 

## 4.4 TOWARDS A DISCRETE CHOICE THEORY OF TRAVEL DEMAND MODEL STRUCTURES

## 4.4.1 Prior Influential Work

Having examined some applications of MNL models in the US in the early 1970s, we next consider another major theoretical challenge noted in section 4.1: extending the modelling capabilities to address combinations of choice dimensions, such as frequency, destination and mode of travel at the disaggregate level. The key early research on this problem was undertaken by McFadden and Domencich (CRA, 1972) and Ben-Akiva (1973, 1974). 

To understand their motivation, it is helpful to refer to prior influential work, notably the development of aggregate econometric models in the US in the mid-1960s, and to the backdrop provided by the traditional travel forecasting models, which were not endowed with a coherent behavioural basis. In this respect we recall that the traditional aggregate zone-based models were viewed as reflecting a sequential decision-making process over the various choices, whether in G/D/M/A or G/M/D/A form, as described in section 3.7. The nature of this link between model structure and decision process over frequency, destination, mode and route alternatives, however, was vague and lacked a first principles derivation. As we saw in Chapters 2 and 3, the justification of the ordering of the four steps and the interrelationships among them were subject to different interpretations and variations in practice. 

A major source of weakness of such traditional forms was their failure to represent consistently the influence of price and level-of-service variables throughout the model (CRA, 1972; Manheim, 1973). One of the consequences of the sequential procedure was that research on the demand models in the 1960s and early 1970s became rather specialised; academics and practitioners often spent many years of their professional lives investigating the intricacies of individual steps, which were then assembled in a rather ad hoc way. 

The aggregate econometric models of the late 1960s, largely associated with intercity travel forecasting, sought to represent choices over several dimensions, including frequency, destination and mode. They were initially viewed as a generalisation of the gravity model to allow the travel market as a whole to be sensitive to changes in transportation characteristics. The common approach developed in these models was the simultaneous treatment of generation, distribution and modal split (Stopher and Meyburg, 1975, Chapter 15). In an influential review of passenger travel demand models, Kraft and Wohl (1967) contrasted such economically motivated models with traditional forms: 

It is of crucial importance to note that this type of model, one that incorporates both direct elasticities and cross-elasticities, differs in structure from the socalled ‘gravity model’ (and others most often used in traffic forecasting processes) in at least two significant ways. First, the use of demand relations and cross-relations permits both the total amount of tripmaking and the split among modes (for example) to be altered as the trip price or travel time for any mode is changed; this differs considerably from the more usual ‘trip generation, trip distribution, modal split and route assignment procedures' which hold the amount of trip making constant and vary only the ‘split’ of trips among attraction zones, modes and routes. Second, with demand models of the sort proposed (in form at least), trip maker decisions about whether to take a trip, where to take it, and by what mode and route to take it are treated as simultaneous and interrelated decisions, rather than dealt with as sequential, separate and unrelated decisions faced by tripmakers (Kraft and Wohl, 1967, 211). 

To emphasise the point, they reaffirm: ‘Tripmaking decisions are made simultaneously rather than sequentially’ (Kraft and Wohl, 1967, 212). 

The extension of the disaggregate approach beyond modal choice to complex decisions was not contemplated in detail before the late 1960s. Peter Stopher and Thomas Lisco (1970) discussed the application of extended disaggregate behavioural models to urban travel forecasting, offering numerous insights and proposing the application of a hierarchy of logit models within a disaggregate framework. Although limited in its theoretical scope, their paper was one of the first to indicate how the traditional approach to demand forecasting could be moulded to be more consistent with a behavioural formulation at the micro-level. 

## 4.4.2 A Pioneering Study of Model Structure

Because this chapter is not structured chronologically, there is a danger that we will fail to convey the full contribution and sense of ambition of the study by Charles River Associates for FHWA (CRA, 1972), later revised and published as Domencich and McFadden (1975). To obtain a sense of what was attempted and achieved we quote from the report’s summary: 

This study has developed, and successfully tested in limited applications, a new methodology for designing and calibrating disaggregated, policy oriented behavioral models of urban travel demand. By travel demand, we mean not simply the choice of mode but rather the entire set of decisions faced by the traveller – the choices of mode, destination, time of day of travel and trip frequency. With the approach developed in this study, the entire demand function is policy sensitive. Thus, both the number of trips and the percentage splits between competing modes, destinations and times of day are responsive to changes in the transportation system (CRA, 1972, 1–1). 

According to McFadden (2000b, 1), the founding ideas for the original model were based on the research of MIT economists Peter Diamond and Robert Hall. McFadden noted: 

From the economic principles of consumer demand, they developed a behayioral travel demand model that emphasized separable utility and multi-stage budgeting, so that the complex dimensions of trip generation, timing, destination, and mode choice could be broken into manageable segments, with ‘inclusive values’ tying the segments together in a coherent utility-maximization framework. In the style of the times, they developed this theory for a representative utility-maximizing consumer, and were then faced with the problem of putting the model together with data on individual trips from trip diaries (McFadden, 2000b, 2). 

McFadden recalled being asked to implement this model after coming to MIT in 1970 (McFadden, 2000b). It was the theoretical development and practical implementation of the Diamond–Hall framework to accommodate data on individual choices that broke new ground in travel behaviour modelling, and econometrics more generally. 

At the heart of the behavioural representation, individuals were considered to engage in several decisions – where to live and work, how many vehicles to own, how to travel to work, how often, where, when and how to shop, and so on – in terms of discrete choices over the options available. To simplify the process of choice, it was assumed that the utility function governing choices had an additive, separable structure, which allowed the demand function to be factored into component decisions, as illustrated in Figure 4.4(a), ‘in a way that enables the separate decisions to be modelled separately but tied back together into a conceptually satisfying demand function’ (CRA, 1972, 1–4). 

Individuals were first considered to exercise a choice of work and residential location, then vehicle ownership and then the shopping journey. The tree structure for the shopping trip shown in Figure 4.4(b) reflects the decomposition of the underlying choice process into a decision ‘sequence’, although it was stressed that each individual was seeking the maximum utility option over the alternative choice combinations of frequency (f), location (d), time period (t) and mode (m). The model thus represented a process of optimal choice within a decision hierarchy composed of several levels, corresponding to these individual choice dimensions. 

With regard to the information flows accompanying the process of arriving at a decision, the authors noted: 

At each decision level, choice can be viewed as being made conditional on fixed preceding decisions and optimal succeeding decisions. For example, destination choice is made conditional on fixed decisions on location, vehicle ownership, and trip frequency, with time-of-day of travel and mode assumed to be chosen for each alternative destination to be the most desirable. The solid arrows in the  diagram represent the decision sequence while the broken arrows represent  the flows of information on optimal values of succeeding choices which enter the decision process at any level (Domencich and McFadden, 1975, 43–44). 

This representation permitted the probability P(f, d, t, m) of selecting a given combination of frequency (f), destination (d), time of day (t) and mode (m) for the shopping trip to be expressed as the product of marginal and conditional probability distributions: P(f), P(d|f), P(t|d, f) and P(m|d, f, t), here taken as MNL models in which level-of-service variables in the different models were linked through the underpinning assumption of utility maximising behaviour by ‘inclusive prices’. 

At the lowest level of the tree, choices were determined by the times and costs on the different modes in an ‘index of desirability’ or ‘inclusive price of travel’, or what we referred to in section 4.2 as a disutility function or generalised cost. This information is then transmitted to decisions at higher levels of the tree through further inclusive price functions, in earlier chapters referred to as composite utilities or composite costs. The form of these inclusive prices at a particular level of the tree was taken to be equal to the generalised prices for the various choices at the next lower level weighted by the conditional probability of that choice.<sup>20</sup> Interestingly, in the context of destination choices, Domencich and McFadden (1975, 175) saw the inclusive price as having a role to play in the definition of accessibilities which ‘would be useful in land use planning, in shopping center location studies, and in urban development analysis’. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/38754b84-3c6e-4874-b89a-d84630ad82f8/71a878dc5c0b2955e0df3fcd0e427abf425647fcc41cacb0746eaf295241a6dc.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/38754b84-3c6e-4874-b89a-d84630ad82f8/c6b8f1101306b295be542709e71129b9b8b17360bea3d4a60d7d7c60812bcec3.jpg)



Source: (a) Based on Domencich and McFadden (1975, Figure 3.2); (b) based on Domencich and McFadden (1975, Chapter 3).



Figure 4.4 (a) Observed travel behaviour arising from multiple discrete choices (b) Decision tree for the shopping demand model


We note, for later reference, an observation by the authors: 

It is instructive to compare the decision structure outlined above with conventional modal split and trip generation and distribution models. One may depict such models on the figure above with the trip–no trip choice corresponding to trip generation, and the destination choice corresponding to trip distribution. In this sense, conventional models are compatible with the utility maximization structure we have outlined. However, the information on succeeding decisions implicit in the conventional models is often either inconsistent with a theory of individual utility maximization or corresponds to an implausible utility structure (Domencich and McFadden, 1975, 44). 

In the actual implementation of the framework, the multiple choices were decomposed into a modal choice model for travel to work and a demand model for shopping trips. The empirical estimation of the linked hierarchy of MNL models for the latter proceeded from the bottom of the tree (mode) to the top or apex (frequency). Through the transference of information from one level of the tree to the next, the effect of policy variables was expressed explicitly and consistently throughout the model. Data on individual trip decisions from the Pittsburgh home interview survey were adopted for the study, and alternative transportation and socio-economic variables were explored in model specification and parameter estimation. 

Working with samples of 115 observations for work trips and 140 observations for shopping trips, the researchers viewed the statistical results as ‘extremely encouraging’ (CRA, 1972, 1–5). Although in this study the methodology was stressed rather than empirical findings, the authors noted the following interesting result regarding the sensitivity of the various shopping choices to changes in policy variables: ‘time of day, destination, and trip frequency decisions are far more responsive to changes in relative travel times and costs than are modal choice decisions’ (Domencich and McFadden, 1975, 180). 

Apart from its innovative applications to choice contexts other than mode, CRA (1972) demonstrated in theory and application how a ‘sequential’ decomposition of a probabilistic choice model was consistent with a utility maximising decision process in which decisions over combinations of alternatives were considered ‘jointly’. Here, the inclusive values play a key role of information transfer between separate choice dimensions to preserve the notion of an optimal decision maker. There was a ‘significant flaw’ in the analysis (McFadden, 2000b, 5), relating to this transfer of information between the different choice models within the hierarchy (see section 5.2), and subsequent research would suggest that different orderings of the component choices might have been justified. Nevertheless, in our view, for the sheer number of influential ideas presented, this pioneering project represents the single most important research contribution to disaggregate travel behavioural analysis based on the economics of discrete choices. We shall encounter the full implications of this analysis in Chapter 5. 

## 4.4.3 An Alternative Approach to Model Structure

Moshe Ben-Akiva has been responsible for some of the most significant and innovative applications of disaggregate travel forecasting models, and we shall refer to a number of them in this and subsequent chapters. A graduate of the Technion – Israel Institute of Technology, Ben-Akiva came to MIT for graduate study in the late 1960s. Research for his Ph.D. thesis, described here, represented a further development of, and alternative to, the analysis of CRA. While both studies were conceived within the discrete choice framework based on random utility theory, they expounded different approaches to the behavioural theory of model structures involving combinations of choice dimensions. 

According to Ben-Akiva, his research was inspired by two developments: 

Rejecting the conditional dependency inherent in the recursive<sup>21</sup> model structure selected by CRA (1972), in which the traveller was assumed to decompose his or her decision into several linked stages, as unrealistic, Ben-Akiva strove to capture the complexity and interdependence of the decision process over multiple dimensions and, in particular, the destination and mode of shopping trips. In addressing the question of how the characteristics of modes serving different destinations were to be reflected in the choice of destination, and vice versa, he adopted a ‘symmetric’ model structure in which the different choice dimensions were treated on the same footing. This structure contrasted with CRA’s ‘asymmetric’ approach in which one particular hierarchy' of the choices was favoured, as reflected by the structure of the utility function, with the ordering imposed a priori. The symmetric treatment harmonised with Ben-Akiva’s view that there was a close correspondence between the analytic structure of the model and the nature of the joint decision process underpinning it, as follows: ‘simultaneous and recursive structures represent simultaneous and sequential decision-making processes. Theoretical reasoning indicates that the simultaneous structure is more sensible. Moreover, if a sequence assumption is accepted, there are several conceivable sequences, and generally there are no a priori reasons to justify a selection among them’ (Ben-Akiva, 1974, 26). What this study set out to do was to show that a simultaneous structure, although complex when combining different choice dimensions with many accompanying explanatory variables, was operationally feasible, and he chose the multinomial logit model for the investigation. 

More generally, as a basis for treating the interdependency between the many location and travel-related choices facing individuals and households over the short, medium and longer term, Ben-Akiva (1973) hypothesised that these would be grouped according to the frequency with which the decisions were taken and the potential speed of response to changes in the transportation system. Two groups of choices were distinguished: (a) ‘mobility choices’, consisting of employment and residential location, housing type, car ownership and journey-to-work modal choice decisions, were considered to be made infrequently; (b) ‘travel-related choices’ for non-work trips, consisting of frequency, destination, mode, time of day and route, were made frequently, perhaps every day, and assumed to respond rapidly to changes in transportation variables. He then hypothesised that: 

1. mobility and travel choices were made ‘hierarchically’, the latter conditional on the former; 

2. within each group of decisions, the choices were highly interdependent and should be modelled as a joint decision process. 

The shopping trip was the main subject of empirical study. Although advocating the simultaneous structure provided by the MNL model applied to combinations of destination and mode, Ben-Akiva also considered what he referred to as alternative recursive models (which, he argued, corresponded to alternative behavioural assumptions) in order to identify and evaluate significant differences between the two model  forms. By analogy with the notation adopted in Chapter 3 we shall refer to these simultaneous and recursive structures at the disaggregate level by D-M and D/M, M/D, respectively. For the destination and modal choices associated with shopping trips he thus considered the following: 

1. D-M: a multinomial logit model for the probability of choosing each alternative $( d , m )$ out of a choice set containing combinations of destination and mode; 

2. two sequential or recursive structures, expressible as the product of marginal and conditional probability distributions, which we shall label, symbolically, D/M: $P \{ d \} P \{ m | d \}$ and M/D: P{m}P{d|m}, respectively. 

The recursive structures, which were similar in their general conception to the CRA model, were expressed as a hierarchy of marginal and conditional probability models, as illustrated in Figure 4.5, with MNL models applied at each stage of the hierarchy. The solid arrows in the diagrams indicate the conditionality assumed, while the dashed arrows indicate the transmission of information, via compositional rules, from the lower to the upper level of the tree, as in the CRA study. 

For each of the structures D/M and M/D, three different ‘composition rules’ for combining the attributes of travel times and costs from the MNL model at the ‘lower level’ for entry as an inclusive value at the ‘upper level’ were examined. Ben-Akiva (1974, 34) referred to these as: 

1. ‘weighted prices’, in which the level-of-service variables were weighted by the conditional probability, for example that of selecting a mode given the destination choice, in the $P \{ d \} P \{ m | d \}$ structure; 

2. ‘weighted generalised prices’ (equivalent to the CRA procedure of inclusive prices, described above); 

3. ‘log of the denominator’, the natural logarithm of the denominator of the MNL model expressing conditional choice, for example the log of the denominator of $P \{ m | d \}$ in the structure $P \{ d \} P \{ m | d \}$ . Later this expression was referred to as the ‘logsum’, and we shall use this expression below. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/38754b84-3c6e-4874-b89a-d84630ad82f8/fdd48baa642c3a0eed742ebd2ba6b04d476d9628785981d579fe14f346217c0e.jpg)



Source: Based on Ben-Akiva (1973, 1974).



Figure 4.5 Three probabilistic choice model structures with their corresponding decision trees


In all, seven alternative models were specified: one D-M structure; three D/M structures; and three M/D models, based on the three composition rules. 

Ben-Akiva noted that if the coefficient, say q, of the ‘logsum’ variable in the ‘higher-level’ choice, destination choice in the D/M structure, turned out to be equal to unity (or statistically not significantly different from unity), the whole sequential model structure ‘collapsed’ into an MNL model form extending over the combination of destination–modal choice alternatives. In other words, Ben-Akiva formulated and made operational a choice model structure, in which MNL models were arranged in a hierarchy with a ‘logsum’ link, which contained the extended MNL model, over destination and mode combinations, as a special case. This formulation would turn out to be of great theoretical and practical interest.<sup>22</sup> 

The sample used for estimation of the various models consisted of 123 household home–shop–home round trips selected randomly from a home interview survey from the northern corridor of metropolitan Washington, DC. Ben-Akiva showed that five of the seven alternative models specified gave reasonable coefficient estimates, as determined by maximum likelihood. He remarked: 

As expected, the empirical evidence does not show which of the alternative structures, one simultaneous and two recursive, is more likely to be correct. All the models gave reasonable coefficient estimates. Furthermore, all the models gave essentially equal goodness of fit: $\rho ^ { 2 } = 0 . 2 5$ . The simultaneous model includes seven coefficients, whereas the recursive models included eight. This implies that the simultaneous model has a slight edge in this category, but it is certainly not a conclusive difference (Ben-Akiva, 1974, 39). 

However, Ben-Akiva was able to demonstrate an important result: the estimated parameters, the resultant elasticities and therefore the sensitivity to policy variables of alternative models which passed standard goodness-of-fit tests for micro-models vary considerably with the model structure selected. With regard to the wider development of the models, he concluded: ‘The empirical evidence taken together with the theoretical assumptions of a simultaneous structure and the advantages of disaggregate models suggests that future efforts in travel demand modeling should be in the direction of simultaneous disaggregate probabilistic models’ (Ben-Akiva, 1974, 40). 

## 4.4.4 Related Studies

The research agenda suggested by the hierarchical framework of mobility and travel choice groups, and the application of the MNL to jointly determined choices within each group, was subject to extensive development. The findings of Ben-Akiva’s Ph.D. thesis were extended by Adler and Ben-Akiva (1975) to incorporate the frequency of shopping journeys in a joint structure based on the MNL model applied to frequency, destination and modal alternatives. 

The first joint disaggregate model for a subset of mobility choices, namely car ownership CO of the household and mode to work M of its primary worker, applied in the form CO-M, was that of Steven Lerman, the MNL model adopted for this purpose. It was argued that ‘car ownership and mode to work are closely related and therefore to model them as jointly determined is most appropriate’ (Lerman and Ben-Akiva, 1975, 35). Further research by Lerman (1976) on choices in the ‘mobility bundle’ argued that household location decisions were closely related to other choices of housing, car ownership and mode to work, and as such were jointly determined. The application of the joint choice MNL model ‘eliminat[ed] the need for an arbitrary set of assumptions about a sequence of choices. . . . Each potential location–housing–automobile ownership–mode of work combination is a distinct alternative’ (Lerman, 1976, 6). 

The study by Ben-Akiva and Atherton (1977) made a number of contributions to the methodological development of the field, and was distinguished in its treatment of: 

1. A substantial application of the disaggregate approach to test various policies to promote car pooling, and disincentives to drivealone options, as a basis for reduction in traffic congestion and energy consumption, and improving air quality. These policies included: employer-based car pool matching and promotion; preferential parking measures; preferential traffic control; and fuel price increases. 

2. A micro-level specification of interrelated individual decisions within households. 

3. A clear discussion of the aggregation of behaviour by sample enumeration (section 4.3). 

4. An early example of the application of the MNL model in pivot-point or incremental form in which the probability of selecting an alternative under a change in the attribute values is expressed in terms of the base probabilities and the utility differences associated with each alternative before and after the change. 

5. The validation of forecasts on the basis of a before-and-after study. 

To our knowledge this was the first example of a model which addressed ‘micro-level interdependency’ directly; in this case, it allowed the effect of choice of mode for the journey to work by the primary worker of a household to impact directly on the car availability of other household workers. The MNL model was applied in the four separate contexts: 

1. joint car ownership, work mode choice model for the household’s primary worker; 

2. work trip mode choice for the household’s secondary workers; 

3. car ownership model for households without workers; 

4. joint frequency–destination–mode choice model for non-work trips. 

## 4.5 SOME EARLY EUROPEAN STUDIES

During the second half of the 1960s and early years of the 1970s several important disaggregate studies of modal choice and the value of time were conducted by researchers in Europe and, as noted in section 3.4, particularly the UK. The following studies, selected for their relevance to the application of the disaggregate approach and the theory of model structures, illustrate how the discrete choice RUM approach was transferred from the US to the Netherlands and also adapted and independently developed in the UK from earlier ideas. 

In 1970 documentation of discrete choice models based on random utility maximisation was very sparse, and confined to a small number of articles, such as those of Quandt (1968, 1970) and Golob and Beckmann (1971). Prior to the release of CRA (1972), Brand and Manheim (1973) and particularly McFadden (1973), a broad academic reference did not exist. 

## 4.5.1 Transfer of the Approach to the Netherlands

A study by Buro Goudappel en Coffeng in association with Cambridge Systematics in 1973–74 is an example of the way that ideas were transferred through collaborations of US and European researchers, just as the traditional travel forecasting procedure had been transferred from the US to the UK a decade earlier. The project methodology drew extensively on research conducted at MIT at the time and in particular that of Ben-Akiva. Its development was testimony to the openness of the Dutch government to the import of ideas from abroad and was possible because the Dutch ministry had funded a major household interview survey designed as a demonstration project.<sup>23</sup> 

The objective of the project, conducted in the Eindhoven region of the Netherlands, was to ‘further the development of behavioural urban travel models, and in particular to implement the methods of disaggregate and simultaneous probabilistic travel demand models in a Dutch context’ (Richards and Ben-Akiva, 1975, 7). The study focused on choices for two trip purposes: choice of mode for home-to-work trips; and joint choice of destination and mode for shopping trips. For the journey to work, an MNL model was constructed in which the modes included car, bus, train, bicycle and moped, appropriate to the Dutch context. The study ‘demonstrated that multinomial logit is a practical tool in the development of multi-modal models’ (Richards and Ben-Akiva, 1975, 115). For the shopping trip, the joint choice of destination and mode was also represented by the multinomial logit model. 

Interestingly, this is one of the few studies on the disaggregate approach in this period that makes detailed reference to UK work and specifically to generalised cost formulations in what the authors refer to as Wilson-type models<sup>24</sup> (Richards and Ben-Akiva, 1975, Chapter 7). In relation to the specification and application of choice models at the micro-level and, in particular, the adoption of the MNL model, the authors concluded: 

Using disaggregate data and the multinomial logit model it is possible to estimate a destination- and mode-choice model essentially comparable with that of the origin constrained Wilson-type distribution/modal split model, but with many fewer observations. . . . As with the mode choice model, the ability to include socio-economic variables in the utility function adds considerably to the potential power of disaggregate modelling using multinomial logit. Thus the disaggregate conditional and disaggregate simultaneous models estimated using the multinomial logit model offer major improvements over most conventional urban transportation modelling procedures, even those based on the Wilson model (Richards and Ben-Akiva, 1975, 138). 

In relation to the efficiency in the use of data the study team eloquently expressed the case for disaggregate modelling and the relative advantages over the traditional aggregate approach: 

The advantages are two-fold. First, with the same range of variables, the various coefficients can be estimated more readily, with fewer observations and probably with a greater degree of reliability; thus they offer a potential saving in either time or cost, or both. Secondly, they offer the opportunity to include more variables, and thus, for a similar cost, to develop models with more complete specifications, and therefore, better models (Richards and Ben-Akiva, 1975, 138). 

The book that followed the study (Richards and Ben-Akiva, 1975) was, along with that of Domencich and McFadden (1975), among the earliest accessible introductions to practical applications for those new to this area of research. 

## 4.5.2 A Mode–Route Freight Model Developed for the Channel Tunnel Study

Although our review focuses mainly on urban transportation systems, in view of the generic nature of the modelling process and some common assumptions made for longer distance travel, we include an innovative study for the economic assessment of the proposed Channel Tunnel linking Britain with France undertaken by Coopers and Lybrand Associates (1973) during the period 1972–73. Separate hierarchical models were developed for passengers and freight transportation. The discussion here refers to the freight model.<sup>25</sup> 

The study was unusual in that data were available from a specially commissioned freight survey of unitised trade between regions of the UK and continental Europe, which allowed a disaggregate approach to be used for model estimation and forecasting. For the large majority of unitised shipments, two modes were available: lift-on/lift-off containers; and roll-on/ roll-off heavy goods vehicles (HGVs), some carrying containers and some with fixed covered trailers. For each origin–destination pair, two or three routes were identified for each pair of ports. 

Choices of mode and route for commodities depended on many factors: (a) characteristics of the consignment itself; (b) characteristics of the freight forwarders and manufacturers; and (c) transportation service attributes such as freight charges and transit time. The model eventually selected was a nested or hierarchical probit model for choices among route and mode combinations in which the choice of route was conditional on the choice of mode. The modal choice adopted for a shipment, between roll-on/roll-off HGVs and lift-on/lift-off containerisation, was of binary probit form; the choice of route (ferry services) was determined by a least generalised cost model with normally distributed costs, represented by a multinomial probit model. The approach was proposed by Tony Flowerdew and developed further by Robert Cochrane and colleagues (Coopers and Lybrand Associates, 1973, 80). 

In the probabilistic route choice model, the sources of variation in generalised costs were: (a) terminal costs in relation to the relative location of shipper or receiver and the ports; (b) charge rates and discounts; and (c) the value of time. The probability that a given route would be selected, expressed as a multiple integral over the joint distribution of costs, was equal to the probability that the generalised cost on the route was less than that on any other. Maximum likelihood estimates of the parameters of the probit model were computed by numerical integration. 

The commodity characteristics and service available by each mode were known to be important determinants of mode choice. The binary probit model was formulated in terms of minimisation over normally distributed generalised costs, establishing a methodological consistency between route and mode selection. Various methods were considered for expressing the modal generalised costs in terms of the various route generalised costs available to each mode. The one selected ‘was computationally the simplest yet provided much the best fit to the data. For each origin– destination pair, the characteristics of the best routes on average observed for the two modes were used for all comparisons’ (Coopers and Lybrand Associates, 1973, 88). 

Almost as an aside, the consultants note what later became an important issue in the development of linked multi-stage demand models: 

There is in fact an interesting theoretical justification for this approach in the methodology of the route model. A statistical expression for the distribution of generalised cost on the optimal route of a set can be developed. This will, of course, in general have a lower mean than any of the individual route costs, and a slightly different distribution. The route which is on average the best will however normally provide a reasonable approximation to it (Coopers and Lybrand Associates, 1973, 88, emphasis added in italics). 

As applied to forecasting, the Channel Tunnel was added to the routes available to the two modes. For the lift-on/lift-off container component, re-marshalled block container trains ran through the tunnel, since demand was too low for dedicated trains from origins to destinations at that time; for the roll-on/roll-off vehicles, a rail ferry link through the tunnel was included. An estimate of the diversion of traffic to the tunnel was determined for this new arrangement. 

## 4.5.3 Random Utility Models of Destination Choice

Robert Cochrane’s derivation of spatial interaction models of the gravity type from random utility theory is noteworthy for several reasons (Cochrane, 1975). Although an economic basis for the gravity model appeared earlier in the literature (Neidercorn and Bechdolt, 1969; Neuberger, 1971), here was an approach based on random utility theory which better reflected the discrete choices involved.<sup>26</sup> His paper made three important contributions in the present context: (a) an economic derivation of the family of zone-based spatial interaction (gravity) models proposed earlier by Wilson (1967); (b) derivation of compatible measures of the net benefit associated with the spatial choices, reproducing the results of Neuberger (1971); and (c) constructive suggestions for linking generation, distribution and modal split models. 

By the early 1970s Wilson’s entropy maximising formulation of the gravity model provided a practical basis for forecasting trip interactions between the zones of cities and regions, and was becoming the dominant form applied in UK transportation studies. The theoretical basis for that model, however, was not appealing to those who sought some constructive behavioural explanation for trip making and destination choice. In Cochrane’s derivation, offered as an alternative to Wilson’s approach, aggregation of the spatial decisions made in a zoned system was a key part of deriving the probabilistic choice model. The central assumption was that ‘the probability that a particular trip maker from one zone will travel to a second zone is the probability that a trip to that zone offers a surplus (or net benefit) greater than that of a trip to any other zone’ (Cochrane, 1975, 38). 

The essence of the argument involved the decomposition of the problem to determine: (a) the distribution of consumer surplus (utility minus generalised cost) over the opportunities within zones to obtain the distribution of utility of the best trip associated with a journey to each zone; and (b) the resultant choice of the destination zone according to the maximum surplus offered by each zone. 

Referring to point (a), a crucial and innovative aspect of Cochrane’s argument was the observation that, as a result of the maximisation process, it would be the form of the (net) utility curves in the upper tails of their distributions that would be the essential determinant of the probabilities of choice. No specific functional forms for the utility distributions were given, other than that the behaviour in the tails was assumed to decline in an approximately exponential fashion. This choice was not arbitrary, but ensured that two axiomatic requirements, noted below, could be met. The distribution of maximum surplus over the opportunities within each zone was then determined under the two further assumptions about the number of opportunities: that it was large, and that it was proportional to a measure of zonal attraction (such as floor space). Drawing on the classic work of Gumbel (1958), Cochrane showed that the probability density function for the surplus of the ‘best trip’ to any zone approximated to a Gumbel Type I extreme value distribution, a result which held for a wide range of utility distributions, including Gaussian, log normal, logistic and Gumbel forms. The distribution of maximum surplus within each zone was thus expressed in terms of the number of opportunities and therefore the attraction of the zone. 

The second stage of the argument, that of determining the probability that a particular zone was selected, led directly to the ‘singly-constrained gravity model’. Through the addition of zonal costs, which were assumed to reflect a bidding process that reconciled the number of trips to different zones with the number of opportunities available, the doubly-constrained spatial interaction model was also derived. 

Because an intrinsic part of the calculation involved the determination of the distribution of consumer surplus over the zonal system, it was a straightforward process to find the mean and total surplus attained in the choice process, and the change arising from a modification to the trip costs between two situations accompanying the introduction of a transportation project. In this way Cochrane showed the social benefit to have the same ‘logsum’ form as in Neuberger (1971). 

Cochrane also considered the integration of the three aspects of a trip, corresponding to a combined generation, distribution and modal split model. As in Quandt (1968), the generation of trips was made sensitive to the generalised cost by assuming a threshold; a trip would only be made when the utility of doing so exceeded the generalised cost, reflected in the limits of integration over the distribution of net utilities. In this way a combined generation–distribution model was found in which the total interzonal demand was sensitive to the travel cost. 

To integrate the distribution model with the modal split model, Cochrane drew on the model of MacNicholas and Collins (1971). They had considered a random parameter model in which modal choice was determined on the basis of the minimum generalised cost specified in terms of travel time and money cost, with a value of travel time normally distributed over the choice making population. Cochrane suggested using the mean of the distribution of minimum cost as the basis for integrating the two models, noting: 

In order to determine the likely choice of destination, we can use the distribution of trip costs for the modes actually chosen . . . and consider the two modes as being a single mode with this probabilistic distribution of cost. The mean cost for this combined mode is in fact lower than the mean cost for each mode separately. Averaging trip costs across modes would give a very biased estimate of the combined mean trip cost. A much better (but still biased) estimate would be the lower mean cost of the two (Cochrane, 1975, 44, emphasis added in italics). 

This approach to integration of the two choices within a combined hierarchical model reflected Cochrane’s contributions to the mode–route problem for the Channel Tunnel. 

We also note here the independent contribution of Jean-Gerard Koenig, who studied the destination choice problem within a random utility approach and derived a similar ‘logsum’ expression for the relationship between average utility received in the choice process and commonly used measures of accessibility. Koenig’s results were distributed in French in 1974, but were probably part of his 1972 doctoral thesis. A fuller description of this study and, in particular, the role of random utility measures of accessibility in planning and welfare measurement was given in Koenig (1975). 

## 4.5.4 A ‘General Theory of Travel Demand

Finally, we draw attention to a rarely cited, but historically important, contribution by A.J. Harris and John Tanner (1974) of the UK Transport and Road Research Laboratory. The study was highly technical, but had important practical implications. Its full significance was certainly not widely recognised at that time. The study offers great insights, addressing major theoretical problems and anticipating important key developments in the field. The research of Quandt (1968, 1970) and Neuberger (1971) appeared to be particularly influential in the development of their approach. 

Their analysis sought to establish the properties of probabilistic choice models within the framework of random utility theory in which the variation in utilities was distributed over a population in different ways. The paper set out: 

a general theory from which a variety of models can be derived by making different assumptions about the statistical distributions of parameters which vary from one person to another and which give rise to observable differences in trip making behaviour. . . . The basic model assumes that there are observable variables representing times, money costs etc. which are common to all people. Each potential trip has a personal generalised cost which is a linear function of the observable variables; the coefficients of this function, which represent terminal costs, values of time etc. have a distribution over the population of potential trips. By integrating over regions of this distribution one obtains trip demand functions which are functions of the observable variables only (Harris and Tanner, 1974, 1). 

A central part of their investigation concerned the relationship between such random utility models and consumer surplus measures, defined as the mean value of the distribution of maximum net benefit achieved in the choice process. A primary motivation of the work was to place methods of demand analysis and evaluation measures derived from generalised costs on a rigorous footing. Although most of the paper was directed at the problem of modal choice, the analysis had far wider implications, and related to any discrete choice modelling context in which that option with the highest value of benefit minus cost was selected. Following Quandt, a cut-off in the distribution of net benefit was introduced, where generalised cost exceeds benefit, to represent the condition in which a trip would not be made. 

Although the paper was for the most part concerned with a general mathematical analysis, important special cases were taken to illustrate the power of their approach. Of particular interest and importance for future developments was their analysis of discrete choice models generated by distributions in which the (dis-)utility associated with any alternative was written as the sum of a term common to all in the relevant choice making population and a random error term. The authors referred to this as ‘the personal difference case’, which can also be termed a translational invariant case in which the random term in the utility function is independent of the average or representative value. They also considered what they referred to as ‘the personal multiplier case’. For its wide relevance to urban transportation modelling we shall restrict our discussion to the former case.<sup>27</sup> 

The authors addressed two questions: 

1. For an arbitrary distribution of utilities satisfying the personal difference case, what is the resulting demand function and corresponding consumer surplus measure derived from the utility maximising process? And its converse: 

2. For a demand function generated by the random utility function of translational invariant form, what is the distribution of utilities that gives rise to it? 

Harris and Tanner (1974) established general expressions for the demand function and the consumer surplus measure associated with the choice process, and then showed for the ‘personal difference case’ that the demand function could be derived directly from the consumer surplus function by the mathematical process of differentiation. As an immediate consequence of this result, they established that the demand function was characterised by integrability or symmetry conditions (Hotelling, 1938), which we considered in section 3.8.3. They argued that demand functions satisfying such symmetry conditions were consistent with generalised cost formulations. They then reversed the process and derived an expression for the density function for the utility distribution that would generate an arbitrary demand model consistent with the translational invariant utility functions. 

What was the practical relevance of this approach and how would specific models, consistent with these technical conditions, be generated? Because the demand models could be derived from consumer surplus (CS) functions, they argued that suitable forms for CS could be sought to generate demand models that were consistent with a personal difference generalised cost formulation. As the authors put it: 

By taking different arbitrary forms for the function CS we can get a variety of expressions for the T [the demand function]. It is clear that the function CS is not completely arbitrary; it must satisfy certain conditions. . . . In the personal difference case, for example, these probably reduce to the condition that the implied probability distribution must never be negative (Harris and Tanner, 1974, 13). 

They then illustrated their argument by selecting expressions for the consumer surplus measures that generated demand models of MNL and other related forms such as singly-constrained spatial interaction models. These models were generalised to incorporate net utility thresholds to render the generation of trips sensitive to changes in generalised costs. 

For the purpose of what followed, we summarise their major contributions as follows: 

1. integration of the process of choice model formulation and the derivation of economic (consumer surplus) measures appropriate to welfare assessment and their relationship in the case of particular forms of utility function; 

2. development of a strategy for generating choice models by selecting suitable consumer surplus functions and forming the demand function consistent with the theory by differentiation; 

3. demonstration of this integration in the formulation of commonly applied models, such as the MNL model and its associated consumer surplus measure of ‘logsum’ form. 

The authors concluded their paper in this way: 

The fact that a paper dealing with such a fundamental aspect of transport models needed to be written is a reflection of the youth of the subject. In the past 10 or 15 years, our understanding of the interaction between land use, transport facilities, costs, trips, flows, speeds and so forth have developed enormously, and so has our capacity to process the relevant data. But there is still no consensus about how models should be constructed (Harris and Tanner, 1974, 15). 

But how was this theory to be applied in the more complex choice contexts typical of practical transportation studies? We address this question in Chapter 5. 

## 4.6 SOME CHALLENGES IN MULTI-MODAL AND MULTI-DIMENSIONAL CHOICE MODELLING

## 4.6.1 Problem of Similar Alternatives and the IIA Property

## 4.6.1.1 Mixed blessing of the IIA property

As the review of Spear (1977) and other studies confirmed, applications of the MNL model in travel forecasting, particularly to problems involving multi-modal choice, resulted from its relatively simple structure, modest data requirements and growing availability of parameter estimation software. The simplicity of its structure had important practical implications, which had long been recognised as characteristic of simple share models. McFadden later referred to the mixed blessing of its independence of irrelevant alternatives property (section 4.2): 

The IIA property is a blessing and a curse for share models. It has two advantageous implications which make it extremely useful in practical planning. First, it implies that model calibration can be carried out by studying conditional choice in a small subset of the full set of alternatives. Thus, the dimension of the calibration data set can be reduced substantially, particularly when the full set of alternatives is large. Further, data for the omitted alternatives need not be collected, leading to economy in data collection and the possibility of improved detail on the examined alternatives. . . . A second, and related advantage that IIA has for a share model is that it allows quick analysis of the effects of introducing new alternatives. . . . The IIA property implies that the relative odds among the old alternatives are unchanged when the new alternative is introduced (McFadden, 1976b, 49–50). 

However, the MNL model was starting to be used with impunity, even though the potential drawbacks of its structure and associated elasticity properties were becoming increasingly well known. McFadden had earlier warned: 

The primary limitation of the model is that the independence of irrelevant alternatives axiom is implausible for alternative sets containing choices that are close substitutes. . . . Application of the model should be limited to situations where the alternatives can plausibly be assumed to be distinct and weighed independently in the eyes of each decision-maker (McFadden, 1973, 113). 

The consequences of applying the MNL model in a multiple choice context, where two of the alternatives were considered by individuals to be very similar, had long been recognised (Debreu, 1960). In transportation applications, this concept was illustrated in a binary choice setting between car and bus as the notorious ‘red bus – blue bus’ problem, when a particular alternative is artificially partitioned into two, according to a superficial attribute, colour, which (presumably) would have negligible effect on demand. The subsequent application of a three-mode MNL model for choice among car, red bus and blue bus clearly yields implausible results (Mayberry, 1970; McFadden, 1973). 

This conundrum, which represents an extreme case of similarity between a subset of options, could be readily resolved in practice by specifying a choice model in hierarchical form with successive binary choice models used to divide the relevant market between car and bus, and then divide the latter share between the two coloured bus modes. But, in more realistic practical applications, how was the problem of similarity among alternatives to be treated? What constituted a distinct alternative? Would the MNL model prove satisfactory in most applications? More generally, could the potential limitations arising from the failure of the IIA property of the MNL model in different mode choice situations be empirically detected and suitable adjustments applied? 

## 4.6.1.2 Avoiding the IIA property: hierarchical structures in multi-modal choice

Over the wide experience gained in traditional aggregate (zone-based) demand models and the growing applications of disaggregate methods, two possible ways of forecasting within a multi-modal system between car and two public transport modes, such as bus and rail (PT1 and PT2) had been formulated and applied. These are represented by the hierarchical approach in Figure 4.6(a) and the MNL model approach extended over three modes in Figure 4.6(b). In the former, which is not subject to the IIA property, the public transport option (PT) was effectively treated as a ‘composite’ mode, requiring the specification of appropriate level-of-service attributes in the main mode selection between car and the composite PT mode. Different composition formulations were proposed, including the ‘maximum method’, in which the attributes of the public transport submode with maximum probability were assigned to the composite PT mode, and in US terminology the ‘cascade method’, in which attributes of the different alternatives were weighted by their choice probabilities (McFadden, 1974). But, according to Spear, ‘None of these approaches have proved to be satisfactory because none of them attacks the cause of the IIA issue – the fact that there is no place in the share model formulation where the relative similarity or competitiveness of alternatives can be defined' (Spear, 1977, 146). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/38754b84-3c6e-4874-b89a-d84630ad82f8/b4aca99587e029daedc13380098541b0696a3b424d881ac074d908c47d3ae1b3.jpg)



(a) Hierarchical PT model


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/38754b84-3c6e-4874-b89a-d84630ad82f8/5c04bbc3c9288db2e2b03f9256a86372ad81176d8457554d09555de8549dc4da.jpg)



(b) MNL model



Figure 4.6 Alternative model structures for representing choice between car and two public transport modes (PT1 and PT2)


## 4.6.1.3 Diagnostic tests for the failure of the IIA property

A more general issue of key relevance to practice emerged. If the MNL model had a downside in a multi-modal choice setting, in what circumstances could its advantages of ease of application outweigh its potential disadvantages? Was the IIA property acceptable in the majority of practical studies, and to what extent was its potential failure important in relation to other problems of model misspecification or data quality? A study by Charles River Associates (1976) addressed these problems and provided diagnostic tests for the failure of the IIA property in the application of the MNL model to modal choice (McFadden et al, 1977b). They described a ‘typology of failures of the IIA property’, identifying six possible reasons with their origins in the nature of the ‘unobserved’ components of the utility functions that determined choice over the discrete alternatives. ‘As a rule, the violations may be traced to the MNL assumption that the unobserved utility component (the e ) is independent across alternatives and independent of the observed attributes’ (McFadden et al, 1977b). 

The diagnostic tests for the IIA property were based on a generalisation of the MNL model referred to as the ‘universal logit’ model, introduced by McFadden, and an interesting structure in its own right. Although not in general consistent with the random utility maximisation hypothesis, the universal logit model provided the basis for a statistical exploration of the failure from the IIA property. Its formulation ‘takes advantage of the fact that every choice model with positive probabilities can be written in apparent MNL form except that the scale function of alternative i will depend on attributes of other alternatives’ (McFadden et al, 1977b). 

At that time the significance of the IIA property in practice was unclear in relation to the practical problems associated with assembling appropriate and accurate data (Train, 1978). McFadden remarked: 

practicing planners should accept MNL as a working model, concentrate on expanding data sources for calibration, market segmentation, and variable specification, and test the IIA assumption during each application. The practicing planner should avoid ‘miracle cures’ for the IIA restriction, and examine carefully whether proposed solutions have a sound behavioral foundation or establish a germane or sensible mathematical proposition (McFadden, 1976b, 55). 

## 4.6.2 Structure of More General Urban Travel Forecasting Models

The work of CRA (1972), Ben-Akiva (1973, 1974), Ben-Akiva and Koppelman (1974) and the related studies described above offered a first principles attack on the problem of deriving a behavioural basis for structuring travel demand models that had been around for many years, at least since the issue of ‘where to put modal split’ in the traditional multi-step model had emerged in the early 1960s. These authors proposed different hypotheses for the appropriate relationship between the structure of models and the (assumed) underlying decision process. However, no definitive solution to the treatment of travel-related choices had emerged, whether a hierarchy of MNL models should be applied to the different choices or a single MNL model should be applied to the combined set of choices. 

Among some researchers it appeared that the simultaneous structure based on the MNL model had considerable appeal and was starting to be applied in studies at both the aggregate (zone-based) and disaggregate levels. Ben-Akiva and others had made an important point: in a problem of joint selection between combinations of choice alternatives, such as destination and mode, why should one ordering of choices be preferred to another? The appeal was both intuitive and practical. There was something inherently satisfying about representing a problem in which alternatives were treated jointly with a symmetric model structure, in this case the MNL model, which favoured neither choice dimension. This offered the practical benefit of avoiding the ambiguity of what particular ordering to choose. But what about the IIA property of the MNL model? Would this property cause problems in practice? Were the choices consisting of combinations of location and mode perceived to be sufficiently distinct to justify the use of such a model? 

The relationship between the structure of the demand model and the nature of the decision process in different choice contexts continued to attract comment throughout the period (Brand, 1973; Liou and Talvitie, 1974; Stopher and Meyburg, 1975). With regard to the application of behavioural models across the whole range of choice situations of relevance to urban travel forecasting, Stopher and Meyburg remarked: ‘On balance, it must be concluded that the evidence for simultaneous or recursive, sequential models is inconclusive as yet and may depend upon the specific modelling situation, and the specification problems of the models’ (Stopher and Meyburg, 1975, 305–306). 

## 4.7 CONCLUSION

Within a brief period in the early 1970s, significant advances were made in the theoretical development and practical application of the disaggregate behavioural approach to travel demand founded on discrete choice theory. These advances built on, and provided a post-hoc rationalisation for, the studies of binary modal choice of the 1960s. Most applications were still associated with the choice of mode for its relevance to peak period flows and potential policy and project development. Relative to traditional forecasting methods of that time, the new approach offered greater sophistication in the representation of individual and household behaviour, data efficiency, and applicability at any level of aggregation, as well as the prospect of (approximate) transferability in space, with the suggestion that forecasts would be more reliable. 

With the increasing availability of software for the maximum likelihood estimation of its parameters, the MNL model was becoming more widely applied: (a) in more elaborate modal choice applications; (b) to a wide variety of other decision contexts; and (c) as a component of more complex multi-dimensional models.<sup>28</sup> Many theoretical and technical issues accompanying specification, parameter estimation, transferability, validation and aggregation were studied in depth, together with applications to substantive planning problems involving transportation infrastructure projects and system management. Substantial progress was also made in a first principles approach to the structuring of travel demand models based on discrete choice theory. 

By 1976 the problems of similarity in mode choice selection and of ambiguity in structuring more complex demand models appeared somewhat distinct and still to be resolved in practice: the former, a consequence of assumptions about the random components of utility accompanying different alternatives; and the latter, somehow related to the nature of the decision process and the utility functions determining preferences over alternative choices, for which different solutions had been proposed. It appeared that corresponding problems of specification were also present in the application of conventional aggregate travel forecasting models. 

At that time it appeared that the general multinomial normal model (section 4.2) might have a significant role to play in choice modelling and, in particular, resolving ‘similarity issues’ in multi-modal choice. Indeed, in addressing unresolved problems in the mid-1970s, McFadden expressed the opinion: 

There is a pressing need for development of practical models for selection probabilities which do not have the independence of irrelevant alternatives property. . . . It would be particularly useful to achieve a computational breakthrough on the multinomial normal model. . . . An alternative approach which may yield practical functional forms for applications is to seek more general axioms characterizing classes of selection probabilities. One such construction is the elimination by aspects model of Tversky (1972) (McFadden, 1976a, 381, 370). 

On the distinction between aggregate and disaggregate models, McFadden (1976b) commented: 

They differ primarily in degree. Disaggregation carries . . . market segmentation to the extreme; it emphasizes the regularity of individual choice behavior. . . .  Aggregate and disaggregate models differ significantly in the number and form of explanatory variables, consistency across different aspects of travel behaviour, calibration methods, and forecasting technique. These differences are, however, primarily technical, the result of historical development and the practical limitations of data compilation and computation. Behind every good aggregate model is a disaggregate model, and vice versa. The discovery of empirically valid regularities which simplify and extend forecasting methodology and the relaxation of empirically invalid restrictions should be the goal of every transportation analyst. From this point of view, disaggregate behavioural forecasting is a natural evolution of traditional aggregate demand analysis (McFadden, 1976b, 8). 

In retrospect, the disaggregate approach based on random utility theory clearly encouraged a range of sentiments among researchers and practitioners. From the literature one senses a true spirit of optimism among its pioneers. Here was an approach based on what were considered sound behavioural foundations that addressed some of the perennial problems of traditional practice, and appeared up to the challenge of the times. Moreover, in practice a barrier was breached in the application of complex choice models; those coming after would be able to improve on the approach and be less daunted by practical challenges. 

The number of active researchers in disaggregate modelling remained relatively small, but was growing in various university departments, some consultancies and some government agencies. By the mid-1970s the new thinking had been exported from the US, and was becoming increasingly applied in research and some applications in Canada, Europe and Australia. The development and transfer of ideas require inspirational people with intellectual energy and powers of persuasion. In this regard Marvin Manheim [1937–2000] was a key figure in the introduction of the disaggregate behavioural approach, not only in persuading people to work in the area, but also in founding the consultancy Cambridge Systematics. His collaboration with Moshe Ben-Akiva was particularly productive in this regard, especially in transferring the approach to the Netherlands. Moreover, the random utility approach to behavioural modelling was being independently developed for local requirements and interests, as illustrated by the innovative British studies noted. As Stopher and Meyburg stated, by the mid-1970s it was ‘widely held by researchers that this approach has the greatest likelihood of providing the basis for a totally new and more policy-responsive travel-forecasting procedure’ (Stopher and Meyburg, 1975, 273). 

Among the broad community of urban policy analysts and transportation practitioners, however, feelings at this time appear to have been rather mixed. Although the theory and techniques were becoming increasingly widely known, whether they were accompanied by wide acceptance is debatable. Indeed, notwithstanding the advances claimed, some (perhaps many) practitioners at the time considered the approach rather naïve and impractical relative to tested aggregate methods.<sup>29</sup> After all, the approach had yet to be fully tested on the traditional application grounds of urban travel forecasting models. In this regard, many eyes were on the Metropolitan Transportation Commission (MTC) of the San Francisco Bay Area; unsatisfied with its existing travel demand model system, MTC was implementing the new approach to address the prospects for a wide range of long-run and short-run plans and policies. Spear remarked: 

The MTC project is clearly at the forefront of applications of individual choice models. Both researchers and planners alike are watching this project closely to see whether the resulting travel demand forecasts are more reliable or can be obtained more efficiently than with traditional models. Its outcome should go a long way towards determining the ultimate role of individual choice models in transportation planning (Spear, 1977, 31–32). 

We recount the outcome of these developments in the next chapter. 

## NOTES



1. The earliest study of route choice from a choice theoretic perspective is that by Abraham (1961). See also Thomas and Thompson (1971) and the references cited therein. 





2. en.wikipedia.org/wiki/R._Duncan_Luce (accessed 28 December 2013). 





3. The IIA axiom is sometimes referred to as the independence from irrelevant alternatives axiom. 





4. en.wikipedia.org/wiki/Louis_Leon_Thurstone (accessed 6 March 2014). 





5. en.wikipedia.org/wiki/Jacob_Marschak (accessed 6 March 2014). 





6. en.wikipedia.org/wiki/Daniel_McFadden (accessed 2 January 2014). 





7. The probability that an arbitrary individual $q$ will select an alternative $A _ { j }$ from a set of alternatives ${ \cal A } = ( A _ { 1 } . \ . \ A _ { i } . \ . \ A _ { N } )$ will be written $P _ { j q } .$ In general the choice set will vary within the population, and we shall denote $A ( q ) { \in } \tilde { A }$ as the set of alternatives from A that are available to the individual $q .$ . From the modeller’s perspective, the probability that a utility maximising individual $q$ will select $A _ { j }$ is given by: 



$$
P _ {j q} = \operatorname{Prob} \left(U _ {j q} \geq U _ {i q} f o r a l l A _ {i} \in A (q)\right)
$$

In terms of the representative utilities and residual errors the choice probability becomes: 

$$
P _ {j q} = \operatorname{Prob} \left(V _ {j q} + E _ {j q} \geq V _ {i q} + E _ {i q} \text {   for   all   } A _ {i} \in A (q)\right).
$$

8. The compensatory linear-in-parameters utility function is written as follows: 

$$
V _ {j q} = \sum_ {k} \theta_ {k j q} h \left(x _ {k j q}\right)
$$

where $h ( . )$ is a function of the measured attributes $x _ { j k q } .$ The parameters $\theta _ { k j q }$ will, in general, vary over the alternatives $( j ) ,$ the attributes $( k )$ and the individuals $\overset { \cdot } { ( q ) }$ . In the common ‘fixed coefficients’ model, the parameters $\theta _ { k j q }$ are common across individuals, while in ‘random coefficients’ or ‘random parameters’ models the parameters $\begin{array} { r } { \ \Theta = ( \theta _ { k j q } ) } \end{array}$ will vary over individuals. In the linear-in-parameters–linear-in-attributes form (this is not unduly restrictive), with the parameter set q independent of the individual: 

$$
V _ {j q} = \sum_ {k = 1} ^ {K} \theta_ {w j k} x _ {j k q},
$$

which in vector notation is abbreviated as 

$$
V _ {j q} = \theta_ {j} \cdot x _ {j q}.
$$

In the practical implementation of the MNL, the utility function may be expressed in several ways. For a full discussion of utility forms, see McFadden (1976b) and the texts: Hensher and Johnson (1981), Ben-Akiva and Lerman (1985), Hensher et al (2005), Koppelman and Bhat (2006) and Ortúzar and Willumsen (2011, Chapters 7, 8). 

9. Two different strategies were applied to suggest different functional forms for the utility functions. The utility-theoretic approach based on goods–leisure trade-off models of individual budgeting, in which the representative utilities $V$ emerge as indirect utility functions, was first considered by McFadden (1976b) and McFadden and Train (1978). For a discussion of an alternative approach that identified the functional form that gives the best fit to the data see Gaudry and Wills (1978), Jara-Diaz (2007) and Ortúzar and Willumsen (2011). 

10. Dropping the individual label $q ,$ the probability that an arbitrary individual will select $A _ { j }$ is given in terms of the joint probability density function of the residuals $F ( E _ { 1 } . \cdot . E _ { N } )$ as follows: 

$$
P _ {j} = \int_ {R (j)} F (E _ {1} \dots \dots E _ {N}) d E _ {1} \dots d E _ {N},
$$

in which the region of integration $R ( j )$ is defined by: 

$$
R (j) \colon U _ {j} \geq U _ {i} \text {   or   } E _ {i} \leq E _ {j} + (V _ {j} - V _ {i}) \text {   for   all   } A _ {i} \in A.
$$

11. In Quandt’s model, the selection probabilities for each mode were determined by identifying the combination of parameters which minimised disutility (a process of integrating over the parameter distributions) with a cut-off introduced to reflect the hypothesis that a trip would not be made if the disutility exceeded that threshold. In this way, a generation effect, in which the total journevs were made sensitive to the transportation service characteristics, was built into the modal split model. The determination of the selection probabilities for this model required numerical solution. 

12. Gaudry and Quinet (2011) have discussed the seminal work of French engineers in the late 1950s and in particular the work of Abraham (1961), who derived choice models for two and three routes, in which the link generalised costs were distributed according to a variety of assumptions, including normal and rectangular forms. Various probabilistic choice models were derived including the probit, which were seen as a justification of the then current use of the ‘log logit’ forms. The complexity arising from the existence of a common link in the three-route case was also considered. 

13. The difference between this distribution and the normal curve is portrayed in several texts, for example Domencich and McFadden (1975, 62) and Koppelman and Bhat (2006, 27). 

14. For the MNL model written in the form: 

$$
P _ {j} = \frac {\exp (\lambda V _ {j})}{\sum_ {A _ {i} \in A} \exp (\lambda V _ {i})}
$$

the ‘logsum’ is given by: 

$$
\text { `logsum' } = \frac {1}{\lambda} \left(\ln \sum_ {A _ {i} \in A} \exp (\lambda V _ {i})\right),
$$

$$
\text { or   } \text { `logsum' } = \left(\ln \sum_ {A _ {i} \in A} \exp (V _ {i})\right)
$$

if the model is standardised such that $\lambda = 1$ 

15. The formulation of the MNL model from distributed utilities was first established by Marschak (1960), adopting a ‘nonconstructive proof’ (McFadden, 1973, 111), and was strengthened by E. Holman and A. Marley (cited by Luce and Suppes, 1965). ‘McFadden (1968, 1973) completed the analysis by showing the converse: that the logit formula for the choice probabilities necessarily implies that unobserved utility is distributed extreme value' (Train, 2009). 

16. en.wikipedia.org/wiki/Waloddi_Weibull (accessed 29 December 2013). 

17. We are grateful to Jorgen Weibull for this anecdote about his grandfather. 

18. The Gumbel Type I extreme value distribution is written as follows: 

$$
f (U _ {j}, V _ {j}) = f (U _ {j} - V _ {j}) \equiv f (\varepsilon_ {j})
$$

with $\begin{array} { r } { f ( \mathfrak { E } _ { j } ) = \lambda \exp ( - \lambda \mathfrak { E } _ { j } ) \cdot \exp ( - \exp ( - \lambda \mathfrak { E } _ { j } ) ) } \end{array}$ , and cumulative distribution given by the double exponential form: 

$$
F (\varepsilon_ {j}) = \exp (- \exp (- \lambda \varepsilon_ {j}))
$$

The mean of the random variable $U _ { j }$ is given by $V _ { \mathrm { ~ i ~ } } + \mathrm { ~ } \forall / \lambda$ where $\gamma$ is Euler's constant 5 0.577, and the variance of $U _ { j } ^ { ' }$ is given by $\pi ^ { 2 } / 6 \lambda ^ { 2 }$ . The derivation of the MNL model from the IID Gumbel distributions is relatively straightforward; details may be found in McFadden (1973) and Domencich and McFadden (1975); see also Stopher and Meyburg (1975) and Ben-Akiva and Lerman (1985). 

19. The authors are grateful to Frank Koppelman for discussion on this point. 

20. The form of the shopping model adopted by CRA (1972) was as follows: the probability of selecting a given combination of frequency, destination, timing and mode $P ( f , d , \tau , m )$ was written: 

$$
P (f, d, \tau , m) = P (f) P (d | f)   P (\tau | d, f)   P (m | \tau , d, f)
$$

in which $f , d , \tau$ and m denote choices relating to: frequency (one trip per day versus no trip), destination (ranging from three to five for each observation), time of day of travel (both legs in the off-peak versus one leg in the off-peak and one leg in the peak) and mode (car driver versus transit rider with walk access), respectively. Linear probability and logit models were applied and many variable combinations were tested. 

21. When applied to model structure, Ben-Akiva used the term ‘recursive’ to correspond to a sequential decision-making process. In the general literature the term ‘sequential’ is also used to describe the structure of a model. 

22. For example, in a context involving destination and mode with a utility function of the form: 

$$
V (d, m) = V _ {d} + V _ {d m}
$$

the MNL model with probabilities $P _ { d m }$ can be written: 

$$
P _ {d m} = \frac {\exp (V _ {d} + V _ {d m})}{\sum_ {d \in D} \exp (V _ {d} + V _ {d m})} = \frac {\exp (V _ {d} + \theta V _ {d} ^ {*})}{\sum_ {d \in D} \exp (V _ {d} + \theta V _ {d} ^ {*})} \frac {\exp (V _ {d m})}{\sum_ {m \in M} \exp (V _ {d m})}
$$

with q 5 1 and $V _ { d } ^ { * } = \ln \sum _ { m \in M } \exp ( V _ { d m } ) .$ 

23. Martin Richards, personal communication to Huw Williams, 2013. 

24. Wilson (1967, 1970) proposed many models according to different contexts and assumptions. Here Richards and Ben-Akiva (1975) are referring to his ‘joint distribution modal split model’. 

25. Robert Cochrane, personal communication to Huw Williams, 2011, stated that the passenger demand model, developed by John Pendlebury, was of hierarchical logit form with generalised cost in power function form. 

26. Cochrane’s paper was submitted to the Journal of Transport Economics and Policy in 1972. It had a protracted journey through the review process, and its publication was delayed until 1975, partly because of the difficulty of selecting suitable reviewers (Robert Cochrane, personal communication to Huw Williams, 2010). 

27. Interestingly, the personal multiplier case has recently received attention by Fosgerau and Bierlaire (2009), who report improvements in ‘goodness-of-fit’ compared with the more usual error structures. 

28. There are many specialist texts and manuals that discuss the specification, estimation and application of the MNL model: see, for example, Ben-Akiva and Lerman (1985), Hensher et al (2005) and Ortúzar and Willumsen (2011), as well as the excellent Self Instructing Course by Koppelman and Bhat (2006, Chapters 4–7) for more details. 

29. Peter Stopher, personal communication to Huw Williams, 2009. 

## 5. Travel forecasting based on discrete choice models, II

## 5.1 INTRODUCTION

Great strides were made in the early 1970s to develop an approach to urban travel forecasting that involved summing up (aggregating) the probable behaviour of individuals derived from models specified and estimated at the micro-level. For such models, the discrete choice random utility maximising (RUM) framework provided the theoretical and practical foundations for multi-modal forecasting and for exploring the relationship between the structure of models and hypotheses relating to the trip decision process. In this chapter we recount further theoretical and practical developments of this approach. We arrange this material in two parts: sections 5.2 to 5.6 recount developments in the period from the mid-1970s to the mid-1980s, while section 5.7 provides a guide to more recent advances. 

The reasons for this partition are as follows. The first period contains a large amount of innovative material, which found its way fairly quickly into applied studies and remains of great practical relevance today. However, a very substantial volume of research on discrete choice travelrelated modelling based on random utility theory has been conducted since the mid-1980s and disseminated in journals, conferences and texts. Although it is too early to say which models and methods will become widely absorbed into routine travel forecasting practice, this work proved to be conceptually appealing, technically demanding and (therefore) irresistible to exponents of quantitative research. This divide in the mid-1980s is also rather convenient for introducing what some have described as a new behavioural paradigm based on the human activity approach, considered in Chapter 6, which began to make a major impression on how travel behaviour was viewed and analysed. Those who seek to preserve a broadly chronological progression between chapters might find it convenient to skip section 5.7 on first reading. 

Let us return now to the mid-1970s when the multinomial logit (MNL) model had become the dominant instrument of practical analysis within the disaggregate modelling approach to travel forecasting. In section 4.6.1 we saw how the ease of application of the MNL model was offset by a set of potential problems that were also encountered with some conventional aggregate models. We also noted that by the mid-1970s the selection of the order of individual choice models within model hierarchies, the means of interfacing or linking' them, and indeed whether that structure should be abandoned in favour of an approach consisting of a single MNL model extended over several choice dimensions were all outstanding issues requiring further research. 

In seeking to relax the restrictive properties of the MNL model, researchers had been aware since the early 1970s (McFadden, 1973) of the need to balance the generality attributed to the joint distribution of utility variables over the different alternatives with the practical consequences for the solution of the model and estimation of its parameters. From the mid-1970s two approaches would be adopted to achieve practical extensions to the family of random utility models. The first, the direct approach, involved specifving explicit distributions for the random components of the utilities of alternatives that reflected credible behavioural assumptions. With careful selection these might be amenable to analytic resolution of the choice model and result in closed form expressions for the probabilities of choice. Otherwise, a direct numerical attack would be required in order to solve the mathematical problem (the multiple integral) that determined the choice probabilities. The second approach to generating choice models was through the establishment of general mathematical conditions to be satisfied by the model, which rendered it consistent with the hypothesis of random utility maximisation, and to seek suitable model forms that offered behavioural realism while being amenable to practical implementation (McFadden, 1973, 1976b; Harris and Tanner, 1974). In this chapter we shall encounter both of these approaches. 

By the early 1970s the construction of travel demand models by linking together MNL models in a sequence or hierarchy had appeared in various studies both at the aggregate zone-based level (Wilson, 1969, 1970; Wilson et al, 1969; Manheim, 1973) and in discrete choice models applied at the micro-level (see section 4.1 for a discussion of the term) (Stopher and Lisco, 1970; Charles River Associates, CRA, 1972; Ben-Akiva, 1973, 1974). In such models travel markets (associated with different modes, destinations, etc.) were successively partitioned according to MNL shares in aggregate forms or through the product of MNL probabilities in discrete choice models applied at the micro-level. 

For more than one MNL model arranged hierarchically it would turn out that the ‘logsum’, the logarithm of the denominator of the MNL model at a lower level, would be a particularly suitable choice of variable for the linkage to the MNL at the next higher level. To our knowledge the first application of a correctly specified ‘logsum’ linkage within a hierarchical arrangement of MNL models was by Ben-Akiva (1973, 1974), as described in section 4.4.3. The full theoretical significance of this linkage, as Ortúzar (2001) remarked, was not however fully resolved until the mid-1970s. Indeed, it is interesting to note that by the early 1970s a ‘logsum’ expression was making an appearance in travel demand modelling in different ways and, from a historical perspective, it is important to note the distinction between them. The ‘logsum’, or an equivalent analytical form,<sup>1</sup> appeared in three different contexts: 

1. structural decomposition of the MNL model applied to two or more dimensions, such as destination and mode (Wilson, 1967, 1970; Ben-Akiva, 1973, 1974; Manheim, 1973); 

2. generalised consumer surplus measures derived for spatial interaction models of MNL form (Wilson and Kirwan, 1969; Neuberger, 1971) (section 3.8); 

3. expected maximum utility (or expected minimum generalised cost) measures for discrete choice problems involving Gumbel distributed utility (or generalised cost) variables (Harris and Tanner, 1974; Cochrane, 1975; Domencich and McFadden, 1975; Koenig, 1975) (sections 4.2, 4.5). 

The first was a purely mathematical consequence of the properties of the MNL share model applied to different subsets of the alternative choices; the second and third were theoretical consequences of the economic analysis of travel choice at the aggregate and micro-levels, respectively, arising from particular forms for the utility functions used to generate the MNL demand model. In the early 1970s the connection between these different interpretations was not apparent. 

The search for a practical generalisation of the MNL model, consistent with random utility maximisation (RUM), that was not subject to the independence of irrelevant alternatives (IIA) property led to the derivation of the nested logit (NL) model by Williams (1977a) and Daly and Zachary (1978), and a wider class of choice models by McFadden (1978), which contained the NL model as an important special case. Because the NL model and its special case, the MNL model, have dominated practical applications of discrete choice methods in urban travel forecasting to this day, we give an extended description of the contexts within which these studies took place. 

In section 5.2 we discuss alternative approaches to the derivation, interpretation and application of the variously described structured logit, tree logit, hierarchical logit and nested logit model of Williams and that of 

Daly and Zachary. These British researchers first became aware of their independent work on the NL model in December 1975, prior to presentations at conferences in Leeds and the 1976 annual meeting of the Planning and Transport Research and Computation Co. (PTRC), respectively. In section 5.3 we turn to the theoretical highpoint of the discrete choice random utility maximising approach in this period with an account of McFadden’s research on the generalised extreme value (GEV) model (McFadden, 1978, 1981). 

Concurrent with efforts in the early 1970s to achieve manageable closed form generalisations of the MNL model were direct numerical approaches to solve a range of individual choice models within the discrete choice random utility framework. In particular, an efficient solution of the multinomial probit (MNP) model that would address both general patterns of similarity among alternatives and taste variation over a population was keenly sought. In section 5.4 we consider these numerical approaches, and in particular the early use of the microsimulation technique and some of the wider contexts within which it was applied. 

We return in section 5.5 from the broader theoretical development of the behavioural approach based on discrete choice theory to consider progress on the practical challenge of adapting the new disaggregate style of travel forecasting to the short-run and longer-term policy requirements of a metropolitan planning organisation. We describe the first successful attempts, achieved initially in the US and subsequently in the Netherlands, to apply behaviourally sophisticated models as practical alternatives to conventional methods. These efforts constituted the highpoint of what is sometimes referred to as the ‘trip-based’ approach to travel forecasting. 

One of the most significant developments in the history of our field was the introduction of experimental methods for the examination of attitudes, preferences and choices as a basis for travel forecasting. In section 5.6 we discuss the emergence of ‘stated preference’ methods out of the fields of mathematical psychology and marketing, and their gradual acceptance by the travel forecasting community in the first half of the 1980s. 

In section 5.7 we turn to the second part of the chapter and describe those developments of the discrete choice random utility maximising approach that have occurred since the mid-1980s, only a few of which have as vet found routine application in urban travel forecasting. All are, neyertheless, of great significance in the conceptual development of the field, currently widely applied in research, and an essential means by which the assumptions underpinning more widely used models are scrutinised. 

An assessment of the contribution of the behavioural approach to travel forecasting based on discrete choice random utility models concludes the chapter. 

## 5.2 CHOICE BETWEEN SIMILAR ALTERNATIVES: THE NESTED LOGIT (NL) MODEL

## 5.2.1 Derivation and Application of the NL Model: Research by Williams and Senior

In late 1973 Huw Williams was working at the Institute for Transport Studies at the University of Leeds on a set of problems that, at the outset, appeared to him to have little or no connection. Having completed a review of the travel demand models adopted in 25 British transportation studies (see section 3.7.3), Williams was seeking to understand a number of aspects: 

1. justifications for the different ordering of the steps in the traditional forecasting structure and the means by which they were inter-linked; 

2. different ways models were specified for multi-modal systems and, in particular, for ‘pure mode’ and ‘mixed mode’ problems; 

3. means by which the demand models were ‘interfaced with’ the evaluation stage to compute measures of user benefits derived from projects and policies. 

To address these problems Williams turned to the discrete choice approach and, in particular, to the random utility formulation proposed by CRA (1972) and Ben-Akiva (1973, 1974). 

## 5.2.1.1 Tree representations, patterns of similarity and the NL model

Williams argued that the conditions required for the MNL model to be applied, that of ‘distinctness of the alternatives’, and mathematically expressed by the independence of the random utility variables, would in general be violated for many applications involving both multiple modes and complex combinations of choice dimensions, and for the same reasons. He suggested that the issue of similarity between the alternative choices and the correlation of their utilities was at the heart of model specification for both applications, and rejected the view that the MNL form would in general prove to be appropriate for practical analysis in these cases. 

Drawing on the findings in CRA (1972), Williams explored the formation of random utility models in terms of the transmission of information required for individuals to make optimal choices over a set of alternatives (either a set of modes, or more complex multi-dimensional cases involving combinations of frequency, location, mode and route) endowed with utility functions of additive separable forms. As discussed in section 4.4, these forms allowed the decision process to be conveniently represented as choices in tree-like structures in which conditional utility maximising decisions were made at the different nodes N and at different levels L of the tree. 

Williams argued that the structure of the tree reflected the pattern of similarity among the different alternative choices and that correlation between the utilities of those alternatives occurred because of the presence of random components of utility on the various branches above the ‘lowest’ choice, which would be common to a subset of the choices. He proposed that the distinctions between alternative ordering of choices underpinning travel forecasting models and, in particular, the structures F/D/M/R, F/M/D/R and F/D − M/R, shown in Figure 5.1, could be interpreted as representing different assumptions about the distinct patterns of similarity among the choice combinations of frequency (F), destination (D), mode (M) and route (R). In all cases, individuals were considered to make rational choices according to utility maximisation, and the structure of the demand model would reflect a priori assumptions about the pattern of correlation among the utilities of the different alternatives in the set of choices available. 

In a similar fashion, in the case of multiple modes and mixed modes, the tree structures shown in Figures 5.2 and 5.3, respectively, represented choice between alternatives whose associated utility functions contain a common (random) utility component among subsets of choices. For the three modes, car, train and bus, the existence of this random component of utility, common to the public transport modes, as shown in Figure 5.2, reflects a pattern of correlation and similarity which required their inclusion within a composite public transport ‘nest’ within the tree. For the case of mixed modes involving park and ride Williams hypothesised that the location of parking with respect to the origin and destination of the trip would determine the extent of any common component of utility, and therefore of any similarity, between the park-and-ride option and an alternative mode (car or public transport). This would then determine the form of hierarchy adopted, as shown in Figure 5.3. 

As in the analysis of CRA (1972), individuals could be thought of as making conditional decisions at each node N over the relevant set of alternatives within such tree structures (within an overall utility maximising framework). The solution for the probability of choice of any combined alternative thus involved solving the problem as if individuals were making decisions progressively, at each node seeking their maximum utility option from the available set of subsequent choices, and progressing upwards through the tree to achieve an optimal (utility maximising) solution. 

In order to generate the MNL probabilities for the conditional probabilities at each node and at every level of the tree, Williams made the assumption that the utilities at the nodes were Gumbel distributed with standard deviation that was common to all alternatives at the same level of the tree. At any node and at every level, the probability of selecting an option in the relevant set of choices would be represented by an MNL model, with a characteristic response parameter $\lambda _ { \mathrm { { L } } } ,$ common to all nodes at that level L. The probability of an individual selecting a given combination of frequency, location, mode and route was then described as a product of MNL models with associated parameter values $\lambda _ { \mathrm { B } } \ldots \lambda _ { \mathrm { L } } \ldots \lambda _ { \mathrm { T } }$ for the various levels L from the bottom (B) to the top (T), or apex, of the tree. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/38754b84-3c6e-4874-b89a-d84630ad82f8/7b4e49aa50568037d9ef43706146ed0742dd95d9cbd6e8225f3f7e835b105e9e.jpg)



<sub>and</sub> <sub>routes</sub> <sub>(R),</sub> <sub>wit</sub>h <sup>parameter</sup> <sup>restrictions</sup> <sup>appropriate</sup> <sup>to</sup> <sup>the</sup> <sup>selec</sup> <sub>uctures</sub> <sub>for</sub> <sub>alternative</sub> <sub>nested</sub> <sub>logit</sub> <sub>models</sub> <sub>over</sub> m<sup>ultiple</sup> <sup>dimensions:</sup> <sup>frequenci</sup>



<sub>sed</sub> <sub>on</sub> <sub>Williams</sub> <sub>(1</sub>9<sup>77a)</sup> <sup>and</sup> <sup>Williams</sup> <sup>and</sup> <sup>Se</sup>


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/38754b84-3c6e-4874-b89a-d84630ad82f8/017bc216a8ff452c928324c7f1bc64798f21f417bb702c494e226bad96cd1180.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/38754b84-3c6e-4874-b89a-d84630ad82f8/ad407a956595ff4a392176e353cdf9c06a27208bd816a3054ccd0fe6e7e33a1f.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/38754b84-3c6e-4874-b89a-d84630ad82f8/0d49d8bc760cb98f574ce9b29e0f68126ec8372eee7f1636eb14847e7040d799.jpg)



Source: Adapted from Williams (1977a, 1977b).



Figure 5.2 Tree structures for nested logit and multinomial logit models for choice between car, rail and bus


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-15/38754b84-3c6e-4874-b89a-d84630ad82f8/cecf698a7f2d3b966566a462fdac90d53e468a9d60553f9f9ef85514707e4c55.jpg)



Source: Adapted from Williams (1977b).



Figure 5.3 Alternative nested logit and multinomial logit model structures for mixed mode forecasting


## 5.2.1.2 Nature of composite utilities or costs

With regard to the nature of the variously described ‘composite utility’, ‘composite cost’ or ‘combination rule’, CRA (1972) had already done most of the hard work; however, ‘inclusive values using linear averaging formulas brought over from the theory of separable preferences for a representative consumer’ (McFadden, 2000b, 5) had resulted in an inappropriate form. Williams argued that within the random utility framework the mean of the distribution of maximum utility $F _ { M A X } ( U )$ over the set of choices at any node was responsible for transmitting information about optimal choices ‘further down’ the tree to its higher levels.<sup>2</sup> For Gumbel distributed variables, responsible for generating the MNL models at each level of the tree, expressions for the expected maximum utilities, and hence the composite cost functions, were given by the ‘logsums’ over the appropriate choice set. Williams provided these expressions for the different levels to derive random utility models corresponding to the three tree structures in Figure 5.1. Similarly, in the multiple mode context the mean of the distribution of the maximum utility, the ‘logsum’ (in this case, the natural logarithm of the denominator of the bus–rail binary logit choice model in Figure 5.2), would be used to represent the composite utility (disutility) associated with choice over the public transport ‘nest’. 

In exploring the properties of the composite utilities or costs, Williams (1977a, 1977b) also sought to explain why the widely adopted form, the mean of the representative utilities (or generalised costs) of the different choice alternatives weighted by their probabilities of selection, was unsuitable for use as an ‘average measure’ for transmitting information to different levels in structuring demand models. This question led him to consider the distribution of utilities over ‘selected choices’, and he gave some attention to what is now referred to as the distinction between the ‘offered’ and ‘achieved’ or ‘received’ utilities.<sup>3</sup> This distinction had also been noted by Cochrane (1975), as discussed in section 4.5.3. Williams showed that the expected value of the distribution of maximum utility could also be 