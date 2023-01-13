import mysql.connector
from mysql.connector import Error
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import matplotlib.cm as cmap
plt.style.use('ggplot')
import seaborn as sns
from plotly import graph_objects as go

class get_df_visual():
    def __init__(self,records):
        self.records=records
        
    # Each function is a question.
    def Q0(self):
        df = pd.DataFrame(self.records, columns=['utm_source','utm_campaign','http_referer','sessions'])
        print(df)
        
        return df

    def Q1(self):
        df = pd.DataFrame(self.records, columns=['sessions','orders','conv_rate'])
        print(df)
        
        return df
    
    def Q2(self):
        #Get dataframe
        df = pd.DataFrame(self.records, columns=['week_start_date','sessions'])
        print(df)

        #Visualise data
        x=df["week_start_date"]
        y= df["sessions"]

        plt.plot(x,y, marker='.')
        plt.vlines(x=datetime.date(2012,4,15),
                    ymin=0, ymax=1300, 
                    colors='black', 
                    linestyles='dashed', lw=1)
        plt.text(datetime.date(2012,4,17), 1200, 'Bidding down',fontsize=7, ha='left', va='center', backgroundcolor='white')
        plt.gcf().autofmt_xdate()
        plt.xlabel("Week start date", fontsize = 10)
        plt.ylabel ("Sessions", fontsize=10)
        plt.title("Sessions by week from 22-03-2012 to 08-05-2012 for\ngsearch sources and non-brand campaigns", 
                    fontsize=10,
                    fontweight='bold')
        for i, j in zip(x, y):
            label = j
            plt.annotate(label, (i, j),
                        xycoords="data",
                        textcoords="offset points",
                        xytext=(2, 10), ha="left",
                        fontsize = 8)
        plt.ylim(0,1300)
        plt.show() 
        return df
    
    def Q3(self):
        df = pd.DataFrame(self.records, columns=['device_type','sessions','orders','conv_rate'])
        print(df)
        
        return df

    def Q4(self):
        #Get data
        df = pd.DataFrame(self.records, columns=['week_start_date','desktop_sessions','mobile_orders'])
        print(df)

        #Visualise data
        x= df["week_start_date"]
        y1=df["desktop_sessions"]
        y2=df["mobile_sessions"]

        plt.plot(x,y1, marker='.', label="desktop")
        plt.plot(x,y2, marker='.',label="mobile")
        plt.vlines(x=datetime.date(2012,5,19),
                    ymin=0, ymax=max(y1)*1.2, 
                    colors='black', 
                    linestyles='dashed', lw=1)
        plt.text(datetime.date(2012,5,20), max(y1)*1.13, 'Bidding up',fontsize=7, ha='left', va='center', backgroundcolor='white')
        plt.gcf().autofmt_xdate()
        plt.xlabel("Week start date", fontsize = 10)
        plt.ylabel ("Sessions", fontsize=10)
        plt.title("Sessions by week from 15-04-2012 to 06-09-2012 by decive types for\ngsearch sources and non-brand campaigns", 
                    fontsize=10,
                    fontweight='bold')
        for i, j in zip(x, y1):
            label = j
            plt.annotate(label, (i, j),
                        xycoords="data",
                        textcoords="offset points",
                        xytext=(2, 7), ha="left",
                        fontsize = 8)
        for i, j in zip(x, y2):
            label = j
            plt.annotate(label, (i, j),
                        xycoords="data",
                        textcoords="offset points",
                        xytext=(2, 7), ha="left",
                        fontsize = 8)
        plt.ylim(0,max(y1)*1.2)
        plt.legend()
        plt.show()
        return df
    
    def Q5(self):
        df = pd.DataFrame(self.records, columns=['device_type','utm_source','sessions','orders','conv_rate'])
        print(df)
        
        return df

    def Q6(self):
        # Get dataframe
        df = pd.DataFrame(self.records, columns=['year','month','sessions','channel_group'])
        df=df.pivot_table(index=['month'],columns='channel_group',values='sessions')
        df.columns = [''.join(map(str, c)).strip('_') for c in df]
        df = df.reset_index(level=0)
        print(df)

        # Visualise dataframe
        x= df['month']
        y1=df['direct']
        y2=df['organic_search']
        y3=df['paid_brand']
        y4=df['paid_nonbrand']

        plt.plot(x,y1, marker='.', label="direct")
        plt.plot(x,y2, marker='.',label="organic_search")
        plt.plot(x,y3, marker='.',label="paid_brand")
        plt.plot(x,y4, marker='.',label="paid_nonbrand")
        plt.gcf().autofmt_xdate()
        plt.xlabel("Month", fontsize = 10)
        plt.ylabel ("Sessions", fontsize=10)
        plt.title("Sessions by channels from Mar to Dec 2012", 
                    fontsize=10,
                    fontweight='bold')
        for i, j in zip(x, y1):
            label = j
            plt.annotate(label, (i, j),
                        xycoords="data",
                        textcoords="offset points",
                        xytext=(2, 7), ha="left",
                        fontsize = 8)
        for i, j in zip(x, y2):
            label = j
            plt.annotate(label, (i, j),
                        xycoords="data",
                        textcoords="offset points",
                        xytext=(2, 7), ha="left",
                        fontsize = 8)
        for i, j in zip(x, y3):
            label = j
            plt.annotate(label, (i, j),
                        xycoords="data",
                        textcoords="offset points",
                        xytext=(2, 7), ha="left",
                        fontsize = 8)
        for i, j in zip(x, y4):
            label = j
            plt.annotate(label, (i, j),
                        xycoords="data",
                        textcoords="offset points",
                        xytext=(2, 7), ha="left",
                        fontsize = 8)
        plt.ylim(0,max(y4)*1.2)
        plt.legend()
        plt.show()
        return df
    
    def Q7(self):
        # Get data
        df = pd.DataFrame(self.records, columns=['pageview_url','sessions'])
        print(df)

        # Visualise data
        x=df["sessions"]
        y=df["pageview_url"]

        plt.barh(y,x)
        plt.xlabel("Sessions", fontsize = 10)
        plt.ylabel ("Page view url", fontsize=10)
        plt.yticks(fontsize=7)
        plt.title("Total sessions by page view url by 09-06-2012", 
                    fontsize=10,
                    fontweight='bold')
        for i, j in zip(x, y):
            label = i
            plt.annotate(label, (i, j),
                        xycoords="data",
                        textcoords="offset points",
                        xytext=(5, 5), ha="left",
                        va='center',
                        fontsize = 7)
        plt.show()
        return df

    def Q8(self):
        df = pd.DataFrame(self.records, columns=['total_session','product_sessions','landing_ctr','mrfuzzy_sessions','product_ctr','cart_session','mrfuzzy_ctr','shipping_sessions','cart_ctr','billing_sessions','shipping_ctr','thankyou_sessions','billing_ctr'])
        print(df)

        # Visualise funnel chart with plotly
        stages = ["/lander-1", "/products", "/mrfuzzy", "/cart", "/shipping",'/billing','/thank-you']
        fig = go.Figure()
        fig.add_trace(go.Funnel(
            name = 'Mr Fuzzy',
            y = stages,
            x = list(df.iloc[0,[0,1,3,5,7,9,11]]),
            textposition = "inside",
            textinfo = "value+percent previous",
            marker = {'color' : '#EF553B'}))
        fig.update_layout(template='ggplot2',title_text= '<b> Funnel sessions and percentages from 05-08-2012 to 05-09-2012 </b>')
        fig.show()
        return df
    
    def Q9(self):
        df = pd.DataFrame(self.records, columns=['pageview_url','sessions','orders',"conv_rate"])
        print(df)
        
        return df

    def Q10(self):
        #Get data
        df = pd.DataFrame(self.records, columns=['month','sessions','orders','conv_rate'])
        print(df)
        
        #Visualise data
        x=df['month']
        y1=df['sessions']
        y2=df['orders']
        y3=[round(i,3) for i in df['conv_rate']]

        fig,(ax1, ax2) = plt.subplots(2, sharex=True)

        ax1.set_ylabel('Sessions')
        ax1.plot(x,y1, marker='.', label="sessions")
        ax1.set_ylim(ymin=0,ymax=16000)
        ax1.plot(x,y2, marker='.', label="orders")
        ax1.set_title('Sessions and orders by month in 2012', size=10)
        for i, j in zip(x, y1):
            label = j
            ax1.annotate(label, (i, j),
                        xycoords="data",
                        textcoords="offset points",
                        xytext=(2, 7), ha="left",
                        fontsize = 8)
        for i, j in zip(x, y2):
            label = j
            ax1.annotate(label, (i, j),
                        xycoords="data",
                        textcoords="offset points",
                        xytext=(2, 7), ha="left",
                        fontsize = 8)  
        ax1.legend(loc='upper left')

        ax2.bar(x,y3,width = 0.7,color='gray')
        ax2.set_ylim(ymin=0,ymax=0.06)
        ax2.set_ylabel('Conversion rate (%)')
        for i, j in zip(x, y3):
            label = j
            ax2.annotate(label, (i, j),
                        xycoords="data",
                        textcoords="offset points",
                        xytext=(2, 7), ha="center",
                        fontsize = 8)
        ax2.set_title('Conversion rate by month in 2012', size=10)
        ax2.set_xlabel('Month')

        fig.suptitle('Conversion rate, sessions and orders by months in 2012', fontsize=15,fontweight='bold')
        plt.xticks(x)
        plt.show()

        return df

    def Q11(self):
        #Get data
        df = pd.DataFrame(self.records,columns=['Hour','Mon','Tue','Wed','Thu','Fri','Sat','Sun'])
        df=df.set_index('Hour')
        df = df[df.columns].astype(float)
        print(df)

        #Visualise data
        ax= sns.heatmap(df,square=True)
        ax.set_aspect(df.shape[1]/df.shape[0])
        plt.yticks(rotation=0) 
        plt.xticks(rotation=0) 
        plt.xlabel("Weekday", fontsize = 10)
        plt.ylabel ("Hour", fontsize=10)
        plt.title("Average sessions by weekdays and hours\nfrom 2012-09-15 to 2012-11-15", 
                    fontsize=15,
                    fontweight='bold')
        plt.show()
        return df

    def Q12(self):
        #Get data
        df = pd.DataFrame(self.records, columns=['year','month','number_of_sales','total_revenue','total_profit'])
        print(df)

        #Visualise data
        x=[str(i)+"-"+str(j) for i,j in zip(df['month'], df['year'])]
        y1=df['number_of_sales']
        y2=df['total_revenue']
        y3=df['total_profit']

        fig,(ax1, ax2) = plt.subplots(2, sharex=True)
        ax1.set_ylim(ymin=0,ymax=max(y1)*1.2)
        ax1.bar(x,y1,width = 1,color='grey')
        ax1.set_ylabel('Number of sales (order)', size=8)
        ax1.grid(alpha=0.5)
        for i, j in zip(x, y1):
            label = j
            ax1.annotate(label, (i, j),
                        xycoords="data",
                        textcoords="offset points",
                        xytext=(2, 7), ha="center",
                        fontsize = 8)
        ax1.set_title('Number of sales by month', size=10)


        ax2.set_xlabel('Month', size=9)
        ax2.set_ylabel('USD', size=9)
        ax2.plot(x,y2, marker='.', label="Revenue")
        ax2.plot(x,y3, marker='.', label="Profit")
        ax2.grid(alpha=0.5)
        ax2.set_title('Total revenue and profit by month', size=10)

        fig.suptitle('Sales by month from Mar-2012 to Jan-2013', fontsize=15,fontweight='bold')
        plt.xticks(x)
        plt.legend(loc='upper left')
        plt.show()

        return df

    def Q13(self):
        #Get df
        df = pd.DataFrame(self.records, columns=['year','month','sessions','orders','conv_rate','revenue_per_session','product_1_order','product_2_order'])
        print(df)

        #Visualise data
        x=[str(i)+"-"+str(j) for i,j in zip(df['month'], df['year'])]
        y1=[round(i,2) for i in df['conv_rate']]
        y2=df['product_1_order']
        y3=df['product_2_order']

        fig,(ax1, ax2) = plt.subplots(2, sharex=True)

        ax1.plot(x,y1,marker='.',color="grey")
        ax1.set_ylim(ymin=0,ymax=0.1)
        ax1.set_ylabel('Conversion rate (%)', size=8)
        ax1.grid(alpha=0.5)
        for i, j in zip(x, y1):
            label = j
            ax1.annotate(label, (i, j),
                        xycoords="data",
                        textcoords="offset points",
                        xytext=(2, 7), ha="center",
                        fontsize = 8)
        ax1.set_title('Conversion rates by month', size=10)

        ax2.set_xlabel('Month', size=9)
        ax2.set_ylabel('Order', size=9)
        ax2.set_ylim(ymin=0,ymax=max(y2)*1.1)
        ax2.bar(x,y2, width = 0.7,label="Mr Fuzzy")
        ax2.bar(x,y3, width = 0.7, label="Love Bear",  bottom=y2)
        ax2.grid(alpha=0.5)
        ax2.set_title('Number of order by product by month', size=10)

        fig.suptitle('Conversion rates and orders by products and months from Apr-2012 to Apr-2013', fontsize=15,fontweight='bold')
        plt.xticks(x)
        plt.legend(loc='upper left')
        plt.show()
        return df

    def Q14(self):
        #Get df
        df = pd.DataFrame(self.records, columns=['time_period','sessions','next_pageview_sessions', 'next_page_ctr',
                                                'to_mrfuzzy','to_mrfuzzy_ctr','to_lovebear','to_lovebear_ctr'])
        print(df)

        return df

    def Q15(self):
        # Get df
        df = pd.DataFrame(self.records, columns=['product_page','product_sessions','cart_sessions','shipping_sessions','billing_sessions','thankyou_sessions','product_conversion','cart_conversion','shipping_conversion','billing_conversion'])
        print(df)

        # Visualise funnel chart with plotly
        stages = ["View product", "Add cart", "Choose shipping", "Pay bill", "Reach thankyou page"]
        fig = go.Figure()
        fig.add_trace(go.Funnel(
            name = 'Mr Fuzzy',
            y = stages,
            x = list(df.iloc[1,1:6]),
            textposition = "inside",
            textinfo = "value+percent previous",
            marker = {'color' : '#EF553B'}))
        fig.add_trace(go.Funnel(
            name = 'Love Bear',
            y = stages,
            x = list(df.iloc[0,1:6]),
            textposition = "inside",
            textinfo = "value+percent previous",
            marker = {'color' : '#1F77B4'}))
        fig.update_layout(template='ggplot2',title_text= '<b> Funnel sessions and percentages by product from 06-01-2013 to 10-04-2013 </b>')
        fig.show()

        return df
                        
    def Q16(self):
        df = pd.DataFrame(self.records, columns=[ 'time_period','cart_sessions','clickthroughs','cart_ctr','product_per_order',
                                                    'average_order_rev','rev_per_cart_session'])
        print(df)
        return df

    def Q17(self):
        #Get data
        df = pd.DataFrame(self.records, columns=[ 'year','month','order_p1','refund_p1_rate','order_p2','refund_p2_rate',
                                                    'order_p3','refund_p3_rate','order_p4','refund_p4_rate'])
        print(df)

        # Visualise data
        x= [str(i)+"-"+str(j) for i,j in zip(df['month'], df['year'])]
        y1 = [i if i != 0 else None for i in df['order_p1']]
        y2 = [i if i != 0 else None for i in df['order_p2']]
        y3 = [i if i != 0 else None for i in df['order_p3']]
        y4 = [i if i != 0 else None for i in df['order_p4']]

        y11 = df['refund_p1_rate']
        y22 = df['refund_p2_rate']
        y33 = df['refund_p3_rate']
        y44 = df['refund_p4_rate']

        fig,(ax1, ax2) = plt.subplots(2, sharex=True)

        ax1.plot(x,y1,label='Product 1')
        ax1.plot(x,y2,label='Product 2')
        ax1.plot(x,y3,label='Product 3')
        ax1.plot(x,y4,label='Product 4')
       # ax1.set_ylim(ymin=0,ymax=0.1)
        ax1.set_ylabel('Order ', size=9)
        ax1.grid(alpha=0.5)
        ax1.set_title('Orders over time by product by month', size=10)

        ax2.set_xlabel('Month', size=9)
        ax2.set_ylabel('Refund rate (%)', size=9)
        #ax2.set_ylim(ymin=0,ymax=max(y2)*1.1)
        ax2.plot(x,y11,label='Product 1')
        ax2.plot(x,y22,label='Product 2')
        ax2.plot(x,y33,label='Product 3')
        ax2.plot(x,y44,label='Product 4')
        ax2.grid(alpha=0.5)
        ax2.set_title('Refund rates by product by month', size=10)

        fig.suptitle('Orders and refund rates by products and months from Mar-2012 to Oct-2014', fontsize=15,fontweight='bold')
        ax1.legend(loc='upper left', bbox_to_anchor=(1,1))
        plt.xticks(x, rotation=70)
        plt.show()

        return df

    def Q18(self):
        #Get data
        df = pd.DataFrame(self.records,columns=['repeat_session','users'])
        print(df)

        # Visualise data
        x = df['repeat_session']
        y = df['users']

        explode = [0.1,0.1,0.1,0.1]

        plt.pie(y, labels=['%s repeat session users' % i for i in x],
                pctdistance=1.1, labeldistance=1.3 , autopct='%1.2f%%',
                explode=explode)
        plt.title("Percentages of users by number of repeat sessions in 2014", 
                    fontsize=15,
                    fontweight='bold')
        plt.show()

        return df

    def Q19(self):
        #Get data
        df = pd.DataFrame(self.records,columns=['avg_days','min_days','max_days'])
        print(df)

        return df

    def Q20(self):
        #Get data
        df = pd.DataFrame(self.records,columns=['channel_group','new_sessions','repeat_sessions'])
        print(df)
        
        #Visualise data
        ax = df.plot(x="channel_group", y=["new_sessions", "repeat_sessions"], kind="bar",
                title = 'Users by channels in 2014', rot=0) 
        ax.set_ylabel('Users')
        ax.set_xlabel('Channels')
        ax.set_ylim(ymin=0,ymax=max(df["new_sessions"]*1.1))
        for p in ax.patches:
            ax.annotate(str(p.get_height()), (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='center', xytext=(0, 10), textcoords='offset points')
        ax.legend(["New sessions", "Repeat sessions"]);

        plt.show()

        return df
    
    def Q21(self):
        #Get data
        df = pd.DataFrame(self.records,columns=['is_repeat_session','sessions','conv_rate','rev_per_session'])
        print(df)

        return df
