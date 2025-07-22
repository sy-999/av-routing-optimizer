% MATLAB script to calculate averages for the given dataset

% Data extracted from the XML dataset
% Each row corresponds to a vehicle in the format:
% [duration, routeLength, timeLoss, waitingTime]
% Updated data based on new XML with fuel_abs included
% Updated dataset with fuel_abs included
data = [
    76.00, 640.57, 17.85, 219820.671354, 70113.380202;
    60.00, 640.57, 13.15, 220497.003193, 70328.403138;
    61.00, 640.57, 13.70, 207206.379684, 66089.331054;
    62.00, 640.57, 14.88, 210140.420092, 67025.206956;
    58.00, 640.57, 14.90, 214009.349505, 68258.986975;
    60.00, 640.57, 11.56, 208934.862864, 66640.724997;
    63.00, 640.57, 16.09, 208156.850610, 66392.521953;
    61.00, 640.57, 12.55, 214925.934027, 68551.441232;
    71.00, 640.57, 24.25, 245309.243160, 78242.690263;
    56.00, 640.57, 14.57, 225062.391875, 71784.383685;
    69.00, 640.57, 22.73, 225234.028191, 71839.382941;
    70.00, 640.57, 23.23, 247570.102671, 78963.704966;
    141.00, 640.57, 93.20, 322898.786235, 102992.511633;
    61.00, 636.24, 14.50, 235565.991108, 75134.702108;
    59.00, 636.24, 14.52, 232010.619722, 74000.544969;
    60.00, 636.24, 14.27, 236258.828520, 75355.623227;
    61.00, 636.24, 15.33, 235396.756071, 75080.729464;
    60.00, 636.24, 14.80, 235368.538579, 75071.652967;
    66.00, 636.24, 15.34, 221358.349010, 70603.169277;
    62.00, 636.24, 14.98, 222038.483876, 70820.017390;
];

% Extract columns for calculation
durations = data(:, 1);
routeLengths = data(:, 2);
timeLosses = data(:, 3);
co2Emissions = data(:, 4);
fuelConsumptions = data(:, 5);

% Calculate averages
average_duration = mean(durations);
average_route_length = mean(routeLengths);
average_time_loss = mean(timeLosses);
ave_co2 = mean(co2Emissions);
avg_fuel = mean(fuelConsumptions);

% Display results
fprintf('Average Duration: %.2f seconds\n', average_duration);
fprintf('Average Route Length: %.2f meters\n', average_route_length);
fprintf('Average Time Loss: %.2f seconds\n', average_time_loss);
fprintf('Average CO2 Comsumption: %.2f mg\n', ave_co2);
fprintf('Average Fuel Comsumption: %.2f mg\n', avg_fuel);
