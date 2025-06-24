import random

# Datos iniciales
listaAmigos = ["Ana", "Juan", "Carla", "Pedro", "Sofía", "Luis", "Marta", "Diego", "Laura", "Pablo"]
listaRoles = ["Pone la casa", "Asador", "Encargado de utensilios", "Encargado de bebidas", "Encargado de ensaladas"]
listaConfirmados = []

# Título principal
print("\n\t🎉 ¡ORGANIZACIÓN FINAL DEL ASADO DEL SÁBADO! 🎉")

# Confirmaciones
for i in range(len(listaAmigos)):
    asistencia = input(f"\t{i+1}. {listaAmigos[i]} asiste (s/n)? ").lower()
    if asistencia == 's':
        listaConfirmados.append(listaAmigos[i])

# Decisión según quórum
if len(listaConfirmados) < 8:
    print("\t❌ Asado cancelado por falta de quórum. ¡Será la próxima!")
else:
    print("\t🎉 ¡Tenemos asado!")

    costoTotal= int(input("\n\t💲 Costo total para el asado: "))
    costoIndividual = round(costoTotal/len(listaConfirmados),2)

    # Mezclar confirmados y asignar roles
    random.shuffle(listaConfirmados)
    listaRolesAsignados = []

    for i in range(len(listaConfirmados)):
        if i < len(listaRoles):
            rol = listaRoles[i]
        else:
            rol = "invitado"
        listaRolesAsignados.append(f"{listaConfirmados[i]} - {rol}")

    # Filtrar roles
    invitados = [persona.split(" - ")[0] for persona in listaRolesAsignados if "invitado" in persona]
    anfitrion = [persona.split(" - ")[0] for persona in listaRolesAsignados if "Pone la casa" in persona]


    # Mostrar organización final
    with open('organizacion_asado.txt', 'w', encoding='utf-8') as f:

        f.write("\n" + "="*60 + "\n")
        f.write("🎉 ORGANIZACIÓN FINAL DEL ASADO DEL SÁBADO 🎉\n")
        f.write("="*60 + "\n\n")

        f.write(f"👥 Confirmados ({len(listaConfirmados)}):\n")
        f.write("   " + ", ".join(listaConfirmados) + ".\n\n")

        f.write("📋 Roles asignados:\n")
        f.write(f"   🏠 Pone la casa:       {listaRolesAsignados[0].split(' - ')[0]}\n")
        f.write(f"   🔥 Asador/a:           {listaRolesAsignados[1].split(' - ')[0]}\n")
        f.write(f"   🍴 Utensilios:         {listaRolesAsignados[2].split(' - ')[0]}\n")
        f.write(f"   🥤 Bebidas:            {listaRolesAsignados[3].split(' - ')[0]}\n")
        f.write(f"   🥗 Ensaladas:          {listaRolesAsignados[4].split(' - ')[0]}\n\n")

        if invitados:
            f.write("🕺 Invitados que solo traen buena onda y su presencia:\n")
            f.write("   " + ", ".join(invitados) + ".\n\n")

        f.write("💰 Aporte por persona:\n")
        f.write(f"   Total estimado:        {costoTotal}$\n")
        f.write(f"   Aporte individual:     {costoIndividual}$\n")
        f.write("   💸 Transferir a alias: martinouvilla20 (o se paga en el momento)\n\n")

        f.write("📍 Dónde y Cuándo:\n")
        f.write(f"   Lugar:                 Casa de {anfitrion[0]}\n")
        f.write(f"   Dirección:             [Dirección de {anfitrion[0]}]\n")
        f.write("   Hora de llegada:       13:00 hrs\n\n")

        f.write("   ¡Nos vemos el sábado para disfrutar! ¡No olviden su aporte y la mejor energía! 💪\n")

    print("\n✅ ¡Perfecto! Se ha generado el archivo 'organizacion_asado.txt' con toda la información.")
    print("   Puedes copiar y pegar su contenido en el grupo de WhatsApp.")

