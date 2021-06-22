import dash
import dash_html_components as html
from dash_extensions import Lottie  # pip install dash-extensions
import dash_bootstrap_components as dbc  # pip install dash-bootstrap-components

# Lottie by Emil - https://github.com/thedirtyfew/dash-extensions
url_location = "https://assets2.lottiefiles.com/packages/lf20_7wk7kgde.json"
url_email = "https://assets1.lottiefiles.com/packages/lf20_tsdhbs.json"
url_phone = "https://assets7.lottiefiles.com/packages/lf20_Vx5c3M/13_phone.json"
url_linkedin = "https://assets5.lottiefiles.com/private_files/lf30_USzW1X.json"
url_education = "https://assets4.lottiefiles.com/private_files/lf30_ufoa7nnt.json"
url_hiking = "https://assets3.lottiefiles.com/packages/lf20_jtqgvzal.json"
url_reading = "https://assets8.lottiefiles.com/packages/lf20_2wesdfa5.json"
url_movie = "https://assets3.lottiefiles.com/private_files/lf30_xMRTDW.json"
url_music = "https://assets4.lottiefiles.com/packages/lf20_NUz0ZU.json"
url_github = "https://assets4.lottiefiles.com/packages/lf20_6HFXXE.json"
options = dict(loop=True,autoplay=True,rendererSettings=dict(preserveAspectRatio='xMidYMid slice'))

# DATA INPUT VARIABLES
name = "HILMAN REVISIONERY"

job_role = "DATA SCIENTIST"

pf1 = html.P("""Start as Proposal Engineer for 2 years, it makes me
                comfortable working with large of data. So I
                decided to shift my career to be a Data
                Scientist.""",
             style={'text-indent': '3em',"text-align": "justify", "margin-bottom": "0px"})

pf2 = html.P("""My first jump into this field is taking a course
        in Data Science. Now I’ve worked as Data
        Scientist for 1 and a half years, and get
        experience working with real data. It makes me
        always love to learn about Data Science and its
        related field with high curiosity and passionate.""",
             style={'text-indent': '3em', "text-align": "justify", "margin-bottom": "0px"})

location = 'Jakarta, Indonesia'
handphone = '087885271600'
email_adress = "hilman.revisionery@gmail.com"
linkedin_name = 'Hilman Revisionery'
linkedin_link = "https://www.linkedin.com/in/hilman-revisionery-48ba21191/"
git_name = 'hilmandei'
git_url = "https://github.com/hilmandei"


company_1 = {'position': 'DATA SCIENTIST',
             'company': "PT. ASURANSI SINARMAS | Sept 2019 - January 2021",
             'jobdesc': ["""Developing an automation system that's used for increasing cost 
              efficiency based on an insight from existing data.""",
              "Maintaining & improving the accuracy of an automation system.",
              """Developing OCR optimization from offered Proposal, then it's used to evaluate 
              the feasibility of the Proposal (based on company policy).""",
             """Crawling data to find the occurrence liability (i.e. vehicle accident or natural disaster in news, 
              blacklist person, measure the shortest distance of firefighters to risk location, etc.)""",
             """Developing machine learning to predict News Classification, that meets with Insurance coverage.""",
             """Developing OCR system for handwritten digit based on form
                claim."""]}

company_2 = {'position': 'PROJECT ENGINEER',
             'company': "PT. TRUBA JAYA ENGINEERING | June 2017 - March 2019",
             'jobdesc': ["Make a progress from Subcont Work and also review the Subcont’s report.",
                         "Clarifying the scope of work, technical issue, engineering docs with Subcont."]}

company_3 = {'position': 'PROPOSAL ENGINEER',
             'company': "PT. TRUBA JAYA ENGINEERING | June 2015 - June 2017",
             'jobdesc': ["Make an estimation and calculation for mechanical projects.",
                         "Preparing all the required bidding doc for Mechanical project."]}

