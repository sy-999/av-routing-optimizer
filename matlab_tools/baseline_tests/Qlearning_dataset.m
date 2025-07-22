% MATLAB script to calculate averages for the given dataset

% Data extracted from the XML dataset
% Each row corresponds to a vehicle in the format:
% [duration, routeLength, timeLoss, waitingTime]
% Updated data based on XML with fuel_abs included
% Updated data based on new XML with fuel_abs included
% Updated data based on XML
% Updated data based on XML with fuel_abs included
data = [
    62.00, 636.24, 15.52, 224174.032363, 71501.230273;
    62.00, 640.57, 10.89, 197600.798617, 63025.646981;
    61.00, 640.57, 13.77, 205862.156275, 65660.661939;
    58.00, 640.57, 13.53, 216477.382087, 69046.345395;
    58.00, 640.57, 11.25, 194263.802010, 61961.190464;
    70.00, 640.57, 12.55, 192689.124062, 61459.492405;
    60.00, 640.57, 14.27, 203615.200906, 64943.872349;
    65.00, 640.57, 10.70, 203497.420584, 64906.486368;
    71.00, 640.57, 19.80, 225142.332501, 71810.536535;
    69.00, 640.57, 12.84, 204603.282762, 65259.475405;
    57.00, 640.57, 12.93, 199789.052560, 63723.465381;
    59.00, 640.57, 12.35, 213469.874807, 68087.009528;
    58.00, 640.57, 12.30, 214634.852187, 68458.593393;
    60.00, 636.24, 15.41, 226049.928236, 72099.416975;
    67.00, 631.91, 16.26, 240096.663661, 76579.886689;
    67.00, 636.24, 13.60, 217245.609288, 69291.575372;
    72.00, 631.91, 15.33, 224241.372592, 71522.885091;
    69.00, 631.91, 16.50, 234591.990059, 74824.221378;
    70.00, 631.91, 16.87, 239334.540401, 76336.974485;
    60.00, 631.91, 16.09, 268782.818495, 85729.034371;
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
