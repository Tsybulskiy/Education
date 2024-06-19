function main()
    while true
        disp('Главное меню');
        disp('1. Запуск задачи на алгоритм перцептрона');
        disp('2. Запуск задачи на минимизацию среднеквадратической ошибки');
        disp('3. Выход');
        
        choice = input('Выберите действие: ', 's');
        
        switch choice
            case '1'
                run_perceptron();
            case '2'
                run_mse();
            case '3'
                break;
            otherwise
                disp('Некорректный выбор. Попробуйте снова.');
        end
    end
end

function run_perceptron()
    [female_data, male_data] = request_data();

    labels_female = ones(size(female_data, 1), 1);
    labels_male = -ones(size(male_data, 1), 1);
    
    data = [female_data; male_data];
    labels = [labels_female; labels_male];

    [weights, iterations, train_time] = train_perceptron(data, labels, 1);

    fprintf('\nПервый запуск (исходные данные):\n');
    fprintf('Количество итераций: %d\n', iterations);
    fprintf('Конечный весовой вектор: [%f, %f, %f]\n', weights);
    fprintf('Время обучения: %.4f секунд\n\n', train_time);

    figure;
    scatter(female_data(:, 1), female_data(:, 2), 'r', 'DisplayName', 'Женский пол');
    hold on;
    scatter(male_data(:, 1), male_data(:, 2), 'b', 'DisplayName', 'Мужской пол');

    x_vals = linspace(-250, 250, 100);
    if weights(2) ~= 0
        y_vals = -(weights(3) + weights(1) * x_vals) / weights(2);
    else
        x_vals = -weights(3) / weights(1) * ones(size(x_vals));
        y_vals = linspace(-250, 250, 100);
    end

    plot(x_vals, y_vals, 'k', 'LineWidth', 2);
    legend;
    xlabel('Рост (см)');
    ylabel('Вес (кг)');
    title(sprintf('Уравнение прямой: %.2fx + %.2fy + %.2f = 0', weights));
    xlim([-250, 250]);
    ylim([-250, 250]);
    hold off;
end

function [class1_data, class2_data] = request_data()
    class1_data = [];
    class2_data = [];

    disp("Введите точки для первого класса, формат: x,y. Введите '0' для завершения.");
    while true
        input_point = input('', 's');
        if strcmp(input_point, '0')
            break;
        end
        try
            point = sscanf(input_point, '%f,%f');
            class1_data = [class1_data; point'];
        catch
            disp("Некорректный формат. Попробуйте снова.");
        end
    end

    disp("Введите точки для второго класса, формат: x,y. Введите '0' для завершения.");
    while true
        input_point = input('', 's');
        if strcmp(input_point, '0')
            break;
        end
        try
            point = sscanf(input_point, '%f,%f');
            class2_data = [class2_data; point'];
        catch
            disp("Некорректный формат. Попробуйте снова.");
        end
    end
end

function [weights, iterations, elapsed_time] = train_perceptron(data, labels, learning_rate)
    data = [data, ones(size(data, 1), 1)];
    weights = zeros(size(data, 2), 1);

    [weights, iterations, elapsed_time] = do_perceptron(data, labels, weights, learning_rate);
end

function [weights, iterations, elapsed_time] = do_perceptron(data, labels, weights, learning_rate)
    converged = false;
    iterations = 1;
    start_time = tic;

    while ~converged
        converged = true;
        for i = 1:size(data, 1)
            y = dot(data(i, :), weights);
            fprintf('%d. W%d = [%s]*[%s] = %f\n', iterations, iterations, sprintf('%f ', data(i, :)), sprintf('%f ', weights), y);
            if labels(i) * y <= 0
                weightsNew = weights + learning_rate * labels(i) * data(i, :)';
                if labels(i) == 1
                    fprintf('Wnew%d: [%s]+[%s] = [%s]\n', iterations, sprintf('%f ', weights), sprintf('%f ', data(i, :)), sprintf('%f ', weightsNew));
                else
                    fprintf('Wnew%d: [%s]-%s = [%s]\n', iterations, sprintf('%f ', weights), sprintf('%f ', data(i, :)), sprintf('%f ', weightsNew));
                end
                weights = weightsNew;
                converged = false;
            end
            iterations = iterations + 1;
        end
    end
    
    elapsed_time = toc(start_time);
end
function run_mse()
    [class1_data, class2_data] = request_data();

    class1_data = [class1_data, ones(size(class1_data, 1), 1)];
    class2_data = [class2_data, ones(size(class2_data, 1), 1)];

    data = [class1_data; -class2_data];
    disp('Исходная матрица:');
    disp(data);

    pseudo_inv = inv(data' * data) * data';
    
    disp('Обобщенная обратная матрица:');
    disp(pseudo_inv);

    b = ones(size(data, 1), 1);
    disp('b:');
    disp(b);
    c = 1;
    weights = pseudo_inv * b;

    disp('Начальный вектор весов:');
    disp(weights);

    max_iter = 694863;
    epsilon = 1e-4;

    for iter = 1:max_iter
        error_vector = data * weights - b;
        disp('Вектор ошибок:');
        disp(error_vector);

        disp(['Итерация ', num2str(iter)]);
        disp('Весовой вектор:');
        abs_error_vector = abs(error_vector);
        disp(weights + c * pseudo_inv * (error_vector + abs_error_vector));

        if all(error_vector >= 0)
            disp('Решение найдено на итерации:');
            disp(iter);
            disp('Конечный вектор весов:');
            disp(weights);

            plot_data_and_boundary(class1_data, class2_data, weights, 'Классификация данных');
            break;
        elseif all(error_vector < 0)
            disp('Алгоритм не имеет решения на итерации:');
            disp(iter);
            break;
        else
            abs_error_vector = abs(error_vector);
            weights = weights + c * pseudo_inv * (error_vector + abs_error_vector);
            disp('b =');
            disp(b + c * (error_vector + abs_error_vector));
            b = b + c * (error_vector + abs_error_vector);

            if norm(error_vector) < epsilon
                disp('Количество итераций:');
                disp(iter);
                disp('Конечный весовой вектор:');
                disp(weights);

                plot_data_and_boundary(class1_data, class2_data, weights, 'Классификация данных');
                break;
            end
        end
    end

    if iter == max_iter
        disp('Превышено максимальное количество итераций. Решение не найдено.');
    end
end



function plot_data_and_boundary(class1_data, class2_data, weights, title_text, xlim_vals, ylim_vals)
    if nargin < 5
        xlim_vals = [-250, 250];
    end
    if nargin < 6
        ylim_vals = [-250, 250];
    end
    
    figure;
    hold on;
    scatter(class1_data(:, 1), class1_data(:, 2), 'b', 'DisplayName', 'Class 1');
    scatter(class2_data(:, 1), class2_data(:, 2), 'r', 'DisplayName', 'Class 2');

    a = weights(1);
    b = weights(2);
    c = weights(3);
    
    x_vals = linspace(xlim_vals(1), xlim_vals(2), 1000);
    if b == 0
        x_vert = -c / a;
        plot([x_vert, x_vert], ylim_vals, 'k', 'LineWidth', 2);
    else
        y_vals = -(a * x_vals + c) / b;
        plot(x_vals, y_vals, 'k', 'LineWidth', 2);
    end

    title(title_text);
    xlabel('x');
    ylabel('y');
    xlim(xlim_vals);
    ylim(ylim_vals);
    legend();
    hold off;
end