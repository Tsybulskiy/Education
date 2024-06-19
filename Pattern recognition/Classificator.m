men_heights = [185,182,176,180,181,182,176,178,172,178,179,175,187,185,176,170,183,185,180,182,178,177,186,170,178,187,186,176,185];
men_weights = [63,55,81,75,98,102,73,70,87,85,84,63,68,79,68,55,84,79,70,60,80,71,78,70,60,75,73,75,82];
women_heights = [160,179,164,167,175,168,160,158,160,169,160,174,169,151,158,168];
women_weights = [62,52,55,50,68,58,47,57,45,57,58,60,53,42,59,63];

mean_men_heights = mean(men_heights);
std_men_heights = std(men_heights);
mean_men_weights = mean(men_weights);
std_men_weights = std(men_weights);

mean_women_heights = mean(women_heights);
std_women_heights = std(women_heights);
mean_women_weights = mean(women_weights);
std_women_weights = std(women_weights);

[r_men, ~] = corrcoef(men_heights, men_weights);
[r_women, ~] = corrcoef(women_heights, women_weights);

T = table(['Мужской Пол'; 'Женский Пол'], ...
          [mean_men_heights; mean_women_heights], ...
          [std_men_heights; std_women_heights], ...
          [mean_men_weights; mean_women_weights], ...
          [std_men_weights; std_women_weights], ...
          [r_men(1,2); r_women(1,2)], ...
          'VariableNames', {'Группа', 'Рост_Мат.Ожидание', 'Рост_СКО', 'Вес_Мат.Ожидание', 'Вес_СКО', 'Коэффициент Корреляции'});

disp(T);

X = [men_heights', men_weights'; women_heights', women_weights'];
Y = [ones(length(men_heights), 1); -ones(length(women_heights), 1)]; 

X_bias = [X, ones(size(X, 1), 1)]; 
coefficients = inv(X_bias' * X_bias) * X_bias' * Y;

classify_gender = @(data) sign(data * coefficients);
predicted_gender_labels = classify_gender(X_bias);
accuracy = sum(predicted_gender_labels == Y) / length(Y);
fprintf('Точность классификатора: %.2f%%\n', accuracy * 100);

equation_str = sprintf('Уравнение решающей функции: %.6fx + %.6fy + (%.6f) = 0', coefficients(1), coefficients(2), coefficients(3));
fprintf('%s\n', equation_str);

figure;
scatter(men_heights, men_weights, 'b'); hold on;
scatter(women_heights, women_weights, 'r');
xlabel('Рост');
ylabel('Вес');
title('Классификация по полу на основе роста и веса');

x_fit = linspace(min(X(:, 1)) - 5, max(X(:, 1)) + 5, 100)';
y_fit = (-coefficients(1) * x_fit - coefficients(3)) ./ coefficients(2);
plot(x_fit, y_fit, 'k', 'LineWidth', 2); 

legend({'Мужской Пол', 'Женский Пол', 'Решающая функция'}, 'Location', 'best');
hold off;

test_data = [184, 73, 1; 168, 68, 1; 188, 73, 1; 185, 75, 1; 176, 70, 1;    % Мужчины
             162, 45, -1; 177, 57, -1; 170, 65, -1; 165, 52, -1; 167, 62, -1]; % Женщины
test_data_bias = [test_data(:, 1:2), ones(size(test_data, 1), 1)];

predictions = classify_gender(test_data_bias);

decision_values = test_data_bias * coefficients;

results = array2table(test_data(:, 1:2), 'VariableNames', {'Рост', 'Вес'});
results.("Настоящий Пол") = repmat({'Мужской'}, size(test_data, 1), 1);
results.("Настоящий Пол")(test_data(:, 3) == -1) = {'Женский'};
results.("Предсказанный Пол") = repmat({'Мужской'}, length(predictions), 1);
results.("Предсказанный Пол")(predictions == -1) = {'Женский'};
results.("Значение Решающей Функции") = decision_values; 
disp(results);

figure;
scatter(men_heights, men_weights, 'b'); hold on;
scatter(women_heights, women_weights, 'r');
xlabel('Рост');
ylabel('Вес');
title('Классификация по полу на основе роста и веса (с тестовыми данными)');

% Решающая граница
plot(x_fit, y_fit, 'k', 'LineWidth', 2); 

% Визуализация тестовых данных
scatter(test_data(1:5, 1), test_data(1:5, 2), 'b', 'filled'); % Мужчины
scatter(test_data(6:10, 1), test_data(6:10, 2), 'r', 'filled'); % Женщины

legend({'Мужской Пол', 'Женский Пол', 'Решающая функция', 'Тестовые данные Мужской Пол', 'Тестовые данные Женский Пол'}, 'Location', 'best');
hold off;
