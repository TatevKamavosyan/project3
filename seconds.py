import time

def is_valid_time_format(time_input):
    # Ստուգում՝ արդյոք մուտքում կա երկու երկանորդակետ
    if time_input.count(":") != 2:
        return False

    # Ստուգում՝ արդյոք մուտքում միայն թվեր են և երկանորդակետեր
    if not all(c.isdigit() or c == ":" for c in time_input):
        return False

    return True


def countdown_timer():
    try:
        while True:
            # Մուտքագրում՝ ժամ, րոպե, վայրկյան
            time_input = input("Insert time to count down (hh:mm:ss): ")

            # Ստուգել մուտքի ձևաչափը
            if not is_valid_time_format(time_input):
                print("Invalid format! Please use the format hh:mm:ss with only numbers and colons.")
                continue  # Կրկին խնդրիր մուտքգրել ժամանակը

            # Մուտքի ժամանակները կտրել և վերածել թվերի
            h, m, s = map(int, time_input.split(":"))

            # Ստուգել ժամերի, րոպեների և վայրկյանների սահմանները
            if not (0 <= h < 24 and 0 <= m < 60 and 0 <= s < 60):
                print("Please ensure hours are 0-23, minutes and seconds are 0-59.")
                continue  # Կրկին խնդրել մուտքագրում

            # Հավաստի մուտքի դեպքում դուրս գալ ցիկլից
            break

        total_time = h * 3600 + m * 60 + s  # Պատրաստել ընդհանուր վայրկյաններ

        while total_time >= 0:
            # Կոնվերտացնել մնացած ժամանակը ժամերի, րոպեների ու վայրկյանների
            hours, remainder = divmod(total_time, 3600)
            minutes, seconds = divmod(remainder, 60)
            print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")  # Սահմանված ձևաչափով
            time.sleep(1)  # Սպասել մեկ վայրկյան
            total_time -= 1

        print("Time's up!")  # Երբ ժամանակը ավարտվի
    except ValueError as e:
        print(e)  # Տպել սխալի հաղորդագրությունը


if __name__ == "__main__":
    countdown_timer()
