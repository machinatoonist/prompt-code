library(shiny)
library(openai)
library(shinythemes)
library(waiter)

waiting_screen <- tagList(
    spin_flower(),
    h4("Text being generated...")
)

ui <- fluidPage(
    useWaiter(),
    titlePanel("OpenAI API Text Generation App"),
    theme = shinytheme("flatly"),
    sidebarLayout(
        sidebarPanel(
            sliderInput("temperature",
                        "Increase the temperature for wider variations",
                        min = 0.0, max = 1.0, value = 0.5, step = 0.1),
            sliderInput("num_tokens",
                        "Maximum number of tokens",
                        min = 10, max = 2000, value = 100, step = 10),
            selectInput("model", "Select model",
                        choices = c("text-davinci-002",
                                    "code-davinci-002",
                                    "code-search-ada-text-001"),
                        selected = "text-davinci-002"),
            passwordInput("api_key", "Enter your OpenAI API key:"),
            p("Get your own OpenAI API key at https://openai.com/api/")
        ),
        mainPanel(
            textAreaInput(
                "prompt", "Enter your free text prompt:",
                value = 'Write a 100 word introductory paragraph for an acceptance speech for Best Film of the Year at the Oscars',
                placeholder = "eg: 'write a python script to print hello world'",
                height = "200px"),
            actionButton("submit", "Submit"),
            div(style = "background-color: white; padding: 10px; border-radius: 5px; max-width: 50%;",
                tags$code(id = "api_response", class = "language-python"),
                textOutput("api_response")
            )
        )
    )
)


server <- function(input, output) {

    observeEvent(input$submit, {
        if (input$api_key == "") {
            # If API key is not entered, display error message
            showModal(modalDialog(title = "Error", "Please enter your API key then submit."))
        } else {
            waiter_show(html = waiting_screen, color = "black")
            # Set up the API request
            rs <- openai::create_completion(engine_id = input$model,
                                      prompt = input$prompt,
                                      temperature = input$temperature,
                                      max_tokens = input$num_tokens,
                                      openai_api_key = input$api_key)


            # Display the response to the user
            output$api_response <- renderText({
                rs$choices$text
            })
            waiter_hide()
        }
    })
}

shinyApp(ui = ui, server = server)
