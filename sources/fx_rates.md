# FX rate reference table — v1.1 (verified against RBA on 2026-05-11)

All figures in this report are expressed in **Australian dollars (AUD)**.
Where a primary source publishes a figure in another currency, the
conversion uses the rate published in this table.

## Reference rates (used throughout the report — v1.1)

These rates have been verified directly against the **Reserve Bank of
Australia, Statistical Table F11.1 (Exchange Rates — Daily)** on
2026-05-11. The earlier v1.0 of this report used 1 USD = 1.55 AUD;
the public v1.1 package corrects that value.

| Currency | A$1 buys | A$ per 1 unit | Notes |
|---|---:|---:|---|
| USD | 0.7225 | **1.384** | RBA F11.1 daily fix, latest highlight value 2026-05-08. |
| EUR | 0.6155 | **1.625** | RBA F11.1 daily fix. |
| GBP | 0.5323 | **1.879** | RBA F11.1 daily fix. |
| JPY | 113.32 | **0.00883** | RBA F11.1 daily fix. A$1 ≈ ¥113. |
| MYR (Malaysian ringgit) | 2.8326 | **0.353** | RBA F11.1 daily fix. |
| NOK | (not published by RBA daily) | **0.130** | Cross-rate via USD: 1 USD ≈ 7.0 NOK (Norges Bank) × 1.384 = 9.68 NOK/AUD → 1 NOK ≈ A$0.130 (verified independently against Norges Bank's USD/NOK fix). |
| QAR (Qatari riyal) | 2.63 | **0.380** | Pegged to USD at 3.64 QAR/USD; cross-rate 3.64/1.384 = 2.63. |

## Sensitivity to FX correction in v1.1

Every figure in the v1.0 draft that used 1 USD = 1.55 AUD is now
multiplied by 0.893 (= 1.384 / 1.55) to give the corrected v1.1 figure.
For NOK conversions, the correction is from 0.144 to 0.130 (× 0.903).

### Worked examples after v1.1 correction

| Native figure | × rate | AUD figure (v1.1) | (v1.0 was) |
|---|---|---|---|
| Norway 2024 state petroleum: NOK 702 bn¹ | × 0.130 | **A$91.3 bn** | (was A$98 bn at NOK 680 + 0.144) |
| Norway GPFG end-2025: NOK 21,268 bn | × 0.130 | **A$2.77 trillion** | (was A$3.07 tn) |
| GPFG per Norwegian resident (NOK 3.8 m) | × 0.130 | **A$494,000** | (was A$547k) |
| Qatar 2024 hydrocarbon revenue: USD 47.5 bn | × 1.384 | **A$65.7 bn** | (was A$73.6 bn) |
| Qatar 2024 total revenue: USD 58.6 bn | × 1.384 | **A$81.1 bn** | (was A$90.8 bn) |
| QIA AUM (Aug 2025): USD 557 bn | × 1.384 | **A$771 bn** | (was A$863 bn) |
| QIA per Qatari citizen (USD 1.47 m) | × 1.384 | **A$2.03 m** | (was A$2.28 m) |
| QIA per resident (USD 180,000) | × 1.384 | **A$249,000** | (was A$279k) |
| US Interior FY2024 energy revenue: USD 16.45 bn | × 1.384 | **A$22.8 bn** | (was A$25.5 bn) |
| US OCS oil & gas FY2024: USD 7.0 bn | × 1.384 | **A$9.69 bn** | (was A$10.85 bn) |
| UK petroleum receipts 2023-24: GBP 6.1 bn | × 1.879 | **A$11.46 bn** | (was A$11.96 bn) |
| UK petroleum receipts 2024-25: GBP 4.5 bn | × 1.879 | **A$8.46 bn** | (was A$8.82 bn) |
| PETRONAS 2024 government contribution: RM 72.4 bn | × 0.353 | **A$25.6 bn** | (was A$23.9 bn) |
| PETRONAS cumulative since 1974: RM 1.5 trillion | × 0.353 | **A$530 bn** | (was A$495 bn) |
| Japan Petroleum & Coal Tax on LNG: JPY 1,860/t | × 0.00883 | **A$16.42/tonne** | (was A$18.23/t) |
| Australia main Future Fund end-2025 | (native AUD) | **A$267.4 bn** | (was A$335.3 bn — v3.0.4 corrected to main Fund only, not Board-managed total funds) |
| Per-tonne state take, Norway (gas-only attribution) | NOK 702 bn × 50% × 0.130 / 93 Mt | **A$491/t** | (was A$527/t) |
| Per-tonne state take, Qatar (gas-only attribution) | USD 47.5 bn × 85% × 1.384 / 77 Mt | **A$725/t** | (was A$813/t) |
| Per-tonne state take, Malaysia (gas-only attribution) | A$25.6 bn × 95% / 35.7 Mt | **A$682/t** | (was A$667/t — net of FX and gas-share refinement) |
| Per-tonne state take, USA (gas-only, offshore) | USD 7 bn × 55% × 1.384 / 88 Mt | **A$61/t** | (was A$68/t) |
| Per-tonne state take, Australia (all heads) | A$4 bn / 82 Mt | **A$49/t** | (native AUD — unchanged) |
| 25% LNG export tax revenue (AI / ACTU estimate) | (already AUD) | **A$17 bn/year** | (unchanged; the AI uses its own model) |

¹ Norway 2024 actual outcome per *Statsbudsjettet 2026* is NOK 702 bn,
not the NOK 680 bn estimate originally released October 2024. v1.1
adopts the actual outcome figure.

## Sensitivity

The headline conclusions remain insensitive to FX-rate variation at
±10 per cent. The Australia / Norway per-tonne ratio is ~10× at the
corrected rate (A$491 vs A$49); the Australia / Qatar ratio is ~15×.
The qualitative claims of the report do not depend on rate selection
or attribution choice.

## Primary-source links

- RBA Statistical Tables F11.1 (Exchange Rates - Daily):
  https://www.rba.gov.au/statistics/frequency/exchange-rates.html
- RBA Statistical Tables F11.2 (Monthly historical):
  https://www.rba.gov.au/statistics/tables/xls-hist/f11.2-data.xlsx
- Norges Bank exchange rates: https://www.norges-bank.no/en/topics/Statistics/exchange_rates/

Reference date for the spot rates above: **2026-05-11**, RBA daily fix.
NOK rate is cross-derived via USD because NOK is not in the RBA's
published daily-fix table; verified independently against Norges Bank.

## Citation
Cite this file as: Zyphur, M. (2026). *FX rate reference table*. In
*Australia's gas export tax revenue: the definitive accounting* v1.1.
Instats Policy Series. https://github.com/mzyphur/gas-tax/blob/main/sources/fx_rates.md
