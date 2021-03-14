from discord_webhook import DiscordWebhook, DiscordEmbed
class DiscordNotifications:
    def __init__(self, discord_id_var, discord_url_var) -> None:
        self.discord_id_var = discord_id_var
        self.discord_url_var = discord_url_var

    def send_webhook_for_image_notfound_error(self):
        webhook = DiscordWebhook(url=self.discord_url_var.get(), content= "<@{0}>".format(self.discord_id_var.get()))
        embed = DiscordEmbed(title="Ark Smart Feeder", description = "I can't find anything to feed your baby, check your inventory", color= "03b2f8")
        webhook.add_embed(embed)
        response = webhook.execute()