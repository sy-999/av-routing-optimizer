% Define data
data = [0.0767946243, 0.0010335];  % Processing speeds for CPU and FPGA
labels = {'CPU', 'FPGA'};          % Axis labels

% Set X-axis positions (centred between bars)
x = [0.75, 1.25];  % X coordinates for visual centring

% Create the plot
figure;
plot(x, data, '-o', 'LineWidth', 2, 'MarkerSize', 8, 'Color', 'b');  % Set line and marker styles

% Axis labels and title
set(gca, 'XTick', x, 'XTickLabel', labels);  % Set X-axis labels
ylabel('Processing Time (s)');               % Y-axis label
title('Processing Time Comparison: CPU vs FPGA');  % Chart title

% Set logarithmic scale (to emphasise slope)
set(gca, 'YScale', 'log');  % Logarithmic scale for Y-axis

% Adjust X-axis range (add margin on both sides)
xlim([0.5, 1.5]);  % Set X-axis limits with extra spacing

% Add grid
grid on;

% Display the graph

