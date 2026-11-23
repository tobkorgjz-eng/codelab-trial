import unittest

from chatcard import render_chat_card


class RenderChatCardTests(unittest.TestCase):
    def test_normal_text(self):
        html = render_chat_card("Helper Bot", "Hi there", "Hello, how can I help?")
        self.assertTrue(html.startswith('<figure class="hp-chat">'))
        self.assertTrue(html.endswith("</figure>"))
        self.assertIn(">You</span>", html)
        self.assertIn("<p>Hi there</p>", html)
        self.assertIn(">Helper Bot</span>", html)
        self.assertIn("<p>Hello, how can I help?</p>", html)
        self.assertIn("<figcaption>Example chat with example data</figcaption>", html)

    def test_special_characters_are_escaped(self):
        html = render_chat_card(
            'Bot <b>"A"</b>',
            "1 < 2 & 3 > 2 'ok'",
            '<script>alert("x")</script> & \'y\'',
        )
        self.assertNotIn("<script>", html)
        self.assertNotIn("<b>", html)
        self.assertIn("Bot &lt;b&gt;&quot;A&quot;&lt;/b&gt;", html)
        self.assertIn("1 &lt; 2 &amp; 3 &gt; 2 &#x27;ok&#x27;", html)
        self.assertIn(
            "&lt;script&gt;alert(&quot;x&quot;)&lt;/script&gt; &amp; &#x27;y&#x27;",
            html,
        )

    def test_empty_bot_text_raises(self):
        with self.assertRaises(ValueError):
            render_chat_card("Helper Bot", "Hi", "")
        with self.assertRaises(ValueError):
            render_chat_card("Helper Bot", "Hi", "   ")


if __name__ == "__main__":
    unittest.main()
