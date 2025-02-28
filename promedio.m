% Lee los últimos 10 datos de temperatura de field1
data = thingSpeakRead(2856350, 'Fields', 1, 'NumPoints', 10);

% Muestra los últimos 10 datos en la consola
disp('Últimos 10 datos de temperatura:');
disp(data);

% Calcula el promedio de los últimos 10 datos
promedio_temp = mean(data);

% Muestra el promedio en la consola
fprintf('Promedio de temperatura: %.2f°C\n', promedio_temp);

% Verifica si el promedio supera el umbral de 35°C
if promedio_temp > 35
    mensaje = '¡Alerta! Temperatura promedio mayor a 35°C detectada.';
    disp(mensaje);
    % thingSpeakWrite(YOUR_CHANNEL_ID, mensaje, 'Fields', 3); % Opcional: Enviar alerta a ThingSpeak en field3
else
    disp('Temperatura promedio en rango normal.');
end