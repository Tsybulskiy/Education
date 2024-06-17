e_1 = sqrt(4.2);
Go_values = [];
Gp_values = [];
To_values = [];
Tp_values = [];

% Вычисление значений Go, Gp, To, Tp
for phi = 0:0.1:90
    try
        ro = abs(sind(asind(sind(phi)*e_1) - phi) / sind(asind(sind(phi) * e_1) + phi));
        rp = abs(tand(asind(sind(phi) * e_1) - phi) / tand(asind(sind(phi) * e_1) + phi));
        to = abs(2 * sind(asind(sind(phi) * e_1)) * cosd(phi) / (sind(asind(sind(phi) * e_1) + phi)));
        tp = abs(2 * sind(asind(sind(phi) * e_1)) * cosd(phi) / (sind(asind(sind(phi) * e_1) + phi) * cosd(asind(sind(phi) * e_1) - phi)));

        Go_values = [Go_values, abs(ro)];
        Gp_values = [Gp_values, abs(rp)];
        To_values = [To_values, abs(to)];
        Tp_values = [Tp_values, abs(tp)];
    catch
        continue
    end
end

phi_values = 0:0.1:90;

% Создание графика с 4 линиями
figure;
plot(phi_values, Go_values, 'b', 'DisplayName', 'Г⊥');
hold on;
plot(phi_values, Gp_values, 'r', 'DisplayName', 'Г∥');
plot(phi_values, To_values, 'g', 'DisplayName', 'T⊥');
plot(phi_values, Tp_values, 'c', 'DisplayName', 'T∥');
hold off;

title('Графики Г⊥, Г∥, T⊥ и T∥');
xlabel('Phi (градусы)');
ylabel('Значение');
ylim([0, 4.5]);
xlim([0, 90]);
legend('Location', 'best');
set(gcf, 'Position', [100, 100, 800, 600]);
