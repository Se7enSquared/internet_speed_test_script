import speedtest
from datetime import datetime, timedelta
import time

iteration = 0
while 1:
    # Specify servers in list
    servers = []
    iteration += 1

    date_time = str(datetime.now())
    s = speedtest.Speedtest()
    print('Getting servers...')
    s.get_servers(servers)
    print('Finding best servers...')
    s.get_best_server()
    print('Download Test...')
    s.download()
    print('Upload Test...')
    s.upload()

    print('Fetching results...')

    results_dict = s.results.dict()
    print(results_dict)
    print('Writing file... \'results.csv\'')
    with open('results.csv', 'a') as f:
        # Convert dl and ul data to string and drop insignificant digits
        dl = str(results_dict['download'] // 1000000)
        ul = str(results_dict['upload'] // 1000000)
        f.writelines('\n' + date_time + "," + dl + "," + ul)
        print('Closing file...')
    print(f'Iteration {iteration} Sleeping 1 hour...')

    dt = datetime.now() + timedelta(hours=1)
    dt = dt.replace(minute=10)

    # Sleep 1 hour
    while datetime.now() < dt:
        time.sleep(1)


