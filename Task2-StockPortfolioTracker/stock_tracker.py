
import csv

def get_stock_prices():
    # Prix des actions codés en dur
    return {"AAPL": 180.00, "TSLA": 250.00, "GOOG": 150.00, "AMZN": 130.00, "MSFT": 300.00}

def calculate_portfolio_value(portfolio, stock_prices):
    total_value = 0.0
    for stock, quantity in portfolio.items():
        if stock in stock_prices:
            total_value += stock_prices[stock] * quantity
        else:
            print(f"Attention: Le prix de l'action {stock} n'est pas disponible.")
    return total_value

def save_portfolio_to_file(portfolio, filename="portfolio_summary.txt", file_format="txt"):
    if file_format == "txt":
        with open(filename, "w") as f:
            f.write("Résumé du portefeuille boursier:\n")
            for stock, quantity in portfolio.items():
                f.write(f"  {stock}: {quantity} actions\n")
    elif file_format == "csv":
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Action", "Quantité"])
            for stock, quantity in portfolio.items():
                writer.writerow([stock, quantity])
    print(f"Le résumé du portefeuille a été enregistré dans {filename} au format {file_format}.")

def main():
    stock_prices = get_stock_prices()
    portfolio = {}

    print("Bienvenue dans le Suivi de Portefeuille Boursier!")
    print("Entrez les actions et les quantités (tapez 'fin' pour terminer).")

    while True:
        stock_name = input("Nom de l'action (ex: AAPL, TSLA) ou 'fin': ").upper()
        if stock_name == 'FIN':
            break

        if stock_name not in stock_prices:
            print(f"L'action {stock_name} n'est pas reconnue. Veuillez choisir parmi {', '.join(stock_prices.keys())}.")
            continue

        while True:
            try:
                quantity = int(input(f"Quantité de {stock_name}: "))
                if quantity <= 0:
                    print("La quantité doit être un nombre positif.")
                else:
                    break
            except ValueError:
                print("Quantité invalide. Veuillez entrer un nombre entier.")

        portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity
        print(f"Portefeuille actuel: {portfolio}\n")

    if not portfolio:
        print("Aucune action ajoutée au portefeuille. Fin du programme.")
        return

    total_value = calculate_portfolio_value(portfolio, stock_prices)
    print("\n--- Résumé du Portefeuille ---")
    for stock, quantity in portfolio.items():
        price = stock_prices.get(stock, 0)
        print(f"  {stock}: {quantity} actions (Valeur: {quantity * price:.2f}€)")
    print(f"Valeur totale du portefeuille: {total_value:.2f}€")

    save_option = input("Voulez-vous enregistrer le résumé du portefeuille dans un fichier? (oui/non): ").lower()
    if save_option == 'oui':
        file_type = input("Quel format de fichier? (txt/csv): ").lower()
        if file_type in ["txt", "csv"]:
            save_portfolio_to_file(portfolio, file_format=file_type)
        else:
            print("Format de fichier non supporté. Le résumé ne sera pas enregistré.")

    print("Merci d'avoir utilisé le Suivi de Portefeuille Boursier!")

if __name__ == "__main__":
    main()