soft_skill = ["2 years experience in analytical skills as Proposal Engineer",
              "Enjoy working with others as a Team","Problem-Solving Mindset",
              'Passionate in learning something new']

certificate = ["AIML at Letsupgrade, 2020",
               "Statistic for Data Science at Greatlearning, 2020",
               "Data Science for Industry at Codplex, 2020",
               "Data Science at Purwadhika - Coding School, 2019"]

# Setting Lay-Out CV
# Bootstrap themes by Ann: https://hellodash.pythonanywhere.com/theme_explorer
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX])
app.layout = dbc.Container([
    dbc.Row([
        # Column 1 ====================================================================================================
        dbc.Col([
            # Photo section
            dbc.Card([
                dbc.CardImg(src='/assets/Hilman.jpg',
                            style={'width': '120px','height': '150px',"margin-left": "5%","margin-top": "1%"})
                # 150px by 45px
            ],style={'border': 'None'}),

            # Name Section
            dbc.Card([
                dbc.CardBody([
                    html.H3(name,style={"color": "black","font-weight": "bold"}),
                    html.H4(job_role,style={"color": "blue","font-weight": "bold"})])
            ],style={'border': 'None',"margin-top": "1%","margin-bottom": "1%"}),

            # Personal Profile
            dbc.Card([dbc.CardHeader('PERSONAL PROFILE',style={"color": "blue","font-weight": "bold"}),
                      dbc.CardBody([html.P([pf1,html.Nobr(),pf2])])]),

            # Contact Info
            dbc.Card([dbc.CardHeader('CONTACT INFO',style={"color": "blue","font-weight": "bold"}),
                      dbc.CardBody([
                          dbc.Row([dbc.Col(Lottie(options=options,width="30px",height="30px", url=url_location,),
                                           width="auto",align='center'),
                                   dbc.Col(location,width="auto",style={"text-align": "center"})],
                                  style={'width': '400px','height': '30px'}),
                          dbc.Row([dbc.Col(Lottie(options=options,width="30px",height="30px",url=url_phone),
                                           width="auto",align='center'),
                                   dbc.Col(handphone,width="auto",style={"text-align": "center"})],
                                  style={'width': '400px','height': '30px'}),
                          dbc.Row([dbc.Col(Lottie(options=options,width="30px",height="30px",url=url_email),
                                           width="auto",align='center'),
                                   dbc.Col(email_adress,width="auto",style={"text-align": "center"})],
                                  style={'width': '400px','height': '30px'}),
                          dbc.Row([dbc.Col([Lottie(options=options,width="30px",height="30px",url=url_linkedin)],
                                           width="auto", align='center'),
                                   dbc.Col(dbc.CardLink(linkedin_name,target="_blank",
                                                        href=linkedin_link,style={"text-align": "center"}),width="auto",
                                           align='center')],
                                  style={'width': '450px'}),
                          dbc.Row([dbc.Col([Lottie(options=options,width="30px",height="30px", url=url_github)],
                                           width="auto", align='center'),
                                   dbc.Col(dbc.CardLink(git_name,target="_blank",
                                                        href=git_url, style={"text-align": "center"}), width="auto",
                                           align='center')],
                                  style={'width': '450px'})
                      ])
                      ]),

            # Education
            dbc.Card([dbc.CardHeader('EDUCATION',style={"color": "blue","font-weight": "bold"}),
                      dbc.CardBody([
                          dbc.Row([
                              dbc.Col([Lottie(options=options,width="70px",height="70px",url=url_education),html.P()],
                                      width="6%",align='center',style={"margin-left": "5px"}
                                      ),
                              dbc.Col([html.H6('TRISAKTI UNIVERSITY',style={"font-weight": "bold"}),
                                       html.P('Petroleum Engineering | May 2010 - Oct 2014',
                                              style={"margin-bottom": "0px"}),
                                       html.P('GPA: 3.61 | 4.0')],width="370",align='center',
                                      style={"margin-left": "15px"})],
                              style={'width': '450px','height': '70px'})])]),

            # Hobbies
            dbc.Card([dbc.CardHeader('HOBBIES',style={"font-weight": "bold",'color': "blue",}),
                      dbc.CardBody([
                          dbc.Row([dbc.Col(Lottie(options=options,width="40px",height="40px",url=url_hiking),
                                           width="auto",align='center'),
                                   dbc.Col("Hiking Mountain",width="auto",
                                           style={"text-align": "center","margin-top": "10px"})],
                                  style={'width': '400px','height': '40px'}),
                          dbc.Row(
                              [dbc.Col(Lottie(options=options,width="40px",height="40px",url=url_reading),width="auto",
                                       align='center'),
                               dbc.Col("Reading Book",width="auto",
                                       style={"text-align": "center","margin-top": "10px"})],
                              style={'width': '400px','height': '40px'}),
                          dbc.Row(
                              [dbc.Col(Lottie(options=options,width="40px",height="40px",url=url_movie),width="auto",
                                       align='center'),
                               dbc.Col("Watching Movie",width="auto",
                                       style={"text-align": "center","margin-top": "10px"})],
                              style={'width': '400px','height': '40px'}),
                          dbc.Row([dbc.Col(Lottie(options=options,width="40px",height="40px",url=url_music),
                                           width="auto",align='center'),
                                   dbc.Col("Listening Music",width="auto",
                                           style={"text-align": "center","margin-top": "10px"})],
                                  style={'width': '450px','height': '40px'})
                      ])],style={"margin-bottom": "10px"})
        ],width=3,style={'border': 'solid',"box-shadow": "5px 10px #888888"}),

        # COLUMN 2 ====================================================================================================
        dbc.Col([
            # Experience
            dbc.Card([dbc.CardHeader('WORK EXPERIENCES',style={"color": "blue","font-weight": "bold"}),
                      dbc.CardBody([
                          dbc.Row(html.H4(company_1['position'],style={"text-decoration": "underline"})),
                          dbc.Row(html.P(company_1['company'],style={"font-weight": "bold"})),
                          dbc.Row(html.Ul([html.Li(item) for item in company_1['jobdesc']]))
                      ],style={"padding-bottom": '10px','padding-left': '35px'}),

                      dbc.CardBody([
                          dbc.Row(html.H4(company_2['position'],style={"text-decoration": "underline"})),
                          dbc.Row(html.P(company_2['company'],style={"font-weight": "bold"})),
                          dbc.Row(html.Ul([html.Li(item) for item in company_2['jobdesc']]))
                      ],style={"padding-top": "0px","padding-bottom": '10px','padding-left': '35px'}),

                      dbc.CardBody([
                          dbc.Row(html.H4(company_3['position'],style={"text-decoration": "underline"})),
                          dbc.Row(html.P(company_3['company'],style={"font-weight": "bold"})),
                          dbc.Row(html.Ul([html.Li(item) for item in company_3['jobdesc']]))
                      ],style={"padding-top": "0px","padding-bottom": '10px','padding-left': '35px'})
                      ]),

            # Skill
            dbc.Card([dbc.CardHeader('SKILLS HIGHLIGHT',style={"color": "blue","font-weight": "bold"}),
                      # Professional Skills
                      dbc.Row(html.H4('Professional',style={"text-decoration": "underline","margin-left": "35px",
                                                            'margin-top': '20px','margin-bottom': '0px'})),
                      dbc.CardBody(
                          dbc.Row([
                              # Right - Colomn 1
                              dbc.Col([
                                  dbc.Row([dbc.Col(
                                      dbc.CardImg(src='/assets/python2.png',style={'width': '40px','height': '40px'}),
                                      width="auto",align='center'),
                                           dbc.Col("Python Programming",width="auto",style={"text-align": "center"})],
                                          style={'width': '300px','height': '30px','margin-bottom': '15px'}),
                                  dbc.Row([dbc.Col(
                                      dbc.CardImg(src='/assets/pandas.png',style={'width': '40px','height': '40px'}),
                                      width="auto",align='center'),
                                           dbc.Col("Pandas Library",width="auto",style={"text-align": "center"})],
                                          style={'width': '300px','height': '30px','margin-bottom': '15px'}),
                                  dbc.Row([dbc.Col(
                                      dbc.CardImg(src='/assets/numpy.png',style={'width': '40px','height': '40px'}),
                                      width="auto",align='center'),
                                           dbc.Col("Numpy Library",width="auto",style={"text-align": "center"})],
                                          style={'width': '300px','height': '30px','margin-bottom': '15px'}),
                                  dbc.Row([dbc.Col(dbc.CardImg(src='/assets/db.png',
                                                               style={'width': '40px','height': '40px'}),
                                                   width="auto",align='center'),
                                           dbc.Col("Database (Sql-NoSql)",width="auto",style={"text-align": "center"})],
                                          style={'width': '300px','height': '30px','margin-bottom': '15px'})

                              ],width='auto',style={'padding-left': '10px','padding-right': '0px'}),

                              # Right - Colomn 2
                              dbc.Col([
                                  dbc.Row([dbc.Col(
                                      dbc.CardImg(src='/assets/data_viz.png',style={'width': '40px','height': '40px'}),
                                      width="auto",align='center'),
                                           dbc.Col("Matplotlib, Dash-Plotly, Tableau",width="auto",
                                                   style={"text-align": "center"})],
                                          style={'width': '400px','height': '30px','margin-bottom': '15px'}),
                                  dbc.Row([dbc.Col(
                                      dbc.CardImg(src='/assets/webscrap.png',style={'width': '40px','height': '40px'}),
                                      width="auto",align='center'),
                                      dbc.Col("Web Crawling Library",width="auto",style={"text-align": "center"})],
                                      style={'width': '400px','height': '30px','margin-bottom': '15px'}),
                                  dbc.Row([dbc.Col(
                                      dbc.CardImg(src='/assets/ml_dl.png',style={'width': '40px','height': '40px'}),
                                      width="auto",align='center'),
                                      dbc.Col("Machine Learning, Deep Learning, OpenCV",width="auto",
                                              style={"text-align": "center"})],
                                      style={'width': '430px','height': '30px','margin-bottom': '15px'}),
                                  dbc.Row([dbc.Col(dbc.CardImg(src='/assets/msoffice.png',
                                                               style={'width': '40px','height': '40px'}),
                                                   width="auto",align='center'),
                                           dbc.Col("MS Office",width="auto",style={"text-align": "center"})],
                                          style={'width': '400px','height': '30px','margin-bottom': '15px'})
                              ],width='auto',style={'padding-left': '20px','padding-right': '0px'})],
                              style={'padding-left': '15px'})),

                      # Character Skills
                      dbc.Row(html.H4('Character',style={"text-decoration": "underline","margin-left": "35px",
                                                         'margin-top': '0px','margin-bottom': '0px'})),
                      dbc.CardBody([
                          html.Ul([html.Li(item) for item in soft_skill], style={'margin-left': '7px'})

                      ],style={'margin-left': '10px','margin-top': '5px','padding': '5px'})
                      ]),

            # Course and Certifications
            dbc.Card([dbc.CardHeader('COURSE & CERTIFICATION', style={"color": "blue", "font-weight": "bold"}),
                      dbc.CardBody([ html.Ul([html.Li(item) for item in certificate], style={'margin-left': '7px'})
                          ])])

        ],width=5),
    ],className='mb-2 mt-2',justify="center"),

],fluid=True)

if __name__=='__main__':
    app.run_server(debug=True,port=8009)
