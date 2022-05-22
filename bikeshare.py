import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city=input('Which city would you want to analyze? input :  chicago , new york city, washington\n').lower()
    while True:
        if city not in CITY_DATA.keys():
           city=input("Invalid data \n")
        else:
           break   

    # TO DO: get user input for month (all, january, february, ... , june)
    months=set(['all','january','february','march','april','may','june'])
    month=input('Which month would you want to analyze? input : all, january, february, march , april, may,june\n').lower()
    while True:
        if month not in months:
           month=input("Invalid data \n").lower()
        else:
           break 

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days=['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    day=input('Which month would you want to analyze? input : all,monday,tuesday,wednesday,thursday,friday,saturday,sunday\n').lower()
    while True:
        if day not in days:
           day=input("Invalid data \n").lower()
        else:
           break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    df['day_of_week']=df['Start Time'].dt.weekday_name
    
    if month !='all':
        months=['january','february','march','april','may','june']
        month = months.index(month)+1
        df=df[df['month'] == month]
    
    if day !='all':
        df=df[df['day_of_week'] == day.title()]
    
    #display 5 line data
    x=5
    while True:
        display_5_line = input('\nWould you like to display 5 line data? Enter yes or no.\n')
        display=df.head(x)
        print(display)
        x+=5
        if display_5_line.lower() != 'yes':
            break
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month=df['month'].mode()[0]
    print("The Most Frequent Month of Travel:\n",(popular_month))
    # TO DO: display the most common day of week
    popular_day=df['day_of_week'].mode()[0]
    print("The Most Frequent day of Travel:\n",(popular_day))
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print("The Most Frequent hour of Travel:\n",(popular_hour))
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station=df['Start Station'].mode()[0]
    print("The Most Frequent Start Station of Travel:\n",(popular_start_station))
    
    # TO DO: display most commonly used end station
    popular_end_station=df['End Station'].mode()[0]
    print("The Most Frequent end Station of Travel:\n",(popular_end_station))
    
    # TO DO: display most frequent combination of start station and end station trip
    df['start_end_station']=df['Start Station']+"_"+df['End Station']
    popular_start_end_station=df['start_end_station'].mode()[0]
    print("The Most Frequent route of Travel:\n",(popular_start_end_station)) 
    
         
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    
    # TO DO: display total travel time
    total_travel_time=df['Trip Duration'].sum()
    total_travel_time=total_travel_time/3600
    print(" Total Travel Time (hours):\n",total_travel_time)
    
    # TO DO: display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    mean_travel_time/=3600
    print(" Average Travel Time(hours):\n",(mean_travel_time))
    
         
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("counts of user types\n",user_types)
    
    # TO DO: Display counts of gender
    try:
        user_gender = df['Gender'].value_counts()
        print("counts of user gender\n",user_gender)
    except keyError:
        print("counts of user gender: sorry, this city have no this data.")
    
    # TO DO: Display brith year of oldest user
    try:
        oldest_user = df['Birth Year'].min()
        print(" Oldest User:\n",(oldest_user))
    
    # TO DO: Display brith year of yougest user
        youngest_user = df['Birth Year'].max()
        print(" Youngest User:\n",(youngest_user))
    
    # TO DO: Display brith year of common user
        common_age_user = df['Birth Year'].mode()[0]
        print(" Most Common Age:\n",(common_age_user))    
    except keyError:
        print("sorry, this city have no this data.")
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
