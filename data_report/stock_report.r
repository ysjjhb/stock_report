## candlechart ##
# https://cran.r-project.org/web/packages/tidyquant/vignettes/TQ04-charting-with-tidyquant.html#candlestick-chart
## tidyquant ##
# https://business-science.github.io/tidyquant/
## quantmod ##
# https://bookdown.org/kochiuyu/Technical-Analysis-with-R/quantmod.html
library(ggpubr)
library(tidyverse)
library(plotly)
library(tidyquant) # chart
library(plotly)
stock_day <- read_csv("../stock_data/stock_day.csv")
stock_week <- read_csv("../stock_data/stock_week.csv")
stock_month <- read_csv("../stock_data/stock_month.csv")


# 가격 지표----

# Funtion : add indicator #
create_indicator <- function(data) {
  plot_rsi <- ggplot(data = eval(data)) +
    geom_line(aes(x = Date, y = RSI)) +
    geom_hline(yintercept = c(70, 30), 
               color = c("red", "blue"))
  plot_macd_oscillator <- ggplot(data = eval(data)) +
    geom_col(aes(x = Date, y = MACD_oscillator, fill = MACD_oscillator >= 0),
             show.legend = FALSE) +
    scale_fill_manual(values = c("blue", "red"))
  
  plot <- ggarrange(plotlist = list(plot, plot_rsi, plot_macd_oscillator),
                    ncol = 1,
                    heights = c(3, 1, 1))
  return(plot)
}

# day
plot <- stock_day %>%
  ggplot(aes(x = Date, y = Close)) +
  geom_candlestick(aes(
    open = Open,
    high = High,
    low = Low,
    close = Close
  )) +
  labs(title = "Verizon Candlestick Chart", y = "Closing Price", x = "") +
  theme_tq()

day_plot <- create_indicator(data = quote(stock_day))
day_plot

# week
plot <- stock_week %>%
  ggplot(aes(x = Date, y = Close)) +
  geom_candlestick(aes(
    open = Open,
    high = High,
    low = Low,
    close = Close
  )) +
  labs(title = "Verizon Candlestick Chart", y = "Closing Price", x = "") +
  theme_tq()

week_plot <- create_indicator(data = quote(stock_week))
week_plot

# month
plot <- stock_month %>%
  ggplot(aes(x = Date, y = Close)) +
  geom_candlestick(aes(
    open = Open,
    high = High,
    low = Low,
    close = Close
  )) +
  labs(title = "Verizon Candlestick Chart", y = "Closing Price", x = "") +
  theme_tq()


month_plot <- create_indicator(data = quote(stock_month))
month_plot


# 기본 통계----
