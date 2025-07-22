% MATLAB script to calculate averages for the given dataset

% Data extracted from the XML dataset
% Each row corresponds to a vehicle in the format:
% [duration, routeLength, timeLoss, CO2_abs]
% Updated data based on new XML with fuel_abs included
data = [
    114.00, 640.57, 56.11, 270564.976529, 86299.201318;
    140.00, 640.57, 93.80, 331761.512981, 105819.178066;
    139.00, 640.57, 91.67, 313889.972623, 100118.785854;
    140.00, 640.57, 92.59, 331124.205552, 105615.706122;
    140.00, 640.57, 97.39, 356001.844949, 113550.871274;
    142.00, 640.57, 93.52, 319089.430453, 101777.244277;
    60.00, 640.57, 13.63, 199873.425606, 63750.461711;
    76.00, 640.57, 28.09, 251648.336908, 80264.904170;
    72.00, 640.57, 24.18, 237389.936130, 75716.755381;
    54.00, 640.57, 12.72, 222624.022470, 71006.633320;
    69.00, 640.57, 22.33, 236479.914883, 75426.408600;
    68.00, 640.57, 22.26, 243992.090697, 77822.358605;
    141.00, 640.57, 92.93, 311898.057340, 99483.505457;
    136.00, 640.57, 90.88, 298076.684558, 95074.974713;
    95.00, 640.57, 52.28, 288876.434208, 92139.104646;
    94.00, 640.57, 49.44, 281700.083552, 89850.042604;
    134.00, 640.57, 89.59, 345886.459771, 110324.183791;
    132.00, 640.57, 88.16, 302702.285801, 96550.142748;
    133.00, 640.57, 82.89, 292902.585702, 93424.540791;
    90.00, 640.57, 43.21, 279806.723805, 89246.144654;
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
average_co2_emissions = mean(co2Emissions);
avg_fuel = mean(fuelConsumptions);


% Display results
fprintf('Average Duration: %.2f seconds\n', average_duration);
fprintf('Average Route Length: %.2f meters\n', average_route_length);
fprintf('Average Time Loss: %.2f seconds\n', average_time_loss);
fprintf('Average CO2 Emissions: %.2f mg\n', average_co2_emissions);
fprintf('Average Fuel Comsumption: %.2f mg\n', avg_fuel);
